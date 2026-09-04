# Object crosswalk log

## Purpose

PDHD may encounter the same historical object through more than one repository layer. A catalog record, a full-text landing page and the underlying digital-serial interface are not interchangeable identifiers. This log documents cross-repository bridges without changing the canonical `source_id` of the PDHD document.

`catalog_object != digital_serial_container`

`object_crosswalk != page_locator`

## 2026-09-04 — La Enseñanza primaria, UNAM-RI to HNDM

The Repositorio Institucional UNAM records used by PDHD for *La Enseñanza primaria* expose a `Texto completo` link. Following that link resolves to the HNDM digital-serial object `558075be7d1e63c9fea1a250` with issue-specific date parameters.

The crosswalks now registered in `data/catalog/object_aliases.csv` are:

| PDHD document | UNAM-RI object | Issue date | Underlying HNDM serial object |
|---|---|---|---|
| `PDHD-D000003` | `746481` | 1901-12-01 | `558075be7d1e63c9fea1a250` |
| `PDHD-D000004` | `746576` | 1908-05-01 | `558075be7d1e63c9fea1a250` |
| `PDHD-D000005` | `746583` | 1909-07-15 | `558075be7d1e63c9fea1a250` |

The shared HNDM identifier represents the serial container; the URL date parameters distinguish the requested issue. Automated retrieval of the HNDM interface returned HTTP 502 during this pass. PDHD therefore records the bridge as `repository_fulltext_link_resolved_interface_fetch_failed` and does not infer a page number, page image identifier or OCR availability.

This is useful because the selected pilot object `PDHD-D000003` can now be targeted through its underlying HNDM serial identity rather than searched again from scratch.

## Content lead inside PDHD-D000003

Peer-reviewed scholarship identifies Ponciano Rodríguez's article *El método en los libros de texto* in *La Enseñanza Primaria*, tomo I, núm. 11, dated 1 December 1901. The issue identity matches `PDHD-D000003`.

The scholarship also treats the magazine as a publication by and for teachers and places Rodríguez's textbook articles within its pedagogical program. The article is therefore a strong candidate for the pilot's instructional/source-criticism slots. However, the current research pass did not resolve its original page number in the 1901 issue.

The lead is consequently stored in `data/samples/pilot_content_leads.csv` with:

- `page_status=page_unresolved`;
- `promotion_status=not_eligible_for_fragment_locator`.

It must not be inserted into `fragment_locator_progress*.csv` until an original page or stable page-level locator is established.

## Integrity decision

`scripts/validate_object_aliases.py` validates document-to-alias crosswalks. `scripts/validate_content_leads.py` enforces the rule that a page-unresolved content lead cannot become eligible for fragment-locator promotion.

This preserves a three-stage retrieval chain:

`issue identity -> content lead -> page-level fragment locator`

None of those stages is silently collapsed into the next.
