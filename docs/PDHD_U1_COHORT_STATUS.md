# PDHD-U1 cohort status

Reference cut: **2026-09-04**

## Current thresholds

| Layer | Count | Status |
|---|---:|---|
| Registered discovery candidates | 25 | threshold reached |
| Object-level documents | 75 | stabilization advanced |
| Issue-level leads | 21 total / 19 unresolved | active balancing queue |
| Sources with explicit rights policy | 13 / 13 | complete at source-policy level |
| Registered chronology conflicts | 5 | explicitly preserved |
| Frozen pilot documents | 24 | document-selection gate passed |
| Target fixed fragments | 96 | preparation active |
| Fragment locator rows resolved/candidate | **75 / 96** | 78.1% of reliability slots localized |
| Fully frozen fragments | **15 / 96** | three complete batches plus one three-slot primary-image batch |
| Human-validated pedagogical fragments | 0 | not started |

The 75-object cohort remains a stabilization corpus, not a national representative sample. PDHD-U1 now has **75 of the 96 deterministic reliability slots** tied to a documented page, scan or section target. Fifteen units have crossed the stronger frozen-fragment gate.

## Sampling status

The first reliability corpus remains frozen in `data/samples/pilot_document_selection_0_1.csv`: 10 E1 documents, 12 E3 documents and 2 E4 documents. It includes regional origins outside Mexico City, multiple documentary regimes and no publication contributing more than six documents. This is a methodological reliability sample rather than an estimator of national historical frequencies.

## Frozen-fragment evidence

