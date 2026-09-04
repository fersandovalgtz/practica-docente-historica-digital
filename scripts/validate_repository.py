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
PILOT_SLOTS = ("A", "B", "C", "D")
LOCATOR_FREEZE_STATES = {
    "locator_candidate",
    "locator_resolved_text_package_pending",
    "frozen",
}
TRANSCRIPTION_STATES = {
    "source_text_verified",
    "ocr_human_corrected",
    "ocr_unverified",
    "manual_transcription_unverified",
    "not_transcribed",
    "not_started",
}
PUBLIC_TEXT_STATES = {
    "public_text_permitted",
    "short_excerpt_only",
    "coder_local_text",
    "metadata_only",
    "access_unresolved",
}
SELECTION_ROLES = {
    "explicit_pedagogical_act",
    "institutional_relation",
    "source_criticism_salient",
    "control",
}


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
    locator_path = ROOT / "data/samples/fragment_locator_progress_0_1.csv"
    locator_progress = read_csv(locator_path) if locator_path.exists() else []
    frozen_path = ROOT / "data/samples/frozen_fragments_0_1.csv"
    frozen_fragments = read_csv(frozen_path) if frozen_path.exists() else []
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
    if locator_progress:
        check_unique(locator_progress, "fragment_id", "fragment_locator_progress")
    if frozen_fragments:
        check_unique(frozen_fragments, "fragment_id", "frozen_fragments")

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

    expected_fragments: dict[str, tuple[str, str]] = {}
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
                order = int(row["selection_order"])
            except ValueError:
                ERRORS.append(
                    f"pilot_document_selection: invalid integer field for {doc_id}"
                )
                continue

            first_fragment = (order - 1) * 4 + 1
            for offset, slot in enumerate(PILOT_SLOTS):
                fragment_id = f"PDHD-F{first_fragment + offset:06d}"
                expected_fragments[fragment_id] = (doc_id, slot)

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

    locator_index = {r.get("fragment_id", "").strip(): r for r in locator_progress}
    frozen_index = {r.get("fragment_id", "").strip(): r for r in frozen_fragments}

    frozen_locator_count = 0
    for row in locator_progress:
        fragment_id = row.get("fragment_id", "").strip()
        if not re.fullmatch(r"PDHD-F\d{6}", fragment_id):
            ERRORS.append(
                f"fragment_locator_progress: invalid fragment_id {fragment_id!r}"
            )
            continue
        if fragment_id not in expected_fragments:
            ERRORS.append(
                f"fragment_locator_progress: fragment {fragment_id} is outside the pilot manifest"
            )
            continue

        expected_doc, expected_slot = expected_fragments[fragment_id]
        if row.get("document_id", "").strip() != expected_doc:
            ERRORS.append(
                f"fragment_locator_progress: document mismatch for {fragment_id}"
            )
        if row.get("slot", "").strip() != expected_slot:
            ERRORS.append(
                f"fragment_locator_progress: slot mismatch for {fragment_id}"
            )
        if not row.get("page", "").strip():
            ERRORS.append(
                f"fragment_locator_progress: missing page for {fragment_id}"
            )
        if not row.get("source_locator", "").strip():
            ERRORS.append(
                f"fragment_locator_progress: missing source_locator for {fragment_id}"
            )
        if not row.get("locator_evidence_url", "").strip():
            ERRORS.append(
                f"fragment_locator_progress: missing locator_evidence_url for {fragment_id}"
            )

        freeze_status = row.get("freeze_status", "").strip()
        if freeze_status not in LOCATOR_FREEZE_STATES:
            ERRORS.append(
                f"fragment_locator_progress: invalid freeze_status {freeze_status!r} for {fragment_id}"
            )
        if freeze_status == "frozen":
            frozen_locator_count += 1
            if row.get("boundary_status", "").strip() != "fixed":
                ERRORS.append(
                    f"fragment_locator_progress: frozen fragment {fragment_id} lacks fixed boundaries"
                )
            if fragment_id not in frozen_index:
                ERRORS.append(
                    f"fragment_locator_progress: frozen fragment {fragment_id} lacks frozen registry row"
                )

    for row in frozen_fragments:
        fragment_id = row.get("fragment_id", "").strip()
        if fragment_id not in expected_fragments:
            ERRORS.append(f"frozen_fragments: unknown pilot fragment {fragment_id}")
            continue
        if fragment_id not in locator_index:
            ERRORS.append(f"frozen_fragments: {fragment_id} lacks locator-progress row")
            continue
        locator = locator_index[fragment_id]
        expected_doc, expected_slot = expected_fragments[fragment_id]
        if row.get("document_id", "").strip() != expected_doc:
            ERRORS.append(f"frozen_fragments: document mismatch for {fragment_id}")
        if row.get("slot", "").strip() != expected_slot:
            ERRORS.append(f"frozen_fragments: slot mismatch for {fragment_id}")
        for field in (
            "page",
            "source_locator",
            "locator_evidence_url",
            "boundary_definition",
            "access_basis",
            "preparation_note",
            "checked_at",
        ):
            if not row.get(field, "").strip():
                ERRORS.append(f"frozen_fragments: missing {field} for {fragment_id}")
        for field in ("page", "source_locator", "locator_evidence_url"):
            if row.get(field, "").strip() != locator.get(field, "").strip():
                ERRORS.append(
                    f"frozen_fragments: {field} does not match locator row for {fragment_id}"
                )
        if row.get("transcription_status", "").strip() not in TRANSCRIPTION_STATES:
            ERRORS.append(
                f"frozen_fragments: invalid transcription_status for {fragment_id}"
            )
        if row.get("public_text_status", "").strip() not in PUBLIC_TEXT_STATES:
            ERRORS.append(
                f"frozen_fragments: invalid public_text_status for {fragment_id}"
            )
        if row.get("selection_role", "").strip() not in SELECTION_ROLES:
            ERRORS.append(f"frozen_fragments: invalid selection_role for {fragment_id}")
        if row.get("freeze_status", "").strip() != "frozen":
            ERRORS.append(f"frozen_fragments: non-frozen registry row {fragment_id}")
        if locator.get("freeze_status", "").strip() != "frozen":
            ERRORS.append(
                f"frozen_fragments: locator row is not frozen for {fragment_id}"
            )

    if frozen_locator_count != len(frozen_fragments):
        ERRORS.append(
            "frozen fragment count mismatch between locator queue and frozen registry"
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
    locator_note = (
        f"; {len(locator_progress)} locator rows [{frozen_locator_count} frozen]"
        if locator_progress
        else ""
    )
    print(
        "PDHD repository checks passed "
        f"({len(sources)} sources; {len(candidates)} candidates; "
        f"{total_documents} documents; {len(issue_leads)} issue leads "
        f"[{unresolved_leads} unresolved, {resolved_leads} resolved]; "
        f"{len(chronology_conflicts)} chronology conflicts{pilot_note}{locator_note})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
