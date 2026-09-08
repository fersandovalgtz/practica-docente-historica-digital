# PDHD data paper — submission note 0.1

## Recommended product

**Data paper:** *Práctica Docente Histórica Digital (PDHD): a provenance-first corpus for reproducible research on Mexican teaching-practice history*.

The manuscript in `PDHD_DATA_PAPER_DRAFT_0_1.md` is intentionally written as a corpus-construction and data-stewardship article. It does not report semantic findings that require human validation.

## Primary target

**Research Data Journal for the Humanities and Social Sciences (RDJ).**

Rationale:

- the journal publishes peer-reviewed data papers in the humanities and social sciences;
- data papers may be up to 2,500 words;
- the journal requires the underlying dataset to be deposited in a trusted repository;
- it operates as Diamond Open Access, so authors do not incur an APC;
- the PDHD manuscript fits the journal's emphasis on dataset documentation, transparency, reuse, and FAIR research practice.

Current journal information should be rechecked immediately before submission because editorial policies can change.

## Secondary target

**Journal of Open Humanities Data (JOHD).**

JOHD is a strong disciplinary fit for history and digital humanities. Its current Data Paper format is shorter, approximately 1,000–1,500 words, and requires a public repository deposit with a DOI or similar persistent identifier. The present manuscript would therefore need a condensed version for JOHD.

## What is already submission-grade

The repository already provides:

- a stable project identity and ORCID metadata;
- a field-level data dictionary;
- JSON schemas separating documents, frozen fragments, human annotations, machine candidates, and future gold annotations;
- an explicit rights registry;
- retrieval provenance, including failed routes;
- four versioned pilot substitutions;
- a deterministic 24-document / 96-fragment pilot;
- 96/96 localized and 96/96 frozen fragments;
- a signed pre-validation scientific snapshot;
- reproducible CI and integrity checks;
- a deterministic 12-item calibration cohort and 84-item reliability reserve;
- explicit gates that prevent automated outputs from being treated as human validation.

## What must happen before journal submission

### Archival deposit

Create a citable archival deposit of the exact pre-validation dataset in a trusted repository. The deposit must receive a DOI or comparable persistent identifier. GitHub remains the development repository; the archival deposit is the immutable object cited by the paper.

The deposit should contain PDHD-created metadata, schemas, documentation, and code that are eligible for redistribution. It must not add third-party facsimiles, full OCR, or historical source files when the rights registry does not permit redistribution.

### Manuscript DOI insertion

Replace the placeholder `Dataset DOI` in the manuscript with the archival DOI. Update the Data and code availability section accordingly.

### Journal-format pass

Reformat the manuscript to the selected journal template. Preserve the scientific state as pre-validation. Do not rewrite `0 human-coded`, `0 gold labels`, or the closed reliability/phase-5 gates merely to make the paper appear more complete.

### Final literature and reference audit

Verify all bibliographic metadata and DOI links immediately before submission. Expand the humanities-data literature if the selected editor or journal template expects a broader disciplinary discussion.

## Claims the paper may make now

The article may state that PDHD-U1 has completed documentary localization and fragment freezing for the 96-unit pilot. It may describe provenance, rights handling, retrieval routes, versioned substitutions, deterministic sampling infrastructure, schemas, reproducibility, and reuse potential.

## Claims the paper must not make now

The manuscript must not claim validated pedagogical prevalence, formal inter-coder reliability, benchmark accuracy, gold-standard status, model performance, or national representativeness. It must not treat prescriptive text as observed classroom practice.

## Publication logic

This product creates an academically citable output **before** semantic analysis. A later research article can cite the data paper and then report validated historical findings after human calibration, formal reliability, adjudication, and phase-5 analysis have legitimately opened.
