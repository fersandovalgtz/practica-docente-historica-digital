#!/usr/bin/env python3
"""Build a leakage-aware 96-item manifest for experimental machine annotation.

The manifest deliberately excludes researcher-facing selection roles, semantic
locator slugs and preparation notes. Only calibration items currently have
neutral boundary instructions. Remaining items stay blocked rather than leaking
selection semantics into model inputs.
"""
from __future__ import annotations

import argparse
import csv
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data/samples"
DEFAULT_OUT = ROOT / "artifacts/machine/machine_input_manifest_0_1.csv"
CODEBOOK = "PDHD-CB-0.2-calibration"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def frozen_union() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for path in sorted(SAMPLES.glob("frozen_fragments*.csv")):
        for row in read_csv(path):
            fid = row["fragment_id"]
            if fid in result:
                raise RuntimeError(f"duplicate frozen fragment {fid}")
            result[fid] = row
    if len(result) != 96:
        raise RuntimeError(f"expected 96 frozen fragments, found {len(result)}")
    return result


def rows() -> list[dict[str, str]]:
    frozen = frozen_union()
    neutral = {r["fragment_id"]: r["boundary_instruction"] for r in read_csv(SAMPLES / "calibration_coder_sheet_0_1.csv")}
    result: list[dict[str, str]] = []
    for index, fid in enumerate(sorted(frozen, key=lambda x: int(x.removeprefix("PDHD-F"))), 1):
        source = frozen[fid]
        boundary = neutral.get(fid, "")
        status = "ready_neutral_boundary" if boundary else "blocked_pending_neutral_boundary"
        result.append({
            "machine_item_id": f"MACH{index:03d}",
            "fragment_id": fid,
            "document_id": source["document_id"],
            "page": source.get("page", ""),
            "source_url": source.get("locator_evidence_url", ""),
            "neutral_boundary_instruction": boundary,
            "codebook_version": CODEBOOK,
            "input_status": status,
            "leakage_policy": "exclude_selection_role_source_locator_preparation_note",
        })
    ready = sum(r["input_status"] == "ready_neutral_boundary" for r in result)
    blocked = sum(r["input_status"] == "blocked_pending_neutral_boundary" for r in result)
    if (len(result), ready, blocked) != (96, 12, 84):
        raise RuntimeError(f"unexpected machine-input state: total={len(result)} ready={ready} blocked={blocked}")
    return result


FIELDS = [
    "machine_item_id", "fragment_id", "document_id", "page", "source_url",
    "neutral_boundary_instruction", "codebook_version", "input_status", "leakage_policy"
]


def render() -> str:
    buf = StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader(); writer.writerows(rows())
    return buf.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--check-state", action="store_true")
    args = parser.parse_args()
    built = rows()
    ready = sum(r["input_status"] == "ready_neutral_boundary" for r in built)
    blocked = len(built) - ready
    if args.check_state:
        print(f"PDHD machine input gate valid: {len(built)} total = {ready} leakage-safe + {blocked} blocked")
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(), encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
