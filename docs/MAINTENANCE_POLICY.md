# Repository maintenance policy

This policy defines the operational controls that keep PDHD reproducible and reviewable between scientific releases.

## Protected development model

`main` is the canonical integration branch and should be protected in GitHub settings. Scientific or infrastructure changes should arrive through pull requests after the `Validate PDHD` workflow succeeds. Direct pushes to `main` should be disallowed except for explicitly documented emergency recovery.

Recommended branch protection / ruleset settings:

- require a pull request before merging;
- require the `integrity` job from `Validate PDHD` to pass;
- require branches to be up to date before merge when GitHub can evaluate the check deterministically;
- block force pushes and branch deletion;
- require conversation resolution;
- require CODEOWNERS review when a second qualified maintainer is available;
- do not permit bypass for ordinary maintenance.

## Dependency and GitHub Actions policy

Active third-party Actions must be referenced by immutable 40-character commit SHA. A trailing comment records the human-readable major version. Dependabot checks GitHub Actions weekly; update PRs must pass the complete repository suite before merge.

A major-version upgrade should be inspected for runtime changes, permission changes and deprecations before the pin is advanced.

## Least privilege

Every workflow declares explicit `permissions`. Read-only jobs should use `contents: read`. Deployment workflows receive only the additional permissions they require. `pull_request_target` is prohibited unless a separately reviewed threat model demonstrates why it is necessary.

## Release posture

PDHD remains `0.1.0-dev` until the release gates in the scientific plan are satisfied. A final release must not be inferred from documentary completeness alone.

Before a release:

1. run all canonical validators from a clean checkout;
2. confirm the snapshot, version, CITATION.cff and CodeMeta agree;
3. verify rights and public-redistribution surfaces;
4. verify human/machine/gold lifecycle separation;
5. confirm formal reliability and adjudication status when the release claims semantic validation;
6. create a reproducible tagged state and preserve the associated CI run;
7. record substantive changes in `CHANGELOG.md`.

## Branch retirement

Historical branches are retired only after determining whether they contain unique source-recovery or provenance evidence. Naming convention alone is never sufficient evidence that a branch is safe to delete.

Use three dispositions:

- merged/superseded → retire;
- obsolete and scientifically abandoned → document abandonment, then retire;
- unique recovery/provenance evidence → preserve until promoted or explicitly abandoned.

## Source-link observability

The scheduled link audit is non-blocking. Network state is operational evidence, not historical-source existence evidence. Repeated failures may trigger a recovery issue but do not silently alter catalog identity.

## Dashboard publication

The public dashboard consumes descriptive metadata only. Semantic human labels, machine candidates and future gold outputs must not enter the dashboard unless a separately reviewed publication design explicitly introduces them and preserves epistemic labels.

## Machine experiments

Machine runs require leakage-safe inputs, registered model provenance and immutable prompt/input hashes. Machine output remains `machine_candidate`; it cannot satisfy calibration, reliability, adjudication or phase-5 gold gates.

## Annual / milestone maintenance

At major project milestones, audit:

- branch protection/rulesets;
- Action pins and Dependabot health;
- stale branches;
- rights registries and source terms;
- link-audit trends;
- schema/documentation alignment;
- metadata standards and citation files;
- whether archived workflows remain clearly non-executable;
- whether any new public artifact leaks restricted or semantic data.
