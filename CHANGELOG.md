# Changelog

All notable changes to PDHD are documented here.

## [Unreleased] — pre-validation state - 2026-09-07

### Added

- Completed the documentary pilot at **96/96 localized** and **96/96 frozen** across 24 selected documents.
- Versioned pilot substitution `PDHD-PS000004`: position 21 moves from inaccessible-for-primary-review 1932 `PDHD-D000072` to directly inspected 1926 `PDHD-D000078`; freezes `PDHD-F000081`–`PDHD-F000084` and completes the pilot at 96/96 frozen.
- Versioned pilot substitution `PDHD-PS000003`: position 23 moves from inaccessible-for-primary-review 1937 `PDHD-D000074` to directly inspected 1939 `PDHD-D000077`; freezes `PDHD-F000089`–`PDHD-F000092` and advances the pilot to 92/96 frozen at that historical step.
- Deterministic 12-fragment human-calibration package under `PDHD-CAL-0.1-20260907`, with a blind coder sheet and `PDHD-CB-0.2-calibration` pinned as the exact pre-calibration codebook baseline.
- Safe coder-copy generation and validation utilities that prepare and check real future human sheets without generating labels.
- Pre-registered 84-fragment reliability reserve `PDHD-RR-0.1-20260907`, defined as the exact complement of the 12 calibration fragments within the frozen 96.
- Pre-label analysis plan in `docs/ANALYSIS_PLAN_0_1.md`, fixing inference limits, document-level dependence, missing-data rules and exploratory/confirmatory distinctions before any human labels exist.
- Human-gated formal reliability generator that remains blocked until exactly one codebook is registered as `frozen_for_independent_reliability` and its Git blob hashes verify.
- Non-adjudicating calibration disagreement comparator for future valid human first-pass sheets.
- Canonical pre-validation snapshot `PDHD-U1-PREVALIDATION-0.1-20260907`, pinning commit `513d64ee6b8ba053ceed0f204bc1419f37954365`, Git tree `21d5ac4245d52254ae0cbd14828386f01d5d0842` and successful CI run #296.
- `docs/DATASET_CARD_0_1.md` documenting intended uses, unsupported claims, rights constraints, coverage limitations and the distinction between documentary completion and semantic validation.
- `codemeta.json` for interoperable FAIR software metadata.
- Executable metadata consistency validation tying `VERSION`, `CITATION.cff`, CodeMeta, the pre-validation snapshot and the canonical 96/12/84 state together.

### State

- Project version remains **`0.1.0-dev`**. The final `v0.1.0` criterion is intentionally not claimed because human semantic validation and formal inter-coder reliability have not occurred.
- Human-coded fragments: **0**.
- Formal reliability round: **not started**.
- Gold labels: **0**.

## [0.1.0-dev] - 2026-09-05

### Added

- Deterministic 24-document / 96-fragment reliability pilot with auditable locator and frozen-fragment shards.
- Exact-page and primary-OCR locator evidence for the active pilot, including `PDHD-F000027` and `PDHD-F000050`.
- Exact secondary page localization of `PDHD-F000003` in *El Periquito*, núm. 4, 6 November 1870, p. 2, supported by a Biblioteca Nacional de México scholarly monograph.
- Explicit chronology-conflict registry preserving unresolved publication-date discrepancies instead of silently normalizing them.
- `scripts/validate_status_counts.py` to make fragment CSVs the source of truth for public pilot counts.
- CI enforcement that README and `docs/PDHD_U1_COHORT_STATUS.md` remain synchronized with locator, frozen and gap-queue data.
- Explicit `promoted_fragment_id` crosswalks in `pilot_content_leads.csv`, including the newly registered Gregorio Torres Quintero lead for `PDHD-F000027` and the *El Periquito* lead for `PDHD-F000003`.
- CI validation that every promoted content lead resolves to an existing locator fragment in the same pilot document and that no two leads claim the same promoted fragment.
- `data/samples/retrieval_attempts.csv` for structured provenance of primary-source access attempts that remain blocked or incomplete.
- `scripts/validate_retrieval_attempts.py` and CI enforcement of retrieval-attempt IDs, document/fragment relationships, object URLs, blocker states and next recovery routes.

### Changed

- At the 2026-09-05 development cut, PDHD-U1 public status stood at **79/96 localized**, **15/96 frozen** and **17/96 unlocated**. This entry is retained as historical development provenance rather than rewritten to the later 96/96 state.
- README and cohort-status documentation now distinguish primary OCR retrieval evidence from image-verified fixed spans.
- The evidence-promotion chain is now explicit: `issue identity -> content lead -> promoted_fragment_id -> page locator -> frozen fragment -> human annotation`.
- High-value unresolved routes were refined for the 37-page HNDM issue of *Revista de la Instrucción Pública Mexicana* (15 March 1896), the exact BVMC PDF of *La Enseñanza Moderna* (1 July 1907), HathiTrust item `txu.059173025410517` for *El papel social del maestro rural*, and the HNDM bound-volume route for *El Periquito*.
- The stale `PDHD-PL000001` state was corrected: *El método en los libros de texto* is page-resolved at pp. 167–168 and explicitly promoted to `PDHD-F000025` rather than remaining incorrectly marked `page_unresolved`.
- Negative access results are now retained as reproducible retrieval provenance rather than being lost or treated as page evidence.
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
