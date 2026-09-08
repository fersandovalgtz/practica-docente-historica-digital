# PDHD data dictionary 0.1

This dictionary describes the public, reusable data surfaces of **Práctica Docente Histórica Digital (PDHD)**. It is intentionally field-oriented so a third party can understand the corpus without reading the Python scripts.

## Reading rules

- `data/catalog/` contains source, object, rights and chronology metadata.
- `data/samples/` contains pilot selection, retrieval provenance, fragment localization/freezing and validation-preparation records.
- `data/taxonomy/` contains controlled vocabularies.
- `data/snapshots/` identifies reproducible scientific states.
- `data/machine/` is reserved for model-generated **machine candidates** and can never stand in for human validation.
- Files named `*_wN.csv` are auditable shards or historical work batches. Their logical union is validated by repository scripts where applicable.
- Blank does not mean false. It means unknown, not applicable, not yet determined or intentionally absent according to the table-specific protocol.

## Identifier families

| Prefix | Meaning |
|---|---|
| `PDHD-C` | documentary candidate |
| `PDHD-D` | canonical document/object |
| `PDHD-F` | fixed pilot fragment |
| `PDHD-L` | unresolved/resolved issue lead |
| `PDHD-A` | object alias/crosswalk |
| `PDHD-X` | chronology conflict |
| `PDHD-RA` | retrieval attempt |
| `PDHD-PS` | versioned pilot substitution |
| `PDHD-CAL` | calibration item |
| `PDHD-CB` | codebook version |
| `PDHD-MRUN` | machine-annotation run |
| `PDHD-MANN` | machine candidate annotation |

# Catalog tables

## `data/catalog/sources.csv`

One row per source family or repository.

| Field | Meaning |
|---|---|
| `source_id` | Stable short identifier used as a foreign key. |
| `source_name` | Human-readable repository/collection name. |
| `institution` | Custodial or publishing institution. |
| `source_type` | Repository/source class. |
| `base_url` | Root public URL for the source. |
| `scope_note` | What kinds of material the source contributes. |
| `accessed_at` | Date PDHD last established the source-level record. |

## `data/catalog/rights_registry.csv`

One operational rights policy per `source_id`.

| Field | Meaning |
|---|---|
| `source_id` | Foreign key to `sources.csv`. |
| `rights_status` | PDHD operational rights class. |
| `source_terms_url` | URL for terms/reproduction guidance when available. |
| `public_commit_policy` | What PDHD may commit publicly from this source. |
| `review_note` | Source-critical/legal caution or object-level review rule. |
| `accessed_at` | Date the rights policy was checked. |

Canonical `rights_status` values: `metadata_only`, `local_processing_only`, `redistributable_with_attribution`, `public_domain_verified`, `permission_granted`, `review_required`.

## `data/catalog/source_candidates.csv`

Discovery-stage registry. A candidate is not automatically a selected pilot document.

| Field | Meaning |
|---|---|
| `candidate_id` | Stable candidate identifier. |
| `source_id` | Repository/source family. |
| `item_level` | Granularity of the candidate, e.g. serial title or object. |
| `title` | Candidate title. |
| `subtitle_or_scope` | Subtitle, scope or discovery qualifier. |
| `date_start` / `date_end` | Known chronological coverage. |
| `place` | Place of publication/production when known. |
| `source_url` | Evidence/discovery URL. |
| `rights_status` | Operational rights class at discovery time. |
| `priority` | Research priority. |
| `status` | Candidate workflow state. |
| `verification_note` | Why the candidate is considered identified/useful. |
| `checked_at` | Last check date. |

## `data/catalog/documents.csv` and `documents_balancing_w1.csv`

Canonical object-level document records. The two files form a validated union; IDs and source identifiers cannot collide.

| Field | Meaning |
|---|---|
| `document_id` | Canonical `PDHD-D######` identifier. |
| `source_id` | Repository/source family. |
| `title` | Object title. |
| `author` | Author/creator when known. |
| `publication` | Serial, collection or publication title. |
| `publication_date` | Best canonical object date. |
| `volume` | Volume/tome. |
| `issue` | Issue/number. |
| `page_start` / `page_end` | Object page range when known. |
| `place` | Publication/production place. |
| `publisher` | Publisher/institution when known. |
| `source_url` | Canonical object locator. |
| `source_identifier` | Repository-native stable identifier. |
| `accessed_at` | Access/check date. |
| `rights_status` | Operational rights class. |
| `document_type` | Analytical documentary type, not a semantic teaching label. |
| `period` | Broad historical period. |
| `notes` | Source-critical/object notes. |

