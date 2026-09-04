# PDHD-U1 cohort status

Reference cut: **2026-09-04**

## Current thresholds

| Layer | Count | Status |
|---|---:|---|
| Registered discovery candidates | 25 | threshold reached |
| Object-level documents | 75 | stabilization advanced |
| Issue-level leads | 21 total / 19 unresolved | active balancing queue |
| Sources with explicit rights policy | 13 / 13 | complete at source-policy level |
| Registered chronology conflicts | 2 | explicitly preserved |
| Frozen pilot documents | 24 | document-selection gate passed |
| Target fixed fragments | 96 | preparation active |
| Fragment locator rows resolved/candidate | **38 / 96** | source-localization pass active |
| Fully frozen fragments | **4 / 96** | first true freeze batch completed |
| Human-validated pedagogical fragments | 0 | not started |

The original 50-document threshold established that PDHD-U1 could sustain object identity, provenance, rights and annotation workflows. The cohort has now reached **75 object-level records** while reducing the original dependence on two 1904–1907 pedagogical series. The project has also crossed a second methodological threshold: exact fragment freezing is no longer only a protocol; four pilot fragments now have fixed structural boundaries and a dedicated frozen registry.

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

The original 80% dependence on BVM-CERVANTES has fallen to **53.3%**. Concentration remains visible, but the balancing strategy adds independent institutional sources and documentary regimes rather than merely accumulating more issues from the best-digitized series.

## Rural-teacher primary-source block resolved

The previous hard blocking condition was the absence of primary-localized rural-teacher material. That condition is now resolved through direct historical objects.

`PDHD-D000067` is the SEP pamphlet *El papel social del maestro rural*. `PDHD-D000068` is *El sistema de escuelas rurales en México*. `PDHD-D000069` is *Las misiones culturales en 1927: Las escuelas normales rurales*. `PDHD-D000071` is *Las misiones culturales, 1932-1933*. Together with `PDHD-D000066`, *El esfuerzo educativo en México*, and the SEP institutional memories `PDHD-D000072` through `PDHD-D000075`, these objects provide a primary documentary basis for rural teaching, missions, teacher preparation, inspection, supervision and federal educational administration.

This means PDHD no longer needs to treat citations in later historiography as substitutes for the historical objects required by the pilot. Secondary scholarship remains useful as a retrieval layer and is explicitly marked when it supplies only a page pointer.

## Documentary-type depth

The stabilized union includes at least `issue`, `hemerographic_object`, `official_report`, `teacher_guidance`, `institutional_monograph` and `policy_proposal`. This matters because the coding scheme can be tested across documentary regimes rather than merely across periodical titles.

## Geographic condition

Direct object-level records provide regional origins outside Mexico City for Xalapa, Veracruz (*México intelectual*), Aguascalientes (*El Instructor*) and Campeche (*El Periquito*). These records satisfy the geographic-diversity condition for the methodological pilot. They do not establish national representativeness.

## First 24-document pilot selection

The first document set for human validation is frozen in `data/samples/pilot_document_selection_0_1.csv` and documented in `docs/PILOT_DOCUMENT_SELECTION_0_1.md`.

| Era | Documents |
|---|---:|
| E1 — 1870–1910 | 10 |
| E3 — 1921–1934 | 12 |
| E4 — 1935–1940 | 2 |

No publication contributes more than six documents; *El Maestro. Revista de Cultura Nacional* contributes four, and no other selected periodical approaches the 25% ceiling. The pilot contains more than three documentary types and at least three geographic origins outside Mexico City. The **document-selection gate is therefore passed**.

## First true fragment-freeze batch

`PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888, now contributes the first four genuinely frozen units: `PDHD-F000013` through `PDHD-F000016`.

The source page was inspected directly in the HNDM interface. PDHD fixed structural boundaries for an instructional/pedagogical paragraph, a professional editorial roster, a historically salient methodological passage and a deliberately non-analytical masthead/control block. Because HNDM remains `metadata_only`, the repository does **not** commit the historical text or page image. It stores the page, structural locator, boundary definition, access basis and preparation provenance.

The canonical frozen registry is `data/samples/frozen_fragments_0_1.csv`. Its separation from `fragment_locator_progress_0_1.csv` is intentional: a locator queue records work in progress, whereas the frozen registry records only units that have crossed the full boundary and access gate.

This creates a new operational distinction:

`locator_candidate != frozen_fragment`

`fixed_boundary != public_text_permission`

`frozen_fragment != validated_annotation`

## Fragment-localization progress

Thirty-eight pilot slots now have documented page-level or section-level locator candidates in `data/samples/fragment_locator_progress_0_1.csv`.

The queue includes four frozen HNDM slots from `PDHD-D000002`; four candidates from `PDHD-D000068`; four from `PDHD-D000069`; four from `PDHD-D000070`; four from `PDHD-D000071`; three from `PDHD-D000072`; four from `PDHD-D000073`; four from `PDHD-D000075`; four newly localized slots from `PDHD-D000066`; and three newly localized slots from `PDHD-D000067`.

For `PDHD-D000066`, *El esfuerzo educativo en México*, Google Books directly exposes the beginning of the Department of Rural Primary Schools on page 1 and the Directorate of Cultural Missions and Normal Schools on page 113. Historical scholarship supplies a weaker page-level pointer to pages 94–95 and 104 for quantitative evidence on rural-school expansion and schooling in predominantly Indigenous settlements. The title page, exposed directly as Google Books `PR5`, is retained as a control candidate.

For `PDHD-D000067`, *El papel social del maestro rural*, a recent historical study explicitly cites page 5 for hygiene and household routines, the rural teacher's social function and the promotion of vocational preparation. These three rows remain `secondary_page_pointer_primary_check_pending`; none may be frozen until page 5 is inspected in the primary SEP pamphlet.

The queue therefore intentionally mixes different evidentiary strengths. `docs/LOCATOR_EVIDENCE_POLICY.md` distinguishes direct primary passages, direct primary section starts, scholarly page pointers, embedded reproduced facsimiles and bibliographic leads.

The rule remains explicit:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`table_of_contents_entry != passage`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Integrity checks for frozen units

`scripts/validate_repository.py` now validates the frozen-fragment registry against both the deterministic 96-slot manifest and the locator queue. A frozen row must match its expected document and slot, preserve the same page and source locator as the locator record, contain a boundary definition and access basis, use controlled transcription/public-text/selection-role states, and have a corresponding locator row marked `frozen` with `boundary_status=fixed`.

This prevents a fragment from being called frozen merely because a page number has been found.

## What remains before human coding

Human annotation has **not** started. Four fixed fragments must ultimately be prepared per document, yielding **96 reliability fragments**. Every fragment must retain document ID, page or stable localizer, boundary definition, transcription status, access/rights basis, selection rationale and immutable `fragment_id`.

A separate 12-fragment calibration set remains required before the 96-fragment independent reliability round. The first four frozen fragments are methodological proof that the pipeline works; they are not permission to begin coder labeling early.

## Rights constraint during fragment freezing

Primary-source resolution does not equal republication permission. HNDM remains `metadata_only`; HathiTrust and Google Books/Google Play full-view status is treated as research access rather than a blanket license to mirror scans or full OCR. Where public excerpt storage is not clearly supported, coder-local text or source-interface consultation must remain separated from public metadata and localizers.

## Epistemic status

The current set is a **pilot-ready document cohort with fragment freezing underway**, not an analysis-ready national sample.

`document_selection_ready != annotation_started`

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`page_locator_resolved != fixed_coder_span`

`section_start != analytical_fragment`

`pilot_reliability != historical_representativeness`

`primary_source_resolved != source_text_republishable`

`digitized_series_density != historical_importance`

## Decision

PDHD-U1 has advanced from infrastructure testing to **active pilot freezing**. Issue #1 remains open through completion of the 96-fragment package and the first independent human reliability round. The next meaningful threshold is to increase the proportion of directly inspected primary passages and frozen spans, not merely the raw locator count.
