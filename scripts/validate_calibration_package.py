#!/usr/bin/env python3
"""Validate PDHD-U1 calibration selection, blinding, and codebook provenance."""
from __future__ import annotations

import csv
import hashlib
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data" / "samples"
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_calibration_package as builder  # noqa: E402

ERRORS: list[str] = []


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def error(message: str) -> None:
    ERRORS.append(message)


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def main() -> int:
    manifest_path = SAMPLES / "calibration_manifest_0_1.csv"
    coder_path = SAMPLES / "calibration_coder_sheet_0_1.csv"
    registry_path = SAMPLES / "codebook_registry.csv"

    manifest = read_csv(manifest_path)
    coder = read_csv(coder_path)
    registry = read_csv(registry_path)

    # Structural calibration design.
    if len(manifest) != 12:
        error(f"calibration manifest must contain 12 rows, found {len(manifest)}")
    if len({r["fragment_id"] for r in manifest}) != len(manifest):
        error("calibration manifest contains duplicate fragment_id")
    if len({r["document_id"] for r in manifest}) != len(manifest):
        error("calibration manifest must use 12 distinct documents")
    if [r["item_id"] for r in manifest] != [f"CAL{i:03d}" for i in range(1, 13)]:
        error("calibration item IDs/order must be CAL001-CAL012")
    if Counter(r["era_code"] for r in manifest) != Counter({"E1": 5, "E3": 6, "E4": 1}):
        error("calibration era quotas must be E1=5, E3=6, E4=1")
    if Counter(r["slot"] for r in manifest) != Counter({"A": 3, "B": 3, "C": 3, "D": 3}):
        error("calibration slot quotas must be A=B=C=D=3")
    if sum(builder.is_regional(r["place"]) for r in manifest) < 2:
        error("calibration must include at least two non-Mexico-City regional documents")
    if len({r["document_type"] for r in manifest}) < 5:
        error("calibration must include at least five document types")
    if max(Counter(r["publication"] for r in manifest).values(), default=0) > 2:
        error("no publication may contribute more than two calibration items")
    for row in manifest:
        if row["selection_seed"] != builder.SEED:
            error(f"wrong selection seed for {row['item_id']}")
        if row["selection_basis"] != "metadata_only_structural_hash":
            error(f"non-structural selection basis for {row['item_id']}")
        if row["codebook_version"] != builder.CODEBOOK_VERSION:
            error(f"wrong calibration codebook version for {row['item_id']}")
        if row["status"] != "selected_for_calibration":
            error(f"wrong calibration status for {row['item_id']}")

    # The committed files must be exactly reproducible from structural inputs.
    expected = builder.expected_outputs()
    for path, text in expected.items():
        actual = path.read_text(encoding="utf-8") if path.exists() else None
        if actual != text:
            error(f"generated calibration file drift: {path.relative_to(ROOT)}")

    # Coder-facing sheet must remain blind to selection-role metadata.
    if len(coder) != 12:
        error(f"coder sheet must contain 12 rows, found {len(coder)}")
    forbidden_columns = {
        "slot",
        "era_code",
        "publication",
        "place",
        "document_type",
        "selection_role",
        "source_locator",
        "preparation_note",
        "freeze_status",
    }
    coder_columns = set(coder[0]) if coder else set()
    leaked = sorted(forbidden_columns & coder_columns)
    if leaked:
        error(f"coder sheet leaks researcher-only columns: {leaked}")

    manifest_pairs = [(r["item_id"], r["fragment_id"], r["document_id"]) for r in manifest]
    coder_pairs = [(r["item_id"], r["fragment_id"], r["document_id"]) for r in coder]
    if coder_pairs != manifest_pairs:
        error("coder sheet item/fragment/document order differs from manifest")

    response_fields = ["annotation_id", *builder.annotation_fields()]
    banned_boundary_tokens = {
        "explicit_pedagogical_act",
        "institutional_relation",
        "source_criticism_salient",
        "selected_for_calibration",
        "selection_role",
    }
    for row in coder:
        if row.get("codebook_version") != builder.CODEBOOK_VERSION:
            error(f"wrong coder-sheet codebook version for {row.get('item_id')}")
        if not row.get("source_url", "").strip():
            error(f"missing source URL for {row.get('item_id')}")
        if not row.get("boundary_instruction", "").strip():
            error(f"missing neutral boundary instruction for {row.get('item_id')}")
        lowered = row.get("boundary_instruction", "").lower()
        for token in banned_boundary_tokens:
            if token in lowered:
                error(f"boundary instruction leaks PDHD selection role {token}: {row.get('item_id')}")
        for field in response_fields:
            if row.get(field, "").strip():
                error(f"coder sheet must leave {field} blank for {row.get('item_id')}")

    # Calibration items must never enter a later independent-reliability manifest.
    reliability_path = SAMPLES / "reliability_manifest_0_1.csv"
    if reliability_path.exists():
        reliability = read_csv(reliability_path)
        overlap = sorted(
            {r["fragment_id"] for r in manifest}
            & {r["fragment_id"] for r in reliability}
        )
        if overlap:
            error(f"calibration/reliability overlap is forbidden: {overlap}")

    # Freeze the exact pre-calibration codebook inputs by Git blob SHA.
    if len(registry) != 1:
        error(f"codebook registry currently expects one baseline row, found {len(registry)}")
    else:
        row = registry[0]
        if row.get("codebook_version") != builder.CODEBOOK_VERSION:
            error("codebook registry version does not match calibration package")
        if row.get("status") != "calibration_baseline":
            error("pre-calibration codebook must be calibration_baseline, not independent-round frozen")
        path_fields = [
            ("annotation_manual_path", "annotation_manual_blob_sha"),
            ("pedagogical_acts_path", "pedagogical_acts_blob_sha"),
            ("pedagogical_dimensions_path", "pedagogical_dimensions_blob_sha"),
        ]
        for path_field, sha_field in path_fields:
            target = ROOT / row[path_field]
            if not target.exists():
                error(f"codebook registry path missing: {row[path_field]}")
                continue
            actual_sha = git_blob_sha(target)
            if actual_sha != row[sha_field]:
                error(
                    f"codebook baseline drift for {row[path_field]}: "
                    f"registry={row[sha_field]} actual={actual_sha}"
                )

    if ERRORS:
        for message in ERRORS:
            print(f"ERROR: {message}", file=sys.stderr)
        return 1

    print(
        "PDHD calibration package checks passed "
        "(12 items; E1=5 E3=6 E4=1; A-D=3 each; blind coder sheet; codebook baseline pinned)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
