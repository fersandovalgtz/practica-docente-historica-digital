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

`scripts/validate_freeze_conversion_queue.py` requires the queue to equal the complete current set of eligible non-frozen direct-primary candidates. It also requires every queued fragment to have structured retrieval provenance in `retrieval_attempts.csv`. A source-access failure is therefore retained as evidence about the retrieval process instead of disappearing from the research record or being misread as source absence.

## Manual primary-page review bridge

`scripts/prepare_freeze_review.py` projects the canonical queue and locator metadata into a deterministic review sheet for primary-page inspection. It can prepare the complete queue or selected fragment IDs without changing any scientific state.

New review records deliberately begin with `source_image_verified=no` and `decision=pending_primary_visual_review`. Boundary definition, transcription status and access basis remain blank for the reviewer to complete from the actual primary object. The script refuses already frozen fragments and queue/locator identity mismatches. Its `--check` mode is executed in CI.

This separates mechanical metadata transfer from the source-critical decision:

`direct-primary candidate -> structured retrieval provenance -> manual primary-page review -> fixed boundary -> frozen registry`

A completed review sheet is not itself a freeze operation. Promotion still requires synchronized updates to the canonical locator shard and a `frozen_fragments*.csv` registry row that passes repository validation.

The current sprint is documented in `docs/FREEZE_CONVERSION_SPRINT_0_1.md`.

The distinction is intentional:

`content_found != page_localized`

`promoted_content_lead != frozen_fragment`

`freeze_conversion_priority != frozen_fragment`

`prepared_review_record != primary_image_verified`

`primary_image_verified != validated_annotation`

`public_pilot_metadata != public_source_text`

`frozen_fragment != republished_fragment_text`
