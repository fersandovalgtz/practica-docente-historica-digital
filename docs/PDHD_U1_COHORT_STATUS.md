# PDHD-U1 cohort status

Reference cut: **2026-09-07**

## Current thresholds

| Layer | Count | Status |
|---|---:|---|
| Registered discovery candidates | 25 | threshold reached |
| Object-level documents | 78 | stabilization advanced |
| Issue-level leads | 21 total / 19 unresolved | active balancing queue |
| Sources with explicit rights policy | 13 / 13 | complete at source-policy level |
| Registered chronology conflicts | 5 | preserved; one resolved by primary-image evidence |
| Frozen pilot documents | 24 | document-selection gate passed |
| Target fixed fragments | 96 | freeze gate complete |
| Fragment locator rows resolved/candidate | **96 / 96** | 100% of reliability slots localized
| Fully frozen fragments | **96 / 96** | freeze gate complete |
| Human-validated pedagogical fragments | 0 | calibration package prepared; coding not started |

The 78-object cohort remains a stabilization corpus, not a national representative sample. PDHD-U1 now has **96 of the 96 deterministic reliability slots** tied to a documented page, scan or section target. **96 units** have crossed the stronger frozen-fragment gate.

## Sampling status

The first reliability corpus remains frozen in `data/samples/pilot_document_selection_0_1.csv`: 10 E1 documents, 12 E3 documents and 2 E4 documents. It includes regional origins outside Mexico City, multiple documentary regimes and no publication contributing more than six documents. This is a methodological reliability sample rather than an estimator of national historical frequencies.

## Frozen-fragment evidence

