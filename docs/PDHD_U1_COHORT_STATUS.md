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
| Fragment locator rows resolved/candidate | **64 / 96** | two-thirds localization threshold reached |
| Fully frozen fragments | **15 / 96** | three complete batches plus one three-slot primary-image batch |
| Human-validated pedagogical fragments | 0 | not started |

The 75-object cohort remains a stabilization corpus, not a national representative sample. PDHD-U1 has crossed the **two-thirds localization threshold**: 64 of the 96 deterministic reliability slots have a documented page or section target. Fifteen units have now crossed the stronger frozen-fragment gate.

## Sampling status

The first reliability corpus remains frozen in `data/samples/pilot_document_selection_0_1.csv`: 10 E1 documents, 12 E3 documents and 2 E4 documents. It includes regional origins outside Mexico City, multiple documentary regimes and no publication contributing more than six documents. This is a methodological reliability sample rather than an estimator of national historical frequencies.

## Frozen-fragment evidence

Three selected documents have complete four-slot batches. `PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888, contributes `PDHD-F000013`–`PDHD-F000016`. `PDHD-D000001`, *La Enseñanza Objetiva* of 12 December 1891, contributes `PDHD-F000017`–`PDHD-F000020`. `PDHD-D000055`, the first 1921 number of *El Maestro. Revista de Cultura Nacional*, contributes `PDHD-F000053`–`PDHD-F000056`.

A fourth document now contributes a partial but fully frozen three-slot batch: `PDHD-D000031`, *La Enseñanza Moderna*, tomo I, segunda época, núm. 1, 1 July 1907. BVMC directly exposes the primary first-page image. Direct image inspection fixes `PDHD-F000038` as the editorial/professional masthead region, `PDHD-F000039` as the opening programmatic article region and `PDHD-F000040` as the publication/subscription administrative control. `PDHD-F000037` remains empty because no explicit pedagogical-act span has yet been inspected at sufficient resolution.

The BVMC collection record independently identifies the publication as a pedagogical weekly, records its 1 July 1907 beginning, names Lázaro Pavía as director/owner, and describes its subscription and editorial arrangements. This supports structural identification of the three first-page regions without requiring PDHD to reproduce the historical wording.

HNDM remains `metadata_only`; the BVMC first-page batch is also stored conservatively as `metadata_only`. GitHub retains structural boundaries and provenance rather than source images or full transcriptions.

## El Maestro expansion

The postrevolutionary press block extends beyond the first frozen issue. Exact secondary page pointers are registered for José U. Escobar's *Las tribus indígenas mexicanas* (I,2, pp. 173–176), José Suirob's *Orientación obrera* (I,2, pp. 145–147), Grupo Claridad's *La internacional de los intelectuales* (I,2, pp. 133–135), Abel Ayala's *Mejores maestros* (I,4, pp. 351–352), Gabriela Mistral's *Lecturas escolares. El cardo* (II,III, pp. 299–300) and Rufino Blanco-Fombona's *Democracia Criolla* (II,3, pp. 293–297).

These remain locator candidates until the historical pages themselves are inspected. Internet Archive directly identifies the volume-2 digital object as `n1n3elmaestrorev02mexi`, volume 2, numbers 1–3, with 356 scanned pages and downloadable OCR/full-text derivatives. Open Library crosswalks that object to edition `OL25476443M`; PDHD records the alternate-catalog bridge in `data/catalog/object_aliases.csv` without treating it as page evidence.

The Mistral citation exposed a fifth chronology conflict. Signos Históricos identifies tomo II, núm. 3 as 1922, while a UNAM thesis cites *Lecturas escolares. El cardo* in tomo II, no. III, December 1921. `PDHD-X000005` preserves the disagreement; the working catalog retains 1922 at year precision pending original-imprint inspection.

## 1937 SEP memory block

`PDHD-D000074`, *Memoria de la Secretaría de Educación Pública*, vol. 2 (1937), has all four deterministic slots localized. `PDHD-F000089` uses a secondary exact pointer to p. 371 for a passage relating manual work to mental/intellectual development and application of school knowledge. `PDHD-F000090` uses Google Books' direct contents entry for the Consejo Nacional de la Educación Superior y de la Investigación on p. 41. `PDHD-F000091` uses a UNAM thesis pointer to vol. 2, p. 444 for a library-attendance report. `PDHD-F000092` uses the direct Google Books contents entry *Distribución de Becas en la República* on p. 40 as an administrative control candidate.

The direct contents entries are stronger than bibliographic leads but remain section targets rather than analytical spans. The secondary page pointers remain explicitly below direct primary-page inspection.

## Fragment-localization progress

The union of all `fragment_locator_progress*.csv` shards contains **64/96** pilot slots. Fifteen are frozen. The remaining 49 include direct primary-page candidates, direct section starts, reproduced facsimiles and exact scholarly page pointers.

The retrieval chain remains:

`issue identity -> content lead -> page-level fragment locator -> frozen fragment -> human annotation`

The mandatory distinctions remain:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`table_of_contents_entry != passage`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Integrity and provenance

`scripts/validate_repository.py` validates the base catalog. `scripts/validate_fragment_shards.py` validates the logical union of all locator/frozen shards, including deterministic document/slot identity, duplicate protection, fixed-boundary requirements and cross-checking between frozen rows and locator rows.

`validate_object_aliases.py` protects cross-repository bridges. `validate_content_leads.py` protects the transition from issue-level discovery to page-level evidence. GitHub Actions runs these checks together with the annotation-agreement self-test and deterministic 96-slot manifest check.

## What remains before human coding

Human annotation has **not** started. The target remains 96 frozen reliability fragments, four per selected document, followed by a separate 12-fragment calibration set. Every reliability fragment must retain an immutable ID, source identity, page/localizer, fixed boundary, access/rights basis and selection role.

The current 15 frozen units demonstrate that the pipeline works across HNDM and BVMC primary interfaces and across late-nineteenth-, early-twentieth- and postrevolutionary documentary settings. They do not justify coder labeling before the package is complete.

## Rights constraint

Primary-source access does not equal republication permission. HNDM remains `metadata_only`; HathiTrust and Google Books/Google Play access is treated as research access rather than a blanket license to mirror scans or full OCR. Where reuse is not clearly authorized, coder text remains outside the public repository.

## Decision

PDHD-U1 remains in **active pilot freezing**. Issue #1 stays open through completion of the 96-fragment package and the first independent human reliability round.

The next quantitative threshold is **72/96 located** (three quarters of the pilot). The stronger scientific priority is to increase the frozen count beyond **15/96**, especially by converting directly accessible or page-resolved primary candidates before adding weaker evidence.
