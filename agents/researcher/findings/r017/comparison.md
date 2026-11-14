# R-017 · The independent re-sort against R-012's sort

_Compared 2026-11-14 by the orchestrator, after the second sorter finished. The second sorter (a fresh agent, claude-opus-5-5, no web) saw only the first 60 abstracts and R-012's sorting rules, not R-012's verdicts, result or mid-sort decisions (its brief said not to open anything in the repo, and it reports it didn't). Its full record: `resort.md`. The comparison covers ranks 1–55, the range R-012 recorded._

## The card's statistic on the second sorter's own sample

Its 20th reuse paper is rank 58. Of its first 20, **19 clean, 1 misfit** (rank 56: few-shot fine-tuning of an earlier regression "fits across runs and across many instances equally well"). That is at least 16, so by the rule written before the run, **R-012's keep verdict doesn't depend on who sorted.**

## Agreement, ranks 1–55

Papers both sorters judged: 48. That is 55, minus 2 without an abstract, minus 5 that one sorter or the other called unclear (23 and 31 for both; 41, 49 and 51 for the second sorter only).

| | R-012 lenient (shared sub-terms not reuse) | R-012 strict (shared sub-terms reuse) |
|---|---|---|
| reuse or not, same verdict | 47 of 48 | 45 of 48 |
| Cohen's κ | 0.96 | 0.87 |
| disagreements | rank 50 | ranks 1, 50, 52 |

- **Ranks 1 and 52** (an identical term computed once and shared within one evaluation): the second sorter called both not reuse ("duplicate work removed within one evaluation"), deciding it independently. That is R-012's lenient reading.
- **Rank 50** (subdivision surfaces, a quadtree built per face ahead of time): R-012 said reuse, across many instances; the second sorter said not reuse, a precomputed structure "credited for what it enables, not for avoiding recomputation". It drew the same line for ranks 2 and 14, which R-012 also called not reuse.
- **Axis**, over the 18 papers both called reuse: **18 of 18 on the same axes**, including the two-axis papers 5 (many instances and space) and 46 (space and time).
- **reuse_changes** differed on two mechanisms: rank 46's ReSTIR reuse (R-012: depends; second sorter: the answer) and a second mechanism the second sorter split out of rank 48 (a reused part's reduced model, cost only).

## The components, side by side

| axis (papers among each sorter's first 20) | R-012 strict | R-012 lenient | second sorter |
|---|---|---|---|
| across many instances | 12 | 13 | 13 |
| across space | 4 | 4 | 4 |
| across resolutions | 2 | 3 | 3 |
| across time | 2 | 2 | 2 |
| across runs | 0 | 0 | 1 (rank 56, its one misfit: runs or many instances) |
| across shapes | 0 | 0 | 0 |

## What it says

The axes sort these papers the same way for two sorters who shared rules but not verdicts: same reuse calls on 47 or 45 of 48, same axes on 18 of 18, and the bar cleared in both samples. "Across many instances" holds about two-thirds of the reuse papers for both (T-016). The one place the axes blurred for the second sorter is the line between "across runs" and "across many instances": fine-tuning an earlier model for new conditions is both "an earlier run's result" and "work paid once" (T-009, T-013). The second sorter independently made R-012's lenient call on shared sub-terms (T-015).

What it doesn't remove: both sorters are the same model family, so agreement could be shared habit as much as the axes' clarity. And both worked from abstracts.
