# Security policy

PDHD contains public research infrastructure, metadata, scripts and workflows. Security reports are handled separately from ordinary data corrections.

## Supported state

Security fixes target the current `main` branch and the latest tagged release when one exists. Historical research snapshots remain immutable records; a security correction to current tooling does not rewrite the scientific claims attached to an earlier snapshot.

## Report privately

Do **not** open a public issue for:

- exposed credentials, tokens or private keys;
- a workflow path that could execute untrusted code with write privileges;
- a dependency or action compromise affecting repository integrity;
- a vulnerability that could expose non-public local source material or coder files;
- a method for bypassing the human/machine lifecycle gates in a way that could corrupt validated research outputs.

Use GitHub private vulnerability reporting or a private security advisory when that option is available for the repository. If it is not available, contact the repository maintainer privately through the maintainer's GitHub profile or institutional contact channel.

## Public issues are appropriate for

- broken public links;
- metadata or chronology corrections;
- reproducibility defects that do not expose secrets;
- validation-script bugs without an active exploit path;
- documentation errors.

## Secrets and sensitive research material

No credentials, private correspondence, unpublished coder identities, restricted source facsimiles or non-redistributable working copies belong in Git history. Local working material must remain outside public commits unless its rights and privacy basis are explicit.

## Workflow security posture

Active third-party GitHub Actions are pinned to immutable commit SHAs and maintained through Dependabot. Workflows use least-privilege `GITHUB_TOKEN` permissions. `pull_request_target` is prohibited by the repository hygiene validator unless a future, separately reviewed security design explicitly justifies it.

## Scientific integrity is part of security

For PDHD, integrity includes protection against provenance corruption. Machine candidates cannot become human validation or gold labels through automation, and phase 5 remains gated by explicit human-validation conditions.
