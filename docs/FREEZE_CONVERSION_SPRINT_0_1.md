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

`PDHD-F000050` and `PDHD-F000052` share the Internet Archive primary object. The professional/editorial target is already narrowed by direct primary OCR, while the control target has a stable reader-page locator. Both require page-image verification and exact structural boundaries. The registered chronology conflict must remain explicit; freezing a span does not authorize silent normalization of the object's date.

### P3 — El Maestro, additional issue-opening controls

`PDHD-F000044` and `PDHD-F000048` already have stable direct reader targets for selected 1921 issues. They are control slots and require visual selection of the smallest defensible front-matter or administrative region.

### P4 — El esfuerzo educativo en México

`PDHD-F000060` points directly to Google Books page `PR5`. The page is reserved as a control candidate. It can be frozen only after direct inspection confirms the page-level boundary and the access/transcription decisions are recorded.

## Excluded from fast promotion

High-value L3 and reproduced-facsimile candidates remain in their existing locator shards. Examples include page pointers for *La Enseñanza Primaria*, *El papel social del maestro rural*, *El sistema de escuelas rurales en México*, the 1934 SEP memory and reproduced pages of the 1923 mission project. They must first be checked against the registered primary object.

Likewise, HathiTrust section starts and Google Books table-of-contents entries remain pre-freeze until a concrete primary passage is identified.

## Success criterion

The immediate scientific target is not 84/96 localized. It is to increase the frozen count above **15/96** using only evidence that passes the existing promotion rules.

A successful conversion must produce or update a `frozen_fragments*.csv` row and, where appropriate, synchronize its locator shard, cohort status and README without weakening any rights, chronology or source-criticism constraint.

The first human calibration package remains downstream of fragment freezing. No annotation labels are introduced in this sprint.
