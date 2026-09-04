# Locator evidence policy

## Purpose

PDHD distinguishes the strength of evidence used to locate a candidate fragment from the later act of freezing the exact coder span. A page number found in a secondary study can be extremely useful for discovery, but it is not equivalent to direct inspection of the primary digital object.

This policy prevents source-location convenience from being confused with evidentiary finality.

## Evidence hierarchy

### L1 — direct primary passage

The primary digital object exposes the relevant page and enough text or image context to identify the passage itself.

Typical examples:

- a Google Books page/snippet tied to a specific page;
- an HNDM page image or page-level locator;
- a repository PDF page inspected directly;
- a stable facsimile page in a library platform.

An L1 locator may proceed to exact boundary selection, subject to rights handling and transcription checks.

### L2 — direct primary section or table-of-contents locator

The primary object exposes a section title and starting page, but the exact passage has not yet been selected.

Examples include Google Books contents entries such as `Departamento de Supervisión — 335` or an institutional catalog identifying the start of a named section.

L2 supports a `locator_candidate`. It does **not** support `frozen` status by itself.

### Reproduced-facsimile rule

A scholarly thesis, article or institutional publication may reproduce a visible facsimile page of the historical object. This is stronger than a bare page citation because the historical page itself can be inspected, but the reproduction is still being accessed through a secondary container rather than through PDHD's registered primary object.

Such rows use `embedded_facsimile_primary_check_pending`. They may support a highly targeted locator candidate and provisional boundary planning, but they do not become `frozen` until the page is cross-checked against the registered primary object or an equivalent first-party digital surrogate.

Therefore:

`visible_reproduced_facsimile != primary_object_crosscheck`

### L3 — scholarly page pointer to the primary object

A peer-reviewed or high-quality scholarly source cites a specific page or page range in the historical primary source, while PDHD has not yet inspected that page in the primary digital object.

L3 is useful for targeted retrieval and may be stored in the locator queue, but it must be labeled `secondary_page_pointer_primary_check_pending` or an equivalent explicit state.

L3 can never be promoted directly to a fixed coder span. The primary page must first be checked.

### L4 — bibliographic lead only

The source or issue is known to exist, but no page-level or section-level pointer has been resolved.

L4 belongs in source discovery or issue-lead infrastructure, not in the fixed-fragment manifest.

## Promotion rules

`L4 -> L3` when scholarship or a catalog yields a page/section pointer.

`L3 -> L2/L1` only after the primary object is inspected.

`embedded_facsimile_primary_check_pending -> L1` only after cross-checking the reproduced page against the registered primary object or equivalent first-party surrogate.

`L2 -> L1` when a concrete passage is identified in the primary object.

`L1 -> frozen` only after exact boundaries, transcription status, rights handling and fragment role are fixed.

Therefore:

`secondary_page_citation != primary_page_inspection`

`table_of_contents_entry != passage`

`page_locator_resolved != fixed_coder_span`

`fixed_coder_span != validated_annotation`

## Public repository rule

The public locator table may store page numbers, section names, bibliographic pointers and analytical preparation notes. It should not store long source text unless redistribution is clearly permitted.

When source text cannot be publicly committed, the frozen record may retain only the stable locator plus a controlled coder-local text package whose checksum or version identifier is documented separately.

## Current application

The current pilot queue contains examples of all useful pre-freeze states:

- direct Google Books page-level passages for *Las misiones culturales, 1932-1933*;
- direct Google Books section starts for the 1932 and 1938 SEP memories;
- HathiTrust section/page candidates for *Las misiones culturales en 1927*;
- reproduced facsimile pages of the 1923 *Proyecto para la organización de las misiones federales de educación* embedded in a UNAM thesis, pending cross-check against HathiTrust;
- scholarly page pointers into *El sistema de escuelas rurales en México* and the 1934 SEP memory that remain explicitly pending primary-page verification.

No locator is treated as a human-coded historical claim merely because it has a page number.
