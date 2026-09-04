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


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def check_unique(rows: list[dict[str, str]], key: str, label: str) -> None:
    values = [r.get(key, "").strip() for r in rows]
    if any(not value for value in values):
        ERRORS.append(f"{label}: empty {key}")
    if len(values) != len(set(values)):
        ERRORS.append(f"{label}: duplicate {key}")


def main() -> int:
    sources = read_csv(ROOT / "data/catalog/sources.csv")
    rights = read_csv(ROOT / "data/catalog/rights_registry.csv")
    documents = read_csv(ROOT / "data/catalog/documents.csv")
    dimensions = read_csv(ROOT / "data/taxonomy/pedagogical_dimensions.csv")
    acts = read_csv(ROOT / "data/taxonomy/pedagogical_acts.csv")

    check_unique(sources, "source_id", "sources")
    check_unique(rights, "source_id", "rights_registry")
    check_unique(dimensions, "dimension_code", "pedagogical_dimensions")
    check_unique(acts, "act_code", "pedagogical_acts")

    source_ids = {r["source_id"] for r in sources}
    for row in rights:
        if row.get("source_id") not in source_ids:
            ERRORS.append(f"rights_registry: unknown source_id {row.get('source_id')}")
        if row.get("rights_status") not in RIGHTS:
            ERRORS.append(f"rights_registry: invalid rights_status {row.get('rights_status')}")

    seen_docs: set[str] = set()
    for row in documents:
        doc_id = row.get("document_id", "")
        if not re.fullmatch(r"PDHD-D\d{6}", doc_id):
            ERRORS.append(f"documents: invalid document_id {doc_id!r}")
        if doc_id in seen_docs:
            ERRORS.append(f"documents: duplicate document_id {doc_id}")
        seen_docs.add(doc_id)
        if row.get("source_id") not in source_ids:
            ERRORS.append(f"documents: unknown source_id {row.get('source_id')}")
        if row.get("rights_status") not in RIGHTS:
            ERRORS.append(f"documents: invalid rights_status {row.get('rights_status')}")

    for schema in ("document.schema.json", "pedagogical_fragment.schema.json"):
        with (ROOT / "schemas" / schema).open(encoding="utf-8") as fh:
            json.load(fh)

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("PDHD repository checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
