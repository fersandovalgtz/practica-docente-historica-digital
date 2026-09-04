# Governance

## Scientific responsibility

PDHD is maintained as a research infrastructure for historical and educational scholarship. Changes that alter the documentary universe, taxonomies, validation rules, rights status or interpretation-bearing fields must be reviewable through version control.

## Decision hierarchy

1. **Source integrity:** the source record and its provenance take priority over downstream convenience.
2. **Rights compliance:** unresolved reuse rights block public redistribution of source content.
3. **Human validation:** automated labels are candidates until a documented human validation step occurs.
4. **Reproducibility:** transformations must be attributable to a versioned script, rule or documented manual operation whenever feasible.
5. **Historical caution:** prescriptive discourse, reported practice and observed practice are distinct evidence types.

## Releases

A release freezes a reproducible research state. Subsequent changes on `main` do not retroactively modify claims attached to an earlier release.

## Taxonomy changes

Taxonomic terms may be added, deprecated or redefined only with a documented rationale. Renaming a code must preserve a migration note so previous annotations remain interpretable.

## Corrections

Errors are corrected transparently. Source values are not silently overwritten when the correction would erase evidence of the original record. Where appropriate, PDHD stores both `source_value` and `normalized_value`.
