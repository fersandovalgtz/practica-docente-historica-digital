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
| Fully frozen fragments | **22 / 96** | direct-primary conversion sprint completed |
| Human-validated pedagogical fragments | 0 | not started |

The 75-object cohort remains a stabilization corpus, not a national representative sample. PDHD-U1 now has **80 of the 96 deterministic reliability slots** tied to a documented page, scan or section target. Twenty-two units have crossed the stronger frozen-fragment gate.

## Sampling status

The first reliability corpus remains frozen in `data/samples/pilot_document_selection_0_1.csv`: 10 E1 documents, 12 E3 documents and 2 E4 documents. It includes regional origins outside Mexico City, multiple documentary regimes and no publication contributing more than six documents. This is a methodological reliability sample rather than an estimator of national historical frequencies.

## Frozen-fragment evidence

Three selected documents have complete four-slot batches. `PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888, contributes `PDHD-F000013`–`PDHD-F000016`. `PDHD-D000001`, *La Enseñanza Objetiva* of 12 December 1891, contributes `PDHD-F000017`–`PDHD-F000020`. `PDHD-D000055`, the first 1921 number of *El Maestro. Revista de Cultura Nacional*, contributes `PDHD-F000053`–`PDHD-F000056`.

`PDHD-D000031`, *La Enseñanza Moderna*, tomo I, segunda época, núm. 1, contributes three frozen units from direct BVMC image inspection: `PDHD-F000038`–`PDHD-F000040`. `PDHD-D000011`, the inaugural *La Enseñanza Normal* issue of 15 September 1904, contributes `PDHD-F000034` and `PDHD-F000036` from the exact BVMC primary PDF.

Internet Archive contributes four additional image-verified controls plus the institutional region of *El Maestro*. `PDHD-F000050` and `PDHD-F000052` are fixed from BookReader leaves `n237` and `n236` in tomo II, núm. 3. `PDHD-F000044` uses the issue-II cover cartouche at `n104`; `PDHD-F000048` uses the issue-IV cover cartouche at `n4`. These conversions preserve `reader_page_target != analytical_span`: the reader route supported retrieval, while the final boundary came only from visual inspection of the primary image.

`PDHD-D000066`, *El esfuerzo educativo en México* (1928), now contributes `PDHD-F000060` as a frozen title-page control. Google Books directly exposes `PR5`. A dedicated recovery workflow fetched the live PR5 HTML, resolved its public PDF link, downloaded a valid 29.9 MB primary PDF and rendered the first twelve pages. The Google page model maps `PR5` to book order 6; in the rendered PDF sequence this corresponds to image 009. Direct inspection confirms the title, the 1924–1928 governmental framing, J. M. Puig Casauranc, `Tomo I` and the Secretaría de Educación Pública publication line. The frozen span is the bibliographic title-page core only; handwritten/library annotations and the Google digitization watermark are excluded.

All third-party image-derived frozen records remain conservative in public handling. Source images and full historical transcriptions are not committed merely because the object is viewable or downloadable.

## Chronology and source criticism

The image-verification sequence for *El Maestro*, tomo II, núm. 3 resolved `PDHD-X000005` to **1921-12**. `n236` identifies tomo II, núm. III, diciembre de 1921 and `n237` independently confirms México, diciembre de 1921. The secondary 1922 listing remains preserved as a documented discrepancy rather than being erased.

The P4 route provides a second useful source-critical lesson. HathiTrust identifies two full-view volume-I copies of *El esfuerzo educativo en México*, but automated page-image delivery produced zero auditable images in the retrieval environment. That failed delivery is retained as a technical result, not interpreted as source absence. Google Books subsequently yielded the inspectable primary PDF through a dynamically resolved download route.

## Remaining localization work

The union of all `fragment_locator_progress*.csv` shards contains **80/96** pilot slots. Twenty-two are frozen. The remaining **58** located rows include exact scholarly page pointers, section starts, reproduced facsimiles and snippet-resolved candidates that have not yet crossed the exact-boundary primary-inspection gate. **16 slots remain without a locator.**

The dedicated direct-primary freeze-conversion queue is now empty. This does not mean that all located candidates are frozen. It means that every row already classified as a near-ready direct-primary conversion candidate has either crossed the gate or been reclassified through its canonical locator state.

The next freeze work therefore pivots to the strongest page-resolved candidates where direct historical-page recovery can convert an existing exact pointer into an image-verified coder span. High-value targets include `PDHD-F000033` in *La Enseñanza Normal*, the exact-page *La Enseñanza Primaria* candidates, and other primary objects whose page delivery can be recovered without substituting secondary evidence for inspection.

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

`scripts/validate_repository.py` validates the base catalog. `scripts/validate_fragment_shards.py` validates the logical union of locator/frozen shards, fixed-boundary requirements, deterministic document/slot identity and the exact complement represented by the gap queue. `validate_freeze_conversion_queue.py` requires the direct-primary queue to equal the complete eligible set. With `PDHD-F000060` frozen, that expected set is empty.

`validate_retrieval_attempts.py` preserves both blocked attempts and completed recovery routes. P1 through P4 now retain `superseded_by_locator` provenance where a recovery attempt culminated in a frozen canonical locator. `validate_status_counts.py` keeps README and this cohort-status document synchronized with CSV source-of-truth counts.

## What remains before human coding

Human annotation has **not** started. The target remains 96 frozen reliability fragments, four per selected document, followed by a separate 12-fragment calibration set. Every reliability fragment must retain an immutable ID, source identity, page/localizer, fixed boundary, access/rights basis and selection role.

The current 22 frozen units demonstrate that the pipeline works across HNDM, BVMC, Internet Archive and Google Books primary interfaces. They do not justify coder labeling before the package is complete.

## Rights constraint

Primary-source access does not equal republication permission. HNDM remains `metadata_only`; HathiTrust, Internet Archive and Google Books/Google Play access are treated as research-access or retrieval layers rather than blanket licenses to mirror scans or full OCR. Where reuse is not clearly authorized, coder text remains outside the public repository.

## Decision

PDHD-U1 remains in **active pilot freezing**. Issue #1 stays open through completion of the 96-fragment package and the first independent human reliability round.

The project is now at **80/96 localized**. The direct-primary conversion sprint has advanced the frozen count from 15 to **22/96** without increasing localization through weaker evidence. The next quantitative localization checkpoint remains **84/96**, while the stronger scientific priority is converting high-quality existing page pointers through direct primary inspection.