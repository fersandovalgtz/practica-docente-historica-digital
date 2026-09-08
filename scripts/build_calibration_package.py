#!/usr/bin/env python3
"""Build the deterministic PDHD-U1 human calibration package.

Selection uses structural metadata only. It never reads model labels, proposed
human labels, preparation notes, or historical source text.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
from functools import lru_cache
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "data" / "samples"
SEED = "PDHD-CAL-0.1-20260907"
CODEBOOK_VERSION = "PDHD-CB-0.2-calibration"
ERA_QUOTAS = {"E1": 5, "E3": 6, "E4": 1}
SLOTS = ("A", "B", "C", "D")
MEXICO_PLACES = {"méxico", "ciudad de méxico", "méxico, d.f."}

MANIFEST_PATH = SAMPLES / "calibration_manifest_0_1.csv"
CODER_SHEET_PATH = SAMPLES / "calibration_coder_sheet_0_1.csv"

# Neutral span instructions intentionally omit PDHD selection-role labels and
# semantic locator slugs. They identify boundaries, not expected annotations.
NEUTRAL_BOUNDARIES = {
    "PDHD-F000007": "Printed p. 8, right column: use the two contiguous paragraphs beginning at the prize-distribution moment and ending with the acclamation of the Liceo founders; stop before the following formal-congratulations paragraph.",
    "PDHD-F000009": "Printed p. 34: use the complete paragraph beginning with the primary-school teacher at the head of childhood and ending immediately before the next paragraph on civilization and culture.",
    "PDHD-F000018": "Printed p. 1: use the centered two-line mission statement directly below the publication title and immediately above the redacción/despacho address.",
    "PDHD-F000027": "Printed p. 163: use the closing block of Los ejercicios físicos en la escuela from the left-column summary of the opposing position through the right-column rebuttal, conclusion and author signature; stop before the horizontal rule.",
    "PDHD-F000040": "First page: use only the discrete publication/subscription administration block associated with the masthead; exclude the opening article columns.",
    "PDHD-F000041": "Printed p. 147 / Internet Archive leaf n52: use the single paragraph in José Suirob, Orientación obrera, that contains the teaching sequence; stop before the next paragraph beginning Y no es que se quiera que vayamos despacio.",
    "PDHD-F000047": "Printed p. 341 / Internet Archive leaf n26: use the first paragraph under Rafael Ramos Pedrueza, Historia de Mexico, section IX; stop before the next paragraph on the Liberal Party.",
    "PDHD-F000062": "Printed p. 13 / physical PDF p. 19: use the continuous block describing the rural teacher's community-school responsibility, work with children and adults, preparation context and related courses; stop before detailed methodological recommendations resume.",
    "PDHD-F000080": "Front matter PP7 / physical PDF p. 7: use the bibliographic core from the Secretaría de Educación Pública line through the title, 1932-1933 date range and México 1933 imprint; exclude library marks and margins.",
    "PDHD-F000081": "Printed p. 223 / physical PDF p. 238: use the paragraph beginning with the statement about insufficient preparation and continuing through the March-April preparation period and delivery of concrete work programs; stop before the departure/installation paragraph.",
    "PDHD-F000086": "Printed p. 53: begin with the opening continuation specifying federal programs and teacher appointments; continue through Article 334, Article 428 bis and the immediately following explanatory paragraph; stop before the paragraph beginning En lo que concierne al Departamento de Enseñanza Rural.",
    "PDHD-F000092": "Physical PDF p. 6: use the bibliographic title-page core identifying the SEP Memoria, reporting period, Gonzalo Vázquez Vela, Tomo II, D.A.P.P. and México 1939; exclude seal, blank margins and digitization marks.",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def score(*parts: str) -> int:
    payload = "|".join((SEED, *parts)).encode("utf-8")
    return int(hashlib.sha256(payload).hexdigest(), 16)


def is_regional(place: str) -> bool:
    return place.strip().lower() not in MEXICO_PLACES


def selected_documents() -> list[dict[str, str]]:
    rows = [
        r
        for r in read_csv(SAMPLES / "pilot_document_selection_0_1.csv")
        if r.get("status") == "selected"
    ]
    by_era = {era: [r for r in rows if r["era_code"] == era] for era in ERA_QUOTAS}

    candidates: list[tuple[int, tuple[int, ...], tuple[dict[str, str], ...]]] = []
    for e1 in itertools.combinations(by_era["E1"], ERA_QUOTAS["E1"]):
        if sum(is_regional(r["place"]) for r in e1) < 2:
            continue
        for e3 in itertools.combinations(by_era["E3"], ERA_QUOTAS["E3"]):
            e3_types = {r["document_type"] for r in e3}
            if "institutional_monograph" not in e3_types:
                continue
            if "official_report" not in e3_types:
                continue
            if not ({"teacher_guidance", "policy_proposal"} & e3_types):
                continue
            for e4 in itertools.combinations(by_era["E4"], ERA_QUOTAS["E4"]):
                combo = e1 + e3 + e4
                if len({r["document_type"] for r in combo}) < 5:
                    continue
                publication_counts: dict[str, int] = {}
                for r in combo:
                    publication_counts[r["publication"]] = publication_counts.get(r["publication"], 0) + 1
                if max(publication_counts.values()) > 2:
                    continue
                combo_score = sum(score("doc", r["document_id"]) for r in combo)
                order_key = tuple(sorted(int(r["selection_order"]) for r in combo))
                candidates.append((combo_score, order_key, combo))

    if not candidates:
        raise RuntimeError("no structural calibration selection satisfies declared constraints")
    _, _, winner = min(candidates, key=lambda x: (x[0], x[1]))
    return sorted(winner, key=lambda r: int(r["selection_order"]))


def assign_slots(docs: list[dict[str, str]]) -> tuple[str, ...]:
    @lru_cache(maxsize=None)
    def dp(i: int, a: int, b: int, c: int, d: int) -> tuple[int, tuple[str, ...]]:
        if i == len(docs):
            if (a, b, c, d) == (3, 3, 3, 3):
                return 0, ()
            return 10**1000, ()
        counts = [a, b, c, d]
        best: tuple[int, tuple[str, ...]] = (10**1000, ())
        doc_id = docs[i]["document_id"]
        for j, slot in enumerate(SLOTS):
            if counts[j] >= 3:
                continue
            next_counts = counts.copy()
            next_counts[j] += 1
            tail_score, tail = dp(i + 1, *next_counts)
            candidate = (score("slot", doc_id, slot) + tail_score, (slot,) + tail)
            if candidate < best:
                best = candidate
        return best

    total, assignment = dp(0, 0, 0, 0, 0)
    if total >= 10**1000 or len(assignment) != len(docs):
        raise RuntimeError("could not assign balanced A-D calibration slots")
    return assignment


def fragment_id(selection_order: int, slot: str) -> str:
    offset = SLOTS.index(slot)
    n = (selection_order - 1) * 4 + 1 + offset
    return f"PDHD-F{n:06d}"


def frozen_union() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for path in sorted(SAMPLES.glob("frozen_fragments*.csv")):
        for row in read_csv(path):
            fid = row["fragment_id"]
            if fid in result:
                raise RuntimeError(f"duplicate frozen fragment across shards: {fid}")
            result[fid] = row
    return result


def manifest_rows() -> list[dict[str, str]]:
    docs = selected_documents()
    assignments = assign_slots(docs)
    rows: list[dict[str, str]] = []
    for doc, slot in zip(docs, assignments):
        fid = fragment_id(int(doc["selection_order"]), slot)
        rows.append(
            {
                "item_id": "",  # assigned after deterministic permutation
                "calibration_order": "",
                "fragment_id": fid,
                "document_id": doc["document_id"],
                "selection_order": doc["selection_order"],
                "era_code": doc["era_code"],
                "slot": slot,
                "publication": doc["publication"],
                "place": doc["place"],
                "document_type": doc["document_type"],
                "codebook_version": CODEBOOK_VERSION,
                "selection_seed": SEED,
                "selection_basis": "metadata_only_structural_hash",
                "status": "selected_for_calibration",
            }
        )
    rows.sort(key=lambda r: (score("order", r["fragment_id"]), r["fragment_id"]))
    for i, row in enumerate(rows, 1):
        row["calibration_order"] = str(i)
        row["item_id"] = f"CAL{i:03d}"
    return rows


def annotation_fields() -> list[str]:
    with (SAMPLES / "annotation_pilot_template.csv").open(encoding="utf-8", newline="") as fh:
        header = next(csv.reader(fh))
    start = header.index("coder_id")
    return header[start:]


def coder_rows() -> list[dict[str, str]]:
    frozen = frozen_union()
    rows: list[dict[str, str]] = []
    for manifest in manifest_rows():
        fid = manifest["fragment_id"]
        if fid not in frozen:
            raise RuntimeError(f"calibration fragment is not frozen: {fid}")
        source = frozen[fid]
        if fid not in NEUTRAL_BOUNDARIES:
            raise RuntimeError(f"missing neutral coder boundary instruction: {fid}")
        row = {
            "item_id": manifest["item_id"],
            "fragment_id": fid,
            "document_id": manifest["document_id"],
            "page": source["page"],
            "source_url": source["locator_evidence_url"],
            "boundary_instruction": NEUTRAL_BOUNDARIES[fid],
            "codebook_version": CODEBOOK_VERSION,
            "annotation_id": "",
        }
        for field in annotation_fields():
            row[field] = ""
        rows.append(row)
    return rows


MANIFEST_FIELDS = [
    "item_id",
    "calibration_order",
    "fragment_id",
    "document_id",
    "selection_order",
    "era_code",
    "slot",
    "publication",
    "place",
    "document_type",
    "codebook_version",
    "selection_seed",
    "selection_basis",
    "status",
]


def coder_fields() -> list[str]:
    return [
        "item_id",
        "fragment_id",
        "document_id",
        "page",
        "source_url",
        "boundary_instruction",
        "codebook_version",
        "annotation_id",
        *annotation_fields(),
    ]


def csv_text(rows: list[dict[str, str]], fields: list[str]) -> str:
    buf = StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def expected_outputs() -> dict[Path, str]:
    return {
        MANIFEST_PATH: csv_text(manifest_rows(), MANIFEST_FIELDS),
        CODER_SHEET_PATH: csv_text(coder_rows(), coder_fields()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    outputs = expected_outputs()
    if args.check:
        mismatches = []
        for path, expected in outputs.items():
            actual = path.read_text(encoding="utf-8") if path.exists() else None
            if actual != expected:
                mismatches.append(str(path.relative_to(ROOT)))
        if mismatches:
            raise SystemExit("calibration package is not reproducible: " + ", ".join(mismatches))
        print("PDHD calibration package check passed (12 structurally selected frozen fragments)")
        return 0

    for path, text in outputs.items():
        path.write_text(text, encoding="utf-8")
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
