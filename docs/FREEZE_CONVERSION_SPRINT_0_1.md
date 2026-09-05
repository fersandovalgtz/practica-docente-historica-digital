# PDHD-U1 freeze-conversion sprint 0.1

Reference cut: **2026-09-05**

## Objective

PDHD-U1 is now at **82/96 localized slots** and **28/96 frozen**. The dedicated direct-primary sprint itself closed at 22/96; the post-sprint exact-page phase has since added `PDHD-F000033`, the complete four-slot `PDHD-D000003` batch and `PDHD-F000035`, which completes `PDHD-D000011`, without weakening the evidence hierarchy.

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

`PDHD-F000060` crossed the direct-primary gate after a dedicated Google Books workflow fetched the live `PR5` HTML, resolved the public PDF download link, downloaded a valid 29.9 MB primary PDF and rendered the relevant front matter. Google Books maps `PR5` to book order 6 and the rendered sequence places that title page at image 009.

Visual inspection fixed the bibliographic title-page core as a non-analytical control. A preceding HathiTrust image-delivery attempt yielded zero auditable images and remains documented as a delivery failure rather than source absence.

## Direct-primary queue closed

`data/samples/freeze_conversion_queue_0_1.csv` contains only its header. `scripts/validate_freeze_conversion_queue.py` requires exact equality between the queue and the canonical eligible set. An empty queue is therefore valid only when no eligible direct-primary candidate is omitted.

The empty queue does **not** mean the 96-fragment package is complete. It means the near-ready direct-primary cohort that motivated this sprint has been exhausted under the current state definitions.

## First post-sprint conversion — F000033

The post-sprint phase began with `PDHD-F000033`, *La Enseñanza Normal*, 15 September 1904, printed p. 12. A UNAM thesis supplied an exact page pointer to Leopoldo Kiel's *Conferencias Pedagógicas*, but that secondary citation remained below the primary-inspection gate.

A dedicated BVMC recovery workflow downloaded the exact inaugural-issue PDF and rendered all twenty pages. Printed p. 12 was identified directly rather than inferred from the PDF index. Visual inspection fixed the single right-column paragraph prescribing work with children, observation, experimentation and verification of teaching procedures.

This conversion demonstrates:

`secondary_page_citation -> retrieval_target`, but `secondary_page_citation != primary_page_inspection`

## Second post-sprint conversion — complete La Enseñanza Primaria batch

`PDHD-D000003`, *La Enseñanza Primaria*, tomo I, núm. 11, 1 December 1901, now has all four deterministic slots frozen.

UNAM/HNDM independently resolves the selected issue identity. Because the HNDM viewer returned an access error in the active retrieval route, a separate primary Google Books copy of the 1901 volume was used for page inspection. A dedicated workflow dynamically resolved its current PDF link, downloaded a valid 402-page 28.99 MB scan, extracted a page map only as a retrieval aid and rendered the target neighborhood. Printed p. 161 maps to physical PDF page 175, p. 163 to page 177 and p. 168 to page 182.

`PDHD-F000025` fixes an explicit pedagogical-method block on printed p. 168 inside Ponciano Rodríguez's *El método en los libros de texto*. The selected left-column span prescribes the order in which content should be presented and a sequence from easier to harder, known to unknown, concrete to abstract, sensible to intellectual and empirical to rational.

`PDHD-F000026` fixes the discrete masthead role identifying Gregorio Torres Quintero as Jefe de Redacción on printed p. 161. `PDHD-F000028` fixes the adjacent but structurally separate tomo/date/number cartouche as a non-analytical control. These two primary observations also remove two entries from the unlocalized gap queue.

`PDHD-F000027` fixes the complete closing block of *Los ejercicios físicos en la escuela* on printed p. 163. The span begins with the summary of the opposing position and continues through Torres Quintero's rebuttal, conclusion and signature, ending before the next article. It is retained as the source-critical slot because it concentrates the historical dispute over fatigue, rest, games, physical exercise and intellectual work.

All four records use `not_transcribed`, `metadata_only` and `Google_Books_direct_primary_pdf_image_inspection`. No historical scan or source transcription is committed.

This batch adds a further methodological distinction:

`independent_issue_identity + alternate_primary_scan -> primary_crosscheck`

The alternate primary copy is used to inspect the historical page; secondary scholarship remains only a retrieval guide.

## Third post-sprint conversion — complete La Enseñanza Normal batch

The already recovered twenty-page BVMC primary PDF also resolves `PDHD-F000035` on printed p. 4. Direct inspection confirms the opening of *15 de Septiembre — Fecha grata* and its source-critical framing of school, national education, liberty and progress. The frozen span begins at the article heading, crosses the column break through the opening paragraph on Libertad y Progreso and stops before the following paragraph changes to military commemoration.

This conversion completes `PDHD-D000011` at 4/4. It uses `not_transcribed`, `metadata_only` and `BVMC_direct_primary_pdf_inspection`, with no page image or historical transcription committed. The same recovered primary object can therefore support multiple deterministic slots only when each slot has a distinct, explicitly bounded region.

## Evidence policy retained

No conversion wave promotes a secondary facsimile, generic reader target, table-of-contents entry or OCR-only region as a frozen span. The mandatory distinctions remain:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`reader_page_target != analytical_span`

`primary_ocr_region != image_verified_span`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Result and next phase

The project moves **15/96 -> 17/96 -> 19/96 -> 21/96 -> 22/96 -> 23/96 -> 27/96 -> 28/96 frozen**. Localization moves from **80/96 to 82/96** because primary inspection of the *La Enseñanza Primaria* masthead resolves two previously missing deterministic slots. Localized-but-not-frozen slots are now **54**, and **14** slots remain without a locator.

The next scientific priority is the comparable single-slot completion opportunity `PDHD-F000037` in the exact *La Enseñanza Moderna* BVMC issue. After that, page-resolved *El Maestro*, *México Intelectual* and *La Escuela Moderna* targets should be prioritized by primary-object tractability and expected batch completion value.

Human annotation remains downstream of the complete 96-fragment freeze package.