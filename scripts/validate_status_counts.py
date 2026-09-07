#!/usr/bin/env python3
"""Fail when public PDHD-U1 status counts drift from the fragment shards.

The fragment CSVs are the source of truth. This validator keeps the two public
status surfaces (README.md and docs/PDHD_U1_COHORT_STATUS.md) synchronized with
that source of truth so a new locator/frozen shard cannot silently leave stale
scientific counts in the documentation.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data/samples"
TARGET = 96
ERRORS: list[str] = []


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def union_ids(pattern: str) -> set[str]:
    ids: set[str] = set()
    for path in sorted(SAMPLES.glob(pattern)):
        for row in read_csv(path):
            fid = row.get("fragment_id", "").strip()
            if fid:
                ids.add(fid)
    return ids


def extract_one(text: str, pattern: str, label: str) -> int | None:
    matches = re.findall(pattern, text, flags=re.MULTILINE)
    if len(matches) != 1:
        ERRORS.append(f"{label}: expected exactly one canonical count marker; found {len(matches)}")
        return None
    return int(matches[0])


def expect(value: int | None, actual: int, label: str) -> None:
    if value is not None and value != actual:
        ERRORS.append(f"{label}: documentation says {value}; shards say {actual}")


def validate_readme(text: str, located: int, frozen: int, gaps: int) -> None:
    not_frozen = located - frozen
    expect(
        extract_one(
            text,
            r"\| Slots con localizador candidato/resuelto \| \*\*(\d+) / 96\*\* \|",
            "README located table",
        ),
        located,
        "README located table",
    )
    expect(
        extract_one(
            text,
            r"\| Fragmentos completamente congelados \| \*\*(\d+) / 96\*\* \|",
            "README frozen table",
        ),
        frozen,
        "README frozen table",
    )
    expect(
        extract_one(
            text,
            r"su unión contiene \*\*(\d+)/96\*\* slots",
            "README locator-union prose",
        ),
        located,
        "README locator-union prose",
    )
    expect(
        extract_one(
            text,
            r"su unión contiene \*\*(\d+)/96\*\* fragmentos",
            "README frozen-union prose",
        ),
        frozen,
        "README frozen-union prose",
    )
    expect(
        extract_one(
            text,
            r"\*\*(\d+)/96 slots tienen ya un localizador documentado\.\*\*",
            "README next-gate located prose",
        ),
        located,
        "README next-gate located prose",
    )
    expect(
        extract_one(
            text,
            r"\*\*(\d+) localizadores todavía no congelados\*\*",
            "README located-not-frozen prose",
        ),
        not_frozen,
        "README located-not-frozen prose",
    )
    expect(
        extract_one(
            text,
            r"Los \*\*(\d+)/96\*\* congelados demuestran el pipeline",
            "README frozen pipeline prose",
        ),
        frozen,
        "README frozen pipeline prose",
    )
    expect(
        extract_one(
            text,
            r"Quedan \*\*(\d+) slots sin localizador\*\*",
            "README gap prose",
        ),
        gaps,
        "README gap prose",
    )


def validate_cohort_status(text: str, located: int, frozen: int, gaps: int, complete_batches: int) -> None:
    not_frozen = located - frozen
    expect(
        extract_one(
            text,
            r"\| Fragment locator rows resolved/candidate \| \*\*(\d+) / 96\*\* \|",
            "cohort located table",
        ),
        located,
        "cohort located table",
    )
    expect(
        extract_one(
            text,
            r"\| Fully frozen fragments \| \*\*(\d+) / 96\*\* \|",
            "cohort frozen table",
        ),
        frozen,
        "cohort frozen table",
    )
    expect(
        extract_one(
            text,
            r"now has \*\*(\d+) of the 96 deterministic reliability slots\*\*",
            "cohort headline prose",
        ),
        located,
        "cohort headline prose",
    )
    expect(
        extract_one(
            text,
            r"contains \*\*(\d+)/96\*\* pilot slots",
            "cohort locator-union prose",
        ),
        located,
        "cohort locator-union prose",
    )
    expect(
        extract_one(
            text,
            r"remaining \*\*(\d+)\*\* located rows",
            "cohort located-not-frozen prose",
        ),
        not_frozen,
        "cohort located-not-frozen prose",
    )
    expect(
        extract_one(
            text,
            r"\*\*(\d+) slots remain without a locator\.\*\*",
            "cohort gap prose",
        ),
        gaps,
        "cohort gap prose",
    )
    expect(
        extract_one(
            text,
            r"project is now at \*\*(\d+)/96 localized\*\*",
            "cohort decision prose",
        ),
        located,
        "cohort decision prose",
    )
    expect(
        extract_one(
            text,
            r"project is now at \*\*\d+/96 localized\*\* and \*\*(\d+)/96 frozen\*\*",
            "cohort decision frozen prose",
        ),
        frozen,
        "cohort decision frozen prose",
    )
    expect(
        extract_one(
            text,
            r"preserving the unlocalized complement at (\d+)\.",
            "cohort decision gap prose",
        ),
        gaps,
        "cohort decision gap prose",
    )
    expect(
        extract_one(
            text,
            r"\*\*(\d+) selected documents\*\* now have complete four-slot batches\.",
            "cohort complete-batch prose",
        ),
        complete_batches,
        "cohort complete-batch prose",
    )


def main() -> int:
    locators = union_ids("fragment_locator_progress*.csv")
    frozen = union_ids("frozen_fragments*.csv")
    gaps = read_csv(SAMPLES / "fragment_gap_queue_0_1.csv")

    frozen_slots: dict[str, set[str]] = {}
    for path in sorted(SAMPLES.glob("frozen_fragments*.csv")):
        for row in read_csv(path):
            frozen_slots.setdefault(row.get("document_id", "").strip(), set()).add(row.get("slot", "").strip())
    complete_batches = sum(slots == {"A", "B", "C", "D"} for slots in frozen_slots.values())

    located_count = len(locators)
    frozen_count = len(frozen)
    gap_count = len(gaps)

    if located_count + gap_count != TARGET:
        ERRORS.append(
            f"source-of-truth counts are inconsistent: {located_count} located + "
            f"{gap_count} gaps != {TARGET}"
        )
    if not frozen.issubset(locators):
        ERRORS.append("source-of-truth counts are inconsistent: frozen IDs are not a locator subset")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    cohort = (ROOT / "docs/PDHD_U1_COHORT_STATUS.md").read_text(encoding="utf-8")
    validate_readme(readme, located_count, frozen_count, gap_count)
    validate_cohort_status(cohort, located_count, frozen_count, gap_count, complete_batches)

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "PDHD public status counts match fragment shards "
        f"({located_count}/{TARGET} located; {frozen_count}/{TARGET} frozen; "
        f"{gap_count}/{TARGET} unlocated)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
