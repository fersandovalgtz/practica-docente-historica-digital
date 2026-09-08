#!/usr/bin/env python3
"""Validate one real coder's completed PDHD-U1 calibration first pass.

The validator never supplies or corrects labels. It checks provenance, stable
coder identity, controlled vocabularies, completeness, and the explicit access-
problem escape hatch defined by the annotation manual.
"""
from __future__ import annotations

import argparse
import csv
import re
import tempfile
from datetime import datetime
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data" / "samples"
MASTER = SAMPLES / "calibration_coder_sheet_0_1.csv"
ACTS = ROOT / "data" / "taxonomy" / "pedagogical_acts.csv"
CODER_ID_RE = re.compile(r"C\d{2,3}")

NORMATIVITY = {
    "prescriptive",
    "policy_normative",
    "descriptive",
    "reported_practice",
    "observed_practice",
    "testimonial",
    "analytical",
    "mixed",
    "unclear",
}
ACTORS = {
    "teacher",
    "student",
    "inspector",
    "director",
    "family",
    "community",
    "state_authority",
    "other",
    "unclear",
}
TARGETS = {
    "student",
    "teacher",
    "family",
    "community",
    "institution",
    "self",
    "other",
    "unclear",
}
CONFIDENCE = {"high", "medium", "low"}
STRUCTURAL_FIELDS = [
    "item_id",
    "fragment_id",
    "document_id",
    "page",
    "source_url",
    "boundary_instruction",
    "codebook_version",
]


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader), list(reader.fieldnames or [])


def allowed_acts() -> set[str]:
    rows, _ = read_csv(ACTS)
    return {r["act_code"].strip() for r in rows if r.get("act_code", "").strip()}


def dimension_fields(fields: list[str]) -> list[str]:
    return [f for f in fields if f.startswith("dimension_")]


def parse_timestamp(value: str) -> bool:
    value = value.strip()
    if not value:
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def validate_rows(
    rows: list[dict[str, str]],
    fields: list[str],
    expected_coder: str | None = None,
) -> list[str]:
    errors: list[str] = []
    master_rows, master_fields = read_csv(MASTER)

    if fields != master_fields:
        errors.append("sheet header differs from canonical calibration coder sheet")
        return errors
    if len(rows) != 12:
        errors.append(f"completed calibration sheet must contain 12 rows, found {len(rows)}")
        return errors

    if [(r["item_id"], r["fragment_id"], r["document_id"]) for r in rows] != [
        (r["item_id"], r["fragment_id"], r["document_id"]) for r in master_rows
    ]:
        errors.append("item/fragment/document identity or order differs from canonical blind sheet")

    for row, master in zip(rows, master_rows):
        item = row.get("item_id", "")
        for field in STRUCTURAL_FIELDS:
            if row.get(field, "") != master.get(field, ""):
                errors.append(f"{item}: canonical structural field changed: {field}")

    coder_ids = {r.get("coder_id", "").strip() for r in rows}
    if len(coder_ids) != 1:
        errors.append(f"sheet must use exactly one stable coder_id, found {sorted(coder_ids)}")
        coder_id = ""
    else:
        coder_id = next(iter(coder_ids))
        if not CODER_ID_RE.fullmatch(coder_id):
            errors.append("coder_id must match C followed by 2 or 3 digits")
        if expected_coder and coder_id != expected_coder:
            errors.append(f"coder_id mismatch: expected {expected_coder}, found {coder_id}")

    acts = allowed_acts()
    dims = dimension_fields(fields)
    seen_annotations: set[str] = set()

    for row in rows:
        item = row["item_id"]
        annotation_id = row.get("annotation_id", "").strip()
        expected_annotation = f"PDHD-CALANN-{coder_id}-{item}" if coder_id else ""
        if annotation_id != expected_annotation:
            errors.append(f"{item}: annotation_id must be {expected_annotation!r}")
        if annotation_id in seen_annotations:
            errors.append(f"{item}: duplicate annotation_id {annotation_id!r}")
        seen_annotations.add(annotation_id)

        access_problem = row.get("access_problem", "").strip()
        if len(access_problem) > 1000:
            errors.append(f"{item}: access_problem exceeds 1000 characters")
        if len(row.get("notes", "")) > 2000:
            errors.append(f"{item}: notes exceed 2000 characters; avoid source-text transcription")

        primary = row.get("pedagogical_act_primary", "").strip()
        secondary_raw = row.get("pedagogical_act_secondary", "").strip()
        secondary = [v.strip() for v in secondary_raw.split(";") if v.strip()]

        if primary and primary not in acts | {"none", "unclear"}:
            errors.append(f"{item}: invalid pedagogical_act_primary {primary!r}")
        if len(secondary) != len(set(secondary)):
            errors.append(f"{item}: duplicate pedagogical_act_secondary values")
        for value in secondary:
            if value not in acts:
                errors.append(f"{item}: invalid pedagogical_act_secondary {value!r}")
        if primary in secondary:
            errors.append(f"{item}: primary act must not be repeated as secondary")

        for field in dims:
            value = row.get(field, "").strip()
            if value and value not in {"0", "1"}:
                errors.append(f"{item}: {field} must be 0 or 1")

        controlled = [
            ("normativity", NORMATIVITY),
            ("actor", ACTORS),
            ("target", TARGETS),
            ("evidence_confidence", CONFIDENCE),
        ]
        for field, allowed in controlled:
            value = row.get(field, "").strip()
            if value and value not in allowed:
                errors.append(f"{item}: invalid {field} {value!r}")

        annotated_at = row.get("annotated_at", "").strip()
        if not parse_timestamp(annotated_at):
            errors.append(f"{item}: annotated_at must be ISO 8601 with an explicit timezone offset")

        # Normal completion requires every analytic decision field. An explicit
        # access/legibility problem is the only legitimate route to blanks.
        if not access_problem:
            if not primary:
                errors.append(f"{item}: primary act is required when no access_problem is recorded")
            for field in dims:
                if row.get(field, "").strip() not in {"0", "1"}:
                    errors.append(f"{item}: {field} is required when no access_problem is recorded")
            for field, _ in controlled:
                if not row.get(field, "").strip():
                    errors.append(f"{item}: {field} is required when no access_problem is recorded")
        else:
            # If a coder could still make some decisions despite the access
            # problem, those decisions are allowed but must remain controlled.
            pass

    return errors


