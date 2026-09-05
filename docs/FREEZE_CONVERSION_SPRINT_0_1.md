# PDHD-U1 freeze-conversion sprint 0.1

Reference cut: **2026-09-05**

## Objective

PDHD-U1 remains at **80/96 localized slots** and has advanced from 15 to **21/96 frozen** through three completed direct-primary conversion waves.

The sprint prioritizes conversion of already localized direct-primary candidates into fixed coder spans. No row is promoted merely to improve the metric.

`locator_found != fragment_frozen`

`direct_primary_access != fixed_boundary`

## Completed P1 — La Enseñanza Normal

`PDHD-F000034` and `PDHD-F000036` crossed the freeze gate after direct inspection of the exact BVMC primary PDF for the inaugural 15 September 1904 issue.

`PDHD-F000034` fixes the first-page professional/editorial block. `PDHD-F000036` fixes the autonomous publication-cadence line as the smallest defensible administrative control span. Both use `not_transcribed`, `metadata_only` and `BVMC_direct_primary_pdf_inspection`.

## Completed P2 — El Maestro, tomo II, núm. 3

`PDHD-F000050` and `PDHD-F000052` crossed the freeze gate after the Internet Archive retrieval path was corrected from an erroneous Search Inside mapping to BookReader `n232–n238`.

Direct inspection showed `n236` as the tomo II, núm. III cover dated diciembre de 1921; `n237` as the issue-specific Secretaría de Educación Pública / Talleres Gráficos imprint ending México, diciembre de 1921; and `n238` as the opening of *La inconsciencia de la hora* on printed p. 227.

`PDHD-F000050` is fixed on the institutional imprint in `n237`. `PDHD-F000052` is fixed on the bibliographic title/volume/number/date cartouche in `n236`. Both use `not_transcribed`, `metadata_only` and `Internet_Archive_direct_primary_image_inspection`.

The same image evidence resolves `PDHD-X000005` to canonical **1921-12**, while retaining the secondary 1922 listing as a documented discrepancy.

## Completed P3 — El Maestro issue-opening controls

`PDHD-F000044` and `PDHD-F000048` have now crossed the freeze gate as deliberately non-analytical control spans.

A one-day GitHub Actions retrieval workflow downloaded short primary-image windows around the registered reader targets. The workflow did not alter scientific state; it only exposed auditable source images for manual inspection.

For `PDHD-F000044`, the registered reader target `n103` led to a window in which `n104` is the unequivocal cover for núm. II of 1921. The frozen boundary is the bibliographic cartouche containing the issue number, Mexico and the Roman-numeral year. The illustration and other cover matter are excluded.

For `PDHD-F000048`, the registered reader target `n6` led to a window in which `n4` is the unequivocal cover for núm. IV of 1921. Again, only the bibliographic cartouche is fixed; the illustration and surrounding cover matter are excluded.

Both use `not_transcribed`, `metadata_only` and `Internet_Archive_direct_primary_image_inspection`. Their registry rows are stored in `frozen_fragments_el_maestro_controls_w18.csv`.

This conversion explicitly demonstrates:

`reader_page_target != analytical_span`

The reader route found the relevant neighborhood; the final frozen span was selected only after visual inspection of the primary image.

## Current direct-primary queue

The machine-readable queue now contains exactly **one fragment**.

### P4 — El esfuerzo educativo en México

`PDHD-F000060` points to Google Books page `PR5`. The title-page control remains a candidate until the page itself can be directly inspected and its access/transcription decisions are fixed.

The current blocker is not bibliographic identity. `PDHD-D000066` and `PR5` are already resolved. The blocker is auditable primary-page rendering: the current route has not yet yielded a directly inspectable page image.

## Queue completeness and provenance

`scripts/validate_freeze_conversion_queue.py` requires the queue to equal the complete set of non-frozen locator rows whose canonical `boundary_status` belongs to the direct-primary conversion states. Once a row becomes `fixed`/`frozen`, it must disappear from the queue.

At this cut the complete direct-primary set is exactly `PDHD-F000060`.

Completed retrieval attempts for P1, P2 and P3 remain in `retrieval_attempts.csv` with `superseded_by_locator`, preserving the technical path without presenting a resolved blocker as current. The P4 attempt remains open until a primary page can be inspected.

## Evidence policy retained

None of the three conversion waves weakens PDHD's source-critical distinctions. P1 uses a directly inspected first-party PDF. P2 and P3 use directly inspected primary BookReader page images. No secondary facsimile, generic reader route or OCR-only region is promoted as a frozen span.

The following distinctions remain mandatory:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`reader_page_target != analytical_span`

`primary_ocr_region != image_verified_span`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Success criterion

The sprint has moved the project **15/96 -> 17/96 -> 19/96 -> 21/96 frozen** while localization remains **80/96**. The number of localized-but-not-frozen slots therefore falls from 65 to 63, then 61, and now to **59**.

The immediate scientific objective is to resolve `PDHD-F000060` without weakening the primary-image gate. After that, the sprint should pivot from the direct-primary queue to the strongest remaining page-resolved candidates, prioritizing those where primary inspection can convert existing exact page pointers rather than adding weaker discovery evidence.

Human annotation remains downstream of the complete 96-fragment freeze package.