## `data/catalog/issue_leads.csv`

Hemerographic leads not yet fully promoted to canonical object identity, plus the record of later resolution.

| Field | Meaning |
|---|---|
| `lead_id` | Stable lead ID. |
| `publication` | Publication title. |
| `issue_label` | Issue/number label if known. |
| `reported_date` | Date reported by the evidence source. |
| `date_precision` | Day/month/year precision. |
| `evidence_source` | Source that exposed the lead. |
| `evidence_url` | URL supporting the lead. |
| `primary_locator_status` | Whether an auditable primary object locator is available. |
| `resolved_document_id` | Canonical document once promoted. |
| `priority` | Recovery priority. |
| `notes` | Recovery/source-critical notes. |

## `data/catalog/object_aliases.csv`

Cross-repository identity bridges. An alias is not automatically a page locator.

| Field | Meaning |
|---|---|
| `alias_id` | Stable alias record. |
| `document_id` | Canonical PDHD object. |
| `alias_system` | External repository/system. |
| `alias_identifier` | External identifier. |
| `alias_url` | External locator. |
| `alias_role` | Function of the alias, e.g. full-text target. |
| `verification_status` | What was actually verified. |
| `evidence_url` | Evidence supporting the crosswalk. |
| `checked_at` | Check date. |
| `note` | Limits and interpretation of the alias. |

## `data/catalog/chronology_conflicts.csv`

Explicit preservation of conflicting dates rather than silent normalization.

| Field | Meaning |
|---|---|
| `conflict_id` | Stable conflict ID. |
| `publication` | Object/publication concerned. |
| `field` | Chronological field in dispute. |
| `value_a` / `value_b` | Conflicting values. |
| `source_a` / `source_b` | Evidence supporting each value. |
| `canonical_value` | Current value used by PDHD, which may remain approximate. |
| `canonical_precision` | Precision of the adopted value. |
| `status` | Open/resolved state. |
| `decision_note` | Source-critical rationale. |

# Pilot and fragment tables

## `data/samples/pilot_document_selection_0_1.csv`

The fixed 24-document pilot design.

| Field | Meaning |
|---|---|
| `selection_order` | Deterministic position 1–24. |
| `document_id` | Selected canonical document. |
| `era_code` | Pilot era stratum. |
| `publication` | Publication label copied for auditability. |
| `place` | Place copied for balancing checks. |
| `document_type` | Documentary type used for structural balancing. |
| `fragment_target_count` | Target fragments; currently four per document. |
| `selection_role` | Why the document occupies the design position. |
| `status` | Selection state; active cohort rows are `selected`. |

## `fragment_locator_progress*.csv`

Logical union of candidate/resolved fragment locators.

| Field | Meaning |
|---|---|
| `fragment_id` | Deterministic pilot fragment ID. |
| `document_id` | Parent document. |
| `slot` | Structural slot A–D. |
| `page` | Printed/physical page reference. |
| `source_locator` | Compact local structural locator/slug. |
| `locator_evidence_url` | Direct or auditable evidence URL. |
| `boundary_status` | Whether exact boundaries are still candidate or fixed. |
| `public_text_status` | Whether source text may be public, local only or metadata-only. |
| `freeze_status` | Locator/freeze workflow state. |
| `preparation_note` | Source-critical preparation note. |
| `checked_at` | Review date. |

## `frozen_fragments*.csv`

Canonical fixed-fragment union. These are structural/source-critical records, **not semantic labels**.

| Field | Meaning |
|---|---|
| `fragment_id` | Fixed fragment ID. |
| `document_id` | Parent document. |
| `slot` | Structural slot A–D. |
| `page` | Page reference. |
| `source_locator` | Compact source locator. |
| `locator_evidence_url` | Evidence URL. |
| `boundary_definition` | Exact span boundary definition. |
| `transcription_status` | How, or whether, source text has been transcribed/verified. |
| `access_basis` | Basis on which the source was inspected. |
| `public_text_status` | Public redistribution status for the text. |
| `selection_role` | Researcher-facing sampling role; not a coder response. |
| `freeze_status` | Must be `frozen` for this registry. |
| `preparation_note` | Provenance/caution note. |
| `checked_at` | Freeze/check date. |

## `data/samples/retrieval_attempts.csv`

Negative and positive retrieval provenance.

