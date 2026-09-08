#!/usr/bin/env python3
"""Validate PDHD experimental machine-candidate annotations.

This validator enforces provenance and quarantine boundaries. It never promotes
machine output to human validation or gold evidence.
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MACHINE = ROOT / "data/machine"
RUNS = MACHINE / "runs"
REGISTRY = MACHINE / "machine_run_registry.csv"
SAMPLES = ROOT / "data/samples"
TAXONOMY = ROOT / "data/taxonomy"
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
RUN_RE = re.compile(r"^PDHD-MRUN-[A-Za-z0-9._-]+$")
ANN_RE = re.compile(r"^PDHD-MANN-[A-Za-z0-9._-]+$")

NORMATIVITY = {"prescriptive", "policy_normative", "descriptive", "reported_practice", "observed_practice", "testimonial", "analytical", "mixed", "unclear", ""}
ACTORS = {"teacher", "student", "inspector", "director", "family", "community", "state_authority", "other", "unclear", ""}
TARGETS = {"student", "teacher", "family", "community", "institution", "self", "other", "unclear", ""}
CONFIDENCE = {"high", "medium", "low", ""}
RUN_STATUS = {"planned", "running", "completed", "invalidated"}
FORBIDDEN_COLUMNS = {"coder_id", "human_validated", "gold_label", "adjudicated_by"}


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader), list(reader.fieldnames or [])


def allowed_acts() -> set[str]:
    rows, _ = read_csv(TAXONOMY / "pedagogical_acts.csv")
    return {r["act_code"] for r in rows} | {"none", "unclear", ""}


def dimension_fields() -> set[str]:
    rows, _ = read_csv(TAXONOMY / "pedagogical_dimensions.csv")
    return {f"dimension_{r['dimension_code']}" for r in rows}


def frozen_index() -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(SAMPLES.glob("frozen_fragments*.csv")):
        rows, _ = read_csv(path)
        for row in rows:
            fid = row["fragment_id"]
            if fid in result:
                raise RuntimeError(f"duplicate frozen fragment {fid}")
            result[fid] = row["document_id"]
    if len(result) != 96:
        raise RuntimeError(f"machine validator expected 96 frozen fragments, found {len(result)}")
    return result


def validate_registry() -> tuple[dict[str, dict[str, str]], list[str]]:
    rows, fields = read_csv(REGISTRY)
    required = {"run_id", "model_provider", "model_name", "model_version", "codebook_version", "prompt_sha256", "input_manifest_sha256", "temperature", "seed", "status", "created_at", "notes"}
    errors: list[str] = []
    if set(fields) != required:
        errors.append("machine_run_registry.csv header differs from canonical fields")
    index: dict[str, dict[str, str]] = {}
    for row in rows:
        run_id = row.get("run_id", "").strip()
        if not RUN_RE.fullmatch(run_id): errors.append(f"invalid machine run_id {run_id!r}")
        if run_id in index: errors.append(f"duplicate machine run_id {run_id}")
        index[run_id] = row
        for field in ["model_provider", "model_name", "model_version", "codebook_version"]:
            if not row.get(field, "").strip(): errors.append(f"{run_id}: empty {field}")
        for field in ["prompt_sha256", "input_manifest_sha256"]:
            if not SHA_RE.fullmatch(row.get(field, "").strip()): errors.append(f"{run_id}: invalid {field}")
        if row.get("status", "").strip() not in RUN_STATUS: errors.append(f"{run_id}: invalid status")
    return index, errors


def validate_candidate_rows(rows: list[dict[str, str]], fields: list[str], registry: dict[str, dict[str, str]], frozen: dict[str, str], label: str) -> list[str]:
    errors: list[str] = []
    forbidden = FORBIDDEN_COLUMNS & set(fields)
    if forbidden: errors.append(f"{label}: forbidden human/gold columns {sorted(forbidden)}")
    required = {"machine_annotation_id", "run_id", "fragment_id", "document_id", "model_provider", "model_name", "model_version", "codebook_version", "prompt_sha256", "input_sha256", "candidate_status", "pedagogical_act_primary", "pedagogical_act_secondary", "normativity", "actor", "target", "evidence_confidence", "access_problem", "notes", "generated_at"} | dimension_fields()
    missing = required - set(fields)
    if missing: errors.append(f"{label}: missing required columns {sorted(missing)}")
    seen_ids: set[str] = set(); seen_pairs: set[tuple[str, str]] = set(); acts = allowed_acts()
    for row in rows:
        ann = row.get("machine_annotation_id", "").strip(); run_id = row.get("run_id", "").strip(); fid = row.get("fragment_id", "").strip(); doc = row.get("document_id", "").strip()
        if not ANN_RE.fullmatch(ann): errors.append(f"{label}: invalid machine_annotation_id {ann!r}")
        if ann in seen_ids: errors.append(f"{label}: duplicate machine_annotation_id {ann}")
        seen_ids.add(ann)
        if run_id not in registry: errors.append(f"{label}: unregistered run_id {run_id}")
        pair = (run_id, fid)
        if pair in seen_pairs: errors.append(f"{label}: duplicate run/fragment {pair}")
        seen_pairs.add(pair)
        if fid not in frozen: errors.append(f"{label}: unknown/non-frozen fragment {fid}")
        elif frozen[fid] != doc: errors.append(f"{label}: document mismatch for {fid}")
        if row.get("candidate_status", "").strip() != "machine_candidate": errors.append(f"{label}: candidate_status must be machine_candidate")
        if registry.get(run_id):
            reg = registry[run_id]
            for out_field, reg_field in [("model_provider", "model_provider"), ("model_name", "model_name"), ("model_version", "model_version"), ("codebook_version", "codebook_version"), ("prompt_sha256", "prompt_sha256")]:
                if row.get(out_field, "").strip() != reg.get(reg_field, "").strip(): errors.append(f"{label}: {ann} {out_field} differs from run registry")
        if not SHA_RE.fullmatch(row.get("input_sha256", "").strip()): errors.append(f"{label}: {ann} invalid input_sha256")
        primary = row.get("pedagogical_act_primary", "").strip()
        if primary not in acts: errors.append(f"{label}: {ann} invalid primary act {primary!r}")
        secondary = [v.strip() for v in row.get("pedagogical_act_secondary", "").split(";") if v.strip()]
        if len(secondary) != len(set(secondary)): errors.append(f"{label}: {ann} duplicate secondary act")
        for value in secondary:
            if value not in acts - {"", "none", "unclear"}: errors.append(f"{label}: {ann} invalid secondary act {value!r}")
        for field in dimension_fields():
            if row.get(field, "").strip() not in {"0", "1", ""}: errors.append(f"{label}: {ann} {field} must be 0/1/blank")
        if row.get("normativity", "").strip() not in NORMATIVITY: errors.append(f"{label}: {ann} invalid normativity")
        if row.get("actor", "").strip() not in ACTORS: errors.append(f"{label}: {ann} invalid actor")
        if row.get("target", "").strip() not in TARGETS: errors.append(f"{label}: {ann} invalid target")
        if row.get("evidence_confidence", "").strip() not in CONFIDENCE: errors.append(f"{label}: {ann} invalid evidence_confidence")
    return errors


def self_test() -> int:
    frozen = {"PDHD-F000001": "PDHD-D000065"}
    registry = {"PDHD-MRUN-test": {"model_provider": "p", "model_name": "m", "model_version": "1", "codebook_version": "cb", "prompt_sha256": "a"*64}}
    fields = ["machine_annotation_id", "run_id", "fragment_id", "document_id", "model_provider", "model_name", "model_version", "codebook_version", "prompt_sha256", "input_sha256", "candidate_status", "pedagogical_act_primary", "pedagogical_act_secondary", *sorted(dimension_fields()), "normativity", "actor", "target", "evidence_confidence", "access_problem", "notes", "generated_at"]
    row = {f: "" for f in fields}; row.update({"machine_annotation_id": "PDHD-MANN-test", "run_id": "PDHD-MRUN-test", "fragment_id": "PDHD-F000001", "document_id": "PDHD-D000065", "model_provider": "p", "model_name": "m", "model_version": "1", "codebook_version": "cb", "prompt_sha256": "a"*64, "input_sha256": "b"*64, "candidate_status": "machine_candidate", "pedagogical_act_primary": "unclear", "normativity": "unclear", "actor": "unclear", "target": "unclear", "evidence_confidence": "low"})
    for f in dimension_fields(): row[f] = "0"
    assert not validate_candidate_rows([row], fields, registry, frozen, "synthetic")
    bad_fields = fields + ["gold_label"]
    bad = dict(row); bad["gold_label"] = "yes"
    assert any("forbidden" in e for e in validate_candidate_rows([bad], bad_fields, registry, frozen, "synthetic"))
    print("validate_machine_candidates self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--self-test", action="store_true"); args = parser.parse_args()
    if args.self_test: return self_test()
    registry, errors = validate_registry(); frozen = frozen_index()
    if RUNS.exists():
        for path in sorted(RUNS.glob("*.csv")):
            rows, fields = read_csv(path); errors.extend(validate_candidate_rows(rows, fields, registry, frozen, str(path.relative_to(ROOT))))
    completed = {run_id for run_id, row in registry.items() if row.get("status") == "completed"}
    existing = {path.stem for path in RUNS.glob("*.csv")} if RUNS.exists() else set()
    for run_id in completed:
        if run_id not in existing: errors.append(f"completed run {run_id} has no data/machine/runs/{run_id}.csv")
    if errors:
        for error in errors: print(f"ERROR: {error}")
        return 1
    print(f"PDHD machine-candidate checks passed ({len(registry)} registered runs; {len(existing)} output files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
