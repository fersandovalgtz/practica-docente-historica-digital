#!/usr/bin/env python3
"""Lightweight integrity checks for PDHD public research data."""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

RIGHTS = {
    "metadata_only",
    "local_processing_only",
    "redistributable_with_attribution",
    "public_domain_verified",
    "permission_granted",
    "review_required",
}

ERA_CODES = {f"E{i}" for i in range(1, 8)}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def check_unique(rows: list[dict[str, str]], key: str, label: str) -> None:
    values = [r.get(key, "").strip() for r in rows]
    if any(not value for value in values):
        ERRORS.append(f"{label}: empty {key}")
    if len(values) != len(set(values)):
        ERRORS.append(f"{label}: duplicate {key}")


def validate_document_rows(
    rows: list[dict[str, str]],
    label: str,
    source_ids: set[str],
    seen_docs: set[str],
    seen_source_identifiers: set[str],
) -> None:
    for row in rows:
        doc_id = row.get("document_id", "").strip()
        if not re.fullmatch(r"PDHD-D\d{6}", doc_id):
            ERRORS.append(f"{label}: invalid document_id {doc_id!r}")
        if doc_id in seen_docs:
            ERRORS.append(f"documents union: duplicate document_id {doc_id}")
        seen_docs.add(doc_id)

        source_identifier = row.get("source_identifier", "").strip()
        if not source_identifier:
            ERRORS.append(f"{label}: empty source_identifier for {doc_id}")
        elif source_identifier in seen_source_identifiers:
            ERRORS.append(
                f"documents union: duplicate source_identifier {source_identifier}"
            )
        seen_source_identifiers.add(source_identifier)

        if row.get("source_id") not in source_ids:
            ERRORS.append(f"{label}: unknown source_id {row.get('source_id')}")
        if row.get("rights_status") not in RIGHTS:
            ERRORS.append(f"{label}: invalid rights_status {row.get('rights_status')}")

        era_code = row.get("era_code", "").strip()
        if era_code and era_code not in ERA_CODES:
            ERRORS.append(f"{label}: invalid era_code {era_code}")


