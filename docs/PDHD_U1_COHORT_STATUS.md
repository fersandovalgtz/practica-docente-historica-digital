# PDHD-U1 cohort status

Reference cut: **2026-09-04**

## Current thresholds

| Layer | Count | Status |
|---|---:|---|
| Registered discovery candidates | 25 | threshold reached |
| Object-level documents | 75 | stabilization advanced |
| Issue-level leads | 21 total / 19 unresolved | active balancing queue |
| Sources with explicit rights policy | 13 / 13 | complete at source-policy level |
| Registered chronology conflicts | 4 | explicitly preserved |
| Frozen pilot documents | 24 | document-selection gate passed |
| Target fixed fragments | 96 | preparation active |
| Fragment locator rows resolved/candidate | **54 / 96** | localization majority established |
| Fully frozen fragments | **12 / 96** | three complete four-slot document batches |
| Human-validated pedagogical fragments | 0 | not started |

The 75-object cohort remains a stabilization corpus, not a national representative sample. PDHD-U1 has now crossed two different methodological thresholds: more than half of the deterministic pilot slots have a documented page/section locator, and three selected documents have complete four-slot frozen batches.

## Composition of the 75-document union

PDHD treats `data/catalog/documents.csv` and `data/catalog/documents_balancing_w1.csv` as validated shards of one object catalog. The separation keeps the balancing intervention auditable.

| Source | Documents | Share |
|---|---:|---:|
| BVM-CERVANTES | 40 | 53.3% |
| UNAM-RI | 11 | 14.7% |
| HNDM | 7 | 9.3% |
| INTERNET-ARCHIVE | 7 | 9.3% |
| GOOGLE-BOOKS | 5 | 6.7% |
| HATHITRUST | 4 | 5.3% |
| BIBMX-FR | 1 | 1.3% |

The original 80% dependence on BVM-CERVANTES has fallen to 53.3%. This remains a convenience-driven digitization concentration and must not be interpreted as historical importance.

## Rural and postrevolutionary primary-source block

The former hard bottleneck—absence of stable primary rural-teacher material—is resolved. The pilot now includes direct historical objects such as *El papel social del maestro rural*, *El sistema de escuelas rurales en México*, *Las misiones culturales en 1927*, *Proyecto para la organización de las misiones federales de educación*, *Las misiones culturales, 1932-1933*, *El esfuerzo educativo en México* and several SEP institutional memories.

Secondary scholarship continues to function as a retrieval layer only. When it provides a page pointer, PDHD labels that pointer as secondary until the historical page itself is inspected. The 1925/1926 discrepancy for *El papel social del maestro rural* remains registered as an open chronology conflict.

## First 24-document pilot selection

The first reliability corpus remains frozen in `data/samples/pilot_document_selection_0_1.csv`:

| Era | Documents |
|---|---:|
| E1 — 1870–1910 | 10 |
| E3 — 1921–1934 | 12 |
| E4 — 1935–1940 | 2 |

The selection includes regional objects from Campeche, Aguascalientes and Xalapa, multiple documentary types and no publication contributing more than six documents. This is a methodological reliability sample, not an estimator of national historical frequencies.

## Three complete fragment-freeze batches

The first batch is `PDHD-D000002`, *El Escolar Mexicano* of 2 September 1888 (`PDHD-F000013`–`PDHD-F000016`). Direct HNDM page inspection fixed an instructional passage, a professional editorial roster, a methodological-context passage and an administrative control.

The second batch is `PDHD-D000001`, *La Enseñanza Objetiva* of 12 December 1891 (`PDHD-F000017`–`PDHD-F000020`). Direct inspection fixed a compact vocabulary/reading-teaching unit, an explicit publication mission statement, a grammar exercise sequence and a subscription/publication control.

