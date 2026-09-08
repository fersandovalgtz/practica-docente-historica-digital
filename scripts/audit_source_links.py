#!/usr/bin/env python3
"""Non-blocking observability audit for public URLs referenced by PDHD.

HTTP availability is evidence about a URL, never proof that a historical source
exists or does not exist. The script therefore reports URL state separately from
catalogued-entity state and intentionally does not fail merely because links are
unreachable.
"""
from __future__ import annotations

import argparse
import csv
import json
import socket
import ssl
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
USER_AGENT = "PDHD-link-audit/0.1 (+https://github.com/fersandovalgtz/practica-docente-historica-digital)"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def add(records: dict[str, dict[str, set[str]]], url: str, *, origin: str, role: str, source_id: str = "", document_id: str = "") -> None:
    url = (url or "").strip()
    if not url.startswith(("http://", "https://")):
        return
    rec = records.setdefault(url, {"origins": set(), "roles": set(), "source_ids": set(), "document_ids": set()})
    rec["origins"].add(origin)
    rec["roles"].add(role)
    if source_id:
        rec["source_ids"].add(source_id)
    if document_id:
        rec["document_ids"].add(document_id)


def gather() -> tuple[list[dict[str, object]], set[str], set[str]]:
    sources = read_csv(DATA / "catalog/sources.csv")
    documents = read_csv(DATA / "catalog/documents.csv") + read_csv(DATA / "catalog/documents_balancing_w1.csv")
    source_ids = {r["source_id"] for r in sources}
    document_ids = {r["document_id"] for r in documents}
    records: dict[str, dict[str, set[str]]] = {}

    for r in sources:
        add(records, r.get("base_url", ""), origin="data/catalog/sources.csv", role="source_base", source_id=r.get("source_id", ""))
    for r in read_csv(DATA / "catalog/rights_registry.csv"):
        add(records, r.get("source_terms_url", ""), origin="data/catalog/rights_registry.csv", role="rights_terms", source_id=r.get("source_id", ""))
    for path in [DATA / "catalog/documents.csv", DATA / "catalog/documents_balancing_w1.csv"]:
        for r in read_csv(path):
            add(records, r.get("source_url", ""), origin=str(path.relative_to(ROOT)), role="document_object", source_id=r.get("source_id", ""), document_id=r.get("document_id", ""))
    for r in read_csv(DATA / "catalog/source_candidates.csv"):
        add(records, r.get("source_url", ""), origin="data/catalog/source_candidates.csv", role="candidate_evidence", source_id=r.get("source_id", ""))
    for r in read_csv(DATA / "samples/retrieval_attempts.csv"):
        add(records, r.get("object_url", ""), origin="data/samples/retrieval_attempts.csv", role="retrieval_target", source_id=r.get("source_id", ""), document_id=r.get("document_id", ""))
    for pattern, role in [("fragment_locator_progress*.csv", "fragment_locator"), ("frozen_fragments*.csv", "frozen_fragment_evidence")]:
        for path in sorted((DATA / "samples").glob(pattern)):
            for r in read_csv(path):
                add(records, r.get("locator_evidence_url", ""), origin=str(path.relative_to(ROOT)), role=role, document_id=r.get("document_id", ""))

    normalized = []
    for url, meta in sorted(records.items()):
        normalized.append({
            "url": url,
            "origins": sorted(meta["origins"]),
            "roles": sorted(meta["roles"]),
            "source_ids": sorted(meta["source_ids"]),
            "document_ids": sorted(meta["document_ids"]),
        })
    return normalized, source_ids, document_ids


def classify_http(status: int) -> str:
    if 200 <= status < 400:
        return "reachable"
    if status in {404, 410}:
        return "url_not_found"
    if status in {401, 403}:
        return "access_restricted"
    if status == 429:
        return "rate_limited"
    if 500 <= status < 600:
        return "server_error"
    return "other_http"


