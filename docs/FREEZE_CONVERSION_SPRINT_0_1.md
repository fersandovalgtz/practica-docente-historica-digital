# PDHD-U1 freeze-conversion sprint 0.1

Reference cut: **2026-09-05**

## Objective

PDHD-U1 remains at **80/96 localized slots** and has advanced from 15 to **19/96 frozen** through two completed direct-primary conversion waves.

The sprint prioritizes conversion of already localized direct-primary candidates into fixed coder spans. No row is promoted merely to improve the metric.

`locator_found != fragment_frozen`

`direct_primary_access != fixed_boundary`

## Completed P1 — La Enseñanza Normal

`PDHD-F000034` and `PDHD-F000036` crossed the freeze gate after direct inspection of the exact BVMC primary PDF for the inaugural 15 September 1904 issue.

`PDHD-F000034` fixes the first-page professional/editorial block from `CUERPO DE REDACCION` through the collaborator line and stops before the programmatic article opening. `PDHD-F000036` fixes the autonomous publication-cadence line as the smallest defensible administrative control span.

Both use `not_transcribed`, `metadata_only` and `BVMC_direct_primary_pdf_inspection`. Their registry rows are stored in `frozen_fragments_ensenanza_normal_w16.csv`.

## Completed P2 — El Maestro, tomo II, núm. 3

`PDHD-F000050` and `PDHD-F000052` have also crossed the freeze gate.

The first Internet Archive retrieval workflow used an incorrect Search Inside to BookReader mapping and downloaded later pages. Scandata/page-number reconciliation moved the target to **BookReader `n232–n238`**. The corrected workflow completed successfully and produced seven primary JPEGs for manual source review.

Direct inspection resolves the issue sequence:

- `n236` explicitly identifies *EL MAESTRO*, *REVISTA DE CULTURA NACIONAL*, **TOMO II - NUMERO III**, **DICIEMBRE DE MCMXXI**, México;
- `n237` contains the issue-specific institutional imprint **SECRETARIA DE EDUCACION PUBLICA**, Talleres Gráficos de la Nación, Filomeno Mata número 8, ending **MEXICO, DICIEMBRE DE 1921**;
- `n238` opens *La inconsciencia de la hora* on printed p. 227.

`PDHD-F000050` is therefore fixed on `n237` as the institutional-relation span. This choice is deliberately more conservative than using an adjacent masthead page because the n237 imprint is unambiguously internal to tomo II, núm. III.

`PDHD-F000052` is fixed on the issue-identification cartouche of `n236` as the non-analytical control. It remains separate from the institutional block and requires no historical transcription in the public repository.

Both use `not_transcribed`, `metadata_only` and `Internet_Archive_direct_primary_image_inspection`. Their registry rows are stored in `frozen_fragments_el_maestro_t2n3_w17.csv`.

## Chronology result

The primary images resolve `PDHD-X000005` to **1921-12** at month precision. The secondary 1922 listing is retained as a documented scholarly/catalog discrepancy, but it is no longer the canonical chronology.

This resolution follows the evidence hierarchy rather than OCR convenience:

`primary_ocr_region != image_verified_span`

The OCR guided retrieval; the cover and imprint images supported the chronology decision.

## Current direct-primary queue

The machine-readable queue now contains exactly **three fragments**.

### P3 — El Maestro issue-opening controls

`PDHD-F000044` and `PDHD-F000048` retain stable Internet Archive reader targets for selected 1921 issues. Both are control slots and still require direct primary inspection plus selection of the smallest defensible front-matter or administrative region.

### P4 — El esfuerzo educativo en México

`PDHD-F000060` points to Google Books page `PR5`. The title-page control remains a candidate until the page itself can be directly inspected and its access/transcription decisions are fixed.

## Queue completeness and provenance

`scripts/validate_freeze_conversion_queue.py` requires the queue to equal the complete set of non-frozen locator rows whose canonical `boundary_status` belongs to the direct-primary conversion states. Once a row becomes `fixed`/`frozen`, it must disappear from the queue.

The expected set at this cut is exactly `PDHD-F000044`, `PDHD-F000048` and `PDHD-F000060`. Each retains structured retrieval provenance.

Completed retrieval attempts for P1 and P2 remain in `retrieval_attempts.csv` with `superseded_by_locator`, preserving the technical path without presenting a resolved blocker as current.

## Evidence policy retained

Neither conversion wave weakens PDHD's source-critical distinctions. P1 uses a directly inspected first-party PDF. P2 uses directly inspected primary BookReader page images. No secondary facsimile or OCR-only region is promoted as a frozen span.

The following distinctions remain mandatory:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`primary_ocr_region != image_verified_span`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Success criterion

The sprint has moved the project **15/96 -> 17/96 -> 19/96 frozen** while localization remains **80/96**. The number of localized-but-not-frozen slots therefore falls from 65 to 63 and now to **61**.

The next scientific objective is to convert the remaining three direct-primary candidates without weakening the fixed-boundary, rights or source-inspection gates. Human annotation remains downstream of the complete 96-fragment freeze package.