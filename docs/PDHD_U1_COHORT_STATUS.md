# PDHD-U1 cohort status

Reference cut: **2026-09-03**

## Current thresholds

| Layer | Count | Status |
|---|---:|---|
| Registered discovery candidates | 25 | threshold reached |
| Object-level documents | 75 | stabilization advanced |
| Issue-level leads | 21 total / 19 unresolved | active balancing queue |
| Sources with explicit rights policy | 13 / 13 | complete at source-policy level |
| Registered chronology conflicts | 2 | explicitly preserved |
| Frozen pilot documents | 24 | document-selection gate passed |
| Target fixed fragments | 96 | not yet frozen |
| Human-validated pedagogical fragments | 0 | not started |

The original 50-document threshold established that PDHD-U1 could sustain object identity, provenance, rights and annotation workflows. The cohort has now reached **75 object-level records** while reducing the original dependence on two 1904–1907 pedagogical series.

## Composition of the 75-document union

PDHD currently treats `data/catalog/documents.csv` and `data/catalog/documents_balancing_w1.csv` as two validated shards of one object catalog. The separation remains temporary and keeps the balancing intervention auditable.

### By evidence source

| Source | Documents | Share |
|---|---:|---:|
| BVM-CERVANTES | 40 | 53.3% |
| UNAM-RI | 11 | 14.7% |
| HNDM | 7 | 9.3% |
| INTERNET-ARCHIVE | 7 | 9.3% |
| GOOGLE-BOOKS | 5 | 6.7% |
| HATHITRUST | 4 | 5.3% |
| BIBMX-FR | 1 | 1.3% |

The original 80% dependence on BVM-CERVANTES has fallen to **53.3%**. Concentration remains visible, but the balancing strategy now adds independent institutional sources and documentary regimes rather than only more periodical issues.

## Rural-teacher primary-source block resolved

The previous hard blocking condition was the absence of primary-localized rural-teacher material. That condition is now resolved through direct historical objects.

`PDHD-D000067` is the 1925 SEP pamphlet *El papel social del maestro rural*, cataloged by HathiTrust with a full-view copy. `PDHD-D000068` is the 1927 SEP volume *El sistema de escuelas rurales en México*. `PDHD-D000069` is *Las misiones culturales en 1927: Las escuelas normales rurales*. `PDHD-D000071` is the 1933 SEP volume *Las misiones culturales, 1932-1933*. Together with the SEP institutional memories `PDHD-D000072` through `PDHD-D000075`, these objects provide a primary documentary basis for rural teaching, missions, teacher preparation, inspection, supervision and Cardenista administration.

This means PDHD no longer needs to treat citations in later historiography as substitutes for the historical objects required by the pilot.

## Documentary-type depth

The stabilized union now includes at least the following object types:

- `issue`;
- `hemerographic_object`;
- `official_report`;
- `teacher_guidance`;
- `institutional_monograph`;
- `policy_proposal`.

This is a substantive improvement because the project can now test whether a coding scheme survives changes in documentary regime rather than only changes among periodical titles.

## Geographic condition

Direct object-level records now provide clear regional origins outside Mexico City for at least:

- Xalapa, Veracruz — *México intelectual*;
- Aguascalientes — *El Instructor*;
- Campeche — *El Periquito*.

These records satisfy the geographic diversity condition for the methodological pilot. They do not establish national representativeness.

## First 24-document pilot selection

The first document set for human-validation has been frozen in `data/samples/pilot_document_selection_0_1.csv` and documented in `docs/PILOT_DOCUMENT_SELECTION_0_1.md`.

The selection contains:

| Era | Documents |
|---|---:|
| E1 — 1870–1910 | 10 |
| E3 — 1921–1934 | 12 |
| E4 — 1935–1940 | 2 |

No publication contributes more than six documents; *El Maestro* contributes four, and no other selected periodical approaches the 25% ceiling. The pilot also contains more than three documentary types and at least three geographic origins outside Mexico City.

Therefore the **document-selection gate is passed**.

## What remains before human coding

Human annotation has **not** started. The next required operation is a fragment-freezing pass over the 24 selected documents.

Four fixed fragments must be prepared per document, yielding **96 reliability fragments**. Every fragment must retain document ID, page or stable localizer, transcription status, access/rights basis, selection rationale and immutable `fragment_id`.

The preparation design requires:

1. one explicit pedagogical act or instructional prescription;
2. one passage on professional identity, authority, supervision, evaluation or organization;
3. one historically salient passage selected through source criticism rather than keyword expectation;
4. one control passage capable of receiving `none` or `unclear` for at least one coded field.

A separate 12-fragment calibration set remains required before the 96-fragment independent reliability round.

## Rights constraint during fragment freezing

Primary-source resolution does not equal republication permission. HNDM remains `metadata_only`; HathiTrust and Google Books full-view status is treated as research access rather than a blanket license to mirror scans or full OCR. Where public excerpt storage is not clearly supported, coder-local text or minimal legally defensible excerpts must be separated from public metadata and localizers.

## Epistemic status

The current set is a **pilot-ready document cohort**, not an analysis-ready national sample.

`document_selection_ready != annotation_started`

`pilot_reliability != historical_representativeness`

`primary_source_resolved != source_text_republishable`

`digitized_series_density != historical_importance`

## Decision

PDHD-U1 has advanced from infrastructure testing to **pilot preparation**. Issue #1 should remain open through fragment freezing and the first independent human reliability round. The next meaningful threshold is not a larger raw document count: it is a complete, rights-aware, reproducible set of 96 fixed fragments ready for blind human coding.
