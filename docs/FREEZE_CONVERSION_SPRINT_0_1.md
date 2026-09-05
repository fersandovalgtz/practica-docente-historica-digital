# PDHD-U1 freeze-conversion sprint 0.1

Reference cut: **2026-09-05**

## Objective

PDHD-U1 remains at **80/96 localized slots** and has advanced from 15 to **22/96 frozen** through four completed direct-primary conversion waves.

The sprint converts already localized direct-primary candidates into fixed coder spans. No row is promoted merely to improve the metric.

`locator_found != fragment_frozen`

`direct_primary_access != fixed_boundary`

## Completed P1 — La Enseñanza Normal

`PDHD-F000034` and `PDHD-F000036` crossed the freeze gate after direct inspection of the exact BVMC primary PDF for the inaugural 15 September 1904 issue. The first fixes the professional/editorial block. The second fixes the autonomous publication-cadence line as an administrative control.

## Completed P2 — El Maestro, tomo II, núm. 3

`PDHD-F000050` and `PDHD-F000052` crossed the gate after the Internet Archive route was corrected to BookReader `n232–n238`. Direct inspection fixed the institutional imprint in `n237` and the bibliographic cover cartouche in `n236`. The same evidence resolved `PDHD-X000005` to canonical **1921-12**, preserving the secondary 1922 discrepancy.

## Completed P3 — El Maestro issue-opening controls

`PDHD-F000044` and `PDHD-F000048` crossed the gate after one-day primary-image retrieval around the registered reader anchors. The issue-II control is fixed on the `n104` bibliographic cartouche. The issue-IV control is fixed on the `n4` cartouche. Cover illustrations are excluded.

This conversion demonstrates:

`reader_page_target != analytical_span`

The reader route identified a neighborhood; only direct primary-image inspection fixed the final span.

## Completed P4 — El esfuerzo educativo en México

`PDHD-F000060` now crosses the direct-primary gate.

The registered Google Books selected-page route identifies `PR5` as the title page of *El esfuerzo educativo en México*, tomo I. Initial browser/cache retrieval was insufficient for image verification. A separate HathiTrust recovery attempt also yielded zero auditable images despite two full-view volume-I copies; this remains a documented delivery failure rather than evidence of source absence.

A dedicated Google Books workflow then fetched the live `PR5` HTML, resolved the current public PDF download link, downloaded a valid 29.9 MB PDF and rendered the first twelve PDF pages. Google Books' own page model maps `PR5` to book order 6. In the rendered PDF sequence, after the Google digitization front matter, the same leaf is image 009.

Visual inspection confirms the title, the 1924–1928 governmental framing, J. M. Puig Casauranc, `Tomo I` and the Secretaría de Educación Pública publication line. `PDHD-F000060` is fixed on the bibliographic title-page core from the main title through the volume/publisher lines, excluding handwritten/library annotations and the Google digitization watermark.

The record uses `not_transcribed`, `metadata_only` and `Google_Books_direct_primary_pdf_image_inspection`. No source image or historical transcription is committed.

## Direct-primary queue closed

`data/samples/freeze_conversion_queue_0_1.csv` now contains only its header. `scripts/validate_freeze_conversion_queue.py` requires that this empty queue equal the complete eligible set of non-frozen direct-primary conversion states. If a qualifying locator remains or is introduced later, CI must reject an incorrectly empty queue.

P1 through P4 retrieval provenance remains in `retrieval_attempts.csv`. Completed routes use `superseded_by_locator`; unsuccessful delivery attempts remain described inside their provenance notes rather than being erased.

The empty direct-primary queue does **not** mean the 96-fragment package is complete. It means the near-ready conversion cohort that motivated this sprint has been exhausted under the current evidence-state definitions.

## Evidence policy retained

None of the four conversion waves weakens PDHD's source-critical distinctions. P1 uses a directly inspected first-party PDF. P2 and P3 use directly inspected Internet Archive page images. P4 uses a directly retrieved and rendered primary Google Books PDF. No secondary facsimile, generic reader target, table-of-contents entry or OCR-only region is promoted as a frozen span.

The mandatory distinctions remain:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`reader_page_target != analytical_span`

`primary_ocr_region != image_verified_span`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Sprint result and next phase

The sprint moves the project **15/96 -> 17/96 -> 19/96 -> 21/96 -> 22/96 frozen** while localization remains **80/96**. Localized-but-not-frozen slots fall from 65 to **58**.

The next scientific phase pivots from the direct-primary queue to strong existing page-resolved candidates. Priority should go to cases where an exact secondary or section pointer can be converted through direct inspection of the historical object. `PDHD-F000033` in *La Enseñanza Normal* is a particularly attractive next target because the exact issue and p. 12 pointer are already resolved and the remaining problem is primary PDF page recovery rather than source discovery.

Human annotation remains downstream of the complete 96-fragment freeze package.