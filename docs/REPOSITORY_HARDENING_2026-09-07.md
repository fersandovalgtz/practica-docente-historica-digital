# Repository hardening report — 7 September 2026

## Scope

This hardening pass raises PDHD's operational governance and software-supply-chain controls without changing the scientific corpus, pilot membership, frozen fragment boundaries, calibration membership, reliability reserve, codebook baseline, human-coded count or gold-label count.

## Controls added

- immutable commit-SHA pinning for every active third-party GitHub Action;
- upgrade from `actions/setup-python` v5 to v6 to leave the deprecated Node 20 runtime path;
- weekly Dependabot monitoring for GitHub Actions;
- CODEOWNERS for repository-wide and evidence-critical surfaces;
- contribution, security and code-of-conduct policies;
- structured technical-defect, documentary-correction and source-access issue forms;
- pull-request checklist with explicit scientific, rights, privacy and reproducibility boundaries;
- normalized LF line endings for text/data/code files;
- formal maintenance/release policy;
- executable repository-hygiene validator integrated into canonical CI.

## Automated anti-regression rules

`python scripts/validate_repository_hygiene.py` now rejects:

- missing governance/community files;
- mutable third-party Action refs such as `@v6` instead of a 40-character SHA;
- `pull_request_target` in active workflows;
- `permissions: write-all`;
- missing weekly GitHub Actions Dependabot coverage;
- incomplete critical CODEOWNERS patterns;
- loss of key human/machine/rights/provenance governance language.

## Scientific state preserved

- 24 pilot documents;
- 96/96 localized;
- 96/96 frozen;
- 12 calibration fragments;
- 84 reliability-reserve fragments;
- 0 human-coded fragments;
- formal reliability not started;
- 0 gold labels;
- machine input gate remains 12 leakage-safe + 84 blocked;
- phase 5 remains closed.

## Administrative residual

At the start of this hardening pass GitHub reported `main` as **unprotected**. The connected repository API available in this session can audit but cannot modify branch-protection/ruleset administration.

The recommended settings are encoded in `docs/MAINTENANCE_POLICY.md`: require pull requests, require the `integrity` status check, block force pushes/deletion and require conversation resolution. This is now the principal repository-level control that still requires a GitHub Settings change outside the versioned contents.

GitHub Pages likewise requires the repository Pages source to be enabled for GitHub Actions before the prepared dashboard deployment workflow can publish successfully.
