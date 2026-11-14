# R-012 · Procedure, fixed before the list was drawn

_Written 2026-11-14, before the full hit list was fetched or shuffled. Only an 8-paper test page of the search (in API order, not the shuffled order) had been seen. Anything decided later is marked as a later change, with its reason._

## The sample

1. **Source.** The card says DBLP, or Semantic Scholar if DBLP can't filter by venue. DBLP's API answered with a bot check on 2026-11-14 ("Making sure you're not a bot!"), which was not bypassed. So the source is the Semantic Scholar Graph API, `GET /graph/v1/paper/search/bulk`, with:
   - `query=fast | faster | efficient* | accelerat* | "real-time"`
   - `venue=ACM Transactions on Graphics`
   - `year=2000-2025`
   - `fields=title,year,venue,externalIds,abstract`
   - every page, following `token`.
2. **Title filter.** The bulk search matches title and abstract, while the card asks for title words. So a title filter is applied locally, case-insensitive: `\bfast\b|\bfaster\b|\befficient\w*|\baccelerat\w*|\breal[- ]time\b`. That is the card's five words: "efficient" and "accelerat-" as prefixes ("efficiently" and "acceleration" match, "efficiency" doesn't), and "real-time" with or without the hyphen. "Fastest" is not on the card's list and is left out.
3. **The list.** Duplicates are removed by Semantic Scholar paper id, then by lower-cased title. The list is sorted by paper id, so its order doesn't depend on the API, and saved in full as `hits.csv`. It is then shuffled with Python's `random.Random(1114).shuffle`, and the shuffled order is saved as `shuffled.csv`.

## Sorting

4. **Going down the list.** Papers are taken in shuffled order until 20 whose speedup is reuse have been sorted. Every paper looked at is recorded in `sorted.md`: reuse or not, with a one-line reason that quotes the abstract.
5. **Abstracts.** The abstract comes from Semantic Scholar. If it is missing there, it comes from OpenAlex by DOI, rebuilt from its inverted index. If neither has one, the paper is recorded as "no abstract" and skipped. It doesn't count either way.
6. **Reuse.** The paper's speed comes, as a stated contribution, from using results of work already done instead of computing them again. Each mechanism goes on one of the six axes:
   - **across time:** from a previous frame or time step;
   - **across space:** from neighbouring samples, pixels or elements in the same computation;
   - **across runs:** from an earlier run with different inputs;
   - **across resolutions:** from a coarser solution;
   - **across shapes:** from another shape or body;
   - **across many instances:** from work paid once ahead of time and used for every later problem instance (precomputation, tables, learned models).
7. **Not reuse:**
   - a faster algorithm or data structure that computes from scratch;
   - doing less work (approximation, simplification, culling, pruning, sparsity, early termination) without carrying results over;
   - parallelisation, GPU mapping or hardware;
   - better numerics, such as a preconditioner, unless reusing it across steps or runs is a stated contribution.

   A data structure built once and queried many times within one computation (a BVH for one frame's rays) is not "across many instances", which needs separate problem instances.
8. **Unclear.** If the abstract doesn't say how the speed is achieved, the paper is recorded as "unclear" and skipped, not counted.
9. **Clean or misfit.** A reuse paper is clean if every reuse mechanism in it lands on exactly one axis. It is a misfit if some mechanism fits no axis, or fits two axes equally well; the record says which. Each mechanism also gets `reuse_changes`: cost only, the answer, or depends.

## Branches (from the card, unchanged)

- At least 16 of the 20 clean: the axes hold beyond their own examples, and R-005 to R-010 unblock.
- 5 or more misfits: revise the axes before writing more entries, recording which papers broke them and how.
- Either way, if "across runs" again gets none, that is evidence for folding it into "across time" (T-009).

## Known weakness

The sorter is the orchestrator, the same model family that wrote the axes. Each decision carries the abstract's own words as its reason, so it can be checked. An independent second sort would measure agreement; it isn't part of the card.