The third batch is `PDHD-D000055`, the first 1921 number of *El Maestro. Revista de Cultura Nacional* (`PDHD-F000053`–`PDHD-F000056`). HNDM directly exposes both the issue cover and the printed page 15 carrying the opening of Ezequiel A. Chávez's *Los rasgos distintivos de la educación moderna*. PDHD fixed one conceptual-prescriptive education span, one editorial/professional identity span, one programmatic reader-collaboration span and one administrative control.

This third batch is important because fragment freezing now spans both the late-nineteenth-century pedagogical press and the early postrevolutionary cultural-educational project.

Because these pages are accessed through HNDM and HNDM remains `metadata_only`, the public repository does not store the historical text or page images. It stores page identity, source locator, structural boundary, access basis, selection role and preparation provenance.

## Fragment-localization progress

The union of all `fragment_locator_progress*.csv` shards now contains **54/96** pilot slots. Twelve are frozen. The remaining 42 range from direct primary page candidates to direct section starts, reproduced facsimiles and secondary scholarly page pointers.

Recent pre-1910 additions include page-resolved candidates from *El Instructor*, *México intelectual*, *La Escuela moderna*, *Revista de la Instrucción Pública Mexicana* and *La Enseñanza Normal*. Three more slots from *La Enseñanza Moderna* are anchored to a directly exposed first-page BVMC image.

The new *El Maestro* batch is stored separately in `fragment_locator_progress_hndm_el_maestro_w6.csv` and `frozen_fragments_hndm_el_maestro_w6.csv`. Sharding preserves batch provenance while `scripts/validate_fragment_shards.py` treats every shard as one logical deterministic manifest.

The retrieval chain remains:

`issue identity -> content lead -> page-level fragment locator -> frozen fragment -> human annotation`

And the epistemic distinctions remain mandatory:

`secondary_page_citation != primary_page_inspection`

`visible_reproduced_facsimile != primary_object_crosscheck`

`table_of_contents_entry != passage`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Cross-repository layer

`data/catalog/object_aliases.csv` records explicit bridges between canonical PDHD objects and alternate repository interfaces. UNAM-RI records for *La Enseñanza primaria*, *El Instructor* and *México intelectual* lead to HNDM targets, but those bridges do not become page locators unless a page identity is actually resolved.

`data/samples/pilot_content_leads.csv` retains article-level or passage-level discoveries whose page is still unresolved. The validator prevents such leads from being promoted prematurely.

## Integrity checks

`scripts/validate_repository.py` validates the base catalog. `scripts/validate_fragment_shards.py` validates the logical union of locator/frozen shards, including duplicate detection, deterministic document/slot matching, fixed-boundary requirements and cross-checks between frozen rows and locator rows.

`validate_object_aliases.py` checks cross-repository bridges. `validate_content_leads.py` prevents unresolved content leads from masquerading as page-level fragment evidence. GitHub Actions runs these checks together with the annotation-agreement self-test and deterministic manifest check.

## What remains before human coding

Human annotation has **not** started. The target remains 96 frozen reliability fragments, four per selected document, followed by a separate 12-fragment calibration set. Every reliability fragment must retain immutable ID, source identity, page/localizer, fixed boundary, access/right basis and selection role.

The current 12 frozen units prove that the freeze pipeline works across three historical publications. They do not justify starting coder labeling before the package is complete.

## Rights constraint

Primary-source access does not equal republication permission. HNDM remains `metadata_only`; HathiTrust and Google Books/Google Play access is treated as research access rather than a blanket license to mirror scans or full OCR. Where reuse is not clearly authorized, coder text must remain outside the public GitHub repository.

## Decision

PDHD-U1 remains in **active pilot freezing**. Issue #1 stays open through completion of the 96-fragment package and the first independent human reliability round.

The next quantitative threshold is **64/96 located** (two thirds of the pilot), but the stronger scientific priority is to raise the frozen count from **12/96** by converting existing weak or intermediate locators into directly inspected primary spans rather than merely adding more secondary page pointers.
