#!/usr/bin/env python3
"""Validate PDHD object aliases without promoting them to page-level evidence."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

ALIAS_ROLES = {"full_text_target", "alternate_catalog_record", "serial_container"}
VERIFICATION_STATES = {
    "repository_fulltext_link_resolved_interface_fetch_failed",
    "repository_fulltext_link_resolved",
    "directly_verified",
    "review_required",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    aliases_path = ROOT / "data/catalog/object_aliases.csv"
    if not aliases_path.exists():
        print("PDHD object-alias checks skipped (no object_aliases.csv)")
        return 0

    aliases = read_csv(aliases_path)
    docs = read_csv(ROOT / "data/catalog/documents.csv")
    balancing = ROOT / "data/catalog/documents_balancing_w1.csv"
    if balancing.exists():
        docs += read_csv(balancing)
    doc_ids = {row["document_id"] for row in docs}

    alias_ids: set[str] = set()
    semantic_keys: set[tuple[str, str, str]] = set()
    for row in aliases:
        alias_id = row.get("alias_id", "").strip()
        if not re.fullmatch(r"PDHD-A\d{6}", alias_id):
            ERRORS.append(f"invalid alias_id {alias_id!r}")
        if alias_id in alias_ids:
            ERRORS.append(f"duplicate alias_id {alias_id}")
        alias_ids.add(alias_id)

        doc_id = row.get("document_id", "").strip()
        if doc_id not in doc_ids:
            ERRORS.append(f"{alias_id}: unknown document_id {doc_id}")

        alias_system = row.get("alias_system", "").strip()
        alias_identifier = row.get("alias_identifier", "").strip()
        if not alias_system or not alias_identifier:
            ERRORS.append(f"{alias_id}: missing alias system or identifier")

        key = (doc_id, alias_system, alias_identifier)
        if key in semantic_keys:
            ERRORS.append(f"duplicate document/system/identifier alias {key}")
        semantic_keys.add(key)

        if row.get("alias_role", "").strip() not in ALIAS_ROLES:
            ERRORS.append(f"{alias_id}: invalid alias_role")
        if row.get("verification_status", "").strip() not in VERIFICATION_STATES:
            ERRORS.append(f"{alias_id}: invalid verification_status")

        for field in ("alias_url", "evidence_url", "checked_at", "note"):
            if not row.get(field, "").strip():
                ERRORS.append(f"{alias_id}: missing {field}")

        alias_url = row.get("alias_url", "").strip()
        if alias_system == "HNDM" and alias_url:
            parsed = urlparse(alias_url)
            if "hndm.unam.mx" not in parsed.netloc:
                ERRORS.append(f"{alias_id}: HNDM alias URL has unexpected host")
            if alias_identifier not in parsed.path:
                ERRORS.append(f"{alias_id}: HNDM identifier absent from alias URL path")
            query = parse_qs(parsed.query)
            if row.get("alias_role") == "full_text_target":
                for parameter in ("anio", "mes", "dia"):
                    if parameter not in query:
                        ERRORS.append(
                            f"{alias_id}: issue-specific HNDM full-text target lacks {parameter}"
                        )

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"PDHD object-alias checks passed ({len(aliases)} aliases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
