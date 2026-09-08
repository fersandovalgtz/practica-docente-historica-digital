# Contributing to PDHD

PDHD is a research infrastructure. Contributions are welcome, but documentary evidence, rights, provenance and human-validation boundaries take precedence over convenience or throughput.

## Before opening a pull request

1. Work from a branch; do not treat `main` as a scratch space.
2. Keep source identity, documentary localization, frozen boundaries, human annotation, machine candidates and gold data in their separate lifecycle layers.
3. Do not commit source facsimiles or long transcriptions unless the applicable rights record explicitly permits redistribution.
4. Do not infer historical-source non-existence from an HTTP failure.
5. Do not use model output to satisfy human calibration, reliability, adjudication or gold-set gates.
6. Preserve provenance when correcting a source value; do not silently erase a conflicting or superseded record when the history matters.

## Local validation

Use Python 3.12+ and run the canonical checks before requesting review:

```bash
python scripts/validate_repository.py
python scripts/validate_fragment_shards.py
python scripts/validate_status_counts.py
python scripts/validate_project_metadata.py
python scripts/validate_schema_alignment.py
python scripts/validate_public_dashboard.py
python scripts/build_machine_input_manifest.py --check-state
python scripts/validate_machine_candidates.py
python scripts/run_phase5_analysis.py --expect-closed
python scripts/validate_repository_hygiene.py
```

The GitHub `Validate PDHD` workflow is the authoritative integration check and may include additional self-tests.

## Contribution classes

### Documentary corrections

Provide the affected stable identifier, current value, proposed value, primary evidence URL or repository locator, and why the change improves source fidelity. Chronology conflicts should be registered rather than normalized away when the evidence remains genuinely contradictory.

### Rights changes

A rights-status change requires a source terms/reproduction-policy citation or documented permission basis. Absence of a visible restriction is not equivalent to permission to redistribute.

### Schema or taxonomy changes

Explain migration consequences. Existing codes and historical annotations must remain interpretable. Breaking schema changes require a versioned migration note.

### Human annotation

Only real human coding performed under the registered protocol may enter human-calibration or reliability surfaces. Preserve independent first-pass provenance before discussion or adjudication.

### Machine annotation

Model output belongs only under the `machine_candidate` lifecycle. Inputs must satisfy the leakage gate; model/provider/version, prompt hash and input-manifest hash must be recorded.

## Pull-request expectations

A PR should state what changes, what does not change, the evidence/provenance basis, rights implications, scientific-boundary implications and validation results. Small, reviewable PRs are preferred over mixed scientific and maintenance changes.

## Reproducibility

Generated outputs should be reproducible from versioned code and registered inputs whenever feasible. Deterministic seeds, fixed manifests and immutable identifiers should be preserved rather than regenerated opportunistically.

## Reporting problems

Use the structured issue templates for technical defects, documentary corrections and source-access problems. Security-sensitive reports should follow `SECURITY.md` rather than a public issue.
