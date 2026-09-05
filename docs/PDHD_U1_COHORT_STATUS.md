# PDHD-U1 cohort status

Reference cut: **2026-09-05**

## Current thresholds

| Layer | Count | Status |
|---|---:|---|
| Registered discovery candidates | 25 | threshold reached |
| Object-level documents | 75 | stabilization advanced |
| Issue-level leads | 21 total / 19 unresolved | active balancing queue |
| Sources with explicit rights policy | 13 / 13 | complete at source-policy level |
| Registered chronology conflicts | 5 | preserved; one resolved by primary-image evidence |
| Frozen pilot documents | 24 | document-selection gate passed |
| Target fixed fragments | 96 | preparation active |
| Fragment locator rows resolved/candidate | **80 / 96** | 83.3% of reliability slots localized |
| Fully frozen fragments | **19 / 96** | three complete batches plus three partial primary-source batches |
| Human-validated pedagogical fragments | 0 | not started |

The 75-object cohort remains a stabilization corpus, not a national representative sample. PDHD-U1 now has **80 of the 96 deterministic reliability slots** tied to a documented page, scan or section target. Nineteen units have crossed the stronger frozen-fragment gate.

## Sampling status

The first reliability corpus remains frozen in `data/samples/pilot_document_selection_0_1.csv`: 10 E1 documents, 12 E3 documents and 2 E4 documents. It includes regional origins outside Mexico City, multiple documentary regimes and no publication contributing more than six documents. This is a methodological reliability sample rather than an estimator of national historical frequencies.

## Frozen-fragment evidence

