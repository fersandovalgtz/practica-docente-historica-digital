#!/usr/bin/env python3
"""Validate structured provenance for unresolved primary-source retrieval attempts."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data/samples"
ERRORS: list[str] = []
SLOTS = ("A", "B", "C", "D")
RESULT_STATES = {
    "object_resolved_render_blocked",
    "descriptor_resolved_page_ids_missing",
    "full_view_item_resolved_automated_access_blocked",
    "issue_resolved_manual_page_inspection_pending",
    "superseded_by_locator",
}
REQUIRED_FIELDS = (
    "attempt_id",
    "document_id",
    "fragment_ids",
    "source_id",
    "object_url",
    "target",
    "result_status",
    "blocker",
    "next_route",
    "checked_at",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def expected_manifest() -> dict[str, tuple[str, str]]:
    pilot = read_csv(SAMPLES / "pilot_document_selection_0_1.csv")
    expected: dict[str, tuple[str, str]] = {}
    for row in pilot:
        order = int(row["selection_order"])
        doc_id = row["document_id"].strip()
        first = (order - 1) * 4 + 1
        for offset, slot in enumerate(SLOTS):
            expected[f"PDHD-F{first + offset:06d}"] = (doc_id, slot)
    return expected


def valid_https_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main() -> int:
    path = SAMPLES / "retrieval_attempts.csv"
    if not path.exists():
        print("PDHD retrieval-attempt checks skipped (no retrieval_attempts.csv)")
        return 0

    rows = read_csv(path)
    expected = expected_manifest()
    seen_attempts: set[str] = set()

    for row in rows:
        attempt_id = row.get("attempt_id", "").strip()
        if not re.fullmatch(r"PDHD-RA\d{6}", attempt_id):
            ERRORS.append(f"invalid attempt_id {attempt_id!r}")
        if attempt_id in seen_attempts:
            ERRORS.append(f"duplicate attempt_id {attempt_id}")
        seen_attempts.add(attempt_id)

        for field in REQUIRED_FIELDS:
            if not row.get(field, "").strip():
                ERRORS.append(f"{attempt_id}: missing {field}")

        doc_id = row.get("document_id", "").strip()
        fragment_ids = [
            value.strip()
            for value in row.get("fragment_ids", "").split(";")
            if value.strip()
        ]
        if not fragment_ids:
            ERRORS.append(f"{attempt_id}: fragment_ids must contain at least one pilot fragment")

        if len(fragment_ids) != len(set(fragment_ids)):
            ERRORS.append(f"{attempt_id}: duplicate fragment ID inside fragment_ids")

        for fid in fragment_ids:
            if not re.fullmatch(r"PDHD-F\d{6}", fid):
                ERRORS.append(f"{attempt_id}: invalid fragment_id {fid!r}")
                continue
            manifest_row = expected.get(fid)
            if manifest_row is None:
                ERRORS.append(f"{attempt_id}: {fid} is outside the 96-fragment pilot manifest")
                continue
            expected_doc, _slot = manifest_row
            if expected_doc != doc_id:
                ERRORS.append(
                    f"{attempt_id}: {fid} belongs to {expected_doc}, not declared document {doc_id}"
                )

        object_url = row.get("object_url", "").strip()
        if object_url and not valid_https_url(object_url):
            ERRORS.append(f"{attempt_id}: object_url must be an absolute HTTPS URL")

        result_status = row.get("result_status", "").strip()
        if result_status not in RESULT_STATES:
            ERRORS.append(f"{attempt_id}: invalid result_status {result_status!r}")

        checked_at = row.get("checked_at", "").strip()
        if checked_at and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked_at):
            ERRORS.append(f"{attempt_id}: checked_at must use YYYY-MM-DD")

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    covered_fragments = {
        fid
        for row in rows
        for fid in row.get("fragment_ids", "").split(";")
        if fid.strip()
    }
    print(
        "PDHD retrieval-attempt checks passed "
        f"({len(rows)} attempts; {len(covered_fragments)} pilot fragments with structured retrieval provenance)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
