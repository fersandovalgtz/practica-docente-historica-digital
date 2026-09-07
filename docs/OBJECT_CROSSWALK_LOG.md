# Object crosswalk log

## Purpose

PDHD may encounter the same historical object through more than one repository layer. A catalog record, a full-text landing page and the underlying digital-serial interface are not interchangeable identifiers. This log documents cross-repository bridges without changing the canonical `source_id` of the PDHD document.

`catalog_object != digital_serial_container`

`object_crosswalk != page_locator`

## 2026-09-04 — La Enseñanza primaria, UNAM-RI to HNDM

The Repositorio Institucional UNAM records used by PDHD for *La Enseñanza primaria* expose a `Texto completo` link. Following that link resolves to the HNDM digital-serial object `558075be7d1e63c9fea1a250` with issue-specific date parameters.

The first three crosswalks registered in `data/catalog/object_aliases.csv` are:

| PDHD document | UNAM-RI object | Issue date | Underlying HNDM serial object |
|---|---|---|---|
| `PDHD-D000003` | `746481` | 1901-12-01 | `558075be7d1e63c9fea1a250` |
| `PDHD-D000004` | `746576` | 1908-05-01 | `558075be7d1e63c9fea1a250` |
| `PDHD-D000005` | `746583` | 1909-07-15 | `558075be7d1e63c9fea1a250` |

The shared HNDM identifier represents the serial container; the URL date parameters distinguish the requested issue. Automated retrieval of the HNDM interface returned HTTP 502 during this pass. PDHD therefore records the bridge as `repository_fulltext_link_resolved_interface_fetch_failed` and does not infer a page number, page image identifier or OCR availability.

This is useful because the selected pilot object `PDHD-D000003` can now be targeted through its underlying HNDM serial identity rather than searched again from scratch.

## 2026-09-04 — regional pilot objects

The same method resolved the underlying HNDM serial target for two selected regional objects. UNAM-RI marks both records as `Contenido completo`, identifies their originating HNDM collection and exposes the full-text link.

| PDHD document | UNAM-RI object | Issue date | Underlying HNDM serial object | Region |
|---|---|---|---|---|
| `PDHD-D000064` | `750865` | 1889-01-01 | `558075be7d1e63c9fea1a307` | Aguascalientes |
| `PDHD-D000063` | `897145` | 1889-01-01 | `558075be7d1e63c9fea1a356` | Xalapa, Veracruz |

For `PDHD-D000064`, UNAM-RI describes *El Instructor* as an education object and records the Imp. de Trinidad Pedroza. For `PDHD-D000063`, it identifies *México intelectual* as a primary-education object and records the Imprenta del Gobierno del Estado. Both digital resources carry the repository's CC BY-NC-ND 4.0 statement.

Following the `Texto completo` links resolved the HNDM serial identifiers above, but the HNDM interface again returned HTTP 502 to the automated research client. These are therefore object-level crosswalks only. No page locator has been inferred and neither selected document has been advanced toward `frozen` status on the basis of this bridge alone.

## Content lead inside PDHD-D000003

Peer-reviewed scholarship identifies Ponciano Rodríguez's article *El método en los libros de texto* in *La Enseñanza Primaria*, tomo I, núm. 11, dated 1 December 1901. The issue identity matches `PDHD-D000003`.

The scholarship also treats the magazine as a publication by and for teachers and places Rodríguez's textbook articles within its pedagogical program. The article is therefore a strong candidate for the pilot's instructional/source-criticism slots. However, the current research pass did not resolve its original page number in the 1901 issue.

The lead is consequently stored in `data/samples/pilot_content_leads.csv` with:

- `page_status=page_unresolved`;
- `promotion_status=not_eligible_for_fragment_locator`.

It must not be inserted into `fragment_locator_progress*.csv` until an original page or stable page-level locator is established.

## 2026-09-06 — El Periquito no. 4, UNAM-RI to HNDM

UNAM-RI record `921573` resolves the exact selected issue of *El Periquito* dated 6 November 1870 and exposes `item_pages=4`, HNDM `item_publication_id=558075be7d1e63c9fea1a3df` and persistent `item_first_page_id=558a32a77d1ed64f1688827b`. The corresponding HNDM full-text target is registered as `PDHD-A000007`.

Unlike the earlier descriptor-only state, the persistent first-page identifier was directly usable. Traversal by HNDM's explicit `siguienteLink` identifiers recovered four unique page PDFs and every page preserved the expected title, issue date and four-page count. The crosswalk remains object-level provenance; the direct page locators and fixed coder boundaries are recorded separately in the fragment shards.

## 2026-09-06 — El Maestro no. 2 (mayo de 1921), exact Internet Archive issue object

`PDHD-D000051` previously relied on the combined Internet Archive container `n1n3elmaestrorevista01mexi` for its issue-control fragment. A title/year search resolved the separate exact issue object `el-maestro.-revista-de-cultura-nacional-n-2-1921`, whose metadata identifies *El Maestro. Revista de Cultura Nacional, N° 2* (1921) and exposes a 118-page text PDF plus BookReader derivatives. This object is registered as `PDHD-A000008`.

Direct visual inspection maps printed p. 133 to PDF p. 39, p. 145 to PDF p. 51, p. 147 to PDF p. 53 and p. 173 to PDF p. 79. Independent image comparison against neighboring BookReader derivatives proves the corresponding leaves `n38`, `n50`, `n52` and `n78`; the same continuous one-to-one offset places printed p. 135 / PDF p. 41 at `n40`. The crosswalk remains object-level provenance. F000041-F000043 store their page locators and fixed boundaries separately.

## Integrity decision

`scripts/validate_object_aliases.py` validates document-to-alias crosswalks. `scripts/validate_content_leads.py` enforces the rule that a page-unresolved content lead cannot become eligible for fragment-locator promotion.

This preserves a three-stage retrieval chain:

`issue identity -> content lead -> page-level fragment locator`

None of those stages is silently collapsed into the next.

## 2026-09-06 — El Maestro núm. 4, Internet Archive serial container

`PDHD-D000052` is cross-walked to Internet Archive `elmaestrorevista146mexi`, a 1921 primary container identified as volume 1, numbers 4–6. The container relation is preserved explicitly: `serial_container != issue_page_locator`.

The object does not expose the same `_text.pdf` derivative used for the separate May 1921 issue. Its DjVu XML was therefore used only as a discovery index. Direct BookReader images then confirmed the number-four sequence: `n26` = printed p. 341 (*Historia de México*), `n36` = p. 351 (*Mejores maestros*), `n37` = p. 352 and `n48`–`n50` = pp. 363–365 (*La ilustración de las masas*). The existing `n4` cover control independently identifies número IV.

The earlier secondary slot-A target on pp. 363–365 is retained as a documented recovery lead but rejected for deterministic act fit after primary inspection. `PDHD-F000045` instead uses a directly visible, non-overlapping `guide` prescription on p. 352. `PDHD-F000046` fixes numbered item 3 on p. 351 and `PDHD-F000047` fixes the first analytical paragraph on p. 341. No source image or full historical transcription is committed.

