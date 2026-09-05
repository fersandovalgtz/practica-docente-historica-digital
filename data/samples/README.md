# Samples and pilot-preparation data

This directory stores **PDHD-owned pilot metadata and derived preparation records**. It does not serve as a mirror of third-party historical sources.

Current contents include the frozen 24-document pilot selection, deterministic annotation templates, content-discovery leads, locator-progress shards and frozen-fragment registries. These tables may refer to historical objects by stable identifier, page, structural boundary, access basis and preparation provenance even when the underlying source text cannot be redistributed.

Historical quotation, facsimile, page image or third-party OCR must not be added here unless its reuse status has been verified and recorded. When a source is handled as `metadata_only` or `coder_local_text`, the public repository stores only the rights-compatible locator and PDHD-derived methodological metadata.

## Evidence-promotion chain

`pilot_content_leads.csv` records content-level discoveries before or during page localization. A row marked `promoted_to_fragment_locator` must now carry an explicit `promoted_fragment_id`. `scripts/validate_content_leads.py` verifies that this ID exists in the logical union of `fragment_locator_progress*.csv`, belongs to the same pilot document and is not claimed by a second content lead.

This makes the promotion path auditable rather than implicit:

`issue identity -> content lead -> promoted_fragment_id -> page locator -> frozen fragment -> human annotation`

A content lead is not required for every locator: direct primary-page inspection, stable reader targets and other source-first routes may produce a locator without an earlier secondary discovery row. Conversely, a content lead cannot claim promotion unless a concrete locator row actually exists.

Locator and freeze work may be split into auditable shards such as `fragment_locator_progress*.csv` and `frozen_fragments*.csv`. Their logical union is validated by `scripts/validate_fragment_shards.py`; a fragment ID may occur only once across all shards. `fragment_gap_queue_0_1.csv` must remain the exact complement of the locator union.

## Freeze-conversion queue

`freeze_conversion_queue_0_1.csv` is a derived operational queue for localized fragments that already point to a direct primary object or equivalent first-party surrogate and are close to the `frozen` gate. It does not create a new fragment state and it is not part of the logical locator union.

The queue records the remaining conversion blocker and the next source-critical action. Inclusion therefore means **priority for verification**, not evidentiary promotion. Rows remain governed by their canonical `fragment_locator_progress*.csv` state until direct inspection, exact boundary selection, transcription/access decisions and the other requirements of `docs/FRAGMENT_FREEZE_PROTOCOL.md` are complete.

The current sprint is documented in `docs/FREEZE_CONVERSION_SPRINT_0_1.md`.

The distinction is intentional:

`content_found != page_localized`

`promoted_content_lead != frozen_fragment`

`freeze_conversion_priority != frozen_fragment`

`public_pilot_metadata != public_source_text`

`frozen_fragment != republished_fragment_text`
