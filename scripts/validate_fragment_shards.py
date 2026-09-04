#!/usr/bin/env python3
"""Validate the union of PDHD pilot locator and frozen-fragment shards."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data/samples"
ERRORS: list[str] = []

LOCATOR_FREEZE_STATES = {
    "locator_candidate",
    "locator_resolved_text_package_pending",
    "frozen",
}
TRANSCRIPTION_STATES = {
    "source_text_verified",
    "ocr_human_corrected",
    "ocr_unverified",
    "manual_transcription_unverified",
    "not_transcribed",
    "not_started",
}
PUBLIC_TEXT_STATES = {
    "public_text_permitted",
    "short_excerpt_only",
    "coder_local_text",
    "metadata_only",
    "access_unresolved",
}
SELECTION_ROLES = {
    "explicit_pedagogical_act",
    "institutional_relation",
    "source_criticism_salient",
    "control",
}
SLOTS = ("A", "B", "C", "D")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def load_shards(pattern: str) -> tuple[list[dict[str, str]], list[str]]:
    rows: list[dict[str, str]] = []
    names: list[str] = []
    for path in sorted(SAMPLES.glob(pattern)):
        names.append(path.name)
        for row in read_csv(path):
            row["__shard"] = path.name
            rows.append(row)
    return rows, names


def expected_manifest() -> dict[str, tuple[str, str]]:
    pilot = read_csv(SAMPLES / "pilot_document_selection_0_1.csv")
    if len(pilot) != 24:
        ERRORS.append(f"pilot selection must contain 24 documents; found {len(pilot)}")
    expected: dict[str, tuple[str, str]] = {}
    for row in pilot:
        try:
            order = int(row["selection_order"])
        except ValueError:
            ERRORS.append(f"invalid selection_order {row.get('selection_order')!r}")
            continue
        doc_id = row.get("document_id", "").strip()
        first = (order - 1) * 4 + 1
        for offset, slot in enumerate(SLOTS):
            expected[f"PDHD-F{first + offset:06d}"] = (doc_id, slot)
    return expected


def unique_index(rows: list[dict[str, str]], label: str) -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}
    for row in rows:
        fid = row.get("fragment_id", "").strip()
        if not re.fullmatch(r"PDHD-F\d{6}", fid):
            ERRORS.append(f"{label}: invalid fragment_id {fid!r} in {row.get('__shard')}")
            continue
        if fid in index:
            ERRORS.append(
                f"{label}: duplicate fragment_id {fid} across {index[fid].get('__shard')} and {row.get('__shard')}"
            )
        index[fid] = row
    return index


def main() -> int:
    expected = expected_manifest()
    locator_rows, locator_shards = load_shards("fragment_locator_progress*.csv")
    frozen_rows, frozen_shards = load_shards("frozen_fragments*.csv")

    if not locator_shards:
        ERRORS.append("no locator-progress shards found")
    if not frozen_shards:
        ERRORS.append("no frozen-fragment shards found")

    locators = unique_index(locator_rows, "locator union")
    frozen = unique_index(frozen_rows, "frozen union")

    for fid, row in locators.items():
        if fid not in expected:
            ERRORS.append(f"locator union: {fid} is outside the pilot manifest")
            continue
        expected_doc, expected_slot = expected[fid]
        if row.get("document_id", "").strip() != expected_doc:
            ERRORS.append(f"locator union: document mismatch for {fid}")
        if row.get("slot", "").strip() != expected_slot:
            ERRORS.append(f"locator union: slot mismatch for {fid}")
        for field in ("page", "source_locator", "locator_evidence_url", "checked_at"):
            if not row.get(field, "").strip():
                ERRORS.append(f"locator union: missing {field} for {fid}")
        state = row.get("freeze_status", "").strip()
        if state not in LOCATOR_FREEZE_STATES:
            ERRORS.append(f"locator union: invalid freeze_status {state!r} for {fid}")
        if state == "frozen":
            if row.get("boundary_status", "").strip() != "fixed":
                ERRORS.append(f"locator union: frozen {fid} lacks fixed boundary")
            if fid not in frozen:
                ERRORS.append(f"locator union: frozen {fid} lacks frozen-registry row")

    for fid, row in frozen.items():
        if fid not in expected:
            ERRORS.append(f"frozen union: {fid} is outside the pilot manifest")
            continue
        if fid not in locators:
            ERRORS.append(f"frozen union: {fid} lacks locator row")
            continue
        locator = locators[fid]
        expected_doc, expected_slot = expected[fid]
        if row.get("document_id", "").strip() != expected_doc:
            ERRORS.append(f"frozen union: document mismatch for {fid}")
        if row.get("slot", "").strip() != expected_slot:
            ERRORS.append(f"frozen union: slot mismatch for {fid}")
        for field in (
            "page",
            "source_locator",
            "locator_evidence_url",
            "boundary_definition",
            "access_basis",
            "preparation_note",
            "checked_at",
        ):
            if not row.get(field, "").strip():
                ERRORS.append(f"frozen union: missing {field} for {fid}")
        for field in ("page", "source_locator", "locator_evidence_url"):
            if row.get(field, "").strip() != locator.get(field, "").strip():
                ERRORS.append(f"frozen union: {field} mismatch for {fid}")
        if row.get("transcription_status", "").strip() not in TRANSCRIPTION_STATES:
            ERRORS.append(f"frozen union: invalid transcription_status for {fid}")
        if row.get("public_text_status", "").strip() not in PUBLIC_TEXT_STATES:
            ERRORS.append(f"frozen union: invalid public_text_status for {fid}")
        if row.get("selection_role", "").strip() not in SELECTION_ROLES:
            ERRORS.append(f"frozen union: invalid selection_role for {fid}")
        if row.get("freeze_status", "").strip() != "frozen":
            ERRORS.append(f"frozen union: registry row {fid} is not frozen")
        if locator.get("freeze_status", "").strip() != "frozen":
            ERRORS.append(f"frozen union: corresponding locator {fid} is not frozen")

    frozen_locator_ids = {
        fid for fid, row in locators.items() if row.get("freeze_status", "").strip() == "frozen"
    }
    if frozen_locator_ids != set(frozen):
        ERRORS.append(
            "frozen fragment ID set differs between locator shards and frozen-registry shards"
        )

    if len(locators) > 96:
        ERRORS.append(f"locator union exceeds pilot manifest: {len(locators)} > 96")
    if len(frozen) > len(locators):
        ERRORS.append("frozen union cannot exceed locator union")

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "PDHD fragment-shard checks passed "
        f"({len(locator_shards)} locator shards; {len(locators)}/96 located; "
        f"{len(frozen_shards)} frozen shards; {len(frozen)}/96 frozen)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