def main() -> int:
    sources = read_csv(ROOT / "data/catalog/sources.csv")
    rights = read_csv(ROOT / "data/catalog/rights_registry.csv")
    candidates = read_csv(ROOT / "data/catalog/source_candidates.csv")
    documents_core = read_csv(ROOT / "data/catalog/documents.csv")
    balancing_path = ROOT / "data/catalog/documents_balancing_w1.csv"
    documents_balancing = read_csv(balancing_path) if balancing_path.exists() else []
    leads_path = ROOT / "data/catalog/issue_leads.csv"
    issue_leads = read_csv(leads_path) if leads_path.exists() else []
    conflicts_path = ROOT / "data/catalog/chronology_conflicts.csv"
    chronology_conflicts = read_csv(conflicts_path) if conflicts_path.exists() else []
    pilot_path = ROOT / "data/samples/pilot_document_selection_0_1.csv"
    pilot_selection = read_csv(pilot_path) if pilot_path.exists() else []
    dimensions = read_csv(ROOT / "data/taxonomy/pedagogical_dimensions.csv")
    acts = read_csv(ROOT / "data/taxonomy/pedagogical_acts.csv")

    check_unique(sources, "source_id", "sources")
    check_unique(rights, "source_id", "rights_registry")
    check_unique(candidates, "candidate_id", "source_candidates")
    check_unique(dimensions, "dimension_code", "pedagogical_dimensions")
    check_unique(acts, "act_code", "pedagogical_acts")
    if issue_leads:
        check_unique(issue_leads, "lead_id", "issue_leads")
    if chronology_conflicts:
        check_unique(chronology_conflicts, "conflict_id", "chronology_conflicts")
    if pilot_selection:
        check_unique(pilot_selection, "document_id", "pilot_document_selection")
        check_unique(pilot_selection, "selection_order", "pilot_document_selection")

    source_ids = {r["source_id"] for r in sources}
    rights_ids = {r["source_id"] for r in rights}
    missing_rights = sorted(source_ids - rights_ids)
    extra_rights = sorted(rights_ids - source_ids)
    if missing_rights:
        ERRORS.append(f"rights_registry: missing source_id entries {missing_rights}")
    if extra_rights:
        ERRORS.append(f"rights_registry: unknown source_id entries {extra_rights}")

    for row in rights:
        if row.get("rights_status") not in RIGHTS:
            ERRORS.append(f"rights_registry: invalid rights_status {row.get('rights_status')}")

    seen_candidates: set[str] = set()
    for row in candidates:
        candidate_id = row.get("candidate_id", "")
        if not re.fullmatch(r"PDHD-C\d{6}", candidate_id):
            ERRORS.append(f"source_candidates: invalid candidate_id {candidate_id!r}")
        if candidate_id in seen_candidates:
            ERRORS.append(f"source_candidates: duplicate candidate_id {candidate_id}")
        seen_candidates.add(candidate_id)
        if row.get("source_id") not in source_ids:
            ERRORS.append(f"source_candidates: unknown source_id {row.get('source_id')}")
        if row.get("rights_status") not in RIGHTS:
            ERRORS.append(f"source_candidates: invalid rights_status {row.get('rights_status')}")

    seen_docs: set[str] = set()
    seen_source_identifiers: set[str] = set()
    validate_document_rows(
        documents_core,
        "documents.csv",
        source_ids,
        seen_docs,
        seen_source_identifiers,
    )
    validate_document_rows(
        documents_balancing,
        "documents_balancing_w1.csv",
        source_ids,
        seen_docs,
        seen_source_identifiers,
    )

    document_index = {
        row["document_id"]: row for row in (documents_core + documents_balancing)
    }

    if pilot_selection:
        if len(pilot_selection) != 24:
            ERRORS.append(
                f"pilot_document_selection: expected 24 documents, found {len(pilot_selection)}"
            )
        expected_orders = list(range(1, len(pilot_selection) + 1))
        try:
            actual_orders = sorted(int(r["selection_order"]) for r in pilot_selection)
        except ValueError:
            ERRORS.append("pilot_document_selection: non-integer selection_order")
            actual_orders = []
        if actual_orders and actual_orders != expected_orders:
            ERRORS.append(
                f"pilot_document_selection: selection_order must be contiguous 1-{len(pilot_selection)}"
            )

        fragment_total = 0
        publication_counts: Counter[str] = Counter()
        for row in pilot_selection:
            doc_id = row.get("document_id", "").strip()
            if doc_id not in seen_docs:
                ERRORS.append(
                    f"pilot_document_selection: unknown document_id {doc_id}"
                )
                continue
            doc = document_index[doc_id]
            publication = row.get("publication", "").strip()
            if publication != doc.get("publication", "").strip():
                ERRORS.append(
                    f"pilot_document_selection: publication mismatch for {doc_id}"
                )
            publication_counts[publication] += 1
            era_code = row.get("era_code", "").strip()
            if era_code not in ERA_CODES:
                ERRORS.append(
                    f"pilot_document_selection: invalid era_code {era_code!r} for {doc_id}"
                )
            if row.get("status", "").strip() != "selected":
                ERRORS.append(
                    f"pilot_document_selection: unexpected status for {doc_id}"
                )
            try:
                fragment_total += int(row.get("fragment_target_count", "0"))
            except ValueError:
                ERRORS.append(
                    f"pilot_document_selection: invalid fragment_target_count for {doc_id}"
                )

        if fragment_total != 96:
            ERRORS.append(
                f"pilot_document_selection: expected 96 target fragments, found {fragment_total}"
            )
        overrepresented = {
            publication: count
            for publication, count in publication_counts.items()
            if count > 6
        }
        if overrepresented:
            ERRORS.append(
                f"pilot_document_selection: publication concentration exceeds 6 {overrepresented}"
            )

    unresolved_leads = 0
    resolved_leads = 0
    for row in issue_leads:
        lead_id = row.get("lead_id", "")
        if not re.fullmatch(r"PDHD-L\d{6}", lead_id):
            ERRORS.append(f"issue_leads: invalid lead_id {lead_id!r}")
        if not row.get("publication", "").strip():
            ERRORS.append(f"issue_leads: empty publication for {lead_id}")
        if not row.get("evidence_url", "").strip():
            ERRORS.append(f"issue_leads: empty evidence_url for {lead_id}")

        status = row.get("primary_locator_status", "").strip()
        resolved_document_id = row.get("resolved_document_id", "").strip()
        if status.startswith("resolved"):
            resolved_leads += 1
            if not resolved_document_id:
                ERRORS.append(
                    f"issue_leads: {lead_id} is resolved but lacks resolved_document_id"
                )
            elif resolved_document_id not in seen_docs:
                ERRORS.append(
                    f"issue_leads: {lead_id} points to unknown document {resolved_document_id}"
                )
        else:
            unresolved_leads += 1
            if resolved_document_id:
                ERRORS.append(
                    f"issue_leads: {lead_id} has resolved_document_id but status {status!r}"
                )

    for row in chronology_conflicts:
        conflict_id = row.get("conflict_id", "")
        if not re.fullmatch(r"PDHD-X\d{6}", conflict_id):
            ERRORS.append(f"chronology_conflicts: invalid conflict_id {conflict_id!r}")

    for schema in ("document.schema.json", "pedagogical_fragment.schema.json"):
        with (ROOT / "schemas" / schema).open(encoding="utf-8") as fh:
            json.load(fh)

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    total_documents = len(documents_core) + len(documents_balancing)
    pilot_note = f"; {len(pilot_selection)} pilot documents" if pilot_selection else ""
    print(
        "PDHD repository checks passed "
        f"({len(sources)} sources; {len(candidates)} candidates; "
        f"{total_documents} documents; {len(issue_leads)} issue leads "
        f"[{unresolved_leads} unresolved, {resolved_leads} resolved]; "
        f"{len(chronology_conflicts)} chronology conflicts{pilot_note})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
