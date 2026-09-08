#!/usr/bin/env python3
"""Build the deterministic 84-fragment PDHD-U1 reliability reserve.

The reserve is the exact complement of the 12-item human calibration set within
the already frozen 96-fragment pilot. It locks sample identity before any human
labels exist, but it is not yet the formal reliability package and carries no
independent-round codebook version.
"""
from __future__ import annotations

import argparse
import csv
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data" / "samples"
OUT = SAMPLES / "reliability_reserve_0_1.csv"
SLOTS = ("A", "B", "C", "D")
RESERVE_VERSION = "PDHD-RR-0.1-20260907"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def fragment_id(selection_order: int, slot: str) -> str:
    return f"PDHD-F{((selection_order - 1) * 4 + 1 + SLOTS.index(slot)):06d}"


def frozen_union() -> set[str]:
    frozen: set[str] = set()
    for path in sorted(SAMPLES.glob("frozen_fragments*.csv")):
        for row in read_csv(path):
            fid = row["fragment_id"]
            if fid in frozen:
                raise RuntimeError(f"duplicate frozen fragment across shards: {fid}")
            frozen.add(fid)
    return frozen


def expected_rows() -> list[dict[str, str]]:
    calibration = {r["fragment_id"] for r in read_csv(SAMPLES / "calibration_manifest_0_1.csv")}
    selected = [r for r in read_csv(SAMPLES / "pilot_document_selection_0_1.csv") if r["status"] == "selected"]

    rows: list[dict[str, str]] = []
    for doc in sorted(selected, key=lambda r: int(r["selection_order"])):
        order = int(doc["selection_order"])
        for slot in SLOTS:
            fid = fragment_id(order, slot)
            if fid in calibration:
                continue
            rows.append(
                {
                    "reserve_order": str(len(rows) + 1),
                    "fragment_id": fid,
                    "document_id": doc["document_id"],
                    "selection_order": doc["selection_order"],
                    "era_code": doc["era_code"],
                    "slot": slot,
                    "reserve_version": RESERVE_VERSION,
                    "selection_basis": "exact_complement_of_calibration_within_frozen_96",
                    "status": "reserved_for_formal_reliability_after_codebook_freeze",
                }
            )

    reserve = {r["fragment_id"] for r in rows}
    frozen = frozen_union()
    if len(calibration) != 12:
        raise RuntimeError(f"expected 12 calibration fragments, got {len(calibration)}")
    if len(rows) != 84:
        raise RuntimeError(f"expected 84 reserve fragments, got {len(rows)}")
    if len(reserve) != 84:
        raise RuntimeError("duplicate fragment in reliability reserve")
    if calibration & reserve:
        raise RuntimeError("calibration/reliability reserve overlap")
    if calibration | reserve != frozen:
        missing = sorted(frozen - (calibration | reserve))
        extra = sorted((calibration | reserve) - frozen)
        raise RuntimeError(f"calibration plus reserve does not equal frozen union; missing={missing} extra={extra}")
    if len(frozen) != 96:
        raise RuntimeError(f"expected frozen union of 96 fragments, got {len(frozen)}")
    return rows


FIELDS = [
    "reserve_order",
    "fragment_id",
    "document_id",
    "selection_order",
    "era_code",
    "slot",
    "reserve_version",
    "selection_basis",
    "status",
]


def render() -> str:
    buf = StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(expected_rows())
    return buf.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        actual = OUT.read_text(encoding="utf-8") if OUT.exists() else None
        if actual != expected:
            raise SystemExit("reliability reserve is not reproducible")
        print("PDHD reliability reserve check passed (84 fragments; exact frozen complement; zero calibration overlap)")
        return 0
    OUT.write_text(expected, encoding="utf-8")
    print(OUT.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
