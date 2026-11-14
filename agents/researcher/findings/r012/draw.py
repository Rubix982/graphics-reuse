"""R-012: draw the sample exactly as procedure.md says.

Run with plain Python 3 (standard library only):
    python3 -I draw.py
Writes raw.json (every API result), hits.csv (title-filtered, sorted by paper id)
and shuffled.csv (the same list after random.Random(1114).shuffle).
"""
from __future__ import annotations

import csv
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
API = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
PARAMS: dict[str, str] = {
    "query": 'fast | faster | efficient* | accelerat* | "real-time"',
    "venue": "ACM Transactions on Graphics",
    "year": "2000-2025",
    "fields": "title,year,venue,externalIds,abstract",
}
TITLE = re.compile(r"\bfast\b|\bfaster\b|\befficient\w*|\baccelerat\w*|\breal[- ]time\b", re.I)
SEED = 1114


def fetch_all() -> list[dict]:
    papers: list[dict] = []
    token: str | None = None
    while True:
        params = dict(PARAMS)
        if token:
            params["token"] = token
        url = API + "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"User-Agent": "graphics-reuse-research/0.1"})
        for attempt in range(6):
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    page = json.load(r)
                break
            except Exception as e:  # rate limits answer 429; back off and retry
                print(f"retry {attempt + 1}: {e}")
                time.sleep(5 * (attempt + 1))
        else:
            raise SystemExit("Semantic Scholar did not answer")
        papers.extend(page.get("data", []))
        print(f"page: {len(page.get('data', []))} (total reported {page.get('total')})")
        token = page.get("token")
        if not token:
            return papers
        time.sleep(2)


def main() -> None:
    raw = fetch_all()
    (HERE / "raw.json").write_text(json.dumps(raw, indent=1, ensure_ascii=False))
    seen_ids: set[str] = set()
    seen_titles: set[str] = set()
    hits: list[dict] = []
    for p in sorted(raw, key=lambda p: p["paperId"]):
        title = (p.get("title") or "").strip()
        key = re.sub(r"\s+", " ", title.lower())
        if p["paperId"] in seen_ids or key in seen_titles or not TITLE.search(title):
            continue
        seen_ids.add(p["paperId"])
        seen_titles.add(key)
        hits.append(p)
    cols = ["paperId", "year", "doi", "has_abstract", "title"]

    def row(p: dict) -> dict:
        return {
            "paperId": p["paperId"],
            "year": p.get("year"),
            "doi": (p.get("externalIds") or {}).get("DOI", ""),
            "has_abstract": "yes" if p.get("abstract") else "no",
            "title": p.get("title", ""),
        }

    with open(HERE / "hits.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(row(p) for p in hits)
    shuffled = list(hits)
    import random

    random.Random(SEED).shuffle(shuffled)
    with open(HERE / "shuffled.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["rank"] + cols)
        w.writeheader()
        for i, p in enumerate(shuffled, 1):
            w.writerow({"rank": i, **row(p)})
    print(f"raw {len(raw)}, after title filter and dedup {len(hits)}")


if __name__ == "__main__":
    main()
