# PDHD-U1 academic dataset deposit 0.1

## Deposit identity

**Title:** *Práctica Docente Histórica Digital (PDHD-U1): pre-validation corpus and provenance package for Mexican teaching-practice history*  
**Resource type:** Dataset  
**Version:** `0.1.0-prevalidation`  
**Creator:** Fernando Sandoval Gutiérrez  
**ORCID:** https://orcid.org/0000-0002-3168-6725  
**Repository:** https://github.com/fersandovalgtz/practica-docente-historica-digital  
**Scientific snapshot:** `PDHD-U1-PREVALIDATION-0.1-20260907`  
**DOI:** to be reserved in Zenodo before publication of the deposit.

## Scientific state represented

This deposit packages the first reproducible pre-validation state of PDHD-U1. It contains 24 selected pilot documents, 96 deterministic fragment identities, 96 localized fragments and 96 frozen fragments. The future human-validation design is fixed as 12 calibration fragments plus an 84-fragment reliability reserve. Human semantic coding remains at 0 and gold labels remain at 0.

The dataset therefore documents corpus construction, source identity, provenance, rights handling, retrieval, substitution and fixed evidence boundaries. It is **not** a human-validated benchmark and does not support prevalence claims about Mexican teaching practice.

## Canonical archival contents

The Zenodo deposit must archive the immutable GitHub source archive corresponding to the canonical deposit commit together with this deposit specification. The following files are the minimum scientific surfaces that define the dataset:

### Corpus and catalog

- `data/catalog/documents.csv`
- `data/catalog/sources.csv`
- `data/catalog/rights_registry.csv`
- `data/catalog/object_aliases.csv`
- `data/catalog/chronology_conflicts.csv`
- `data/samples/pilot_document_selection_0_1.csv`
- `data/samples/frozen_fragments_0_1.csv`
- `data/samples/pilot_document_substitutions_0_1.csv`
- `data/samples/retrieval_attempts.csv`
- `data/samples/calibration_manifest_0_1.csv`
- `data/samples/reliability_reserve_0_1.csv`
- `data/samples/codebook_registry.csv`
- `data/snapshots/prevalidation_snapshot_0_1.json`

### Schemas

- `schemas/document.schema.json`
- `schemas/pedagogical_fragment.schema.json`
- `schemas/annotation.schema.json`
- `schemas/machine_candidate.schema.json`
- `schemas/gold_annotation.schema.json`

### Documentation, provenance and rights

- `docs/DATASET_CARD_0_1.md`
- `docs/DATA_DICTIONARY.md`
- `docs/SCHEMA_GUIDE_0_1.md`
- `PROVENANCE.md`
- `RIGHTS.md`
- `DATA_LICENSE.md`
- `CITATION.cff`

The complete source archive may contain additional repository documentation and validation code. Those files do not change the frozen scientific state identified by the snapshot.

## Rights and licensing

Original PDHD-derived data and metadata are intended for release under **CC BY 4.0** where PDHD has legal capacity to license them. This grant does not automatically extend to third-party historical documents, page images, facsimiles, OCR, transcriptions or third-party metadata. The deposit must preserve `RIGHTS.md`, `DATA_LICENSE.md` and `data/catalog/rights_registry.csv` and must not add historical source files merely because they are technically downloadable.

## Recommended Zenodo description

Práctica Docente Histórica Digital (PDHD-U1) is a provenance-first historical research dataset for reproducible study of teaching-practice history in Mexico. This pre-validation release contains a controlled pilot of 24 documents and 96 fixed documentary fragments, together with source and document metadata, rights policies, structured retrieval provenance, versioned substitutions, schemas, a deterministic 12-item calibration cohort and an 84-item reliability reserve. All 96 fragments are localized and frozen, while human semantic coding and gold labels remain deliberately at zero. The release supports auditing, reuse and replication of corpus-construction methods but does not constitute a validated benchmark or a representative sample of Mexican teaching practice.

## Keywords

history of education; teaching practice; digital humanities; historical corpus; Mexico; provenance; reproducibility; FAIR data; source criticism; teacher education

## Recommended citation before DOI assignment

Sandoval Gutiérrez, Fernando. (2026). *Práctica Docente Histórica Digital (PDHD-U1): pre-validation corpus and provenance package for Mexican teaching-practice history* (Version 0.1.0-prevalidation) [Data set]. GitHub. Cite the immutable deposit commit and `PDHD-U1-PREVALIDATION-0.1-20260907`.

## Citation after Zenodo publication

Replace the provisional GitHub citation with the Zenodo-generated citation and DOI. The DOI must identify this dataset record, not the associated data paper.

## Deposit procedure

1. Create a **new manual upload** in Zenodo and choose resource type **Dataset**.
2. Reserve the DOI before publication.
3. Use the metadata in `docs/academic_products/PDHD_ZENODO_METADATA_0_1.json`.
4. Upload the immutable source archive corresponding to the canonical deposit commit.
5. Verify that no restricted source facsimiles or third-party historical transcriptions were introduced.
6. Preview the record and verify creator name, ORCID, version, license, keywords and related GitHub repository.
7. Publish the Zenodo record only after the archive checksum and commit identity have been recorded in `data/snapshots/dataset_deposit_manifest_0_1.json`.
8. Add the assigned DOI back to the repository and to the data-paper manuscript in a subsequent versioned change.

## Scientific boundary

`documentary_freeze_complete != semantic_validation_complete`

`dataset_doi != gold_standard`

`repository_access != source_republication_rights`
