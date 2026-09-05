#!/usr/bin/env python3
"""Prepare deterministic manual-review records for PDHD freeze-conversion candidates.

This helper does not promote or mutate fragments. It projects canonical locator and
queue metadata into a review sheet so a human primary-page inspection can record the
remaining evidence required by FRAGMENT_FREEZE_PROTOCOL.md without retyping stable
identifiers or locators.
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data/samples"
QUEUE = SAMPLES / "freeze_conversion_queue_0_1.csv"

FIELDNAMES = [
    "fragment_id",
    "document_id",
    "slot",
    "page",
    "source_locator",
    "locator_evidence_url",
    "priority_group",
    "current_state",
    "selection_role",
    "source_image_verified",
    "boundary_definition",
    "transcription_status",
    "access_basis",
    "public_text_status",
    "decision",
    "review_note",
    "reviewed_at",
]

ROLE_BY_SLOT = {
    "A": "explicit_pedagogical_act",
    "B": "institutional_relation",
    "C": "source_criticism_salient",
    "D": "control",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def locator_union() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for path in sorted(SAMPLES.glob("fragment_locator_progress*.csv")):
        for row in read_csv(path):
            fid = row.get("fragment_id", "").strip()
            if not fid:
                continue
            if fid in rows:
                raise SystemExit(f"duplicate locator row for {fid}")
            rows[fid] = row
    return rows


def queue_rows() -> list[dict[str, str]]:
    if not QUEUE.exists():
        raise SystemExit("freeze_conversion_queue_0_1.csv is missing")
    return read_csv(QUEUE)


def build_review_row(
    queue_row: dict[str, str], locator: dict[str, str]
) -> dict[str, str]:
    fid = queue_row["fragment_id"].strip()
    slot = queue_row["slot"].strip()
    if slot not in ROLE_BY_SLOT:
        raise SystemExit(f"{fid}: unsupported slot {slot!r}")
    if locator.get("freeze_status", "").strip() == "frozen":
        raise SystemExit(f"{fid}: already frozen; no manual review sheet should be prepared")
    if queue_row.get("document_id", "").strip() != locator.get("document_id", "").strip():
        raise SystemExit(f"{fid}: queue/locator document mismatch")
    if slot != locator.get("slot", "").strip():
        raise SystemExit(f"{fid}: queue/locator slot mismatch")

    return {
        "fragment_id": fid,
        "document_id": locator["document_id"].strip(),
        "slot": slot,
        "page": locator.get("page", "").strip(),
        "source_locator": locator.get("source_locator", "").strip(),
        "locator_evidence_url": locator.get("locator_evidence_url", "").strip(),
        "priority_group": queue_row.get("priority_group", "").strip(),
        "current_state": locator.get("boundary_status", "").strip(),
        "selection_role": ROLE_BY_SLOT[slot],
        "source_image_verified": "no",
        "boundary_definition": "",
        "transcription_status": "",
        "access_basis": "",
        "public_text_status": locator.get("public_text_status", "").strip(),
        "decision": "pending_primary_visual_review",
        "review_note": "",
        "reviewed_at": "",
    }


def render(rows: list[dict[str, str]]) -> str:
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=FIELDNAMES, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "fragment_ids",
        nargs="*",
        help="Optional PDHD fragment IDs. Omit to prepare the complete current conversion queue.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the review sheet to this path instead of stdout.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate that every conversion-queue row can produce a deterministic review record.",
    )
    args = parser.parse_args()

    locators = locator_union()
    queue = queue_rows()
    queue_index = {row["fragment_id"].strip(): row for row in queue}
    if len(queue_index) != len(queue):
        raise SystemExit("freeze-conversion queue contains duplicate fragment IDs")

    requested = args.fragment_ids or [row["fragment_id"].strip() for row in queue]
    review_rows: list[dict[str, str]] = []
    for fid in requested:
        queue_row = queue_index.get(fid)
        if queue_row is None:
            raise SystemExit(f"{fid}: not present in the current freeze-conversion queue")
        locator = locators.get(fid)
        if locator is None:
            raise SystemExit(f"{fid}: missing canonical locator row")
        review_rows.append(build_review_row(queue_row, locator))

    if args.check:
        if len(review_rows) != len(queue):
            raise SystemExit(
                f"expected {len(queue)} conversion review rows, built {len(review_rows)}"
            )
        if len({row["fragment_id"] for row in review_rows}) != len(review_rows):
            raise SystemExit("freeze review contains duplicate fragment IDs")
        if any(row["source_image_verified"] != "no" for row in review_rows):
            raise SystemExit("new review records must not pre-assert primary-image verification")
        if any(row["decision"] != "pending_primary_visual_review" for row in review_rows):
            raise SystemExit("new review records must begin pending primary visual review")
        print(
            "PDHD freeze-review preparation check passed "
            f"({len(review_rows)} current conversion candidates)"
        )
        return 0

    text = render(review_rows)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