**24 selected documents** now have complete four-slot batches. `PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888, contributes `PDHD-F000013`–`PDHD-F000016`. `PDHD-D000001`, *La Enseñanza Objetiva* of 12 December 1891, contributes `PDHD-F000017`–`PDHD-F000020`. `PDHD-D000055`, the first 1921 number of *El Maestro. Revista de Cultura Nacional*, contributes `PDHD-F000053`–`PDHD-F000056`.

`PDHD-D000064`, *El Instructor* of 1 January 1889, now contributes a complete A–D batch from the exact HNDM issue cross-walked from UNAM-RI `750865`. The recovery exposes a second HNDM interface hazard: supplying anio/mes/dia in the viewer URL silently returned the 1 May 1888 issue, so that first artifact was rejected after masthead inspection. UNAM's structured record supplied persistent `item_first_page_id` `558a3e407d1ed64f17176fc2`; entering through that ID and enforcing an `1889-01-01` identity gate recovered exactly eight unique primary pages. Direct inspection fixes F000005 on p. 5 as a learner-directed grammatical prescription, confirms F000006 on p. 8 as an institutional prize-distribution span, fixes a distinct p. 8 source-critical representation of women's education for F000007, and uses the p. 1 publication-conditions block as F000008 control.

`PDHD-D000058`, *La Escuela Moderna* of 31 October 1889, now contributes a complete A–D batch from 20 exact HNDM primary pages. The broken UNAM-RI `924534` route was bypassed only after adjacent record `924533` resolved the same HNDM serial and explicit chronology. Numeric ObjectId adjacency was tested and rejected. The real HNDM selector submits `anio`/`mes`/`dia`; selecting 1889-10-31 resolved first page `558a33387d1ed64f16922984`, after which explicit `siguienteLink` identifiers recovered all 20 pages under strict identity gates. Direct image inspection fixes F000021 p. 18, F000022 and F000023 as distinct p. 17 units, and F000024 p. 32.

`PDHD-D000006`, *Revista de la Instrucción Pública Mexicana* of 15 March 1896, now contributes a complete A–D batch after traversing the exact HNDM issue through 37 unique persistent page IDs. The primary sequence establishes five preliminary cover/index leaves, printed p. 1 at sequence 6 and printed p. 32 at sequence 37. Direct visual inspection fills the three former A/C/D gaps: F000029 fixes a language-teaching prescription in the Escuela de Sordo-Mudos on p. 12; F000031 fixes a separate non-overlapping p. 12 source-critical clause differentiating vocational formation by gender and aptitude; F000032 uses the p. 1 masthead as a non-analytical control. F000030 is independently confirmed on p. 31 as the personnel notice recording Dolores Correa Zapata's resignation and Emilia Tuchs's appointment.

`PDHD-D000063`, *México intelectual* of 1889, now contributes a complete A–D batch from the HNDM primary viewer cross-walked from UNAM-RI `897145`. The recovery itself exposed an important interface trap: changing `intPagina` returned the same current leaf, so that first artifact was rejected. A corrected traversal followed the viewer's persistent `siguienteLink` page IDs and recovered 45 unique primary pages. Direct visual inspection replaces the weak secondary slot-A pointer with the explicit primary-teacher action paragraph on p. 34, confirms a bounded institutional-uniformity paragraph on p. 2 for slot B, fixes the Normal de Jalapa student/faculty/curriculum block on p. 27 for source criticism, and moves the control from the incorrect p. 6 secondary pointer to the actual `CONDICIONES` section on p. 32. No facsimile or source transcription is committed.

`PDHD-D000003`, *La Enseñanza Primaria*, tomo I, núm. 11, 1 December 1901, contributes a complete four-slot batch from a directly retrieved Google Books primary PDF whose issue identity is independently matched by the UNAM/HNDM record. `PDHD-F000025` fixes the explicit-method prescription on printed p. 168. `PDHD-F000026` fixes the discrete masthead role identifying Gregorio Torres Quintero as Jefe de Redacción on p. 161. `PDHD-F000027` fixes the complete source-critical conclusion of *Los ejercicios físicos en la escuela* on p. 163. `PDHD-F000028` fixes the separate tomo/date/number cartouche on p. 161 as a deliberately non-analytical control. The primary PDF maps those printed pages to physical PDF pages 182, 175, 177 and 175 respectively.

`PDHD-D000031`, *La Enseñanza Moderna*, tomo I, segunda época, núm. 1, now contributes a complete four-slot batch. `PDHD-F000038`–`PDHD-F000040` remain fixed from direct BVMC first-page inspection. A dedicated recovery workflow subsequently downloaded and rendered the exact nine-page BVMC PDF. Direct inspection of printed p. 6 resolves `PDHD-F000037` from the *Clase de colores* lesson plan: the coder span begins at `Principio`, includes the contiguous `Medio`, `Fin`, `Método` and `Procedimiento` lines, and ends before `Ilustraciones`. The subsequent demonstration dialogue is deliberately excluded.

`PDHD-D000011`, the inaugural *La Enseñanza Normal* issue of 15 September 1904, contributes a complete four-slot batch from the exact BVMC primary PDF. `PDHD-F000033` fixes an explicit pedagogical-act paragraph on printed p. 12 in Leopoldo Kiel's *Conferencias Pedagógicas*. `PDHD-F000034` fixes the professional/editorial block on p. 1. `PDHD-F000035` fixes the opening of *15 de Septiembre — Fecha grata* on p. 4 as a source-critical political-educational framing of school, education, liberty and progress, ending before the article shifts toward military commemoration. `PDHD-F000036` fixes the publication-cadence control on p. 1. All four boundaries come from direct inspection of the primary PDF.


`PDHD-D000051`, *El Maestro. Revista de Cultura Nacional*, núm. 2 (mayo de 1921), now contributes a complete A–D batch. The separate Internet Archive issue object exposes a 118-page primary PDF. Visual review maps printed p. 147 to PDF p. 53 for F000041, p. 135 to PDF p. 41 for F000042 and p. 173 to PDF p. 79 for F000043. Four independent PDF-to-BookReader image comparisons prove the zero-based leaf mapping across the issue, yielding `n52`, `n40` and `n78` for the selected spans. F000044 remains the previously frozen bibliographic control. The batch preserves the difference between explicit pedagogical action, institutional/network organization and source-critical representation.

`PDHD-D000052`, *El Maestro. Revista de Cultura Nacional*, núm. 4 (julio de 1921), now contributes a complete A–D batch from Internet Archive container `elmaestrorevista146mexi`. Direct images identify printed p. 341 at `n26`, p. 351 at `n36`, p. 352 at `n37`, and pp. 363–365 at `n48`–`n50`; the already frozen control remains `n4`. F000045 deliberately replaces its verified-but-weak Montelongo target with numbered item 7 of *Mejores maestros* on p. 352, where a controlled `guide` act is explicit. F000046 fixes item 3 on p. 351 as an institutional relation around teacher selection, and F000047 fixes the first p. 341 paragraph of *Historia de México* as source-critical ideological framing.

Internet Archive now supplies a complete four-slot batch for the substituted pilot position 13. Exhaustive review of the outgoing December 1921 issue (`PDHD-D000053`) confirmed that *El Cardo* and the remaining lexical candidates do not satisfy deterministic slot A without weakening the explicit-act rule. The pilot therefore substitutes `PDHD-D000056`, *El Maestro*, tomo II, núm. I, October 1921. The substitution preserves E3, México, document type `issue` and the four-document publication concentration.

Direct primary inspection fixes `PDHD-F000049` on printed p. 83 / BookReader `n86` in *La enseñanza del dibujo*, where a compact sequence specifies teacher demonstrations, pupil drawings, a cinematograph visit and subsequent reproduction of what was observed. `PDHD-F000050` fixes the SEP/Talleres institutional imprint at `n5`; `PDHD-F000051` fixes a source-critical passage in Gabriela Mistral’s letter to José Vasconcelos on printed p. 57 / `n60`; and `PDHD-F000052` fixes the October 1921 bibliographic cover at `n4` as the control. The failed December fit remains versioned as provenance, while its former pilot-ID links are retired.

`PDHD-D000066`, *El esfuerzo educativo en México* (1928), contributes `PDHD-F000060` as a frozen title-page control. Google Books directly exposes `PR5`. A dedicated recovery workflow fetched the live PR5 HTML, resolved its public PDF link, downloaded a valid 29.9 MB primary PDF and rendered the relevant front matter. Direct inspection fixes only the bibliographic title-page core.

`PDHD-D000076`, *Cómo dar a todo México un idioma* (1928), now contributes a complete four-slot batch as the versioned replacement at pilot position 16. The outgoing `PDHD-D000067` remains in the catalog, but its HathiTrust access was rechecked as search-only and its secondary page-5 candidates were never promoted. Internet Archive item `cmodartodomxicou00ramr` exposes the exact 1928 primary PDF. Direct visual inspection fixes F000061 on printed p. 15 / physical 21 as an instructional sequence, F000062 on p. 13 / physical 19 as professional conditions and training, F000063 on p. 47 / physical 53 as source-critical assimilatory language-policy evidence, and F000064 on physical 9 as the bibliographic control.

`PDHD-D000077`, *Memoria de la Secretaría de Educación Pública* (September 1938-August 1939, tomo II), now contributes a complete A-D batch as the versioned replacement for pilot position 23. Google Books `08ygAAAAMAAJ` exposes a complete primary PDF whose title page was visually inspected before use, preventing conflation with the outgoing 1937 tomo II. Direct inspection fixes F000089 at printed p. 21 / physical 24 as an explicit practical-teaching prescription; F000090 at p. 11 / physical 14 as the rural-normal departmental and teacher-formation unit; F000091 at p. 27 / physical 30 as source-critical evidence of the official regional and Indigenous-population research frame; and F000092 at physical 6 as a bibliographic control. The outgoing D000074 remains cataloged with its failed-access provenance.


`PDHD-D000078`, the 31 August 1926 SEP memory, now contributes the final complete A–D batch as the versioned replacement for pilot position 21. The outgoing 1932 tomo I remains cataloged and page-localized, but repeated retrieval routes did not expose auditable primary pages. Google Books `yvMEAQAAIAAJ` exposes a complete 503-page primary PDF. Direct inspection fixes F000081 at printed p. 223 / physical 238 for Cultural Missions personnel preparation, F000082 at p. 222 / physical 237 for Regional Schools for Rural Teachers, F000083 at p. 225 / physical 240 for source-critical evidence on the Casa del Estudiante Indígena, and F000084 at physical 6 as the bibliographic control.

`PDHD-D000073`, the 1934 SEP memory, now contributes a complete four-slot batch from the primary Google Books copy `mHgQAAAAYAAJ`. Direct inspection maps printed pp. 29, 53 and 58 to physical PDF pages 39, 63 and 68, while `PP7` maps to physical page 9 and supplies the bibliographic control. A competing Google Books full-view object was rejected after its primary title pages identified 1935, preserving primary-page identity over catalog metadata.

`PDHD-D000068`, *El sistema de escuelas rurales en México* (1927), now contributes a complete A–D batch from Internet Archive item `elsistemadeescue00mexi` (`ark:/13960/t8x951q5m`). The primary scan is the SEP/Talleres Gráficos de la Nación edition, with 404 PDF pages. Direct inspection confirms printed p. 72 at physical page 110 and maps printed pp. 285–286 to physical pages 323–324. More importantly, it disconfirms the prior secondary attribution of Cuernavaca-normal organization and a student-origin table to printed pp. 255–256: those pages belong to the Misión de Oaxaca y Chiapas. The final batch therefore replaces those false content attributions with a directly inspected Project Method span, a professional-recruitment span, a source-critical official representation of the Mazatec population and an unnumbered title-page control.


`PDHD-D000069`, *Las misiones culturales en 1927: Las escuelas normales rurales*, now contributes a complete four-slot batch from Internet Archive item `lasmisionescultu00mexi`. HathiTrust record 103012999 points to the same `ark:/13960/t3dz33208`, allowing the blocked Hathi image route to be cross-walked to the exact open primary scan. Direct visual inspection maps printed pp. 23, 54 and 212 to physical PDF pages 43, 74 and 232; the p. 371 budget-title control maps to physical page 391 and is sequence-checked against printed pp. 370 and 373. The batch deliberately replaces section-title pointers with substantive spans where the slot requires analytical content.

`PDHD-D000070`, *Proyecto para la organización de las misiones federales de educación* (1923), now contributes a complete A–D batch after a HathiTrust-to-Google crosswalk resolved the primary object. HathiTrust Record 102280931 identifies OCLC 16016036 and item `uc1.a0009571225`, while its MARC provenance records Google as the digitization source. The OCLC resolves to Google Books `glW6HEb46VoC`, whose public HTML exposes a complete 33-image / 2.13 MB PDF. Direct inspection maps printed pp. 23, 24 and 25 to physical PDF pages 26, 27 and 28; `PA1` maps to physical page 4. The batch freezes a mission-action prescription, a missionary-teacher professional identity paragraph, a source-critical diagnostic/classificatory block, and a bibliographic control. The earlier UNAM embedded facsimile is thereby independently confirmed but is not itself used as the final freeze basis.

All third-party image-derived frozen records remain conservative in public handling. Source images and full historical transcriptions are not committed merely because the object is viewable or downloadable.

## Chronology and source criticism

The image-verification sequence for *El Maestro*, tomo II, núm. 3 resolved `PDHD-X000005` to **1921-12**. `n236` identifies tomo II, núm. III, diciembre de 1921 and `n237` independently confirms México, diciembre de 1921. The secondary 1922 listing remains preserved as a documented discrepancy rather than being erased.

The P4 route demonstrated that a failed delivery channel is not evidence of source absence. HathiTrust exposed no auditable title-page image in the retrieval environment, while Google Books subsequently yielded the inspectable primary PDF through a dynamically resolved download route.

The `PDHD-F000033` recovery established the post-sprint exact-pointer workflow: a secondary scholarly page citation guides retrieval but cannot freeze a span. The *La Enseñanza Primaria* batch extends that principle. UNAM/HNDM independently fixes the selected issue identity; Google Books provides a separate primary scan of the same 1901 volume. Direct inspection of printed pp. 161, 163 and 168 converts two pre-existing exact page pointers and simultaneously resolves two previously unlocalized masthead slots. This is a primary-object cross-check, not a substitution of secondary text for source inspection.

`PDHD-F000037` demonstrates the complementary path from a pure gap to a fixed primary span. The exact BVMC issue was already object-resolved, but no page beyond the opening had been inspected. Rendering the complete primary PDF exposed a pedagogically explicit lesson-plan block on p. 6, allowing localization and freezing to occur in the same source-critical step.

## Remaining freeze-conversion work

The union of all `fragment_locator_progress*.csv` shards contains **96/96** pilot slots. All ninety-six are frozen. The remaining **0** located rows mean that no localized pilot candidate remains outside the frozen registry. **0 slots remain without a locator.**

The dedicated direct-primary freeze-conversion queue remains empty after its P1–P4 cohort was exhausted. Fragment conversion is complete for the current pilot: no page-resolved candidate remains outside the frozen registry, so the active methodological phase has moved from source recovery to human calibration.

The localization and freeze gates are now both complete. The final position-21 substitution is versioned as `PDHD-PS000004`; the outgoing 1932 object remains provenance, while the active pilot uses the directly inspected 1926 SEP memory. The next high-value work is calibration and independent human reliability testing rather than further fragment conversion.

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

Human annotation has **not** started. The same 96 frozen fragments are now partitioned methodologically into a 12-fragment calibration set and an 84-fragment first independent reliability batch. Calibration items are excluded from the formal reliability calculation; no additional historical fragments are created by this partition. Every fragment retains an immutable ID, source identity, page/localizer, fixed boundary, access/rights basis and selection role.

The current 96 frozen units demonstrate that the pipeline works across HNDM, BVMC, Internet Archive and Google Books primary interfaces and can reconcile independent issue identity with alternate primary scans. The freeze package is complete; coder labeling remains intentionally at zero until two real human coders begin the prepared calibration round.

## Rights constraint

Primary-source access does not equal republication permission. HNDM remains `metadata_only`; HathiTrust, Internet Archive, BVMC and Google Books/Google Play access are treated as research-access or retrieval layers rather than blanket licenses to mirror scans or full OCR. Where reuse is not clearly authorized, coder text remains outside the public repository.

## Decision

PDHD-U1 has completed **pilot freezing**. Issue #1 stays open through the first independent human reliability round.

The project is now at **96/96 localized** and **96/96 frozen**. The final substitution closes the package while preserving the unlocalized complement at 0. The deterministic 12-item calibration package is prepared under `PDHD-CAL-0.1-20260907`, with `PDHD-CB-0.2-calibration` pinned as the pre-calibration baseline. Human coding remains at 0; the next gate requires two real independent first-pass calibration sheets before any codebook revision, formal 84-item reliability round or gold-label adjudication.