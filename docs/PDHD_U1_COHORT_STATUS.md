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
| Fragment locator rows resolved/candidate | **58 / 96** | localization majority established |
| Fully frozen fragments | **12 / 96** | three complete four-slot document batches |
| Human-validated pedagogical fragments | 0 | not started |

The 75-object cohort remains a stabilization corpus, not a national representative sample. PDHD-U1 now has more than half of the deterministic pilot slots localized and three selected documents with complete four-slot frozen batches.

## Composition and sampling status

PDHD treats `data/catalog/documents.csv` and `data/catalog/documents_balancing_w1.csv` as validated shards of one object catalog. BVM-CERVANTES still contributes 40/75 objects (53.3%), but the pilot itself deliberately combines multiple repositories, regions and documentary types so that digitization convenience is not confused with historical importance.

The first reliability corpus remains frozen in `data/samples/pilot_document_selection_0_1.csv`: 10 E1 documents, 12 E3 documents and 2 E4 documents. The selection includes regional objects from Campeche, Aguascalientes and Xalapa, multiple documentary types and no publication contributing more than six documents. It is a methodological reliability sample, not an estimator of national frequencies.

## Three complete fragment-freeze batches

The first batch is `PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888 (`PDHD-F000013`–`PDHD-F000016`). Direct HNDM inspection fixed an instructional passage, a professional roster, a methodological-context passage and an administrative control.

The second is `PDHD-D000001`, *La Enseñanza Objetiva* of 12 December 1891 (`PDHD-F000017`–`PDHD-F000020`). Direct inspection fixed a vocabulary/reading-teaching unit, a publication mission statement, a grammar exercise sequence and a subscription/publication control.

The third is `PDHD-D000055`, the first 1921 number of *El Maestro. Revista de Cultura Nacional* (`PDHD-F000053`–`PDHD-F000056`). HNDM directly exposes the issue cover and printed page 15 with the opening of Ezequiel A. Chávez's *Los rasgos distintivos de la educación moderna*. PDHD fixed one conceptual-prescriptive span, one editorial/professional identity span, one programmatic reader-collaboration span and one administrative control.

This third batch extends direct fragment freezing from late-nineteenth-century pedagogical press into the early postrevolutionary cultural-educational project. Because HNDM remains `metadata_only`, the repository stores structural boundaries and provenance rather than historical text or page images.

## El Maestro localization expansion

The newest locator shard adds four exact secondary page targets across three additional selected *El Maestro* objects.

`PDHD-F000043` targets José U. Escobar's *Las tribus indígenas mexicanas* in tomo I, núm. 2, pp. 173–176. `PDHD-F000046` targets Abel Ayala's *Mejores maestros* in tomo I, núm. 4, pp. 351–352. `PDHD-F000049` targets Gabriela Mistral's *Lecturas escolares. El cardo*, tomo II, núm. III, pp. 299–300. `PDHD-F000051` targets Rufino Blanco-Fombona's *Democracia Criolla*, tomo II, núm. 3, pp. 293–297.

All four remain `locator_candidate`. Exact page citations in scholarship are useful retrieval evidence, but they do not become frozen units until the historical pages themselves are inspected and coder boundaries are fixed.

The Mistral reference exposed a fifth chronology conflict. Signos Históricos identifies the tomo II, núm. 3 digital object as 1922, whereas a UNAM thesis cites *Lecturas escolares. El cardo* in tomo II, no. III, December 1921. `PDHD-X000005` preserves the discrepancy. The current catalog keeps 1922 at year precision pending direct inspection of the original imprint.

## Broader fragment-localization progress

The union of all `fragment_locator_progress*.csv` shards now contains **58/96** pilot slots. Twelve are frozen. The remaining 46 range from direct primary page candidates and section starts to reproduced facsimiles and secondary scholarly page pointers.

Other localized objects include *El Instructor*, *México intelectual*, *La Escuela moderna*, *Revista de la Instrucción Pública Mexicana*, *La Enseñanza Normal*, *La Enseñanza Moderna*, rural-teacher monographs, cultural-mission reports and SEP institutional memories.

The retrieval chain remains:

`issue identity -> content lead -> page-level fragment locator -> frozen fragment -> human annotation`

And the epistemic distinctions remain mandatory:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`table_of_contents_entry != passage`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Cross-repository and content-lead layers

`data/catalog/object_aliases.csv` records explicit bridges between canonical PDHD objects and alternate repository interfaces. Those bridges improve retrieval but do not become page evidence without a resolved page identity.

`data/samples/pilot_content_leads.csv` now preserves both page-unresolved content discoveries and exact scholarly page pointers. `validate_content_leads.py` prevents unresolved leads from being promoted and requires any promoted content lead to have a resolved page state.

## Integrity checks

`scripts/validate_repository.py` validates the base catalog. `scripts/validate_fragment_shards.py` validates the logical union of locator/frozen shards, including duplicate detection, deterministic document/slot matching, fixed-boundary requirements and cross-checks between frozen and locator rows.

`validate_object_aliases.py` checks cross-repository bridges. `validate_content_leads.py` protects the issue-to-page transition. GitHub Actions runs these checks together with the annotation-agreement self-test and deterministic 96-slot manifest check.

## What remains before human coding

Human annotation has **not** started. The target remains 96 frozen reliability fragments, four per selected document, followed by a separate 12-fragment calibration set. Every reliability fragment must retain immutable ID, source identity, page/localizer, fixed boundary, access/rights basis and selection role.

The current 12 frozen units prove that the freeze pipeline works across three historical publications. They do not justify starting coder labeling before the package is complete.

## Rights constraint

Primary-source access does not equal republication permission. HNDM remains `metadata_only`; HathiTrust and Google Books/Google Play access is treated as research access rather than a blanket license to mirror scans or full OCR. Where reuse is not clearly authorized, coder text must remain outside the public GitHub repository.

## Decision

PDHD-U1 remains in **active pilot freezing**. Issue #1 stays open through completion of the 96-fragment package and the first independent human reliability round.

The next quantitative threshold is **64/96 located** (two thirds of the pilot). The stronger scientific priority remains to raise the frozen count from **12/96** by converting intermediate locators into directly inspected primary spans instead of merely accumulating weaker references.
