#!/usr/bin/env python3
"""Run PDHD phase-5 descriptive analysis only after the human gold gate opens.

Current pre-validation state must remain blocked. When a future human-adjudicated
gold set exists, the pipeline produces reproducible descriptive tables and
cluster-aware bootstrap intervals without treating four fragments from one
document as four fully independent documents.
"""
from __future__ import annotations

import argparse
import csv
import json
import random
from collections import Counter, defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GOLD = ROOT / "data/validated/gold_annotations.csv"
DEFAULT_MANIFEST = ROOT / "data/validated/gold_manifest.json"
DEFAULT_OUT = ROOT / "artifacts/phase5"
SAMPLES = ROOT / "data/samples"
CATALOG = ROOT / "data/catalog"
TAXONOMY = ROOT / "data/taxonomy"
BOOTSTRAP_SEED = 20260907
BOOTSTRAP_REPS = 2000


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader), list(reader.fieldnames or [])


def frozen_index() -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(SAMPLES.glob("frozen_fragments*.csv")):
        rows, _ = read_csv(path)
        for row in rows:
            fid = row["fragment_id"]
            if fid in result:
                raise RuntimeError(f"duplicate frozen fragment {fid}")
            result[fid] = row["document_id"]
    return result


def gate(gold_path: Path, manifest_path: Path) -> tuple[bool, list[str], list[dict[str, str]], dict[str, object]]:
    reasons: list[str] = []
    if not manifest_path.exists(): reasons.append("gold manifest absent")
    if not gold_path.exists(): reasons.append("gold annotations absent")
    if reasons: return False, reasons, [], {}

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    rows, fields = read_csv(gold_path)
    required_manifest = {
        "validation_status": "human_validated_adjudicated",
        "formal_reliability_completed": True,
        "adjudication_completed": True,
        "machine_candidates_excluded": True,
    }
    for key, expected in required_manifest.items():
        if manifest.get(key) != expected: reasons.append(f"manifest {key} must be {expected!r}")
    if int(manifest.get("human_coder_count", 0)) < 2: reasons.append("manifest requires at least two human coders")
    codebook = str(manifest.get("codebook_version", "")).strip()
    if not codebook: reasons.append("manifest codebook_version missing")
    expected_count = int(manifest.get("gold_fragment_count", -1))
    if expected_count != len(rows): reasons.append(f"manifest gold_fragment_count={expected_count} but CSV has {len(rows)} rows")
    if not (84 <= len(rows) <= 96): reasons.append("gold set must contain between 84 and 96 adjudicated pilot fragments")

    forbidden = [f for f in fields if f.startswith("model_") or f.startswith("machine_") or f in {"candidate_status", "gold_label"}]
    if forbidden: reasons.append(f"gold CSV contains forbidden machine fields: {sorted(forbidden)}")

    frozen = frozen_index()
    seen: set[str] = set()
    for row in rows:
        fid = row.get("fragment_id", "").strip(); doc = row.get("document_id", "").strip()
        if fid in seen: reasons.append(f"duplicate gold fragment {fid}")
        seen.add(fid)
        if fid not in frozen: reasons.append(f"gold fragment is outside frozen pilot: {fid}")
        elif frozen[fid] != doc: reasons.append(f"gold document mismatch for {fid}")
        if row.get("adjudication_status", "").strip() != "human_adjudicated_gold": reasons.append(f"{fid}: adjudication_status is not human_adjudicated_gold")
        if codebook and row.get("codebook_version", "").strip() != codebook: reasons.append(f"{fid}: codebook differs from gold manifest")
    return not reasons, reasons, rows, manifest


def pilot_metadata() -> dict[str, dict[str, str]]:
    pilot, _ = read_csv(SAMPLES / "pilot_document_selection_0_1.csv")
    docs_core, _ = read_csv(CATALOG / "documents.csv")
    docs_balancing, _ = read_csv(CATALOG / "documents_balancing_w1.csv")
    docs = {r["document_id"]: r for r in docs_core + docs_balancing}
    result: dict[str, dict[str, str]] = {}
    for p in pilot:
        d = docs[p["document_id"]]
        result[p["document_id"]] = {
            "era_code": p["era_code"],
            "document_type": p["document_type"],
            "publication": p["publication"],
            "place": p["place"],
            "source_id": d.get("source_id", ""),
            "period": d.get("period", ""),
        }
    return result


