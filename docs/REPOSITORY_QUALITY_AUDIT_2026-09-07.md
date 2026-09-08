# Repository quality audit — 7 September 2026

**Repository:** `fersandovalgtz/practica-docente-historica-digital`  
**Baseline audited:** `46f5016ce60c6ba52cf00ebd6b74a5864bfc8136`  
**Scientific state at baseline:** PDHD-U1 documentary pilot 96/96 frozen; 12 calibration items fixed; 84 reliability-reserve items fixed; 0 human-coded fragments; 0 gold labels.

## Audit objective

Assess whether the repository is technically reproducible, scientifically unambiguous, reusable by third parties and resistant to accidental contamination between documentary evidence, human validation and experimental machine annotation.

## Overall assessment

The repository already has unusually strong provenance and CI for a research prototype. The principal weaknesses are not missing data; they are **interface clarity, lifecycle separation and operational hygiene**. The most important correction is to separate the structural frozen-fragment schema from semantic annotation. Additional work in this audit adds a public descriptive dashboard, a data dictionary, scheduled link observability, an explicitly gated phase-5 pipeline and a machine-candidate layer that cannot masquerade as human validation.

## Findings and disposition

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| Q01 | High | `pedagogical_fragment.schema.json` mixed frozen-fragment structure with semantic fields (`dimension`, `normativity`, `validation_status`) and its normativity vocabulary lagged behind current validators. | **Fixed.** Fragment schema is structural only; semantic human annotation has its own schema. |
| Q02 | High | No formal schema/lifecycle contract separated model-generated annotations from human annotations/gold labels. | **Fixed.** Added `machine_candidate.schema.json`, run registry/protocol and validator that rejects human/gold fields. |
| Q03 | Medium | Public users had to reconstruct project status from README/CSVs; no descriptive front end existed. | **Fixed.** Added static dashboard driven only by canonical metadata and pre-validation snapshot. |
| Q04 | Medium | Five one-off source-retrieval workflows remained under `.github/workflows` after the pilot reached 96/96 frozen, increasing Actions clutter and accidental-run risk. | **Fixed.** Moved to `archive/workflows/` as historical provenance; canonical CI remains active. |
| Q05 | Medium | Source URLs had no periodic observability layer; link failure could be confused with source non-existence. | **Fixed.** Added scheduled/manual non-blocking link audit with separate URL-state and source-existence semantics. |
| Q06 | Medium | Phase 5 was conceptually planned but had no executable gold-set gate or defined output contract. | **Fixed.** Added gated analysis pipeline with descriptive tables, document-cluster bootstrap intervals and SVG outputs; current state must remain blocked. |
| Q07 | Medium | Reuse required reading scripts to infer field semantics. | **Fixed.** Added comprehensive data dictionary and schema guide. |
| Q08 | Medium | Active workflow actions use major-version tags rather than immutable commit-SHA pins. | **Residual.** This is maintainable but weaker supply-chain hardening. Pinning should be done in a dedicated dependency-maintenance PR with scheduled updates. |
| Q09 | Low | Repository has 61 visible branches at audit time, 60 of them non-`main`, mostly historical freeze/recovery branches. | **Residual.** Do not delete blindly: branch deletion is not available through the current safe connector and some refs preserve recovery history. Cleanup should be done after merged/unmerged verification. |
| Q10 | Low | README is comprehensive but long, making it a poor sole entry point for external audiences. | **Mitigated.** Dashboard becomes the visual front door; README remains the detailed research narrative. |
| Q11 | Low | GitHub Pages deployment depends on repository Pages being configured to use GitHub Actions. | **Operational check after merge.** Deployment workflow is included; if repository settings do not already allow Actions as Pages source, one settings change will still be required. |

## Scientific integrity checks preserved

This audit does **not** alter the 24 selected documents, the 96 fixed fragments, calibration membership, reliability-reserve membership, codebook baseline or any historical source boundary. It creates no human annotations and no gold labels.

The new machine layer is intentionally subordinate to the human-validation boundary. A model run may be useful for prompt/model stability experiments, but machine output cannot:

- satisfy calibration;
- freeze the independent-round codebook;
- satisfy formal inter-coder reliability;
- populate the validated gold set;
- change `human_coded_fragments` or `gold_labels` in the scientific snapshot;
- justify removing the `-dev` suffix from the project version.

## Repository architecture after remediation

```text
catalog/source identity + rights
        ↓
object/document identity
        ↓
locator + exact fragment boundary
        ↓
frozen structural fragment (96)
        ├── human calibration → frozen codebook → reliability → adjudicated gold
        └── machine_candidate experiments (strictly separate; never gold)
        ↓
phase-5 analysis only after validated gold gate
```

## Link-audit interpretation

HTTP/network status is treated as evidence about a **URL**, not proof about historical existence. A `404`/`410` becomes `url_not_found`; it does not become `source_nonexistent`. When the corresponding `source_id` or `document_id` remains catalogued, the report explicitly labels the historical/source entity as `catalogued`. Timeouts, 429s, 5xx and DNS/TLS errors are transient/network classes and never scientific absence claims.

## Phase-5 statistical boundary

Future outputs are descriptive and historically scoped. Because four fragments can derive from one document, the pipeline must not pretend fragment rows are fully independent observations. It therefore reports raw fragment counts/proportions and deterministic **document-cluster bootstrap** intervals. Any later inferential model beyond these descriptive outputs requires an explicit, versioned analysis-plan amendment.

## Branch hygiene recommendation

After this audit is merged, perform a separate branch-retirement pass with three buckets:

1. merged and superseded → delete;
2. unmerged but scientifically obsolete → archive decision in an issue, then delete;
3. unmerged and containing unique recovery evidence → preserve until evidence is promoted or explicitly abandoned.

The branch pass should never infer “safe to delete” from naming alone.

## Release posture

PDHD remains `0.1.0-dev`. The repository is suitable for public demonstration, methods/data-paper preparation and machine-candidate experimentation, but final `v0.1.0` remains gated by human semantic validation and formal reliability as defined in the master plan.