Three selected documents have complete four-slot batches. `PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888, contributes `PDHD-F000013`–`PDHD-F000016`. `PDHD-D000001`, *La Enseñanza Objetiva* of 12 December 1891, contributes `PDHD-F000017`–`PDHD-F000020`. `PDHD-D000055`, the first 1921 number of *El Maestro. Revista de Cultura Nacional*, contributes `PDHD-F000053`–`PDHD-F000056`.

A fourth document contributes a partial but fully frozen three-slot batch: `PDHD-D000031`, *La Enseñanza Moderna*, tomo I, segunda época, núm. 1, 1 July 1907. BVMC directly exposes the primary first-page image. Direct image inspection fixes `PDHD-F000038` as the editorial/professional masthead region, `PDHD-F000039` as the opening programmatic article region and `PDHD-F000040` as the publication/subscription administrative control. `PDHD-F000037` remains empty because no explicit pedagogical-act span has yet been inspected at sufficient resolution.

HNDM remains `metadata_only`; the BVMC first-page batch is also stored conservatively as `metadata_only`. GitHub retains structural boundaries and provenance rather than source images or full transcriptions.

## Three-quarter localization batch

`fragment_locator_progress_threshold72_w9.csv` added eight deterministic slots without changing the frozen count.

`PDHD-D000011`, the inaugural *La Enseñanza Normal* issue of 15 September 1904, gained two first-page targets: `PDHD-F000034` for the professional/editorial region and `PDHD-F000036` for publication/subscription administration. Both are tied to the exact BVMC object but remain candidates until high-resolution structural boundaries are checked.

The *El Maestro* block gained four additional slots. `PDHD-F000044` reserves the stable Internet Archive opening scan for núm. 2 (1921) as a control candidate. `PDHD-F000047` targets Rafael Ramos Pedrueza's *Historia de México*, núm. 4 (1921), pp. 341–348. `PDHD-F000048` reserves the stable opening scan of núm. 4 as a control candidate. `PDHD-F000052` reserves the opening reader page of tomo II, núm. 3 as a control while preserving the existing 1922/December-1921 chronology conflict.

`PDHD-F000045` targets Dionisio Montelongo Jr.'s *La ilustración de las masas*, pp. 363–365, but carries `issue_number_check_pending`: the secondary bibliography places the July 1921 item under a number incompatible with the working issue sequence. PDHD therefore records the page lead without silently normalizing the issue number or promoting it to primary evidence.

Finally, `PDHD-F000083` completes the four-slot localization of the 1932 SEP memory by targeting p. 487 for a source-critical comparison of technical, primary and rural educational organization/costs. It remains a secondary page pointer pending direct verification in the Google Books object.

## México Intelectual and La Enseñanza Normal additions

Three new page-resolved candidates move the pilot from 72 to **75 localized slots**.

`PDHD-F000009` uses *México intelectual*, tomo I, p. 5 for an explicit programmatic prescription centered on diffusion of teaching methods, systems and modern pedagogical approaches to the teaching profession. A recent historical study identifies that page explicitly; direct inspection of the historical page remains pending.

`PDHD-F000012` uses *México intelectual*, tomo I, p. 6 as the deliberately low-pedagogical-content control candidate. The *Anuario Mexicano de Historia de la Educación* cites that page for prices and correspondence-routing instructions. This is page-resolved secondary evidence, not a frozen primary span.

`PDHD-F000033` closes the only remaining localization gap in the inaugural *La Enseñanza Normal* issue. A UNAM thesis cites p. 12 for Leopoldo Kiel's explicit statement that teacher formation requires sustained work with groups of children, observation, experimentation and verification of teaching procedures. This is a strong pedagogical-practice target, but its BVMC page still requires direct inspection before freezing.

These additions preserve the rule:

`secondary_page_pointer != directly_inspected_historical_page`

## El Maestro expansion

The postrevolutionary press block extends beyond the first frozen issue. Exact secondary page pointers are registered for José U. Escobar's *Las tribus indígenas mexicanas* (I,2, pp. 173–176), José Suirob's *Orientación obrera* (I,2, pp. 145–147), Grupo Claridad's *La internacional de los intelectuales* (I,2, pp. 133–135), Abel Ayala's *Mejores maestros* (I,4, pp. 351–352), Rafael Ramos Pedrueza's *Historia de México* (núm. 4, pp. 341–348), Gabriela Mistral's *Lecturas escolares. El cardo* (II,III, pp. 299–300) and Rufino Blanco-Fombona's *Democracia Criolla* (II,3, pp. 293–297).

These remain locator candidates until the historical pages themselves are inspected. Internet Archive supplies stable reader targets for the selected objects, which are treated as retrieval/control candidates rather than page-level analytical proof.

The Mistral citation exposed the fifth registered chronology conflict. Signos Históricos identifies tomo II, núm. 3 as 1922, while a UNAM thesis cites *Lecturas escolares. El cardo* in tomo II, no. III, December 1921. `PDHD-X000005` preserves the disagreement; the working catalog retains 1922 at year precision pending original-imprint inspection.

## SEP memory blocks

`PDHD-D000074`, *Memoria de la Secretaría de Educación Pública*, vol. 2 (1937), has all four deterministic slots localized. `PDHD-F000089` uses a secondary exact pointer to p. 371 for a passage relating manual work to mental/intellectual development and application of school knowledge. `PDHD-F000090` uses Google Books' direct contents entry for the Consejo Nacional de la Educación Superior y de la Investigación on p. 41. `PDHD-F000091` uses a UNAM thesis pointer to vol. 2, p. 444 for a library-attendance report. `PDHD-F000092` uses the direct Google Books contents entry *Distribución de Becas en la República* on p. 40 as an administrative control candidate.

`PDHD-D000072`, the 1932 SEP memory, also has all four slots localized after adding `PDHD-F000083` at p. 487. The direct contents entries are stronger than bibliographic leads but remain section targets rather than analytical spans. Secondary page pointers remain explicitly below direct primary-page inspection.

## Fragment-localization progress

The union of all `fragment_locator_progress*.csv` shards contains **75/96** pilot slots. Fifteen are frozen. The remaining **60** located rows include direct primary-page candidates, direct reader/scan targets, direct section starts, reproduced facsimiles and exact scholarly page pointers. **21 slots remain without a locator.**

The retrieval chain remains:

`issue identity -> content lead -> page-level fragment locator -> frozen fragment -> human annotation`

The mandatory distinctions remain:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`reader_page_target != analytical_span`

`table_of_contents_entry != passage`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Integrity and provenance

`scripts/validate_repository.py` validates the base catalog. `scripts/validate_fragment_shards.py` validates the logical union of all locator/frozen shards, including deterministic document/slot identity, duplicate protection, fixed-boundary requirements and cross-checking between frozen rows and locator rows. It also requires `fragment_gap_queue_0_1.csv` to equal the exact complement of the localized fragment IDs.

`validate_object_aliases.py` protects cross-repository bridges. `validate_content_leads.py` protects the transition from issue-level discovery to page-level evidence. GitHub Actions runs these checks together with the annotation-agreement self-test and deterministic 96-slot manifest check.

## What remains before human coding

Human annotation has **not** started. The target remains 96 frozen reliability fragments, four per selected document, followed by a separate 12-fragment calibration set. Every reliability fragment must retain an immutable ID, source identity, page/localizer, fixed boundary, access/rights basis and selection role.

The current 15 frozen units demonstrate that the pipeline works across HNDM and BVMC primary interfaces and across late-nineteenth-, early-twentieth- and postrevolutionary documentary settings. They do not justify coder labeling before the package is complete.

## Rights constraint

Primary-source access does not equal republication permission. HNDM remains `metadata_only`; HathiTrust, Internet Archive and Google Books/Google Play access are treated as research-access or retrieval layers rather than blanket licenses to mirror scans or full OCR. Where reuse is not clearly authorized, coder text remains outside the public repository.

## Decision

PDHD-U1 remains in **active pilot freezing**. Issue #1 stays open through completion of the 96-fragment package and the first independent human reliability round.

The project is now at **75/96 localized**. The next operational threshold remains **80/96 located**, while the stronger scientific priority is to raise the frozen count beyond **15/96**, especially by converting direct page/scan candidates into exact coder spans rather than adding weaker references.