| Field | Meaning |
|---|---|
| `attempt_id` | Stable retrieval-attempt ID. |
| `document_id` | Target document. |
| `fragment_ids` | Semicolon-separated affected fragments. |
| `source_id` | Repository/source family. |
| `object_url` | URL attempted. |
| `target` | Retrieval purpose. |
| `result_status` | Outcome state. |
| `blocker` | What prevented or complicated recovery. |
| `next_route` | Next documented recovery route or completion note. |
| `checked_at` | Attempt date. |

## `data/samples/pilot_document_substitutions_0_1.csv`

Versioned changes to a pilot position; outgoing documents are never silently overwritten.

| Field | Meaning |
|---|---|
| `substitution_id` | Stable substitution ID. |
| `selection_order` | Pilot position affected. |
| `outgoing_document_id` | Replaced document. |
| `replacement_document_id` | New canonical document. |
| `reason` | Evidence-based reason. |
| `era_effect` | Effect on period balance. |
| `geography_effect` | Effect on geographic balance. |
| `document_type_effect` | Effect on documentary-type balance. |
| `publication_concentration_effect` | Effect on concentration limits. |
| `primary_evidence_basis` | Primary evidence supporting the replacement. |
| `decided_at` | Decision date. |

# Human-validation preparation

## `calibration_manifest_0_1.csv`

Researcher-facing deterministic 12-item calibration selection. Key fields are `item_id`, `calibration_order`, `fragment_id`, `document_id`, structural strata, `codebook_version`, deterministic `selection_seed`, `selection_basis` and `status`.

## `calibration_coder_sheet_0_1.csv`

Blind coder-facing projection. Structural fields identify the item and exact source boundary; response fields are intentionally blank until a real coder completes them.

## `annotation_pilot_template.csv`

Canonical annotation field order. Core identifiers are followed by `coder_id`, primary/secondary pedagogical acts, 16 binary `dimension_*` fields, `normativity`, `actor`, `target`, `evidence_confidence`, `access_problem`, `notes` and `annotated_at`.

## `codebook_registry.csv`

| Field | Meaning |
|---|---|
| `codebook_version` | Stable codebook ID. |
| `status` | Lifecycle state, e.g. calibration baseline or frozen independent-reliability version. |
| `annotation_manual_path` | Manual path. |
| `annotation_manual_blob_sha` | Git blob SHA pinning exact manual content. |
| `pedagogical_acts_path` / `pedagogical_acts_blob_sha` | Controlled act vocabulary and pinned blob. |
| `pedagogical_dimensions_path` / `pedagogical_dimensions_blob_sha` | Dimension vocabulary and pinned blob. |
| `source_commit_sha` | Commit from which the snapshot derives. |
| `created_at` | Version creation date. |
| `note` | Lifecycle/provenance note. |

## `reliability_reserve_0_1.csv`

The 84-item exact complement of calibration inside the frozen 96. Fields: `reserve_order`, `fragment_id`, `document_id`, `selection_order`, `era_code`, `slot`, `reserve_version`, `selection_basis`, `status`.

It is a **reserve**, not a completed reliability study.

# Controlled vocabularies

## `data/taxonomy/pedagogical_dimensions.csv`

`dimension_code` is the machine-readable code, `label_es` the Spanish display label and `definition_es` the operational definition.

## `data/taxonomy/pedagogical_acts.csv`

`act_code` is the machine-readable act, `label_es` its Spanish display label and `definition_es` the operational definition.

# Snapshots

## `data/snapshots/prevalidation_snapshot_0_1.json`

Pins project version, reference date, canonical commit/tree, GitHub signature state, CI run, documentary counts and the validation boundary. It explicitly records `human_coded_fragments: 0` and `gold_labels: 0` for the current pre-validation state.

# Machine candidates

Machine outputs must conform to `schemas/machine_candidate.schema.json` and be registered under `data/machine/`. Required provenance includes model/provider/version, run ID, exact codebook, prompt SHA-256 and input SHA-256. `candidate_status` must remain `machine_candidate`.

A machine candidate cannot supply `coder_id`, `human_validated` or `gold_label` fields. Machine outputs are experimental diagnostics and cannot satisfy any human-validation or `v0.1.0` release gate.

# JSON Schemas

- `schemas/document.schema.json`: canonical document object.
- `schemas/pedagogical_fragment.schema.json`: structural frozen fragment; no semantic labels.
- `schemas/annotation.schema.json`: human semantic annotation field contract.
- `schemas/machine_candidate.schema.json`: experimental model-generated candidate contract.

For lifecycle rules that JSON Schema cannot express safely—cross-file provenance, codebook blob pins, two-coder independence, access exceptions and human/gold gates—use the repository validators and protocols. JSON Schema is a field contract, not a replacement for scientific workflow validation.
