# Machine annotation protocol 0.1

## Purpose

Permit reproducible experiments with one or more language/vision models while preventing any machine output from contaminating PDHD's human-validation benchmark.

## Status vocabulary

`machine_candidate` means exactly: **a model-generated analytical proposal that has not been human validated**.

It never means accepted annotation, adjudicated label, ground truth or evidence of inter-coder reliability.

## Input gate

A model may receive only a leakage-safe input projection containing:

- machine item ID;
- `fragment_id`;
- `document_id`;
- page reference;
- source URL;
- a neutral structural boundary instruction;
- exact codebook version.

It must not receive:

- researcher-facing `selection_role`;
- semantic locator slugs;
- preparation notes that identify why the span was selected;
- human coder responses;
- adjudicated/gold labels;
- reliability outcomes.

`build_machine_input_manifest.py` currently proves that 12/96 items have neutral boundary instructions and 84/96 remain blocked. A full 96-item machine run is prohibited until all 96 have `input_status=ready_neutral_boundary`.

## Model-run provenance

Every run must be registered before its output is treated as a PDHD experimental artifact. Record:

- `run_id`;
- provider;
- model name;
- exact model/version identifier available from the provider;
- codebook version;
- SHA-256 of the complete system+task prompt used for coding;
- SHA-256 of the exact machine input manifest;
- temperature and seed if the provider exposes them;
- creation timestamp;
- notes describing any tool/vision limitations.

Do not commit API keys, access tokens, provider secrets or private source text.

## Recommended comparison design

For model-stability work, use at least two independent conditions—for example two models or the same model under two controlled prompt versions. Keep the input manifest fixed. Differences in prompt, model version or source rendering must create a new `run_id`.

Machine-machine agreement may be reported as an experimental diagnostic, but it is not a substitute for human-human reliability. The same agreement functions may be reused technically only if the output is labelled explicitly as machine-machine agreement.

## Output contract

Each model result must conform to `schemas/machine_candidate.schema.json` and be stored under `data/machine/runs/` only after `scripts/validate_machine_candidates.py` passes.

No machine output may be copied into a future validated/gold directory merely by renaming fields. Gold creation must be governed by the human validation/adjudication protocol.

## Source-access failure

If a model cannot retrieve or read the historical page, it records `access_problem`. It must not infer a label from publication title, selection position, URL slug or surrounding PDHD metadata.

## Future human comparison

After a human gold benchmark exists, PDHD may compare machine candidates against it. That comparison is evaluation of a model against human evidence; it does not retrospectively turn the machine candidates into human annotations.

## Versioning

Changes to machine prompt, input projection, model or codebook require a new run ID. Changes to the machine protocol itself require a versioned protocol update. Human codebook changes remain governed by the human-validation pipeline, not by machine performance.
