#!/usr/bin/env python3
"""Validate separation and alignment of PDHD JSON field contracts."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
SEMANTIC_FRAGMENT_FORBIDDEN = {"dimension", "normativity", "validation_status", "pedagogical_act", "pedagogical_act_primary", "actor", "target"}
MACHINE_HUMAN_FORBIDDEN = {"coder_id", "human_validated", "gold_label", "adjudicated_by"}
GOLD_MACHINE_FORBIDDEN = {"model_provider", "model_name", "model_version", "machine_annotation_id", "candidate_status", "run_id"}


def load(name: str) -> dict:
    return json.loads((SCHEMAS / name).read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    fragment = load("pedagogical_fragment.schema.json")
    annotation = load("annotation.schema.json")
    machine = load("machine_candidate.schema.json")
    gold = load("gold_annotation.schema.json")

    fragment_props = set(fragment.get("properties", {}))
    leaked = fragment_props & SEMANTIC_FRAGMENT_FORBIDDEN
    if leaked: errors.append(f"frozen fragment schema contains semantic annotation fields: {sorted(leaked)}")
    if fragment.get("properties", {}).get("freeze_status", {}).get("const") != "frozen": errors.append("frozen fragment schema must require freeze_status=frozen")

    template = ROOT / "data/samples/annotation_pilot_template.csv"
    with template.open(encoding="utf-8", newline="") as fh:
        template_fields = next(csv.reader(fh))
    annotation_props = set(annotation.get("properties", {}))
    missing = set(template_fields) - annotation_props
    extra = annotation_props - set(template_fields)
    if missing: errors.append(f"annotation schema misses template fields: {sorted(missing)}")
    if extra: errors.append(f"annotation schema has fields absent from template: {sorted(extra)}")

    current_normativity = {"prescriptive", "policy_normative", "descriptive", "reported_practice", "observed_practice", "testimonial", "analytical", "mixed", "unclear", ""}
    schema_normativity = set(annotation.get("properties", {}).get("normativity", {}).get("enum", []))
    if schema_normativity != current_normativity: errors.append("annotation normativity enum drifted from current validator contract")

    machine_props = set(machine.get("properties", {}))
    if machine_props & MACHINE_HUMAN_FORBIDDEN: errors.append(f"machine schema exposes human/gold fields: {sorted(machine_props & MACHINE_HUMAN_FORBIDDEN)}")
    if machine.get("properties", {}).get("candidate_status", {}).get("const") != "machine_candidate": errors.append("machine schema must const candidate_status=machine_candidate")

    gold_props = set(gold.get("properties", {}))
    if gold_props & GOLD_MACHINE_FORBIDDEN: errors.append(f"gold schema exposes machine provenance fields: {sorted(gold_props & GOLD_MACHINE_FORBIDDEN)}")
    if gold.get("properties", {}).get("adjudication_status", {}).get("const") != "human_adjudicated_gold": errors.append("gold schema must const adjudication_status=human_adjudicated_gold")

    dictionary = (ROOT / "docs/DATA_DICTIONARY.md").read_text(encoding="utf-8")
    for filename in ["document.schema.json", "pedagogical_fragment.schema.json", "annotation.schema.json", "machine_candidate.schema.json"]:
        if filename not in dictionary: errors.append(f"data dictionary does not mention {filename}")
    validated_readme = (ROOT / "data/validated/README.md").read_text(encoding="utf-8")
    if "gold_annotation.schema.json" not in validated_readme: errors.append("validated-data contract does not reference gold_annotation.schema.json")

    if errors:
        for error in errors: print(f"ERROR: {error}")
        return 1
    print("PDHD schema alignment checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
