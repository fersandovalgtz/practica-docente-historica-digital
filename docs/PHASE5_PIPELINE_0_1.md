# Phase 5 analysis pipeline 0.1

## Purpose

Prepare the complete descriptive-analysis machinery before human gold labels exist, so analytical choices are not invented after seeing results.

## Current gate

**Closed.** The current repository has no `data/validated/gold_manifest.json` and no `gold_annotations.csv`. `scripts/run_phase5_analysis.py --expect-closed` is therefore the correct CI state.

## Conditions required to open

The future gold manifest must declare all of the following:

- `validation_status=human_validated_adjudicated`;
- formal reliability completed;
- adjudication completed;
- machine candidates explicitly excluded;
- at least two human coders;
- one frozen codebook version;
- a gold-fragment count matching the actual adjudicated CSV.

The gold CSV must contain 84–96 unique frozen pilot fragments, preserve document identity and carry `adjudication_status=human_adjudicated_gold`. Model/machine fields are rejected.

## Planned outputs

When the gate opens, the pipeline writes:

- `phase5_summary.json`;
- `primary_act_distribution.csv`;
- `dimension_prevalence.csv`;
- `normativity_distribution.csv`;
- `era_by_primary_act.csv`;
- `document_type_by_primary_act.csv`;
- `source_by_primary_act.csv`;
- `primary_acts.svg`;
- `dimensions.svg`.

## Statistical unit and dependence

The pilot contains four fixed fragments per selected document. Fragment rows therefore cannot be treated as if they were 96 independent historical documents.

The pipeline reports:

1. transparent fragment-level descriptive counts/proportions; and
2. deterministic 95% percentile intervals from a **document-cluster bootstrap** with 2,000 resamples and seed `20260907`.

The bootstrap resamples documents and carries all of each sampled document's gold fragments with it. These intervals are uncertainty diagnostics for the pilot design; they are not national-population confidence intervals.

## Historical interpretation boundary

The pipeline does not infer causal change, representativeness of Mexican teaching as a whole, or direct equivalence between normative prescription and observed classroom practice. Those claims require source criticism and a later versioned analytical design.

## Reproducibility

The pipeline uses standard-library Python only and generates tables plus standalone SVG figures. It can be rerun from the repository with the exact future gold manifest/codebook provenance.

## Machine candidates

`data/machine/` is never read as a source of gold labels. Future model-vs-human evaluation should be implemented as a separate analysis that consumes human gold and machine candidates side by side while preserving their different epistemic status.
