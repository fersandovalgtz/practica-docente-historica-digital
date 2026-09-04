#!/usr/bin/env python3
"""Build the fixed-fragment manifest skeleton for the PDHD human pilot.

The generator is deterministic: four slots are produced for each document in
`data/samples/pilot_document_selection_0_1.csv`, in selection order. It does
not discover or transcribe source text. Page/localizer fields remain blank
until the fragment-freezing preparation pass is completed.
"""
from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELECTION = ROOT / "data/samples/pilot_document_selection_0_1.csv"

SLOTS = [
    (
        "A",
        "explicit_pedagogical_act",
        "one explicit pedagogical act or instructional prescription",
    ),
    (
        "B",
        "institutional_relation",
        "professional identity authority supervision evaluation or organization",
    ),
    (
        "C",
        "source_criticism_salient",
        "historically salient passage selected through source criticism",
    ),
    (
        "D",
        "control_none_unclear",
        "control passage capable of none or unclear on at least one field",
    ),
]

FIELDNAMES = [
    "fragment_id",
    "document_id",
    "era_code",
    "publication",
    "slot",
    "selection_role",
    "page",
    "fragment_locator",
    "transcription_status",
    "access_basis",
    "public_text_status",
    "freeze_status",
    "notes",
]


def read_selection() -> list[dict[str, str]]:
    with SELECTION.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def build_rows(selection: list[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    fragment_number = 1
    for selected in sorted(selection, key=lambda r: int(r["selection_order"])):
        for slot, role, note in SLOTS:
            rows.append(
                {
                    "fragment_id": f"PDHD-F{fragment_number:06d}",
                    "document_id": selected["document_id"],
                    "era_code": selected["era_code"],
                    "publication": selected["publication"],
                    "slot": slot,
                    "selection_role": role,
                    "page": "",
                    "fragment_locator": "",
                    "transcription_status": "not_started",
                    "access_basis": "pending_object_review",
                    "public_text_status": "metadata_only_until_review",
                    "freeze_status": "pending_locator",
                    "notes": note,
                }
            )
            fragment_number += 1
    return rows


def render_csv(rows: list[dict[str, str]]) -> str:
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=FIELDNAMES, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the generated manifest skeleton to this path instead of stdout.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate the deterministic pilot shape and exit without emitting CSV.",
    )
    args = parser.parse_args()

    selection = read_selection()
    rows = build_rows(selection)

    if len(selection) != 24:
        raise SystemExit(f"expected 24 selected documents, found {len(selection)}")
    if len(rows) != 96:
        raise SystemExit(f"expected 96 fragment slots, found {len(rows)}")
    if len({row["fragment_id"] for row in rows}) != 96:
        raise SystemExit("fragment IDs are not unique")
    if any(row["freeze_status"] != "pending_locator" for row in rows):
        raise SystemExit("new manifest must begin in pending_locator state")

    if args.check:
        print("PDHD fragment manifest generator check passed (24 documents; 96 slots)")
        return 0

    text = render_csv(rows)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
