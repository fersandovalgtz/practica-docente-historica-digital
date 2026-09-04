#!/usr/bin/env python3
"""Lightweight integrity checks for PDHD public research data."""
from __future__ import annotations

import csv
import json
import re
import sys
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

    for row in issue_leads:
        lead_id = row.get("lead_id", "")
        if not re.fullmatch(r"PDHD-L\d{6}", lead_id):
            ERRORS.append(f"issue_leads: invalid lead_id {lead_id!r}")
        if not row.get("publication", "").strip():
            ERRORS.append(f"issue_leads: empty publication for {lead_id}")
        if not row.get("evidence_url", "").strip():
            ERRORS.append(f"issue_leads: empty evidence_url for {lead_id}")

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
    print(
        "PDHD repository checks passed "
        f"({len(sources)} sources; {len(candidates)} candidates; "
        f"{total_documents} documents; {len(issue_leads)} issue leads; "
        f"{len(chronology_conflicts)} chronology conflicts)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
