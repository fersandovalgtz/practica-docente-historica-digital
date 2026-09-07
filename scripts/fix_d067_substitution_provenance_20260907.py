#!/usr/bin/env python3
from pathlib import Path
import csv
import io

ROOT = Path(__file__).resolve().parents[1]


def read_csv(path: Path):
    text = path.read_text(encoding="utf-8")
    reader = csv.DictReader(io.StringIO(text))
    return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows, fieldnames):
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

# Correct the retained outgoing document's access note without deleting it.
docs_path = ROOT / "data" / "catalog" / "documents_balancing_w1.csv"
docs, fields = read_csv(docs_path)
hits = [r for r in docs if r.get("document_id") == "PDHD-D000067"]
assert len(hits) == 1
hits[0]["notes"] = (
    "Primary institutional 8-page SEP pamphlet retained as a historical catalog object. "
    "HathiTrust record 101391797 / University of Texas item txu.059173025410517 was rechecked on "
    "2026-09-07 and is currently Limited (search only), contrary to the earlier full-view assumption. "
    "Secondary scholarship still supplies page-5 content pointers, but those pointers were never promoted "
    "through the direct-primary freeze gate. Pilot position 16 therefore substitutes PDHD-D000076 while "
    "preserving this outgoing object and the access discrepancy as provenance."
)
write_csv(docs_path, docs, fields)

# retrieval_attempts.csv represents active pilot-fragment retrieval attempts. Once position 16 is
# substituted, RA000003 can no longer name F000064 under D000067. Retire that active row; the failed
# Hathi route remains preserved in the outgoing catalog note and the versioned substitution decision.
ra_path = ROOT / "data" / "samples" / "retrieval_attempts.csv"
rows, fields = read_csv(ra_path)
removed = [r for r in rows if r.get("attempt_id") == "PDHD-RA000003"]
assert len(removed) == 1
rows = [r for r in rows if r.get("attempt_id") != "PDHD-RA000003"]
write_csv(ra_path, rows, fields)

print("Retired active RA000003 and corrected D000067 search-only provenance.")
