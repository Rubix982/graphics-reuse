"""R-012: abstracts for the first N papers in shuffled order (procedure.md step 5).

    python3 -I abstracts.py 120

Semantic Scholar's abstract (from raw.json) first; if missing, OpenAlex by DOI,
rebuilt from its inverted index; else "no abstract". Writes abstracts.jsonl.
"""
from __future__ import annotations

import csv
import json
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent


def openalex(doi: str) -> str:
    if not doi:
        return ""
    url = "https://api.openalex.org/works/doi:" + doi
    req = urllib.request.Request(url, headers={"User-Agent": "graphics-reuse-research/0.1"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                work = json.load(r)
            break
        except Exception as e:
            if "404" in str(e):
                return ""
            time.sleep(3 * (attempt + 1))
    else:
        return ""
    inv = work.get("abstract_inverted_index") or {}
    if not inv:
        return ""
    words: dict[int, str] = {}
    for word, positions in inv.items():
        for pos in positions:
            words[pos] = word
    return " ".join(words[i] for i in sorted(words))


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    raw = {p["paperId"]: p for p in json.loads((HERE / "raw.json").read_text())}
    out = HERE / "abstracts.jsonl"
    done = {}
    if out.exists():
        for line in out.read_text().splitlines():
            rec = json.loads(line)
            done[rec["rank"]] = rec
    with open(HERE / "shuffled.csv") as f:
        rows = list(csv.DictReader(f))[:n]
    with open(out, "a") as f:
        for row in rows:
            rank = int(row["rank"])
            if rank in done:
                continue
            p = raw[row["paperId"]]
            text, source = p.get("abstract") or "", "semantic scholar"
            if not text:
                text, source = openalex(row["doi"]), "openalex"
                time.sleep(0.3)
            if not text:
                source = "none"
            rec = {"rank": rank, "paperId": row["paperId"], "year": row["year"], "doi": row["doi"],
                   "title": row["title"], "source": source, "abstract": text}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            print(rank, source, row["title"][:70])


if __name__ == "__main__":
    main()
