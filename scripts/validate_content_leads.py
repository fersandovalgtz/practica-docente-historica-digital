#!/usr/bin/env python3
"""Validate pilot content leads that are not yet page-level fragment locators."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

EVIDENCE_STATES = {"secondary_issue_content_verified", "primary_contents_verified", "review_required"}
PAGE_STATES = {"page_unresolved", "page_candidate_unverified", "page_resolved"}
PROMOTION_STATES = {
    "not_eligible_for_fragment_locator",
    "eligible_for_fragment_locator_review",
    "promoted_to_fragment_locator",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    path = ROOT / "data/samples/pilot_content_leads.csv"
    if not path.exists():
        print("PDHD content-lead checks skipped (no pilot_content_leads.csv)")
        return 0

    leads = read_csv(path)
    docs = read_csv(ROOT / "data/catalog/documents.csv")
    balancing = ROOT / "data/catalog/documents_balancing_w1.csv"
    if balancing.exists():
        docs += read_csv(balancing)
    doc_ids = {row["document_id"] for row in docs}

    seen: set[str] = set()
    for row in leads:
        lead_id = row.get("content_lead_id", "").strip()
        if not re.fullmatch(r"PDHD-PL\d{6}", lead_id):
            ERRORS.append(f"invalid content_lead_id {lead_id!r}")
        if lead_id in seen:
            ERRORS.append(f"duplicate content_lead_id {lead_id}")
        seen.add(lead_id)

        doc_id = row.get("document_id", "").strip()
        if doc_id not in doc_ids:
            ERRORS.append(f"{lead_id}: unknown document_id {doc_id}")

        for field in ("content_title", "content_type", "evidence_url", "checked_at", "note"):
            if not row.get(field, "").strip():
                ERRORS.append(f"{lead_id}: missing {field}")

        evidence_status = row.get("evidence_status", "").strip()
        page_status = row.get("page_status", "").strip()
        promotion_status = row.get("promotion_status", "").strip()
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

    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"PDHD content-lead checks passed ({len(leads)} leads)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