def dimensions() -> list[str]:
    rows, _ = read_csv(TAXONOMY / "pedagogical_dimensions.csv")
    return [f"dimension_{r['dimension_code']}" for r in rows]


def proportion_rows(rows: list[dict[str, str]], field: str) -> list[dict[str, object]]:
    values = [r.get(field, "").strip() or "missing" for r in rows]
    counts = Counter(values); total = len(values)
    return [{"value": value, "count": count, "proportion": count / total if total else 0.0} for value, count in counts.most_common()]


def dimension_rows(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    total = len(rows); output = []
    for field in dimensions():
        count = sum(r.get(field, "").strip() == "1" for r in rows)
        output.append({"dimension": field.removeprefix("dimension_"), "count": count, "proportion": count / total if total else 0.0})
    return sorted(output, key=lambda r: (-float(r["proportion"]), str(r["dimension"])))


def cluster_bootstrap(rows: list[dict[str, str]], category_fn, categories: list[str], reps: int = BOOTSTRAP_REPS) -> dict[str, tuple[float, float]]:
    by_doc: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows: by_doc[row["document_id"]].append(row)
    docs = sorted(by_doc)
    if not docs: return {c: (0.0, 0.0) for c in categories}
    rng = random.Random(BOOTSTRAP_SEED); samples: dict[str, list[float]] = {c: [] for c in categories}
    for _ in range(reps):
        replicate: list[dict[str, str]] = []
        for _j in docs: replicate.extend(by_doc[rng.choice(docs)])
        denom = len(replicate) or 1
        counts = Counter(category_fn(r) for r in replicate)
        for c in categories: samples[c].append(counts.get(c, 0) / denom)
    result: dict[str, tuple[float, float]] = {}
    for c, vals in samples.items():
        vals.sort(); lo = vals[int(0.025 * (len(vals) - 1))]; hi = vals[int(0.975 * (len(vals) - 1))]; result[c] = (lo, hi)
    return result


def add_cluster_ci(rows: list[dict[str, str]], table: list[dict[str, object]], key: str, row_field: str) -> None:
    categories = [str(r[row_field]) for r in table]
    ci = cluster_bootstrap(rows, lambda r: r.get(key, "").strip() or "missing", categories)
    for record in table:
        lo, hi = ci[str(record[row_field])]; record["cluster_bootstrap_ci_low"] = lo; record["cluster_bootstrap_ci_high"] = hi


def add_dimension_ci(rows: list[dict[str, str]], table: list[dict[str, object]]) -> None:
    by_doc: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows: by_doc[row["document_id"]].append(row)
    docs = sorted(by_doc); rng = random.Random(BOOTSTRAP_SEED)
    for record in table:
        field = "dimension_" + str(record["dimension"]); vals = []
        for _ in range(BOOTSTRAP_REPS):
            replicate = []
            for _j in docs: replicate.extend(by_doc[rng.choice(docs)])
            vals.append(sum(r.get(field, "") == "1" for r in replicate) / (len(replicate) or 1))
        vals.sort(); record["cluster_bootstrap_ci_low"] = vals[int(.025 * (len(vals)-1))]; record["cluster_bootstrap_ci_high"] = vals[int(.975 * (len(vals)-1))]


def cross_table(rows: list[dict[str, str]], metadata: dict[str, dict[str, str]], meta_field: str, semantic_field: str) -> list[dict[str, object]]:
    counts: Counter[tuple[str, str]] = Counter(); totals: Counter[str] = Counter()
    for row in rows:
        group = metadata[row["document_id"]].get(meta_field, "") or "missing"
        value = row.get(semantic_field, "").strip() or "missing"
        counts[(group, value)] += 1; totals[group] += 1
    return [{"group": group, "value": value, "count": count, "group_proportion": count / totals[group]} for (group, value), count in sorted(counts.items())]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n"); writer.writeheader(); writer.writerows(rows)


def write_svg(path: Path, title: str, rows: list[dict[str, object]], label_field: str) -> None:
    width = 900; row_h = 34; left = 250; right = 70; top = 55; height = top + row_h * len(rows) + 30
    max_value = max([float(r["proportion"]) for r in rows] or [1.0]) or 1.0
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">', '<style>text{font-family:system-ui,sans-serif;fill:#172033}.title{font-size:20px;font-weight:700}.label{font-size:13px}.value{font-size:12px;font-weight:700}.bar{fill:#496f93}.track{fill:#edf0f4}</style>', f'<text class="title" x="20" y="30">{escape(title)}</text>']
    bar_w = width - left - right
    for i, row in enumerate(rows):
        y = top + i * row_h; p = float(row["proportion"]); label = escape(str(row[label_field])); w = (p / max_value) * bar_w
        parts += [f'<text class="label" x="20" y="{y+15}">{label}</text>', f'<rect class="track" x="{left}" y="{y+3}" width="{bar_w}" height="14" rx="7"/>', f'<rect class="bar" x="{left}" y="{y+3}" width="{w:.2f}" height="14" rx="7"/>', f'<text class="value" x="{left+bar_w+8}" y="{y+15}">{p:.1%}</text>']
    parts.append('</svg>'); path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def run_analysis(rows: list[dict[str, str]], manifest: dict[str, object], out: Path) -> None:
    metadata = pilot_metadata(); out.mkdir(parents=True, exist_ok=True)
    acts = proportion_rows(rows, "pedagogical_act_primary"); add_cluster_ci(rows, acts, "pedagogical_act_primary", "value")
    dims = dimension_rows(rows); add_dimension_ci(rows, dims)
    norm = proportion_rows(rows, "normativity"); add_cluster_ci(rows, norm, "normativity", "value")
    write_csv(out / "primary_act_distribution.csv", acts); write_csv(out / "dimension_prevalence.csv", dims); write_csv(out / "normativity_distribution.csv", norm)
    write_csv(out / "era_by_primary_act.csv", cross_table(rows, metadata, "era_code", "pedagogical_act_primary"))
    write_csv(out / "document_type_by_primary_act.csv", cross_table(rows, metadata, "document_type", "pedagogical_act_primary"))
    write_csv(out / "source_by_primary_act.csv", cross_table(rows, metadata, "source_id", "pedagogical_act_primary"))
    write_svg(out / "primary_acts.svg", "PDHD · actos pedagógicos primarios", acts[:12], "value")
    write_svg(out / "dimensions.svg", "PDHD · prevalencia de dimensiones", dims, "dimension")
    summary = {
        "analysis_status": "human_gold_phase5_descriptive",
        "gold_fragment_count": len(rows),
        "gold_document_count": len({r["document_id"] for r in rows}),
        "codebook_version": manifest["codebook_version"],
        "bootstrap": {"unit": "document cluster", "repetitions": BOOTSTRAP_REPS, "seed": BOOTSTRAP_SEED, "interval": "percentile 95%"},
        "outputs": ["primary_act_distribution.csv", "dimension_prevalence.csv", "normativity_distribution.csv", "era_by_primary_act.csv", "document_type_by_primary_act.csv", "source_by_primary_act.csv", "primary_acts.svg", "dimensions.svg"],
        "caution": "Fragment-level descriptive proportions are not claims of national representativeness or independent sampling."
    }
    (out / "phase5_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def self_test() -> int:
    rows = []
    for d in range(1, 5):
        for i in range(4):
            row = {"document_id": f"D{d}", "pedagogical_act_primary": "explain" if i < 2 else "guide", "normativity": "descriptive"}
            for field in dimensions(): row[field] = "1" if field.endswith("teaching_method") and i == 0 else "0"
            rows.append(row)
    acts = proportion_rows(rows, "pedagogical_act_primary"); assert sum(int(r["count"]) for r in acts) == 16
    ci = cluster_bootstrap(rows, lambda r: r["pedagogical_act_primary"], ["explain", "guide"], reps=50); assert set(ci) == {"explain", "guide"}
    dims = dimension_rows(rows); assert len(dims) == 16
    print("run_phase5_analysis self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--expect-closed", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test: return self_test()
    opened, reasons, rows, manifest = gate(args.gold, args.manifest)
    if args.expect_closed:
        if opened: raise SystemExit("phase-5 gate unexpectedly open; update CI only through an explicit human-validation milestone")
        if args.output_dir.exists() and any(args.output_dir.iterdir()): raise SystemExit("phase-5 outputs exist while human gold gate is closed")
        print("PDHD phase-5 gate correctly closed: " + "; ".join(reasons)); return 0
    if not opened:
        raise SystemExit("phase-5 gate closed: " + "; ".join(reasons))
    run_analysis(rows, manifest, args.output_dir); print(f"PDHD phase-5 outputs written to {args.output_dir}"); return 0


if __name__ == "__main__":
    raise SystemExit(main())
