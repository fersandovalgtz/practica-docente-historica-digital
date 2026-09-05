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

The distinction is intentional:

`content_found != page_localized`

`promoted_content_lead != frozen_fragment`

`public_pilot_metadata != public_source_text`

`frozen_fragment != republished_fragment_text`