Three selected documents have complete four-slot batches. `PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888, contributes `PDHD-F000013`–`PDHD-F000016`. `PDHD-D000001`, *La Enseñanza Objetiva* of 12 December 1891, contributes `PDHD-F000017`–`PDHD-F000020`. `PDHD-D000055`, the first 1921 number of *El Maestro. Revista de Cultura Nacional*, contributes `PDHD-F000053`–`PDHD-F000056`.

`PDHD-D000031`, *La Enseñanza Moderna*, tomo I, segunda época, núm. 1, 1 July 1907, contributes a three-slot frozen batch. Direct BVMC image inspection fixes `PDHD-F000038` as the editorial/professional masthead region, `PDHD-F000039` as the opening programmatic article region and `PDHD-F000040` as the publication/subscription administrative control. `PDHD-F000037` remains pending.

`PDHD-D000011`, the inaugural *La Enseñanza Normal* issue of 15 September 1904, contributes a two-slot frozen batch from the exact BVMC primary PDF. `PDHD-F000034` fixes the first-page professional/editorial block and `PDHD-F000036` fixes the autonomous publication-cadence line as an administrative control. `PDHD-F000033` on p. 12 remains pending primary inspection.

`PDHD-D000053`, *El Maestro*, tomo II, núm. 3, now contributes a two-slot frozen batch from directly inspected Internet Archive BookReader images. `PDHD-F000050` uses leaf `n237` for the issue-specific institutional imprint block of the Secretaría de Educación Pública and Talleres Gráficos de la Nación. `PDHD-F000052` uses leaf `n236` for the title/volume/number/date cartouche as a deliberately non-analytical control. Both remain `metadata_only` and `not_transcribed`; no Internet Archive source image or historical full text is committed.

## El Maestro II.3 chronology and image verification

The P2 retrieval route is now closed. The initial Search Inside to BookReader mapping was incorrect and retrieved later pages. Scandata/page-number reconciliation moved the target to `n232–n238`, after which the corrected GitHub Actions workflow recovered the seven primary JPEGs successfully.

Direct inspection produces a coherent issue sequence. `n236` explicitly identifies *El Maestro*, tomo II, número III, diciembre de 1921, México. `n237` independently records `SECRETARIA DE EDUCACION PUBLICA`, Talleres Gráficos de la Nación and `MEXICO, DICIEMBRE DE 1921`. `n238` begins *La inconsciencia de la hora* on printed p. 227.

This evidence resolves chronology conflict `PDHD-X000005` at month precision. A secondary scholarly source had listed tomo II, núm. 3 as 1922 while a UNAM thesis cited December 1921. PDHD now adopts **1921-12** as the canonical date because two independent regions of the registered primary scan agree. The 1922 listing remains preserved in the conflict registry as a documented scholarly/catalog discrepancy.

The evidentiary sequence matters:

`primary_ocr_region != image_verified_span`

The earlier OCR materially improved retrieval, but only the primary image inspection supported the final chronology decision and fragment boundaries.

## Remaining localization work

The union of all `fragment_locator_progress*.csv` shards contains **80/96** pilot slots. Nineteen are frozen. The remaining **61** located rows include direct primary-page candidates, direct reader/scan targets, direct section starts, reproduced facsimiles and exact scholarly page pointers. **16 slots remain without a locator.**

The current direct-primary freeze-conversion queue contains three fragments: `PDHD-F000044`, `PDHD-F000048` and `PDHD-F000060`. The first two are *El Maestro* issue-opening control candidates with stable Internet Archive reader targets. The third is the `PR5` Google Books title-page control for *El esfuerzo educativo en México*. None is frozen until its exact primary span and access decisions are fixed.

The locator union currently holds 80 of 96 pilot slots and remains the source-of-truth layer for progress accounting. Localization does not imply that the historical page has been validated or that public transcription is permitted.

## Other high-value pending blocks

`PDHD-F000033` points to Leopoldo Kiel in *La Enseñanza Normal*, p. 12, on practice with groups of children, observation, experimentation and verification of teaching procedures. It remains a secondary page pointer until the historical BVMC page is directly inspected.

`PDHD-F000025` targets Ponciano Rodríguez, *El método en los libros de texto*, pp. 167–168 of *La Enseñanza Primaria*. `PDHD-F000027` targets Gregorio Torres Quintero, *Los ejercicios físicos en la escuela*, pp. 161–163. Both require direct HNDM primary-page inspection before freezing.

`PDHD-F000003`, slot C for *El Periquito*, núm. 4, 6 November 1870, targets p. 2 from an exact secondary citation. HNDM confirms the serial chronology and physical issue structure, but the historical page image/page ID remains the next gate.

`PDHD-D000063`, *México intelectual*, has all four deterministic slots localized. Its page-resolved targets remain individually governed by their evidence level and are not promoted solely because the document is fully localized.

The 1932 and 1937 SEP memories also have four-slot localization coverage. Google Books contents entries support section discovery while secondary page pointers support targeted retrieval; neither evidence class is treated as an exact coder span without primary-page inspection.

## Evidence rules retained

The retrieval chain remains:

`issue identity -> content lead -> promoted_fragment_id -> page-level fragment locator -> frozen fragment -> human annotation`

Mandatory distinctions remain:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`reader_page_target != analytical_span`

`primary_ocr_region != image_verified_span`

`table_of_contents_entry != passage`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Integrity and provenance

`scripts/validate_repository.py` validates the base catalog. `scripts/validate_fragment_shards.py` validates the logical union of all locator/frozen shards, including deterministic document/slot identity, duplicate protection, fixed-boundary requirements and cross-checking between frozen rows and locator rows. It also requires `fragment_gap_queue_0_1.csv` to equal the exact complement of the localized fragment IDs.

`validate_object_aliases.py` protects cross-repository bridges. `validate_content_leads.py` checks promoted content leads against the locator union. `validate_retrieval_attempts.py` preserves blocked attempts and completed recovery routes; completed P1/P2 attempts now use `superseded_by_locator`. `validate_status_counts.py` keeps README and this cohort-status document synchronized with the CSV source of truth.

## What remains before human coding

Human annotation has **not** started. The target remains 96 frozen reliability fragments, four per selected document, followed by a separate 12-fragment calibration set. Every reliability fragment must retain an immutable ID, source identity, page/localizer, fixed boundary, access/rights basis and selection role.

The current 19 frozen units demonstrate that the pipeline works across HNDM, BVMC and Internet Archive primary interfaces and across late-nineteenth-, early-twentieth- and postrevolutionary documentary settings. They do not justify coder labeling before the package is complete.

## Rights constraint

Primary-source access does not equal republication permission. HNDM remains `metadata_only`; HathiTrust, Internet Archive and Google Books/Google Play access are treated as research-access or retrieval layers rather than blanket licenses to mirror scans or full OCR. Where reuse is not clearly authorized, coder text remains outside the public repository.

## Decision

PDHD-U1 remains in **active pilot freezing**. Issue #1 stays open through completion of the 96-fragment package and the first independent human reliability round.

The project is now at **80/96 localized**. The 80/96 operational threshold has been reached. The next quantitative checkpoint is **84/96 localized**, but the stronger scientific priority remains raising the frozen count beyond **19/96**, especially by converting direct page/scan candidates into exact source-verified coder spans rather than adding weaker references.