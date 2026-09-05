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
| Fully frozen fragments | **21 / 96** | three complete batches plus five partial primary-source batches |
| Human-validated pedagogical fragments | 0 | not started |

The 75-object cohort remains a stabilization corpus, not a national representative sample. PDHD-U1 now has **80 of the 96 deterministic reliability slots** tied to a documented page, scan or section target. Twenty-one units have crossed the stronger frozen-fragment gate.

## Sampling status

The first reliability corpus remains frozen in `data/samples/pilot_document_selection_0_1.csv`: 10 E1 documents, 12 E3 documents and 2 E4 documents. It includes regional origins outside Mexico City, multiple documentary regimes and no publication contributing more than six documents. This is a methodological reliability sample rather than an estimator of national historical frequencies.

## Frozen-fragment evidence

Three selected documents have complete four-slot batches. `PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888, contributes `PDHD-F000013`–`PDHD-F000016`. `PDHD-D000001`, *La Enseñanza Objetiva* of 12 December 1891, contributes `PDHD-F000017`–`PDHD-F000020`. `PDHD-D000055`, the first 1921 number of *El Maestro. Revista de Cultura Nacional*, contributes `PDHD-F000053`–`PDHD-F000056`.

`PDHD-D000031`, *La Enseñanza Moderna*, tomo I, segunda época, núm. 1, 1 July 1907, contributes a three-slot frozen batch. Direct BVMC image inspection fixes `PDHD-F000038` as the editorial/professional masthead region, `PDHD-F000039` as the opening programmatic article region and `PDHD-F000040` as the publication/subscription administrative control. `PDHD-F000037` remains pending.

`PDHD-D000011`, the inaugural *La Enseñanza Normal* issue of 15 September 1904, contributes a two-slot frozen batch from the exact BVMC primary PDF. `PDHD-F000034` fixes the first-page professional/editorial block and `PDHD-F000036` fixes the autonomous publication-cadence line as an administrative control. `PDHD-F000033` on p. 12 remains pending primary inspection.

`PDHD-D000053`, *El Maestro*, tomo II, núm. 3, contributes a two-slot frozen batch from directly inspected Internet Archive BookReader images. `PDHD-F000050` uses leaf `n237` for the issue-specific institutional imprint block of the Secretaría de Educación Pública and Talleres Gráficos de la Nación. `PDHD-F000052` uses leaf `n236` for the title/volume/number/date cartouche as a deliberately non-analytical control.

Two additional *El Maestro* control slots now cross the same primary-image gate. `PDHD-F000044`, attached to núm. 2 of 1921, is fixed on the issue-identification cartouche of BookReader leaf `n104`, whose cover explicitly shows `NUM II`, `MEXICO` and `MCMXXI`. `PDHD-F000048`, attached to núm. 4 of 1921, is fixed on the corresponding cartouche of leaf `n4`, which explicitly shows `NUM IV`, `MEXICO` and `MCMXXI`. In both cases the frozen span excludes the cover illustration and uses only the bibliographic control region.

All Internet Archive frozen controls remain `metadata_only` and `not_transcribed`; no source image or historical full text is committed.

## El Maestro image-verification sequence

The P2 retrieval route corrected an erroneous Search Inside to BookReader mapping by reconciling scandata and page numbering. Direct inspection of `n236` and `n237` resolved tomo II, núm. 3 to **1921-12** at month precision and closed `PDHD-X000005` while retaining the secondary 1922 listing as a documented discrepancy.

The P3 retrieval route then used short windows around the registered reader targets rather than assuming that the original target leaf itself was the final span. For `PDHD-F000044`, the window around `n103` exposed the unambiguous núm. II cover at `n104`. For `PDHD-F000048`, the window around `n6` exposed the unambiguous núm. IV cover at `n4`. This preserves the distinction:

`reader_page_target != analytical_span`

The registered reader route supported retrieval; only the visually inspected primary image supported the final frozen boundary.

## Remaining localization work

The union of all `fragment_locator_progress*.csv` shards contains **80/96** pilot slots. Twenty-one are frozen. The remaining **59** located rows include direct section starts, reproduced facsimiles, exact scholarly page pointers and other candidates that have not crossed the exact-boundary primary-inspection gate. **16 slots remain without a locator.**

The direct-primary freeze-conversion queue is now reduced to one fragment: `PDHD-F000060`, the `PR5` title-page control for *El esfuerzo educativo en México* in Google Books. It remains unfrozen until a primary page image can be inspected directly and the smallest defensible control span plus access/transcription decisions are fixed.

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

`validate_object_aliases.py` protects cross-repository bridges. `validate_content_leads.py` checks promoted content leads against the locator union. `validate_retrieval_attempts.py` preserves blocked attempts and completed recovery routes; completed P1, P2 and P3 attempts use `superseded_by_locator`. `validate_status_counts.py` keeps README and this cohort-status document synchronized with the CSV source of truth.

## What remains before human coding

Human annotation has **not** started. The target remains 96 frozen reliability fragments, four per selected document, followed by a separate 12-fragment calibration set. Every reliability fragment must retain an immutable ID, source identity, page/localizer, fixed boundary, access/rights basis and selection role.

The current 21 frozen units demonstrate that the pipeline works across HNDM, BVMC and Internet Archive primary interfaces and across late-nineteenth-, early-twentieth- and postrevolutionary documentary settings. They do not justify coder labeling before the package is complete.

## Rights constraint

Primary-source access does not equal republication permission. HNDM remains `metadata_only`; HathiTrust, Internet Archive and Google Books/Google Play access are treated as research-access or retrieval layers rather than blanket licenses to mirror scans or full OCR. Where reuse is not clearly authorized, coder text remains outside the public repository.

## Decision

PDHD-U1 remains in **active pilot freezing**. Issue #1 stays open through completion of the 96-fragment package and the first independent human reliability round.

The project is now at **80/96 localized**. The 80/96 operational threshold has been reached. The next quantitative checkpoint is **84/96 localized**, but the stronger scientific priority remains raising the frozen count beyond **21/96**, beginning with direct primary inspection of `PDHD-F000060` and then converting stronger page-resolved candidates without weakening the evidence hierarchy.