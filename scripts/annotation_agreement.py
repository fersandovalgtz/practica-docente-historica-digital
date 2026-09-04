#!/usr/bin/env python3
"""Compute pilot annotation agreement with standard-library Python only.

Supports nominal Krippendorff alpha for single-label fields and per-dimension
binary alpha plus pairwise Jaccard diagnostics for multi-label dimensions.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

MISSING = {"", "NA", "N/A", "null", "None"}
SINGLE_FIELDS = [
    "pedagogical_act_primary",
    "normativity",
    "actor",
    "target",
    "evidence_confidence",
]


def clean(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.strip()
    return None if value in MISSING else value


def krippendorff_alpha_nominal(units: Iterable[list[str | None]]) -> float | None:
    """Return Krippendorff's alpha for nominal data.

    Coincidences are accumulated with the standard unit-size correction
    1/(m_u - 1), allowing varying coder counts and missing values.
    """
    coincidence: dict[tuple[str, str], float] = defaultdict(float)

    for ratings in units:
        vals = [v for v in ratings if v is not None]
        m = len(vals)
        if m < 2:
            continue
        weight = 1.0 / (m - 1)
        for i, vi in enumerate(vals):
            for j, vj in enumerate(vals):
                if i == j:
                    continue
                coincidence[(vi, vj)] += weight

    n = sum(coincidence.values())
    if n <= 1:
        return None

    marginals: Counter[str] = Counter()
    observed_disagreement = 0.0
    for (vi, vj), value in coincidence.items():
        marginals[vi] += value
        if vi != vj:
            observed_disagreement += value

    do = observed_disagreement / n

    expected_disagreement = 0.0
    labels = list(marginals)
    for vi in labels:
        for vj in labels:
            if vi != vj:
                expected_disagreement += marginals[vi] * marginals[vj]
    de = expected_disagreement / (n * (n - 1))

    if de == 0:
        return 1.0 if do == 0 else None
    return 1.0 - (do / de)


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def group_by_fragment(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        fragment_id = clean(row.get("fragment_id"))
        coder_id = clean(row.get("coder_id"))
        if not fragment_id or not coder_id:
            continue
        grouped[fragment_id].append(row)
    return grouped


def alpha_for_field(grouped: dict[str, list[dict[str, str]]], field: str) -> float | None:
    units = [[clean(row.get(field)) for row in rows] for rows in grouped.values()]
    return krippendorff_alpha_nominal(units)


def dimension_columns(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return []
    return sorted(c for c in rows[0] if c.startswith("dimension_"))


def normalize_binary(value: str | None) -> str | None:
    value = clean(value)
    if value is None:
        return None
    lowered = value.lower()
    if lowered in {"1", "true", "yes", "y", "sí", "si"}:
        return "1"
    if lowered in {"0", "false", "no", "n"}:
        return "0"
    raise ValueError(f"Invalid binary dimension value: {value!r}")


def alpha_for_dimension(
    grouped: dict[str, list[dict[str, str]]], field: str
) -> float | None:
    units = [
        [normalize_binary(row.get(field)) for row in rows]
        for rows in grouped.values()
    ]
    return krippendorff_alpha_nominal(units)


def pairwise_jaccard(
    grouped: dict[str, list[dict[str, str]]], dims: list[str]
) -> dict[str, float | int | None]:
    scores: list[float] = []
    for rows in grouped.values():
        for a, b in itertools.combinations(rows, 2):
            set_a = {d for d in dims if normalize_binary(a.get(d)) == "1"}
            set_b = {d for d in dims if normalize_binary(b.get(d)) == "1"}
            union = set_a | set_b
            score = 1.0 if not union else len(set_a & set_b) / len(union)
            scores.append(score)
    return {
        "pair_count": len(scores),
        "mean_jaccard": (sum(scores) / len(scores)) if scores else None,
    }


def confusion_pairs(
    grouped: dict[str, list[dict[str, str]]], field: str
) -> list[dict[str, object]]:
    counts: Counter[tuple[str, str]] = Counter()
    for rows in grouped.values():
        values = [clean(r.get(field)) for r in rows]
        values = [v for v in values if v is not None]
        for a, b in itertools.combinations(values, 2):
            if a != b:
                counts[tuple(sorted((a, b)))] += 1
    return [
        {"labels": list(pair), "count": count}
        for pair, count in counts.most_common()
    ]


def report(path: Path) -> dict[str, object]:
    rows = load_rows(path)
    grouped = group_by_fragment(rows)
    dims = dimension_columns(rows)

    single = {
        field: {
            "alpha": alpha_for_field(grouped, field),
            "confusions": confusion_pairs(grouped, field),
        }
        for field in SINGLE_FIELDS
        if rows and field in rows[0]
    }
    dimension_results = {
        field.removeprefix("dimension_"): alpha_for_dimension(grouped, field)
        for field in dims
    }

    coder_ids = sorted(
        {clean(r.get("coder_id")) for r in rows if clean(r.get("coder_id"))}
    )
    return {
        "input": str(path),
        "rows": len(rows),
        "fragments": len(grouped),
        "coders": coder_ids,
        "single_label": single,
        "dimensions": dimension_results,
        "dimension_set_overlap": pairwise_jaccard(grouped, dims),
    }


def self_test() -> None:
    perfect = [["a", "a"], ["b", "b"], ["a", "a"]]
    assert krippendorff_alpha_nominal(perfect) == 1.0

    mixed = [["a", "a"], ["b", "a"], ["a", "a"], ["b", "b"]]
    alpha = krippendorff_alpha_nominal(mixed)
    assert alpha is not None and -1.0 <= alpha <= 1.0

    missing = [["a", None], ["a", "a"], [None, "b"], ["b", "b"]]
    assert krippendorff_alpha_nominal(missing) == 1.0

    constant = [["a", "a"], ["a", "a"]]
    assert krippendorff_alpha_nominal(constant) == 1.0

    print("annotation_agreement self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0
    if args.csv is None:
        parser.error("CSV path is required unless --self-test is used")

    result = report(args.csv)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
