# Validated human data — reserved directory

This directory is reserved for the future **human-adjudicated benchmark**. It is intentionally empty of gold annotations in the current pre-validation state.

Phase 5 expects two future files:

## `gold_manifest.json`

Required fields:

```json
{
  "validation_status": "human_validated_adjudicated",
  "formal_reliability_completed": true,
  "adjudication_completed": true,
  "machine_candidates_excluded": true,
  "human_coder_count": 2,
  "codebook_version": "PDHD-CB-...",
  "gold_fragment_count": 84
}
```

The example above is a contract illustration only; it is **not** a current scientific result.

## `gold_annotations.csv`

Future adjudicated rows must conform conceptually to `schemas/gold_annotation.schema.json`, carry `adjudication_status=human_adjudicated_gold`, use one frozen codebook version and contain no model/machine fields.

`python scripts/run_phase5_analysis.py --expect-closed` must continue to pass while these files do not exist. When a real human-validation milestone opens the gate, CI and documentation must be changed explicitly in the same versioned change; no automated process should silently flip the project from pre-validation to gold analysis.