def validate_file(path: Path, expected_coder: str | None = None) -> list[str]:
    rows, fields = read_csv(path)
    return validate_rows(rows, fields, expected_coder)


def self_test() -> int:
    # Import here to avoid coupling normal validation to the copy generator's CLI.
    from prepare_calibration_coder_copy import render

    acts = sorted(allowed_acts())
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)

        # Fully completed synthetic fixture exists only in a temporary directory.
        complete_path = td_path / "complete.csv"
        rows = list(csv.DictReader(StringIO(render("C01"))))
        fields = list(rows[0])
        for row in rows:
            row["pedagogical_act_primary"] = acts[0]
            for field in dimension_fields(fields):
                row[field] = "0"
            row["normativity"] = "unclear"
            row["actor"] = "unclear"
            row["target"] = "unclear"
            row["evidence_confidence"] = "low"
            row["annotated_at"] = "2026-09-08T00:00:00-06:00"
        with complete_path.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        assert not validate_file(complete_path, "C01")

        # Access-problem fixture legitimately leaves analytic decisions blank.
        access_path = td_path / "access.csv"
        rows = list(csv.DictReader(StringIO(render("C02"))))
        fields = list(rows[0])
        for row in rows:
            row["access_problem"] = "primary source unavailable in coder environment"
            row["annotated_at"] = "2026-09-08T00:00:00Z"
        with access_path.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        assert not validate_file(access_path, "C02")

        # Structural mutation must be rejected.
        rows[0]["fragment_id"] = "PDHD-F999999"
        bad_path = td_path / "bad.csv"
        with bad_path.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        assert any("identity" in e or "structural" in e for e in validate_file(bad_path, "C02"))

    print("validate_completed_calibration_sheet self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("sheet", nargs="?", type=Path)
    parser.add_argument("--expected-coder")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.sheet:
        parser.error("a completed calibration sheet is required unless --self-test is used")
    if args.expected_coder and not CODER_ID_RE.fullmatch(args.expected_coder):
        parser.error("--expected-coder must match C followed by 2 or 3 digits")
    if not args.sheet.exists():
        parser.error(f"sheet not found: {args.sheet}")

    errors = validate_file(args.sheet, args.expected_coder)
    if errors:
        for message in errors:
            print(f"ERROR: {message}")
        return 1
    print(f"PDHD completed calibration sheet checks passed: {args.sheet}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
