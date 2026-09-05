# Changelog

All notable changes to PDHD are documented here.

## [0.1.0-dev] - 2026-09-05

### Added

- Deterministic 24-document / 96-fragment reliability pilot with auditable locator and frozen-fragment shards.
- Exact-page and primary-OCR locator evidence for the active pilot, including `PDHD-F000027` and `PDHD-F000050`.
- Explicit chronology-conflict registry preserving unresolved publication-date discrepancies instead of silently normalizing them.
- `scripts/validate_status_counts.py` to make fragment CSVs the source of truth for public pilot counts.
- CI enforcement that README and `docs/PDHD_U1_COHORT_STATUS.md` remain synchronized with locator, frozen and gap-queue data.

### Changed

- PDHD-U1 public status advanced to **78/96 localized**, **15/96 frozen** and **18/96 unlocated**.
- README and cohort-status documentation now distinguish primary OCR retrieval evidence from image-verified fixed spans.
- High-value unresolved routes were refined for the 37-page HNDM issue of *Revista de la Instrucción Pública Mexicana* (15 March 1896), the exact BVMC PDF of *La Enseñanza Moderna* (1 July 1907), and HathiTrust item `txu.059173025410517` for *El papel social del maestro rural*.
- The project continues to prioritize stronger frozen-fragment evidence over reaching localization thresholds with weak secondary references.

## [0.1.0-dev] - 2026-09-03

### Added

- Initial scientific scope and research question.
- PDHD-U1 concept: *Genealogía documental de la práctica docente mexicana*.
- Rights-first architecture for HNDM, UNAM and SEP source families.
- Documentary, fragment and annotation data model.
- Pedagogical dimensions and pedagogical-act taxonomies.
- Source, rights and annotation protocols.
- JSON Schemas and repository validation script.
- GitHub Actions quality-control workflow.
