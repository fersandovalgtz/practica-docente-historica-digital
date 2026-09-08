#!/usr/bin/env python3
"""Validate repository-level governance and supply-chain hygiene.

This script is intentionally standard-library only so it can run in the same
minimal CI environment as the scientific validators.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"

REQUIRED_FILES = [
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "GOVERNANCE.md",
    "docs/MAINTENANCE_POLICY.md",
    ".github/CODEOWNERS",
    ".github/dependabot.yml",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/data_correction.yml",
    ".github/ISSUE_TEMPLATE/source_access.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
]

ACTION_LINE = re.compile(
    r"^\s*uses:\s*([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@([^\s#]+)(?:\s+#.*)?$"
)
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")


def fail(message: str) -> None:
    raise SystemExit(f"repository hygiene failure: {message}")


def check_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing required community/governance files: " + ", ".join(missing))


def check_action_pins() -> int:
    if not WORKFLOWS.is_dir():
        fail(".github/workflows is missing")

    pins = 0
    for workflow in sorted(list(WORKFLOWS.glob("*.yml")) + list(WORKFLOWS.glob("*.yaml"))):
        text = workflow.read_text(encoding="utf-8")
        if "pull_request_target:" in text:
            fail(f"{workflow.relative_to(ROOT)} uses prohibited pull_request_target")
        if re.search(r"(?m)^\s*permissions:\s*write-all\s*$", text):
            fail(f"{workflow.relative_to(ROOT)} grants write-all permissions")
        if "\t" in text:
            fail(f"{workflow.relative_to(ROOT)} contains tab characters")

        for lineno, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if not stripped.startswith("uses:"):
                continue
            if stripped.startswith("uses: ./"):
                continue
            match = ACTION_LINE.match(line)
            if not match:
                fail(f"{workflow.relative_to(ROOT)}:{lineno} has an unparsable external action reference")
            action, ref = match.groups()
            if not FULL_SHA.fullmatch(ref):
                fail(
                    f"{workflow.relative_to(ROOT)}:{lineno} must pin {action} to an immutable 40-char SHA, got {ref!r}"
                )
            pins += 1

    if pins == 0:
        fail("no external GitHub Action pins were found")
    return pins


def check_dependabot() -> None:
    text = (ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8")
    if not re.search(r"package-ecosystem:\s*[\"']?github-actions[\"']?", text):
        fail("Dependabot does not monitor github-actions")
    if not re.search(r"interval:\s*[\"']?weekly[\"']?", text):
        fail("GitHub Actions Dependabot cadence is not weekly")


def check_codeowners() -> None:
    text = (ROOT / ".github" / "CODEOWNERS").read_text(encoding="utf-8")
    required_patterns = ["* @fersandovalgtz", "/data/", "/schemas/", "/.github/workflows/"]
    missing = [pattern for pattern in required_patterns if pattern not in text]
    if missing:
        fail("CODEOWNERS missing critical ownership patterns: " + ", ".join(missing))


def check_scientific_governance() -> None:
    governance = (ROOT / "GOVERNANCE.md").read_text(encoding="utf-8").lower()
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8").lower()
    maintenance = (ROOT / "docs" / "MAINTENANCE_POLICY.md").read_text(encoding="utf-8").lower()

    for token in ["human validation", "machine", "rights", "provenance"]:
        if token not in governance:
            fail(f"GOVERNANCE.md no longer states the {token!r} control")

    for token in ["machine_candidate", "pull request", "rights"]:
        if token not in contributing:
            fail(f"CONTRIBUTING.md missing {token!r} contribution guardrail")

    for token in ["protected", "dependabot", "immutable", "least privilege"]:
        if token not in maintenance:
            fail(f"MAINTENANCE_POLICY.md missing {token!r} maintenance control")


def main() -> int:
    check_required_files()
    pins = check_action_pins()
    check_dependabot()
    check_codeowners()
    check_scientific_governance()
    print(f"PDHD repository hygiene checks passed ({pins} immutable external action pins)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
