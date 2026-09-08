# PDHD data paper — submission note 0.1

## Recommended product

**Data paper:** *Práctica Docente Histórica Digital (PDHD): a provenance-first corpus for reproducible research on Mexican teaching-practice history*.

The manuscript in `PDHD_DATA_PAPER_DRAFT_0_1.md` is intentionally written as a corpus-construction and data-stewardship article. It does not report semantic findings that require human validation.

## Current submission state — 2026-09-08

The archival prerequisite is now complete. PDHD-U1 version `0.1.0-prevalidation` is publicly deposited in Zenodo at DOI `10.5281/zenodo.22659767`, record `https://zenodo.org/records/22659767`.

The canonical archive remains `PDHD-U1-dataset-0.1.0-prevalidation.zip`, SHA-256 `1484838be4c7d29c491f65b88ce65fa8be4a437c64c376ee24e89faf9383ac35`. Dataset publication does not alter the human-validation state: 0 human-coded fragments, no formal reliability round, and 0 gold labels.

## Primary target

**Research Data Journal for the Humanities and Social Sciences (RDJ).**

Current author instructions were rechecked on 8 September 2026. RDJ remains the preferred target because:

- it publishes peer-reviewed data papers in the humanities and social sciences;
- data papers have a maximum length of 2,500 words;
- the underlying dataset must be formally published in a trusted digital archive or repository;
- it is Diamond Open Access and the APC is waived for authors;
- submission is handled through Editorial Manager;
- PDHD's provenance, rights, reproducibility and reuse architecture fits the journal's data-paper model.

Author instructions: `https://brill.com/fileasset/downloads_products/Author_Instructions/RDJ.pdf`.

The no-APC model is strategically preferable while preserving an international, peer-reviewed outlet and avoiding unnecessary publication cost.

## Secondary target

**Journal of Open Humanities Data (JOHD).**

JOHD remains a strong disciplinary fit for history and digital humanities. Its current general submission guidelines specify a highly structured Data Paper of 1,000–1,500 words, require the data to be public before submission and require the repository DOI to appear in the paper. The current PDHD manuscript would need a substantial condensation and journal-template conversion. JOHD also operates with an APC framework unless a discount, institutional agreement or waiver applies, so RDJ remains the economically preferable first target.

Current guidelines: `https://openhumanitiesdata.metajnl.com/about/submissions`.

## Submission-grade components already complete

The project now provides:

- a public archival dataset with DOI `10.5281/zenodo.22659767`;
- a stable project identity and ORCID metadata;
- a field-level data dictionary;
- JSON schemas separating documents, frozen fragments, human annotations, machine candidates and future gold annotations;
- an explicit rights registry;
- retrieval provenance, including failed routes;
- four versioned pilot substitutions;
- a deterministic 24-document / 96-fragment pilot;
- 96/96 localized and 96/96 frozen fragments;
- a signed pre-validation scientific snapshot;
- reproducible CI and integrity checks;
- a deterministic 12-item calibration cohort and 84-item reliability reserve;
- explicit gates that prevent automated outputs from being treated as human validation;
- a canonical archive whose SHA-256 is reproduced by the repository packaging workflow.

## Remaining work before submission

### Journal-format and length pass

Bring the manuscript into the RDJ submission format and confirm that the final count stays within the journal's 2,500-word maximum. If necessary, condense background prose before cutting methodological traceability.

### Final literature and reference audit

Verify bibliographic metadata, DOI links and the disciplinary data-paper literature immediately before submission. Keep the literature focused: provenance, FAIR stewardship, reproducible computational research, historical/digital humanities data and rights-aware reuse.

### Submission metadata and cover material

Prepare the final title, abstract, keywords, author affiliation, ORCID, dataset DOI, repository URL and any cover note required by Editorial Manager. Use the Zenodo dataset as the archival object and GitHub as the live technical repository.

### Final scientific-state check

Immediately before submission, confirm that all manuscript statements remain compatible with the canonical snapshot and current gates. Do not rewrite `0 human-coded`, `0 gold labels`, or the closed reliability/phase-5 gates merely to make the paper appear more complete.

## Claims the paper may make now

The article may state that PDHD-U1 has completed documentary localization and fragment freezing for the 96-unit pilot and that the resulting pre-validation dataset has been publicly archived with a DOI. It may describe provenance, rights handling, retrieval routes, versioned substitutions, deterministic sampling infrastructure, schemas, reproducibility and reuse potential.

## Claims the paper must not make now

The manuscript must not claim validated pedagogical prevalence, formal inter-coder reliability, benchmark accuracy, gold-standard status, model performance or national representativeness. It must not treat prescriptive text as observed classroom practice.

## Immediate execution order

1. Run the RDJ length/template pass.
2. Audit citations and DOI metadata.
3. Prepare submission metadata and cover material.
4. Submit through RDJ Editorial Manager.
5. After submission, record the manuscript status in the master system and move editorial follow-up to waiting/monitoring.
6. Keep issue #39 open; human calibration remains the next scientific gate rather than a prerequisite for this data paper.

## Publication logic

The published dataset plus the data paper produce two distinct citable outputs from the same research infrastructure. A later research article can cite both and report validated historical findings only after human calibration, formal reliability, adjudication and phase-5 analysis have legitimately opened.
