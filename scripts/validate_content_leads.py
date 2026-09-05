#!/usr/bin/env python3
"""Validate pilot content leads and their explicit promotion crosswalk to fragment locators."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data/samples"
ERRORS: list[str] = []

EVIDENCE_STATES = {
    "secondary_issue_content_verified",
    "secondary_page_pointer_verified",
    "primary_contents_verified",
    "review_required",
}
PAGE_STATES = {"page_unresolved", "page_candidate_unverified", "page_resolved"}
PROMOTION_STATES = {
    "not_eligible_for_fragment_locator",
    "eligible_for_fragment_locator_review",
    "promoted_to_fragment_locator",
}
REQUIRED_COLUMNS = {
    "content_lead_id",
    "document_id",
    "content_title",
    "author",
    "content_type",
    "evidence_url",
    "evidence_status",
    "page_status",
    "promotion_status",
    "promoted_fragment_id",
    "checked_at",
    "note",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def csv_columns(path: Path) -> set[str]:
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return set(reader.fieldnames or [])


def load_locator_index() -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}
    for path in sorted(SAMPLES.glob("fragment_locator_progress*.csv")):
        for row in read_csv(path):
            fid = row.get("fragment_id", "").strip()
            if fid:
                index[fid] = row
    return index


def main() -> int:
    path = SAMPLES / "pilot_content_leads.csv"
    if not path.exists():
        print("PDHD content-lead checks skipped (no pilot_content_leads.csv)")
        return 0

    columns = csv_columns(path)
    missing_columns = sorted(REQUIRED_COLUMNS - columns)
    if missing_columns:
        ERRORS.append(
            "pilot_content_leads.csv lacks required columns: " + ", ".join(missing_columns)
        )

    leads = read_csv(path)
    docs = read_csv(ROOT / "data/catalog/documents.csv")
    balancing = ROOT / "data/catalog/documents_balancing_w1.csv"
    if balancing.exists():
        docs += read_csv(balancing)
    doc_ids = {row["document_id"] for row in docs}
    locators = load_locator_index()

    seen_leads: set[str] = set()
    promoted_ids: dict[str, str] = {}

    for row in leads:
        lead_id = row.get("content_lead_id", "").strip()
        if not re.fullmatch(r"PDHD-PL\d{6}", lead_id):
            ERRORS.append(f"invalid content_lead_id {lead_id!r}")
        if lead_id in seen_leads:
            ERRORS.append(f"duplicate content_lead_id {lead_id}")
        seen_leads.add(lead_id)

        doc_id = row.get("document_id", "").strip()
        if doc_id not in doc_ids:
            ERRORS.append(f"{lead_id}: unknown document_id {doc_id}")

        for field in ("content_title", "content_type", "evidence_url", "checked_at", "note"):
            if not row.get(field, "").strip():
                ERRORS.append(f"{lead_id}: missing {field}")

        evidence_status = row.get("evidence_status", "").strip()
        page_status = row.get("page_status", "").strip()
        promotion_status = row.get("promotion_status", "").strip()
        promoted_fragment_id = row.get("promoted_fragment_id", "").strip()

        if evidence_status not in EVIDENCE_STATES:
            ERRORS.append(f"{lead_id}: invalid evidence_status {evidence_status!r}")
        if page_status not in PAGE_STATES:
            ERRORS.append(f"{lead_id}: invalid page_status {page_status!r}")
        if promotion_status not in PROMOTION_STATES:
            ERRORS.append(f"{lead_id}: invalid promotion_status {promotion_status!r}")

        if page_status == "page_unresolved" and promotion_status != "not_eligible_for_fragment_locator":
            ERRORS.append(
                f"{lead_id}: page-unresolved content cannot be eligible for fragment-locator promotion"
            )

        if promotion_status == "promoted_to_fragment_locator":
            if page_status != "page_resolved":
                ERRORS.append(
                    f"{lead_id}: promoted content must have page_status=page_resolved"
                )
            if not re.fullmatch(r"PDHD-F\d{6}", promoted_fragment_id):
                ERRORS.append(
                    f"{lead_id}: promoted content requires a valid promoted_fragment_id"
                )
                continue
            if promoted_fragment_id in promoted_ids:
                ERRORS.append(
                    f"{lead_id}: promoted_fragment_id {promoted_fragment_id} is already linked from "
                    f"{promoted_ids[promoted_fragment_id]}"
                )
            else:
                promoted_ids[promoted_fragment_id] = lead_id

            locator = locators.get(promoted_fragment_id)
            if locator is None:
                ERRORS.append(
                    f"{lead_id}: promoted_fragment_id {promoted_fragment_id} is absent from locator shards"
                )
            elif locator.get("document_id", "").strip() != doc_id:
                ERRORS.append(
                    f"{lead_id}: document mismatch between lead {doc_id} and locator "
                    f"{promoted_fragment_id} ({locator.get('document_id', '').strip()})"
                )
        elif promoted_fragment_id:
            ERRORS.append(
                f"{lead_id}: promoted_fragment_id must be empty unless promotion_status is promoted_to_fragment_locator"
            )

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "PDHD content-lead checks passed "
        f"({len(leads)} leads; {len(promoted_ids)} explicit lead-to-fragment promotions)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
