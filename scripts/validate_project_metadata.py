#!/usr/bin/env python3
"""Validate PDHD project/research metadata against canonical repository state."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data" / "samples"
SNAPSHOT = ROOT / "data" / "snapshots" / "prevalidation_snapshot_0_1.json"
CODEMETA = ROOT / "codemeta.json"
CITATION = ROOT / "CITATION.cff"
VERSION = ROOT / "VERSION"
DATASET_CARD = ROOT / "docs" / "DATASET_CARD_0_1.md"
HEX40 = re.compile(r"^[0-9a-f]{40}$")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def cff_scalar(text: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*[\"']?([^\n\"']+)[\"']?\s*$", text)
    if not match:
        raise RuntimeError(f"CITATION.cff missing scalar: {key}")
    return match.group(1).strip()


def frozen_ids() -> set[str]:
    result: set[str] = set()
    for path in sorted(SAMPLES.glob("frozen_fragments*.csv")):
        for row in read_csv(path):
            fid = row["fragment_id"]
            if fid in result:
                raise RuntimeError(f"duplicate frozen fragment across shards: {fid}")
            result.add(fid)
    return result


def validate() -> list[str]:
    errors: list[str] = []
    version = VERSION.read_text(encoding="utf-8").strip()
    citation_text = CITATION.read_text(encoding="utf-8")
    citation_version = cff_scalar(citation_text, "version")
    citation_repo = cff_scalar(citation_text, "repository-code")
    citation_license = cff_scalar(citation_text, "license")
    orcid_match = re.search(r'(?m)^\s*orcid:\s*"?([^"\n]+)"?\s*$', citation_text)
    citation_orcid = orcid_match.group(1).strip() if orcid_match else ""

    codemeta = json.loads(CODEMETA.read_text(encoding="utf-8"))
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))

    if citation_version != version:
        errors.append(f"VERSION/CITATION mismatch: {version!r} vs {citation_version!r}")
    if codemeta.get("version") != version:
        errors.append("CodeMeta version does not match VERSION")
    if codemeta.get("codeRepository") != citation_repo:
        errors.append("CodeMeta repository does not match CITATION.cff")
    if citation_license != "Apache-2.0":
        errors.append("CITATION.cff software license must remain Apache-2.0")
    if codemeta.get("license") != "https://spdx.org/licenses/Apache-2.0":
        errors.append("CodeMeta software license is not the expected Apache-2.0 SPDX URL")

    authors = codemeta.get("author") or []
    codemeta_orcids = {a.get("@id") for a in authors if isinstance(a, dict)}
    if not citation_orcid or citation_orcid not in codemeta_orcids:
        errors.append("CodeMeta author ORCID does not match CITATION.cff")

    if snapshot.get("project_version") != version:
        errors.append("snapshot project_version does not match VERSION")
    if not HEX40.fullmatch(str(snapshot.get("commit_sha", ""))):
        errors.append("snapshot commit_sha is not a 40-hex Git object ID")
    if not HEX40.fullmatch(str(snapshot.get("tree_sha", ""))):
        errors.append("snapshot tree_sha is not a 40-hex Git object ID")
    if snapshot.get("commit_signature_verified_by_github") is not True:
        errors.append("snapshot does not record a verified GitHub commit signature")
    if snapshot.get("ci", {}).get("conclusion") != "success":
        errors.append("snapshot CI conclusion is not success")

    selected = [r for r in read_csv(SAMPLES / "pilot_document_selection_0_1.csv") if r.get("status") == "selected"]
    calibration = {r["fragment_id"] for r in read_csv(SAMPLES / "calibration_manifest_0_1.csv")}
    reserve = {r["fragment_id"] for r in read_csv(SAMPLES / "reliability_reserve_0_1.csv")}
    frozen = frozen_ids()

    expected_counts = {
        "selected_pilot_documents": len(selected),
        "target_fragments": 96,
        "localized_fragments": 96,
        "frozen_fragments": len(frozen),
        "unlocalized_fragments": 0,
    }
    documentary = snapshot.get("documentary_state", {})
    for key, value in expected_counts.items():
        if documentary.get(key) != value:
            errors.append(f"snapshot documentary count mismatch for {key}: expected {value}")

    validation = snapshot.get("validation_state", {})
    if validation.get("calibration_fragments") != len(calibration):
        errors.append("snapshot calibration count mismatch")
    if validation.get("reliability_reserve_fragments") != len(reserve):
        errors.append("snapshot reliability reserve count mismatch")
    if calibration & reserve:
        errors.append("calibration/reliability reserve overlap")
    if calibration | reserve != frozen:
        errors.append("calibration plus reliability reserve does not equal frozen union")
    if len(frozen) != 96 or len(calibration) != 12 or len(reserve) != 84:
        errors.append("canonical 96/12/84 state is not satisfied")

    if validation.get("human_coded_fragments") != 0:
        errors.append("prevalidation snapshot must record zero human-coded fragments")
    if validation.get("formal_reliability_round_started") is not False:
        errors.append("prevalidation snapshot must record formal reliability as not started")
    if validation.get("gold_labels") != 0:
        errors.append("prevalidation snapshot must record zero gold labels")
    if not version.endswith("-dev") and validation.get("human_coded_fragments") == 0:
        errors.append("non-development version is forbidden while human coding remains zero")

    if not DATASET_CARD.is_file():
        errors.append("dataset card missing")
    if snapshot.get("analysis_plan") != "docs/ANALYSIS_PLAN_0_1.md":
        errors.append("snapshot analysis plan pointer is not canonical")
    if snapshot.get("human_gate_protocol") != "docs/FUTURE_HUMAN_GATE_PROTOCOL_0_1.md":
        errors.append("snapshot human gate protocol pointer is not canonical")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PDHD project metadata checks passed (version, CodeMeta, snapshot, 96/12/84 state)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
