# PDHD-U1 academic dataset deposit 0.1

## Deposit identity

**Title:** *Práctica Docente Histórica Digital (PDHD-U1): pre-validation corpus and provenance package for Mexican teaching-practice history*  
**Resource type:** Dataset  
**Version:** `0.1.0-prevalidation`  
**Creator:** Fernando Sandoval Gutiérrez  
**ORCID:** https://orcid.org/0000-0002-3168-6725  
**Repository:** https://github.com/fersandovalgtz/practica-docente-historica-digital  
**Scientific snapshot:** `PDHD-U1-PREVALIDATION-0.1-20260907`  
**DOI:** `10.5281/zenodo.22659767`  
**Zenodo record:** https://zenodo.org/records/22659767  
**Publication status:** published publicly on 2026-09-08.

## Scientific state represented

This deposit packages the first reproducible pre-validation state of PDHD-U1. It contains 24 selected pilot documents, 96 deterministic fragment identities, 96 localized fragments and 96 frozen fragments. The future human-validation design is fixed as 12 calibration fragments plus an 84-fragment reliability reserve. Human semantic coding remains at 0 and gold labels remain at 0.

The dataset therefore documents corpus construction, source identity, provenance, rights handling, retrieval, substitution and fixed evidence boundaries. It is **not** a human-validated benchmark and does not support prevalence claims about Mexican teaching practice.

## Canonical archival contents

The Zenodo deposit uses the verified archive `PDHD-U1-dataset-0.1.0-prevalidation.zip`, SHA-256 `1484838be4c7d29c491f65b88ce65fa8be4a437c64c376ee24e89faf9383ac35`. The archive is reconstructed from immutable repository state `0daec7850325f08dbb37e3fa053fb182e0e4093a` and future packaging runs must reproduce the same checksum.

The following files are the minimum scientific surfaces that define the dataset:

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

Original PDHD-derived data and metadata are intended for release under **CC BY 4.0** where PDHD has legal capacity to license them. This grant does not automatically extend to third-party historical documents, page images, facsimiles, OCR, transcriptions or third-party metadata. The deposit preserves `RIGHTS.md`, `DATA_LICENSE.md` and `data/catalog/rights_registry.csv`; historical source files are not added merely because they are technically downloadable.

## Published Zenodo description

Práctica Docente Histórica Digital (PDHD-U1) is a provenance-first historical research dataset for reproducible study of teaching-practice history in Mexico. This pre-validation release contains a controlled pilot of 24 documents and 96 fixed documentary fragments, together with source and document metadata, rights policies, structured retrieval provenance, versioned substitutions, schemas, a deterministic 12-item calibration cohort and an 84-item reliability reserve. All 96 fragments are localized and frozen, while human semantic coding and gold labels remain deliberately at zero. The release supports auditing, reuse and replication of corpus-construction methods but does not constitute a validated benchmark or a representative sample of Mexican teaching practice.

## Keywords

history of education; teaching practice; digital humanities; historical corpus; Mexico; provenance; reproducibility; FAIR data; source criticism; teacher education

## Canonical dataset citation

Sandoval Gutiérrez, Fernando. (2026). *Práctica Docente Histórica Digital (PDHD-U1): pre-validation corpus and provenance package for Mexican teaching-practice history* (Version 0.1.0-prevalidation) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.22659767

The DOI identifies this dataset record, not the associated data paper or the live software repository.

## Completed deposit procedure

1. A manual Zenodo dataset deposit was created and DOI `10.5281/zenodo.22659767` reserved.
2. The verified archive `PDHD-U1-dataset-0.1.0-prevalidation.zip` was uploaded.
3. Dataset metadata, creator ORCID, version, CC BY 4.0 rights boundary, keywords and GitHub relationship were entered.
4. The creator published the record publicly on 2026-09-08 at https://zenodo.org/records/22659767.
5. The repository records the published DOI and record URL while preserving the exact archive filename and SHA-256.
6. Any concept DOI exposed by Zenodo remains to be recorded only after independent metadata retrieval; it is not inferred.

## Scientific boundary

`documentary_freeze_complete != semantic_validation_complete`

`dataset_doi != gold_standard`

`repository_access != source_republication_rights`
