#!/usr/bin/env python3
"""Static safety checks for the public PDHD dashboard."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    index = (ROOT / "docs/index.html").read_text(encoding="utf-8")
    app = (ROOT / "docs/dashboard/app.js").read_text(encoding="utf-8")
    errors = []
    for required in ["Tablero público", "0 fragmentos validados por humanos", "machine_candidate", "DATA_DICTIONARY.md"]:
        if required not in index: errors.append(f"dashboard index missing required boundary/reference: {required}")
    forbidden_data = ["data/machine/", "data/validated/", "pedagogical_acts.csv", "pedagogical_dimensions.csv", "gold_annotations"]
    for token in forbidden_data:
        if token in app: errors.append(f"dashboard must not load semantic/experimental data: {token}")
    required_data = ["prevalidation_snapshot_0_1.json", "pilot_document_selection_0_1.csv", "rights_registry.csv", "retrieval_attempts.csv", "pilot_document_substitutions_0_1.csv"]
    for token in required_data:
        if token not in app: errors.append(f"dashboard app missing canonical data dependency: {token}")
    if "raw.githubusercontent.com/fersandovalgtz/practica-docente-historica-digital/main/" not in app:
        errors.append("dashboard must read canonical main data explicitly")
    if errors:
        for error in errors: print(f"ERROR: {error}")
        return 1
    print("PDHD public dashboard safety checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
