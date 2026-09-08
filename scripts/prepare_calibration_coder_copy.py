#!/usr/bin/env python3
"""Prepare a coder-specific local copy of the PDHD-U1 calibration sheet.

This utility writes no human labels. It copies the canonical blind calibration
sheet, assigns one pseudonymous coder ID, and deterministically fills only the
annotation identifiers. Human response fields remain blank.
"""
from __future__ import annotations

import argparse
import csv
import re
import tempfile
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "data" / "samples" / "calibration_coder_sheet_0_1.csv"
CODER_ID_RE = re.compile(r"C\d{2,3}")


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader), list(reader.fieldnames or [])


def render(coder_id: str) -> str:
    if not CODER_ID_RE.fullmatch(coder_id):
        raise ValueError("coder_id must match C followed by 2 or 3 digits, e.g. C01")

    rows, fields = read_csv(MASTER)
    if len(rows) != 12:
        raise RuntimeError(f"canonical calibration sheet must contain 12 rows, found {len(rows)}")

    for row in rows:
        item_id = row.get("item_id", "").strip()
        if not re.fullmatch(r"CAL\d{3}", item_id):
            raise RuntimeError(f"unexpected calibration item_id {item_id!r}")
        # The canonical sheet itself must be blank before a coder copy is built.
        if row.get("annotation_id", "").strip() or row.get("coder_id", "").strip():
            raise RuntimeError("canonical calibration sheet already contains coder identity data")
        row["coder_id"] = coder_id
        row["annotation_id"] = f"PDHD-CALANN-{coder_id}-{item_id}"

    buf = StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def write_copy(coder_id: str, output: Path, allow_in_repo: bool) -> None:
    resolved = output.expanduser().resolve()
    if resolved == MASTER.resolve():
        raise ValueError("refusing to overwrite the canonical blind master sheet")
    if is_within(resolved, ROOT) and not allow_in_repo:
        raise ValueError(
            "refusing to write a coder working copy inside the repository by default; "
            "use a local path outside the repo or pass --allow-in-repo deliberately"
        )
    resolved.parent.mkdir(parents=True, exist_ok=True)
    if resolved.exists():
        raise FileExistsError(f"output already exists: {resolved}")
    resolved.write_text(render(coder_id), encoding="utf-8")
    print(resolved)


def self_test() -> int:
    text = render("C01")
    rows = list(csv.DictReader(StringIO(text)))
    assert len(rows) == 12
    assert {r["coder_id"] for r in rows} == {"C01"}
    assert rows[0]["annotation_id"] == "PDHD-CALANN-C01-CAL001"
    assert rows[-1]["annotation_id"] == "PDHD-CALANN-C01-CAL012"
    # No response fields may be filled by preparation.
    response_start = list(rows[0]).index("pedagogical_act_primary")
    response_fields = list(rows[0])[response_start:]
    assert all(not r[field].strip() for r in rows for field in response_fields)

    with tempfile.TemporaryDirectory() as td:
        target = Path(td) / "C02.csv"
        write_copy("C02", target, allow_in_repo=False)
        copied, _ = read_csv(target)
        assert {r["coder_id"] for r in copied} == {"C02"}
        assert copied[0]["annotation_id"] == "PDHD-CALANN-C02-CAL001"

    print("prepare_calibration_coder_copy self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coder-id")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--allow-in-repo", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.coder_id or not args.output:
        parser.error("--coder-id and --output are required unless --self-test is used")
    try:
        write_copy(args.coder_id, args.output, args.allow_in_repo)
    except (ValueError, RuntimeError, FileExistsError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
