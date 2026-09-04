# Provenance model

PDHD treats provenance as a first-class research object.

## Chain of custody

```text
institution / collection
        ↓
source record
        ↓
document identity
        ↓
locator or asset reference
        ↓
processing event
        ↓
fragment
        ↓
annotation
        ↓
human validation
        ↓
analytical output
```

Each public analytical record should be traceable back to a document identifier and a locator sufficient for a researcher to inspect the source within the rights constraints of the provider.

## Required distinctions

- `source_id` identifies the institutional or collection-level source.
- `document_id` identifies a bibliographic/documentary object within PDHD.
- `fragment_id` identifies an analytical passage or unit.
- `source_url` points to the institutional source when available.
- `accessed_at` records the date on which volatile web metadata or terms were checked.
- `rights_status` records the operational reuse class.
- `validation_status` records whether an annotation has been reviewed by a human.

## Processing provenance

When OCR or automated extraction is performed locally, PDHD should record tool name, version, date, relevant parameters and a checksum of any locally retained input or output when legally permissible. Public release of those outputs remains governed by `RIGHTS.md`.
