#!/usr/bin/env python3
"""Validate the PDHD-U1 direct-primary freeze-conversion priority queue."""
from __future__ import annotations

import csv
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data/samples"
QUEUE = SAMPLES / "freeze_conversion_queue_0_1.csv"
RETRIEVAL_ATTEMPTS = SAMPLES / "retrieval_attempts.csv"
ERRORS: list[str] = []

REQUIRED_COLUMNS = (
    "fragment_id",
    "document_id",
    "slot",
    "source_family",
    "current_state",
    "evidence_level",
    "primary_locator",
    "conversion_blocker",
    "required_action",
    "priority_group",
    "rationale",
    "reviewed_at",
)

DIRECT_PRIMARY_STATES = {
    "direct_primary_page_image_candidate",
    "direct_primary_ocr_region_image_check_pending",
    "direct_primary_reader_page_candidate",
    "direct_primary_reader_scan_candidate",
    "direct_primary_page_control_candidate",
}

EVIDENCE_LEVELS = {
    "L1_preboundary",
    "L1_retrieval_image_pending",
}

PRIORITIES = {"P1", "P2", "P3", "P4"}
SLOTS = {"A", "B", "C", "D"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def load_locator_union() -> dict[str, dict[str, str]]:
    locators: dict[str, dict[str, str]] = {}
    for path in sorted(SAMPLES.glob("fragment_locator_progress*.csv")):
        for row in read_csv(path):
            fid = row.get("fragment_id", "").strip()
            if not fid:
                continue
            if fid in locators:
                ERRORS.append(f"locator union contains duplicate {fid}")
            row["__shard"] = path.name
            locators[fid] = row
    return locators


def load_retrieval_coverage() -> dict[str, set[str]]:
    coverage: dict[str, set[str]] = {}
    if not RETRIEVAL_ATTEMPTS.exists():
        ERRORS.append("retrieval_attempts.csv is required for freeze-conversion work")
        return coverage

    for row in read_csv(RETRIEVAL_ATTEMPTS):
        attempt_id = row.get("attempt_id", "").strip()
        document_id = row.get("document_id", "").strip()
        for raw_fid in row.get("fragment_ids", "").split(";"):
            fid = raw_fid.strip()
            if not fid:
                continue
            coverage.setdefault(fid, set()).add(attempt_id)
            if not document_id:
                ERRORS.append(f"{attempt_id}: retrieval attempt lacks document_id")
    return coverage


def valid_iso_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def main() -> int:
    if not QUEUE.exists():
        print(f"ERROR: missing {QUEUE.relative_to(ROOT)}", file=sys.stderr)
        return 1

    with QUEUE.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        columns = tuple(reader.fieldnames or ())
        rows = list(reader)

    if columns != REQUIRED_COLUMNS:
        ERRORS.append(
            "freeze-conversion queue columns differ from the canonical schema: "
            f"expected {REQUIRED_COLUMNS!r}, found {columns!r}"
        )

    locators = load_locator_union()
    retrieval_coverage = load_retrieval_coverage()
    seen: set[str] = set()

    for row in rows:
        fid = row.get("fragment_id", "").strip()
        if not re.fullmatch(r"PDHD-F\d{6}", fid):
            ERRORS.append(f"invalid fragment_id {fid!r}")
            continue
        if fid in seen:
            ERRORS.append(f"duplicate freeze-conversion fragment_id {fid}")
        seen.add(fid)

        locator = locators.get(fid)
        if locator is None:
            ERRORS.append(f"{fid} is not present in the canonical locator union")
            continue

        document_id = row.get("document_id", "").strip()
        slot = row.get("slot", "").strip()
        current_state = row.get("current_state", "").strip()
        evidence_level = row.get("evidence_level", "").strip()
        priority = row.get("priority_group", "").strip()
        reviewed_at = row.get("reviewed_at", "").strip()

        if document_id != locator.get("document_id", "").strip():
            ERRORS.append(f"{fid}: document_id differs from canonical locator row")
        if slot != locator.get("slot", "").strip():
            ERRORS.append(f"{fid}: slot differs from canonical locator row")
        if slot not in SLOTS:
            ERRORS.append(f"{fid}: invalid slot {slot!r}")

        canonical_state = locator.get("boundary_status", "").strip()
        if current_state != canonical_state:
            ERRORS.append(
                f"{fid}: current_state {current_state!r} differs from locator boundary_status {canonical_state!r}"
            )
        if current_state not in DIRECT_PRIMARY_STATES:
            ERRORS.append(
                f"{fid}: state {current_state!r} is not eligible for the direct-primary conversion queue"
            )

        if locator.get("freeze_status", "").strip() == "frozen":
            ERRORS.append(f"{fid}: already frozen fragments must not remain in the conversion queue")

        if evidence_level not in EVIDENCE_LEVELS:
            ERRORS.append(f"{fid}: invalid evidence_level {evidence_level!r}")
        if priority not in PRIORITIES:
            ERRORS.append(f"{fid}: invalid priority_group {priority!r}")
        if not reviewed_at or not valid_iso_date(reviewed_at):
            ERRORS.append(f"{fid}: reviewed_at must be an ISO date")

        for field in (
            "source_family",
            "primary_locator",
            "conversion_blocker",
            "required_action",
            "rationale",
        ):
            if not row.get(field, "").strip():
                ERRORS.append(f"{fid}: missing {field}")

        if fid not in retrieval_coverage:
            ERRORS.append(
                f"{fid}: direct-primary conversion candidate lacks structured retrieval provenance"
            )

    eligible = {
        fid
        for fid, row in locators.items()
        if row.get("boundary_status", "").strip() in DIRECT_PRIMARY_STATES
        and row.get("freeze_status", "").strip() != "frozen"
    }
    if seen != eligible:
        missing = sorted(eligible - seen)
        stale = sorted(seen - eligible)
        if missing:
            ERRORS.append(
                "freeze-conversion queue omits eligible direct-primary candidates: "
                + ", ".join(missing)
            )
        if stale:
            ERRORS.append(
                "freeze-conversion queue contains rows no longer eligible for direct-primary conversion: "
                + ", ".join(stale)
            )

    # An empty queue is valid only when the canonical eligible set is also empty.
    # Completeness is enforced by the exact set equality above, so this does not
    # weaken the validator or permit an eligible candidate to disappear silently.

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    counts = {priority: 0 for priority in sorted(PRIORITIES)}
    for row in rows:
        counts[row["priority_group"].strip()] += 1
    distribution = ", ".join(f"{key}={value}" for key, value in counts.items())
    covered = sum(1 for fid in seen if fid in retrieval_coverage)
    print(
        "PDHD freeze-conversion queue checks passed "
        f"({len(rows)} complete direct-primary candidates; {covered}/{len(rows)} with retrieval provenance; {distribution})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
