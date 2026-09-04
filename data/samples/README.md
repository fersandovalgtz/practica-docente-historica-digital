# Samples and pilot-preparation data

This directory stores **PDHD-owned pilot metadata and derived preparation records**. It does not serve as a mirror of third-party historical sources.

Current contents include the frozen 24-document pilot selection, deterministic annotation templates, locator-progress shards and frozen-fragment registries. These tables may refer to historical objects by stable identifier, page, structural boundary, access basis and preparation provenance even when the underlying source text cannot be redistributed.

Historical quotation, facsimile, page image or third-party OCR must not be added here unless its reuse status has been verified and recorded. When a source is handled as `metadata_only` or `coder_local_text`, the public repository stores only the rights-compatible locator and PDHD-derived methodological metadata.

Locator and freeze work may be split into auditable shards such as `fragment_locator_progress*.csv` and `frozen_fragments*.csv`. Their logical union is validated by `scripts/validate_fragment_shards.py`; a fragment ID may occur only once across all shards.

The distinction is intentional:

`public_pilot_metadata != public_source_text`

`frozen_fragment != republished_fragment_text`
