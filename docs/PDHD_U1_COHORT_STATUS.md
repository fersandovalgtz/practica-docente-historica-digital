# PDHD-U1 cohort status

Reference cut: **2026-09-04**

## Current thresholds

| Layer | Count | Status |
|---|---:|---|
| Registered discovery candidates | 25 | threshold reached |
| Object-level documents | 75 | stabilization advanced |
| Issue-level leads | 21 total / 19 unresolved | active balancing queue |
| Sources with explicit rights policy | 13 / 13 | complete at source-policy level |
| Registered chronology conflicts | 3 | explicitly preserved |
| Frozen pilot documents | 24 | document-selection gate passed |
| Target fixed fragments | 96 | preparation active |
| Fragment locator rows resolved/candidate | **42 / 96** | source-localization pass active |
| Fully frozen fragments | **8 / 96** | two complete four-slot document batches |
| Human-validated pedagogical fragments | 0 | not started |

The original 50-document threshold established that PDHD-U1 could sustain object identity, provenance, rights and annotation workflows. The cohort has now reached **75 object-level records** while reducing the original dependence on two 1904–1907 pedagogical series. Exact fragment freezing is no longer only a protocol: two complete pilot documents now contribute eight structurally fixed units with a rights-aware public registry.

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

Secondary scholarship remains useful as a retrieval layer and is explicitly marked when it supplies only a page pointer. A new chronology conflict also preserves the difference between the 1925 HathiTrust catalog date for *El papel social del maestro rural* and a 1926 archival citation reported in recent UAA scholarship. PDHD retains 1925 as the working catalog year while leaving the discrepancy open for direct-object inspection.

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

## Two complete fragment-freeze batches

The first complete batch comes from `PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888, and contains `PDHD-F000013` through `PDHD-F000016`. Direct HNDM page inspection fixed an instructional/pedagogical paragraph, a professional editorial roster, a historically salient methodological passage and a deliberately non-analytical masthead/control block.

The second complete batch comes from `PDHD-D000001`, *La Enseñanza Objetiva* of 12 December 1891, and contains `PDHD-F000017` through `PDHD-F000020`. Direct inspection fixed a compact explained-reading/vocabulary teaching unit, the publication's explicit pedagogical mission statement, a grammar sentence-transformation sequence and a non-analytical subscription/publication control block.

Because both sources are HNDM and HNDM remains `metadata_only`, the repository does **not** commit the historical text or page images. It stores page identity, structural localizer, boundary definition, access basis, public-text decision and preparation provenance.

The work is now stored in auditable shards: `data/samples/fragment_locator_progress*.csv` and `data/samples/frozen_fragments*.csv`. Sharding allows new batches to be added without rewriting the preceding frozen evidence, while `scripts/validate_fragment_shards.py` treats every shard as one logical 96-slot union.

The operational distinctions remain:

`locator_candidate != frozen_fragment`

`fixed_boundary != public_text_permission`

`frozen_fragment != validated_annotation`

## Fragment-localization progress

The union of locator shards now contains **42/96** pilot slots. Eight are fully frozen. The remaining 34 rows range from direct primary page/section evidence to secondary scholarly page pointers that still require primary-object verification.

The queue includes `PDHD-D000066`, *El esfuerzo educativo en México*; `PDHD-D000067`, *El papel social del maestro rural*; `PDHD-D000068`, *El sistema de escuelas rurales en México*; `PDHD-D000069`, *Las misiones culturales en 1927*; `PDHD-D000070`, *Proyecto para la organización de las misiones federales de educación*; `PDHD-D000071`, *Las misiones culturales, 1932-1933*; the SEP memories for 1932, 1934 and 1938; and the two directly inspected HNDM periodicals.

For `PDHD-D000067`, recent UAA scholarship points specifically to page 5 for hygiene and household routines, the rural teacher's social function and vocational preparation. Those rows remain `secondary_page_pointer_primary_check_pending`. The same scholarly citation gives a 1926 imprint, while HathiTrust catalogs the pamphlet as 1925; that discrepancy is now preserved in `data/catalog/chronology_conflicts.csv` rather than silently normalized.

The queue intentionally mixes different evidentiary strengths. `docs/LOCATOR_EVIDENCE_POLICY.md` distinguishes direct primary passages, direct primary section starts, scholarly page pointers, embedded reproduced facsimiles and bibliographic leads.

The rule remains explicit:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`table_of_contents_entry != passage`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Integrity checks for frozen units

`scripts/validate_repository.py` continues to validate the base catalog and primary sample files. `scripts/validate_fragment_shards.py` adds union-level validation across every `fragment_locator_progress*.csv` and `frozen_fragments*.csv` shard. It rejects duplicate fragment IDs across batches, mismatches between document and deterministic slot, frozen locators without fixed boundaries, frozen-registry rows without a corresponding locator, and disagreements in page or source identity between the two layers.

This prevents a fragment from being called frozen merely because a page number has been found and prevents batch-oriented work from fragmenting the methodological identity of the pilot.

## What remains before human coding

Human annotation has **not** started. Four fixed fragments must ultimately be prepared per document, yielding **96 reliability fragments**. Every fragment must retain document ID, page or stable localizer, boundary definition, transcription status, access/rights basis, selection rationale and immutable `fragment_id`.

A separate 12-fragment calibration set remains required before the 96-fragment independent reliability round. The eight frozen fragments establish that the pipeline works across two periodicals; they are not permission to begin coder labeling early.

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
