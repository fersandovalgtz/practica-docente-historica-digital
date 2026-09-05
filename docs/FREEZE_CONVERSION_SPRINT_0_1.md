# PDHD-U1 freeze-conversion sprint 0.1

Reference cut: **2026-09-05**

## Objective

The current bottleneck is no longer source discovery. PDHD-U1 has reached **80/96 localized slots**, while only **15/96** have crossed the stronger fragment-freeze gate. This sprint therefore prioritizes conversion of already localized, direct-primary candidates into fixed coder spans.

No row is promoted merely to improve the frozen-fragment count.

`locator_found != fragment_frozen`

`direct_primary_access != fixed_boundary`

## Promotion rule

A candidate enters this sprint only when the existing locator infrastructure already points to the registered primary object or an equivalent first-party surrogate and the remaining blocker is principally page-image inspection, boundary selection, or preparation metadata.

Secondary page pointers, reproduced facsimiles awaiting primary cross-check, table-of-contents locators and unresolved bibliographic leads remain outside the conversion sprint even when they are historically promising.

The operational gate follows `LOCATOR_EVIDENCE_POLICY.md` and `FRAGMENT_FREEZE_PROTOCOL.md`: a direct-primary locator can become `frozen` only after exact boundaries, transcription status, access basis, public-text handling, selection role and reconstruction-quality preparation notes are fixed.

## Priority order

The machine-readable queue is `data/samples/freeze_conversion_queue_0_1.csv`.

### P1 — La Enseñanza Normal, inaugural issue

`PDHD-F000034` and `PDHD-F000036` share the directly exposed BVMC first-page image for the 15 September 1904 issue. Their remaining gate is visual boundary fixation for the professional/editorial region and the publication/subscription control region. One primary-page inspection can therefore potentially convert two slots.

### P2 — El Maestro, tomo II, núm. 3

`PDHD-F000050` and `PDHD-F000052` now share a direct primary-OCR anchor specific to the December issue opening rather than the earlier generic `/page/1` reader route. Internet Archive's full-text derivative shows the preceding number reaching printed p. 224; the next front matter opens *EL MAESTRO / Revista de Cultura Nacional*, names Enrique Monteverde and Agustín Loera y Chávez, gives the Gante 3 office/registration block and sumario, and is followed by the SEP/Talleres Gráficos imprint marked `MEXICO, DICIEMBRE DE 1921`.

This makes P2 the most tightly localized unresolved pair in the sprint. The remaining gate is no longer issue identification: it is mapping this post-p.224 OCR region to the corresponding scan leaf, visually checking the page image and fixing separate B and D boundaries. The registered chronology conflict remains explicit because primary OCR, while stronger than a secondary citation, is still below image-verified imprint evidence in PDHD's hierarchy.

### P3 — El Maestro, additional issue-opening controls

`PDHD-F000044` and `PDHD-F000048` already have stable direct reader targets for selected 1921 issues. They are control slots and require visual selection of the smallest defensible front-matter or administrative region.

### P4 — El esfuerzo educativo en México

`PDHD-F000060` points directly to Google Books page `PR5`. The page is reserved as a control candidate. It can be frozen only after direct inspection confirms the page-level boundary and the access/transcription decisions are recorded.

## Queue completeness and CI

`scripts/validate_freeze_conversion_queue.py` validates row-level integrity, queue completeness and retrieval-provenance coverage. The queue must equal the complete set of non-frozen locator rows whose canonical `boundary_status` belongs to the current direct-primary conversion states. An eligible fragment omitted from the queue, a stale row that is no longer eligible, a row already promoted to `frozen`, or a queue fragment without a structured entry in `retrieval_attempts.csv` causes CI to fail.

This turns the sprint from a manually curated reminder into a reproducible projection of the canonical locator shards. Priority remains a human source-critical decision, but eligibility and retrieval coverage are machine-checked.

At the current cut the complete direct-primary conversion set contains **seven fragments**: two P1, two P2, two P3 and one P4. All **7/7** now have structured retrieval provenance.

`scripts/prepare_freeze_review.py` provides the deterministic handoff from this queue to manual primary-page review. It copies stable IDs, source locators, priority and slot roles without pre-asserting verification: every new review record begins with `source_image_verified=no` and `decision=pending_primary_visual_review`. CI checks that all seven current candidates can be prepared reproducibly.

## Retrieval status at this cut

The source-access passes have not justified any new freeze promotion. This is an evidentiary result rather than a failed sprint: all direct-primary candidates have a documented recovery route and none has been promoted without the required visual gate.

For `PDHD-F000034` and `PDHD-F000036`, BVMC resolves the exact 15 September 1904 issue and the direct first-page image candidate. The exact issue PDF is also resolved, but its roughly 9.5 MB response cannot be rendered through the current automated research route. A UNAM scholarly facsimile independently reproduces the inaugural cover and first-page roster/programmatic matter, while BVMC's own catalog metadata confirms Alberto Correa's directorship, editorial/administrative roles, publication cadence and subscription conditions. This triangulation materially strengthens retrieval confidence but still does not satisfy the project's explicit `visible_reproduced_facsimile != primary_object_crosscheck` rule. The attempt remains `PDHD-RA000005`.

For `PDHD-F000050` and `PDHD-F000052`, `PDHD-RA000006` now records the exact post-p.224 OCR sequence described above. This supersedes the weaker generic reader-page route previously attached to the control slot and ties both P2 candidates to the same December issue opening. Internet Archive also exposes derivative links for OCR page index and page-number JSON, but those derivative downloads currently return cache misses in the research environment; the full PDF likewise redirects through a delivery host that cannot be opened here. The next defensible action therefore remains leaf mapping followed by direct visual inspection, not inference from OCR.

`PDHD-F000044` and `PDHD-F000048` have explicit retrieval attempts `PDHD-RA000007` and `PDHD-RA000008`. Peer-reviewed *Signos Históricos* independently links the exact Internet Archive reader targets to *El Maestro* núm. 2 and núm. 4 of 1921. This independently secures issue identity and reader routing, but the control spans remain unfrozen because a scholarly link to a reader leaf is not equivalent to visual inspection of that leaf.

`PDHD-F000060` is covered by `PDHD-RA000009`. Google Books resolves the selected 1928 volume and exposes `Title Page` as a selected-page route tied to `PR5`; its record identifies the University of California scan and the 1928 SEP publication. The page-specific route resolves, but the current environment returns cache misses for the plain-text and downloadable-PDF routes and does not expose an auditable page image. The title-page control therefore remains correctly at `locator_candidate`.

The same principle governs HNDM retrieval outside the seven-fragment conversion set. Resolving an issue and a sequential page identifier is useful provenance, but it does not count as visual inspection of the historical page when the viewer does not expose readable page content in the research environment.

## Excluded from fast promotion

High-value L3 and reproduced-facsimile candidates remain in their existing locator shards. Examples include page pointers for *La Enseñanza Primaria*, *El papel social del maestro rural*, *El sistema de escuelas rurales en México*, the 1934 SEP memory and reproduced pages of the 1923 mission project. They must first be checked against the registered primary object.

Likewise, HathiTrust section starts and Google Books table-of-contents entries remain pre-freeze until a concrete primary passage is identified.

## Success criterion

The immediate scientific target is not 84/96 localized. It is to increase the frozen count above **15/96** using only evidence that passes the existing promotion rules.

A successful conversion must produce or update a `frozen_fragments*.csv` row and, where appropriate, synchronize its locator shard, cohort status and README without weakening any rights, chronology or source-criticism constraint.

The first human calibration package remains downstream of fragment freezing. No annotation labels are introduced in this sprint.
