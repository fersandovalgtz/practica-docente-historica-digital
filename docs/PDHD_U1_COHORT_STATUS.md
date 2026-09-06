# PDHD-U1 cohort status

Reference cut: **2026-09-06**

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
| Fragment locator rows resolved/candidate | **83 / 96** | 86.5% of reliability slots localized |
| Fully frozen fragments | **49 / 96** | page-resolved conversion phase active |
| Human-validated pedagogical fragments | 0 | not started |

The 75-object cohort remains a stabilization corpus, not a national representative sample. PDHD-U1 now has **83 of the 96 deterministic reliability slots** tied to a documented page, scan or section target. Forty-nine units have crossed the stronger frozen-fragment gate.

## Sampling status

The first reliability corpus remains frozen in `data/samples/pilot_document_selection_0_1.csv`: 10 E1 documents, 12 E3 documents and 2 E4 documents. It includes regional origins outside Mexico City, multiple documentary regimes and no publication contributing more than six documents. This is a methodological reliability sample rather than an estimator of national historical frequencies.

## Frozen-fragment evidence

Eleven selected documents now have complete four-slot batches. `PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888, contributes `PDHD-F000013`–`PDHD-F000016`. `PDHD-D000001`, *La Enseñanza Objetiva* of 12 December 1891, contributes `PDHD-F000017`–`PDHD-F000020`. `PDHD-D000055`, the first 1921 number of *El Maestro. Revista de Cultura Nacional*, contributes `PDHD-F000053`–`PDHD-F000056`.

`PDHD-D000003`, *La Enseñanza Primaria*, tomo I, núm. 11, 1 December 1901, contributes a complete four-slot batch from a directly retrieved Google Books primary PDF whose issue identity is independently matched by the UNAM/HNDM record. `PDHD-F000025` fixes the explicit-method prescription on printed p. 168. `PDHD-F000026` fixes the discrete masthead role identifying Gregorio Torres Quintero as Jefe de Redacción on p. 161. `PDHD-F000027` fixes the complete source-critical conclusion of *Los ejercicios físicos en la escuela* on p. 163. `PDHD-F000028` fixes the separate tomo/date/number cartouche on p. 161 as a deliberately non-analytical control. The primary PDF maps those printed pages to physical PDF pages 182, 175, 177 and 175 respectively.

`PDHD-D000031`, *La Enseñanza Moderna*, tomo I, segunda época, núm. 1, now contributes a complete four-slot batch. `PDHD-F000038`–`PDHD-F000040` remain fixed from direct BVMC first-page inspection. A dedicated recovery workflow subsequently downloaded and rendered the exact nine-page BVMC PDF. Direct inspection of printed p. 6 resolves `PDHD-F000037` from the *Clase de colores* lesson plan: the coder span begins at `Principio`, includes the contiguous `Medio`, `Fin`, `Método` and `Procedimiento` lines, and ends before `Ilustraciones`. The subsequent demonstration dialogue is deliberately excluded.

`PDHD-D000011`, the inaugural *La Enseñanza Normal* issue of 15 September 1904, contributes a complete four-slot batch from the exact BVMC primary PDF. `PDHD-F000033` fixes an explicit pedagogical-act paragraph on printed p. 12 in Leopoldo Kiel's *Conferencias Pedagógicas*. `PDHD-F000034` fixes the professional/editorial block on p. 1. `PDHD-F000035` fixes the opening of *15 de Septiembre — Fecha grata* on p. 4 as a source-critical political-educational framing of school, education, liberty and progress, ending before the article shifts toward military commemoration. `PDHD-F000036` fixes the publication-cadence control on p. 1. All four boundaries come from direct inspection of the primary PDF.

Internet Archive contributes four additional image-verified controls plus the institutional region of *El Maestro*. `PDHD-F000050` and `PDHD-F000052` are fixed from BookReader leaves `n237` and `n236` in tomo II, núm. 3. `PDHD-F000044` uses the issue-II cover cartouche at `n104`; `PDHD-F000048` uses the issue-IV cover cartouche at `n4`. These conversions preserve `reader_page_target != analytical_span`: the reader route supported retrieval, while the final boundary came only from visual inspection of the primary image.

The corrected tomo II, núm. 3 recovery now adds `PDHD-F000051` from printed p. 294 / BookReader `n305` as a directly inspected source-critical span in *Democracia Criolla*. The same inspection maps *El Cardo* to pp. 299–300 / `n310`–`n311`, strengthening `PDHD-F000049` to a direct primary locator while deliberately leaving it unfrozen: the visible literary school-reading unit does not itself satisfy slot A’s explicit pedagogical-act requirement. This preserves a failed-fit decision rather than converting mere educational context into a positive pedagogical fragment.

`PDHD-D000066`, *El esfuerzo educativo en México* (1928), contributes `PDHD-F000060` as a frozen title-page control. Google Books directly exposes `PR5`. A dedicated recovery workflow fetched the live PR5 HTML, resolved its public PDF link, downloaded a valid 29.9 MB primary PDF and rendered the relevant front matter. Direct inspection fixes only the bibliographic title-page core.

`PDHD-D000073`, the 1934 SEP memory, now contributes a complete four-slot batch from the primary Google Books copy `mHgQAAAAYAAJ`. Direct inspection maps printed pp. 29, 53 and 58 to physical PDF pages 39, 63 and 68, while `PP7` maps to physical page 9 and supplies the bibliographic control. A competing Google Books full-view object was rejected after its primary title pages identified 1935, preserving primary-page identity over catalog metadata.

`PDHD-D000069`, *Las misiones culturales en 1927: Las escuelas normales rurales*, now contributes a complete four-slot batch from Internet Archive item `lasmisionescultu00mexi`. HathiTrust record 103012999 points to the same `ark:/13960/t3dz33208`, allowing the blocked Hathi image route to be cross-walked to the exact open primary scan. Direct visual inspection maps printed pp. 23, 54 and 212 to physical PDF pages 43, 74 and 232; the p. 371 budget-title control maps to physical page 391 and is sequence-checked against printed pp. 370 and 373. The batch deliberately replaces section-title pointers with substantive spans where the slot requires analytical content.

All third-party image-derived frozen records remain conservative in public handling. Source images and full historical transcriptions are not committed merely because the object is viewable or downloadable.

## Chronology and source criticism

The image-verification sequence for *El Maestro*, tomo II, núm. 3 resolved `PDHD-X000005` to **1921-12**. `n236` identifies tomo II, núm. III, diciembre de 1921 and `n237` independently confirms México, diciembre de 1921. The secondary 1922 listing remains preserved as a documented discrepancy rather than being erased.

The P4 route demonstrated that a failed delivery channel is not evidence of source absence. HathiTrust exposed no auditable title-page image in the retrieval environment, while Google Books subsequently yielded the inspectable primary PDF through a dynamically resolved download route.

The `PDHD-F000033` recovery established the post-sprint exact-pointer workflow: a secondary scholarly page citation guides retrieval but cannot freeze a span. The *La Enseñanza Primaria* batch extends that principle. UNAM/HNDM independently fixes the selected issue identity; Google Books provides a separate primary scan of the same 1901 volume. Direct inspection of printed pp. 161, 163 and 168 converts two pre-existing exact page pointers and simultaneously resolves two previously unlocalized masthead slots. This is a primary-object cross-check, not a substitution of secondary text for source inspection.

`PDHD-F000037` demonstrates the complementary path from a pure gap to a fixed primary span. The exact BVMC issue was already object-resolved, but no page beyond the opening had been inspected. Rendering the complete primary PDF exposed a pedagogically explicit lesson-plan block on p. 6, allowing localization and freezing to occur in the same source-critical step.

## Remaining localization work

The union of all `fragment_locator_progress*.csv` shards contains **83/96** pilot slots. Forty-nine are frozen. The remaining **34** located rows include exact scholarly page pointers, section starts, reproduced facsimiles and snippet-resolved candidates that have not yet crossed the exact-boundary primary-inspection gate. **13 slots remain without a locator.**

The dedicated direct-primary freeze-conversion queue remains empty after its P1–P4 cohort was exhausted. The active phase now converts strong page-resolved candidates through direct historical-object inspection and opportunistically fills missing deterministic slots when the same inspected page provides structurally distinct evidence.

With `PDHD-D000003`, `PDHD-D000011` and `PDHD-D000031` complete, the next high-value work should target clusters where one primary-object recovery can resolve multiple slots. Strong candidates include page-resolved *El Maestro*, *México Intelectual* and *La Escuela Moderna* fragments, plus the 37-page *Revista de Instrucción Pública Mexicana* issue whose HNDM object is already resolved.

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

`scripts/validate_repository.py` validates the base catalog. `scripts/validate_fragment_shards.py` validates the logical union of locator/frozen shards, fixed-boundary requirements, deterministic document/slot identity and the exact complement represented by the gap queue. `validate_freeze_conversion_queue.py` requires the direct-primary queue to equal the complete eligible set; an empty queue is valid only when that canonical eligible set is also empty.

`validate_retrieval_attempts.py` preserves both blocked attempts and completed recovery routes. `PDHD-RA000001` now records the successful full-PDF BVMC recovery that resolves `PDHD-F000037`. `PDHD-RA000010` records the BVMC p. 12 recovery for `PDHD-F000033`. `PDHD-RA000011` records the complete *La Enseñanza Primaria* primary recovery and physical-to-printed page mapping for `PDHD-F000025`–`PDHD-F000028`. `PDHD-RA000012` records the p. 4 BVMC primary inspection that completes `PDHD-D000011`. `validate_status_counts.py` keeps README and this cohort-status document synchronized with CSV source-of-truth counts.

## What remains before human coding

Human annotation has **not** started. The target remains 96 frozen reliability fragments, four per selected document, followed by a separate 12-fragment calibration set. Every reliability fragment must retain an immutable ID, source identity, page/localizer, fixed boundary, access/rights basis and selection role.

The current 49 frozen units demonstrate that the pipeline works across HNDM, BVMC, Internet Archive and Google Books primary interfaces and can reconcile independent issue identity with an alternate primary scan. They do not justify coder labeling before the package is complete.

## Rights constraint

Primary-source access does not equal republication permission. HNDM remains `metadata_only`; HathiTrust, Internet Archive, BVMC and Google Books/Google Play access are treated as research-access or retrieval layers rather than blanket licenses to mirror scans or full OCR. Where reuse is not clearly authorized, coder text remains outside the public repository.

## Decision

PDHD-U1 remains in **active pilot freezing**. Issue #1 stays open through completion of the 96-fragment package and the first independent human reliability round.

The project is now at **83/96 localized** and **49/96 frozen**. Recent primary-object recovery has expanded the frozen package while preserving the unlocalized complement at 13. The next quantitative localization checkpoint remains **84/96**, while the stronger scientific priority is converting high-quality existing page pointers and completing document batches without weakening the evidence hierarchy.