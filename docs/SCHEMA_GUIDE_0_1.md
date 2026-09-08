# PDHD schema guide 0.1

PDHD uses JSON Schema as a **field contract** and Python validators as **cross-file scientific lifecycle enforcement**. These two layers are complementary.

## Schema map

| Schema | Represents | Must not be interpreted as |
|---|---|---|
| `schemas/document.schema.json` | Canonical documentary object identity and rights metadata | A selected pilot position or a pedagogical interpretation |
| `schemas/pedagogical_fragment.schema.json` | Exact frozen source span and source-critical provenance | A human annotation, gold label or claim that the span documents observed practice |
| `schemas/annotation.schema.json` | Human semantic annotation fields under a versioned codebook | Automatically validated truth; human workflow rules still apply |
| `schemas/machine_candidate.schema.json` | Experimental model-generated semantic candidate with full model/prompt/input provenance | Human validation, adjudication or gold evidence |
| `schemas/gold_annotation.schema.json` | Future human-adjudicated benchmark record | A machine candidate or a current pre-validation artifact; no gold records exist yet |

## Why frozen fragment and annotation are separate

A frozen fragment answers: **what historical source span is being examined, where is it, how was it accessed, what are its exact boundaries and what may be redistributed?**

An annotation answers: **how does a coder classify that span under a specific versioned analytical codebook?**

The distinction is non-negotiable because documentary stabilization can be complete while semantic validation remains at zero. PDHD-U1 is currently in exactly that state.

## Controlled vocabulary authority

The authoritative current vocabularies are:

- `data/taxonomy/pedagogical_acts.csv`
- `data/taxonomy/pedagogical_dimensions.csv`
- the controlled `normativity`, `actor`, `target` and `evidence_confidence` sets enforced by the completed-sheet validator.

The JSON schemas mirror those field contracts, but CI validators remain authoritative for cross-file relationships and lifecycle status.

## Validation responsibilities

### JSON Schema handles

- identifier shape;
- field presence at object-contract level;
- field types;
- controlled categorical values where stable;
- explicit prohibition of human/gold fields in machine candidates;
- explicit prohibition of model provenance fields in human-adjudicated gold records.

### Repository validators handle

- uniqueness across CSV shards;
- foreign-key relationships;
- deterministic 24-document / 96-fragment design;
- 12/84 calibration-reserve partition;
- codebook blob-SHA provenance;
- coder identity and independence;
- access-problem completion exceptions;
- formal-reliability gates;
- metadata/version/snapshot consistency;
- machine/human separation;
- phase-5 gold-set gate.

## CSV versus JSON

Most public PDHD data are CSV because tabular diffability and Git review are important for provenance. JSON Schema is therefore not used as a direct CSV parser. Instead, schema properties define the portable object representation of the same conceptual record. The canonical CSV field semantics are documented in `docs/DATA_DICTIONARY.md`.

## Forward compatibility

Schema changes that alter semantics require:

1. a versioned rationale in `CHANGELOG.md`;
2. synchronized validator changes;
3. an updated data dictionary or lifecycle contract;
4. no silent reinterpretation of previously frozen documentary evidence;
5. a new codebook version if human semantic coding rules are affected.

Adding a new optional structural metadata field does not by itself require a new codebook. Changing the meaning or allowed values of a semantic annotation field does.
