# PDHD-U1 freeze-conversion sprint 0.1

Reference cut: **2026-09-05**

## Objective

PDHD-U1 remains at **80/96 localized slots**. The frozen count has advanced from 15 to **17/96** after direct inspection of the exact BVMC primary PDF for the inaugural 15 September 1904 issue of *La Enseñanza Normal*.

The sprint continues to prioritize conversion of already localized direct-primary candidates into fixed coder spans. No row is promoted merely to improve the metric.

`locator_found != fragment_frozen`

`direct_primary_access != fixed_boundary`

## Completed P1 conversion

`PDHD-F000034` and `PDHD-F000036` have crossed the freeze gate.

For `PDHD-F000034`, the primary BVMC PDF exposes enough first-page structure to fix the professional/editorial block beginning at `CUERPO DE REDACCION`, including the redaction and administration secretary roles and the collaborator line, and ending before the programmatic article opening.

For `PDHD-F000036`, the smallest defensible administrative control span is the autonomous publication-cadence line positioned between the direction heading and the editorial roster.

Both records use `not_transcribed`, `metadata_only` and `BVMC_direct_primary_pdf_inspection`. No historical page image or source text is committed because the BVMC source policy remains `review_required`.

The canonical locator rows are now `fixed`/`frozen`, the corresponding registry rows are stored in `data/samples/frozen_fragments_ensenanza_normal_w16.csv`, and both IDs have been removed from `freeze_conversion_queue_0_1.csv`.

## Current direct-primary queue

The machine-readable queue now contains **five fragments**.

### P2 — El Maestro, tomo II, núm. 3

`PDHD-F000050` and `PDHD-F000052` share the December-issue opening of Internet Archive object `n1n3elmaestrorev02mexi`.

Primary OCR exposes the magazine title, directors Enrique Monteverde and Agustín Loera y Chávez, office/contact material and the December 1921 imprint. That evidence remains below the page-image gate for freezing.

The first retrieval workflow used an incorrect Search Inside to BookReader mapping and downloaded `n272–n277`, which correspond to later printed pages. Scandata/page-number reconciliation now places the relevant December 1921 opening in **BookReader leaves `n232–n238`**. The workflow has been corrected accordingly.

The next gate is direct inspection of those recovered images. Only after the masthead/director block and a separate administrative/control region are verified may `PDHD-F000050` and `PDHD-F000052` move to `fixed`/`frozen`. Chronology conflict `PDHD-X000005` remains open until the primary image/imprint is inspected.

### P3 — El Maestro issue-opening controls

`PDHD-F000044` and `PDHD-F000048` retain stable Internet Archive reader targets for selected 1921 issues. Both are control slots and still require direct primary inspection plus selection of the smallest defensible front-matter or administrative region.

### P4 — El esfuerzo educativo en México

`PDHD-F000060` points to Google Books page `PR5`. The title-page control remains a candidate until the page itself can be directly inspected and its access/transcription decisions are fixed.

## Queue completeness and CI

`scripts/validate_freeze_conversion_queue.py` requires the queue to equal the complete set of non-frozen locator rows whose canonical `boundary_status` is one of the direct-primary conversion states. Once a row becomes `fixed`/`frozen`, it must disappear from the queue.

At this cut the expected set is exactly **five fragments**: two P2, two P3 and one P4. Each retains structured retrieval provenance.

`scripts/prepare_freeze_review.py` remains the deterministic bridge into manual primary-page review. It does not pre-assert source verification and does not itself change scientific state.

## Evidence policy retained

The conversion of the BVMC pair does not weaken PDHD's distinctions. The primary first-party PDF was inspected directly and provided a stable page plus enough structural context to identify the exact spans, which satisfies L1 under `LOCATOR_EVIDENCE_POLICY.md`. No secondary facsimile or OCR-only evidence was promoted in its place.

The following distinctions remain mandatory:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`primary_ocr_region != image_verified_span`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Success criterion

The sprint has achieved its first measurable conversion: **15/96 -> 17/96 frozen** while localization remains **80/96**. Therefore the number of localized-but-not-frozen slots falls from 65 to **63**.

The next scientific objective is to convert the corrected P2 Internet Archive pair without forcing the chronology conflict or treating OCR as image verification. Human annotation remains downstream of the complete 96-fragment freeze package.