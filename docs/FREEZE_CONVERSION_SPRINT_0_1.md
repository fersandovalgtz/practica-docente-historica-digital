# PDHD-U1 freeze-conversion sprint 0.1

Reference cut: **2026-09-05**

## Objective

PDHD-U1 remains at **80/96 localized slots** and has advanced from 15 to **23/96 frozen**. The dedicated direct-primary sprint itself closed at 22/96; the first post-sprint exact-page conversion adds `PDHD-F000033` without weakening the evidence hierarchy.

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

## Completed P4 — El esfuerzo educativo en México

`PDHD-F000060` crossed the direct-primary gate after a dedicated Google Books workflow fetched the live `PR5` HTML, resolved the public PDF download link, downloaded a valid 29.9 MB primary PDF and rendered the first twelve pages. Google Books maps `PR5` to book order 6 and the rendered PDF sequence places that title page at image 009.

Visual inspection fixed the bibliographic title-page core as a non-analytical control. A preceding HathiTrust image-delivery attempt yielded zero auditable images and remains documented as a delivery failure rather than source absence.

## Direct-primary queue closed

`data/samples/freeze_conversion_queue_0_1.csv` contains only its header. `scripts/validate_freeze_conversion_queue.py` requires exact equality between the queue and the canonical eligible set. An empty queue is therefore valid only when no eligible direct-primary candidate is omitted.

The empty queue does **not** mean the 96-fragment package is complete. It means the near-ready direct-primary cohort that motivated this sprint has been exhausted under the current state definitions.

## First post-sprint conversion — F000033

The next phase began with `PDHD-F000033`, *La Enseñanza Normal*, 15 September 1904, printed p. 12. A UNAM thesis already supplied an exact page pointer to Leopoldo Kiel's *Conferencias Pedagógicas*, but that secondary citation remained below the primary-inspection gate.

A dedicated BVMC recovery workflow downloaded the exact 9.5 MB inaugural-issue PDF and rendered all twenty pages. Printed p. 12 was identified directly rather than inferred from the PDF index. Visual inspection confirmed the paragraph prescribing sustained work with a group of children, observation, experimentation and verification of the results of teaching procedures.

`PDHD-F000033` is now fixed on that single right-column paragraph. The following paragraph is excluded. The record uses `not_transcribed`, `metadata_only` and `BVMC_direct_primary_pdf_inspection`; no source image or historical transcription is committed.

This conversion demonstrates:

`secondary_page_citation -> retrieval_target`, but `secondary_page_citation != primary_page_inspection`

The secondary source identified where to look. Only the primary historical page justified the frozen span.

## Evidence policy retained

No conversion wave promotes a secondary facsimile, generic reader target, table-of-contents entry or OCR-only region as a frozen span. The mandatory distinctions remain:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`reader_page_target != analytical_span`

`primary_ocr_region != image_verified_span`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Result and next phase

The project moves **15/96 -> 17/96 -> 19/96 -> 21/96 -> 22/96 -> 23/96 frozen** while localization remains **80/96**. Localized-but-not-frozen slots fall from 65 to **57**.

The next scientific phase should continue converting exact page pointers where primary retrieval is tractable. The strongest immediate candidates are `PDHD-F000025` and `PDHD-F000027` in the 1 December 1901 issue of *La Enseñanza Primaria*. Both already have exact page ranges from scholarship and now require direct HNDM page-image recovery plus exact span selection.

Human annotation remains downstream of the complete 96-fragment freeze package.