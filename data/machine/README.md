# Experimental machine annotations

This directory is a quarantine layer for model-generated **machine candidates**. It is intentionally separate from human calibration, formal reliability and any future validated/gold dataset.

## Current state

- Frozen documentary fragments: **96**.
- Leakage-safe neutral boundary instructions already available: **12** (the human-calibration package).
- Remaining fragments blocked from machine annotation until a neutral boundary projection exists: **84**.
- Machine runs registered: **0**.
- Machine candidates accepted as human validation: **0**, by design.

Run `python scripts/build_machine_input_manifest.py --check-state` to verify the 96 = 12 ready + 84 blocked gate. Run the same script without `--check-state` to generate a local/artifact manifest; the generated manifest is not a semantic output.

## Why 84 items are blocked

Researcher-facing frozen-fragment metadata may contain selection-role or preparation language that would leak expected semantics to a model. PDHD therefore refuses to use `selection_role`, semantic source-locator slugs or preparation notes as machine inputs. Neutralizing those 84 boundaries must be completed before a full 96-item model comparison is scientifically interpretable.

## Run registry

`machine_run_registry.csv` stores one row per experimental model run. It records provider/model/version, exact codebook, SHA-256 of the prompt and input manifest, temperature/seed when applicable and lifecycle status.

Completed output files belong under `data/machine/runs/` and must be validated by `scripts/validate_machine_candidates.py`.

## Non-negotiable separation

A machine output:

- uses `candidate_status=machine_candidate`;
- has no `coder_id`;
- has no `human_validated` field;
- has no `gold_label` field;
- cannot satisfy calibration or reliability gates;
- cannot unlock phase 5;
- cannot change the project snapshot's human/gold counts;
- cannot justify a final `v0.1.0` release.

This layer is for model-stability experiments, error analysis and future comparison against a human benchmark after that benchmark exists.
