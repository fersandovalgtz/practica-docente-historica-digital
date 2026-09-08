# Governance

## Scientific responsibility

PDHD is maintained as a research infrastructure for historical and educational scholarship. Changes that alter the documentary universe, taxonomies, validation rules, rights status or interpretation-bearing fields must be reviewable through version control.

## Decision hierarchy

1. **Source integrity:** the source record and its provenance take priority over downstream convenience.
2. **Rights compliance:** unresolved reuse rights block public redistribution of source content.
3. **Human validation:** automated labels are candidates until a documented human validation step occurs.
4. **Reproducibility:** transformations must be attributable to a versioned script, rule or documented manual operation whenever feasible.
5. **Historical caution:** prescriptive discourse, reported practice and observed practice are distinct evidence types.

## Change control

`main` is the canonical integration branch. Substantive scientific, data, workflow, schema, taxonomy or rights changes should be proposed through a pull request and pass the canonical `Validate PDHD` workflow before merge. Repository settings should protect `main` against force pushes and ordinary direct writes.

CODEOWNERS identifies the maintainer responsible for evidence-, rights-, schema- and workflow-critical surfaces. As the project gains qualified maintainers, review responsibility may be distributed without weakening the requirement for reviewable provenance.

Mixed changes that combine scientific interpretation with unrelated infrastructure maintenance should be separated when feasible so the scientific delta remains auditable.

## Lifecycle separation

PDHD maintains distinct epistemic layers:

```text
source/catalog evidence
        ↓
document/object identity
        ↓
locator + exact boundary
        ↓
frozen structural fragment
        ├── human calibration → independent reliability → human adjudication → gold
        └── machine_candidate experiment
```

A `machine_candidate` is never human validation. Automation cannot promote model output into calibration, formal reliability, adjudicated gold or a phase-5 human-gold gate.

## Releases

A release freezes a reproducible research state. Subsequent changes on `main` do not retroactively modify claims attached to an earlier release.

Final release claims must match the actual validation state. Documentary completeness alone does not justify a semantic-validation release. Version, citation metadata, snapshot, rights posture and validation status must agree.

## Taxonomy and schema changes

Taxonomic terms may be added, deprecated or redefined only with a documented rationale. Renaming a code must preserve a migration note so previous annotations remain interpretable.

Schema changes that alter required fields, controlled vocabularies or lifecycle meaning require explicit migration consequences and validation updates. Structural frozen-fragment schemas must not absorb human or machine semantic status fields.

## Rights governance

Rights are evaluated at the source/object level according to the registered evidence. A source that is publicly accessible is not automatically redistributable. Source facsimiles, long transcriptions and restricted local working copies remain outside public Git history unless a documented rights basis permits reuse.

## Corrections and conflicts

Errors are corrected transparently. Source values are not silently overwritten when the correction would erase evidence of the original record. Where appropriate, PDHD stores both source and normalized values or registers an explicit conflict.

A chronology disagreement or access failure remains unresolved when the evidence does not justify a stronger conclusion. Sample targets are never reached by lowering the evidence gate.

## Security and maintenance

Operational security protects both software and scientific integrity. Active third-party GitHub Actions are pinned to immutable commit SHAs, permissions follow least privilege, and dependency updates are reviewed through CI. Security-sensitive problems follow `SECURITY.md`.

Detailed operational controls, branch-protection recommendations and release maintenance are documented in `docs/MAINTENANCE_POLICY.md`.

## Contributions

External and internal contributions follow `CONTRIBUTING.md`, the structured issue templates and the pull-request template. Scientific disagreement is resolved through evidence, source criticism and explicit uncertainty rather than hidden normalization or unreviewed interpretation.