def check_url(url: str, timeout: float) -> dict[str, object]:
    last_error = ""
    for method in ("HEAD", "GET"):
        headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
        if method == "GET":
            headers["Range"] = "bytes=0-0"
        request = Request(url, method=method, headers=headers)
        try:
            with urlopen(request, timeout=timeout) as response:
                status = int(getattr(response, "status", 200))
                return {"url_state": classify_http(status), "http_status": status, "final_url": response.geturl(), "error": ""}
        except HTTPError as exc:
            status = int(exc.code)
            # HEAD is frequently blocked while GET is valid; retry only for statuses
            # where the request method itself may be the problem.
            if method == "HEAD" and status in {403, 405, 501}:
                last_error = f"HEAD HTTP {status}"
                continue
            return {"url_state": classify_http(status), "http_status": status, "final_url": exc.geturl() or url, "error": str(exc)}
        except socket.timeout as exc:
            return {"url_state": "timeout", "http_status": "", "final_url": url, "error": str(exc)}
        except ssl.SSLError as exc:
            return {"url_state": "tls_error", "http_status": "", "final_url": url, "error": str(exc)}
        except URLError as exc:
            reason = exc.reason
            if isinstance(reason, socket.gaierror):
                state = "dns_error"
            elif isinstance(reason, TimeoutError):
                state = "timeout"
            elif isinstance(reason, ssl.SSLError):
                state = "tls_error"
            else:
                state = "network_error"
            return {"url_state": state, "http_status": "", "final_url": url, "error": str(exc)}
        except Exception as exc:  # audit must record unexpected endpoint behavior rather than crash the whole batch
            return {"url_state": "client_error", "http_status": "", "final_url": url, "error": f"{type(exc).__name__}: {exc}"}
    return {"url_state": "client_error", "http_status": "", "final_url": url, "error": last_error or "request failed"}


def entity_state(meta: dict[str, object], source_ids: set[str], document_ids: set[str]) -> str:
    referenced_sources = set(meta["source_ids"])
    referenced_docs = set(meta["document_ids"])
    if referenced_sources & source_ids or referenced_docs & document_ids:
        return "catalogued"
    return "unknown"


def self_test() -> int:
    assert classify_http(200) == "reachable"
    assert classify_http(302) == "reachable"
    assert classify_http(404) == "url_not_found"
    assert classify_http(410) == "url_not_found"
    assert classify_http(403) == "access_restricted"
    assert classify_http(429) == "rate_limited"
    assert classify_http(503) == "server_error"
    print("audit_source_links self-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-csv", type=Path, default=Path("link_audit.csv"))
    parser.add_argument("--output-json", type=Path, default=Path("link_audit_summary.json"))
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--limit", type=int, default=0, help="optional deterministic URL limit for diagnostics")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    records, source_ids, document_ids = gather()
    if args.limit:
        records = records[: args.limit]
    checked_at = datetime.now(timezone.utc).isoformat()
    rows: list[dict[str, object]] = []
    for index, meta in enumerate(records, 1):
        result = check_url(str(meta["url"]), args.timeout)
        row = {
            "audit_order": index,
            "checked_at": checked_at,
            "url": meta["url"],
            "host": urlparse(str(meta["url"])).netloc,
            "url_state": result["url_state"],
            "http_status": result["http_status"],
            "final_url": result["final_url"],
            "source_entity_state": entity_state(meta, source_ids, document_ids),
            "source_existence_inference": "not_inferred_from_http",
            "reference_count": len(meta["origins"]),
            "source_ids": ";".join(meta["source_ids"]),
            "document_ids": ";".join(meta["document_ids"]),
            "roles": ";".join(meta["roles"]),
            "origins": ";".join(meta["origins"]),
            "error": result["error"],
        }
        rows.append(row)
        print(f"[{index}/{len(records)}] {row['url_state']}: {row['url']}")

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else ["audit_order", "checked_at", "url", "url_state"]
    with args.output_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)

    state_counts = Counter(str(r["url_state"]) for r in rows)
    host_counts = Counter(str(r["host"]) for r in rows)
    summary = {
        "checked_at": checked_at,
        "url_count": len(rows),
        "url_state_counts": dict(sorted(state_counts.items())),
        "host_counts": dict(host_counts.most_common()),
        "interpretation": "URL status is not a historical-source existence claim; 404/410 means url_not_found only."
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
