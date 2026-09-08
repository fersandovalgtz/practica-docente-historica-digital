#!/usr/bin/env python3
"""Compare two validated PDHD-U1 human calibration first-pass sheets.

The output is diagnostic only. It records agreements/disagreements and never
adjudicates, changes labels, freezes a codebook, or creates a gold label.
"""
from __future__ import annotations

import argparse
import csv
import json
import tempfile
from collections import Counter
from io import StringIO
from pathlib import Path

from validate_completed_calibration_sheet import (
    dimension_fields,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[1]

SINGLE_FIELDS = [
    "pedagogical_act_primary",
    "pedagogical_act_secondary",
    "normativity",
    "actor",
    "target",
    "evidence_confidence",
]


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader), list(reader.fieldnames or [])


def secondary_set(value: str) -> tuple[str, ...]:
    return tuple(sorted(v.strip() for v in value.split(";") if v.strip()))


def normalized(field: str, value: str) -> object:
    value = value.strip()
    if field == "pedagogical_act_secondary":
        return secondary_set(value)
    return value


def compare(sheet_a: Path, sheet_b: Path) -> dict[str, object]:
    errors_a = validate_file(sheet_a)
    errors_b = validate_file(sheet_b)
    if errors_a or errors_b:
        messages = []
        messages.extend(f"A: {e}" for e in errors_a)
        messages.extend(f"B: {e}" for e in errors_b)
        raise ValueError("invalid calibration input sheets:\n" + "\n".join(messages))

    rows_a, fields_a = read_csv(sheet_a)
    rows_b, fields_b = read_csv(sheet_b)
    if fields_a != fields_b:
        raise ValueError("validated calibration sheets have different headers")

    coder_a = rows_a[0]["coder_id"].strip()
    coder_b = rows_b[0]["coder_id"].strip()
    if coder_a == coder_b:
        raise ValueError("calibration comparison requires two distinct coder IDs")

    dims = dimension_fields(fields_a)
    analytic_fields = [*SINGLE_FIELDS, *dims]
    field_counts: dict[str, Counter[str]] = {
        field: Counter(agreement=0, disagreement=0, unavailable=0)
        for field in analytic_fields
    }
    item_reports: list[dict[str, object]] = []

    for a, b in zip(rows_a, rows_b):
        if a["item_id"] != b["item_id"] or a["fragment_id"] != b["fragment_id"]:
            raise ValueError("validated sheets unexpectedly differ in item identity/order")

        access_a = a.get("access_problem", "").strip()
        access_b = b.get("access_problem", "").strip()
        differences: list[dict[str, object]] = []
        agreements: list[str] = []
        unavailable: list[str] = []

        for field in analytic_fields:
            va = normalized(field, a.get(field, ""))
            vb = normalized(field, b.get(field, ""))
            # An explicit access problem may legitimately leave analytic fields
            # blank. Those cells are tracked separately rather than treated as
            # semantic disagreement.
            if va == "" or vb == "" or va == () or vb == ():
                if field == "pedagogical_act_secondary":
                    # Empty secondary acts are a valid analytic decision when
                    # both coders otherwise had access to the fragment.
                    if not access_a and not access_b and va == vb:
                        field_counts[field]["agreement"] += 1
                        agreements.append(field)
                        continue
                if access_a or access_b:
                    field_counts[field]["unavailable"] += 1
                    unavailable.append(field)
                    continue

            if va == vb:
                field_counts[field]["agreement"] += 1
                agreements.append(field)
            else:
                field_counts[field]["disagreement"] += 1
                differences.append(
                    {
                        "field": field,
                        coder_a: list(va) if isinstance(va, tuple) else va,
                        coder_b: list(vb) if isinstance(vb, tuple) else vb,
                    }
                )

        item_reports.append(
            {
                "item_id": a["item_id"],
                "fragment_id": a["fragment_id"],
                "access_problem": {
                    coder_a: access_a or None,
                    coder_b: access_b or None,
                },
                "agreement_fields": agreements,
                "unavailable_fields": unavailable,
                "disagreements": differences,
            }
        )

    field_summary: dict[str, dict[str, object]] = {}
    total_disagreements = 0
    for field, counts in field_counts.items():
        comparable = counts["agreement"] + counts["disagreement"]
        total_disagreements += counts["disagreement"]
        field_summary[field] = {
            "agreement": counts["agreement"],
            "disagreement": counts["disagreement"],
            "unavailable": counts["unavailable"],
            "comparable": comparable,
            "observed_agreement": (counts["agreement"] / comparable) if comparable else None,
        }

    return {
        "report_type": "calibration_disagreement_diagnostic_not_formal_reliability",
        "coders": [coder_a, coder_b],
        "items": len(rows_a),
        "fields_compared": len(analytic_fields),
        "total_field_disagreements": total_disagreements,
        "field_summary": field_summary,
        "item_diagnostics": item_reports,
        "adjudicated": False,
        "gold_labels_created": False,
    }


def self_test() -> int:
    from prepare_calibration_coder_copy import render
    from validate_completed_calibration_sheet import allowed_acts

    act = sorted(allowed_acts())[0]
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        paths = []
        for coder in ("C01", "C02"):
            rows = list(csv.DictReader(StringIO(render(coder))))
            fields = list(rows[0])
            for row in rows:
                row["pedagogical_act_primary"] = act
                for field in dimension_fields(fields):
                    row[field] = "0"
                row["normativity"] = "unclear"
                row["actor"] = "unclear"
                row["target"] = "unclear"
                row["evidence_confidence"] = "low"
                row["annotated_at"] = "2026-09-07T18:00:00-06:00"
            path = root / f"{coder}.csv"
            with path.open("w", encoding="utf-8", newline="") as fh:
                writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
                writer.writeheader()
                writer.writerows(rows)
            paths.append(path)

        perfect = compare(paths[0], paths[1])
        assert perfect["total_field_disagreements"] == 0
        assert perfect["adjudicated"] is False
        assert perfect["gold_labels_created"] is False

        rows, fields = read_csv(paths[1])
        rows[0]["normativity"] = "prescriptive"
        with paths[1].open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        changed = compare(paths[0], paths[1])
        assert changed["total_field_disagreements"] == 1
        assert changed["field_summary"]["normativity"]["disagreement"] == 1

    print("compare_calibration_sheets self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("sheet_a", nargs="?", type=Path)
    parser.add_argument("sheet_b", nargs="?", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.sheet_a or not args.sheet_b:
        parser.error("two completed calibration sheets are required unless --self-test is used")
    if not args.sheet_a.exists() or not args.sheet_b.exists():
        parser.error("both calibration sheet paths must exist")

    try:
        result = compare(args.sheet_a, args.sheet_b)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(args.output)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
