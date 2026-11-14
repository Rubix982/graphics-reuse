# Premise

_Written 2026-11-14, from the conversation that started this repository. A premise dry-run: how the idea got here, and what each reframe broke._

## Where it started

The first idea was a knowledge base built from competitive programming. Contest solutions often reach an answer by a shortcut that looks impossible until you have spent days on the same problem, and an asymptotic win beats better hardware once inputs grow. The plan was to distil those solutions with AI, point an agent at an existing library, find a slow part, apply a trick from the knowledge base, and check that the output stayed the same while the code got faster.

## What broke it

Three things, found in roughly this order.

The distillation has been done. PIE (Shypula et al., ICLR 2024) collected over 77,000 slow-to-fast pairs of C++ submissions from CodeNet, kept where the same programmer later submitted a faster solution, and models trained on them beat the best human speedup on held-out contest problems. It didn't carry over to real code. On repository-level benchmarks agents do poorly: under 5 % of tasks solved on GSO (Shetty et al., NeurIPS 2025), and under 0.23× of the expert speedup on SWE-fficiency (ICML 2026).

The catalogue isn't what is missing. Models already have the contest corpus in their weights, and GSO's failure analysis says agents mostly misdiagnose where the time goes. The gap is in finding the problem.

Contest problems are selected for having a trick. Setters choose a problem because a clever shortcut is hidden in it and build the tests so only that shortcut passes. Years of that make it feel as if every problem hides one. Real problems weren't designed by anyone, and most of the time the win is boring (a list that should have been a set) or a reframe that only someone who knows the field would see.

What survived the cut (dry-run move 9) is the contest instinct itself: the habit of looking at a messy problem and asking what known problem it really is. That transfers. The archive of solutions mostly doesn't.

## The example that moved it

A private Blender garment pipeline was the example. Its run records time every step. A full run took 14–22 minutes, or 49–57 with a dupatta, and nearly all of it was the cloth solver. An A-pose drape took 4–7 minutes on garment pieces of about 5,000 vertices each, and the fitting loop, three rounds of re-draping, took 27–35 minutes on its own.

Its own code already used the right algorithms where it was checked: the crossing check uses a bounding-volume tree, and the fitting loop uses grouped finite differences, Levenberg–Marquardt and a sparse Broyden update so it runs as few drapes as it can. A catalogue of contest tricks would find little there. The largest speedup on record was a reframe instead: carrying a settled garment to another body with Surface Deform took 1.2 s against about 6 minutes for a drape.

## Second premise: recomputation

Slow software often redoes work it has already done. This has a name (move 2): incremental computation, with memoization as its simplest form. Detecting exact repeats is solved well enough to have tools. MemoizeIt (Della Toffola, Pradel and Gross, OOPSLA 2015) found 9 memoization opportunities in 11 Java programs that profilers had missed, with speedups of 1.04× to 12.93×.

So exact repeats are the easy case. The expensive cases are work that is nearly the same, like each repair round draping a slightly different cut, and reusing nearly-the-same work changes the answer. The content worth writing down moved from the technique to its validity condition: when is the old answer still good enough? The Surface Deform result already shows the shape of it. The kameez and trousers carried well and the dupatta's free end tore. The technique is generic; the condition is specific to cloth.

## Third premise: geometry, then graphics

Why geometry suits this (move 1): geometric work changes a little at a time. Between frames, iterations or rounds most points barely move, and neighbouring points behave alike. That coherence is what reuse feeds on. Geometric results are also cheap to check (intersections, distances, lengths, volumes), which supplies the "did the answer stay the same" half that the first idea lacked. The formal names are kinetic data structures (Basch, Guibas and Hershberger, SODA 1997) and, in collision detection, temporal coherence.

It is generic across graphics by choice, rather than scoped to the test bed: the expectation is to keep contributing to graphics for a long time, and writing the entries doubles as a map of the field. Two rules keep a generic reference from becoming a list nobody uses:

- Organise by what gets reused, not by subfield. Six axes: across time, across space, across runs, across resolutions, across shapes, across many instances. The same pattern crosses rendering, simulation and CAD, so a new field slots in without adding a section.
- Every entry states whether it has been tested and, if so, what was measured. Entries from reading alone are allowed and marked untested.

## The method, from `style`

A sibling library had already answered several of this one's design questions with data. `style` collects design knowledge for coding agents, filed by the problem it solves, and tests every entry against an agent given no guidance. Its C-003 found that most of a source's devices are conditional, used only when the task has the problem they solve. That is the same finding as "the technique is generic, the condition is specific". Its C-007 found an agent already following 5 of an entry's 6 rules, with the entry's extras making the result worse; that is the risk T-002 names here, and its METHOD.md step 2b is the guard.

The two stay separate repositories. `style` is judged by a blind pick, and its subject is how a page communicates; this library is measured, and its subject is computation. The method was adapted (`METHOD.md`) and the libraries weren't merged. If a third library appears, the shared method is worth lifting into one place.

## What the reframes broke (move 8)

- The agent purpose is unproven. A reference for people is worth having regardless, but as context for an AI tool it still has to beat a model that already knows the techniques. `style`'s C-007 is early evidence that the risk is real. Testing it needs a test bed with a check, which Phase 1 doesn't use (T-002).
- The original tool, which would find performance problems in libraries and fix them, is out of scope for Phase 1.
- For some areas the catalogue already exists in books: *Real-Time Collision Detection* (Ericson) and *Real-Time Rendering* (Akenine-Möller et al.). What this reference adds has to be the validity conditions, the checks and the tested status.
- The six axes are untested. They came from about ten examples in one conversation and may not hold for a wider set. That is the first card.

## The premise now

Much slow graphics software redoes work it has already done. For each kind of reuse, some field's literature has a technique, and this reference writes down when the reused answer is still good enough and how to check.

Two ways it could turn out wrong: the techniques may not sort into kinds of reuse (the first card tests this), or the validity conditions may come out generic, along the lines of "when the change is small", instead of specific to each field. In the second case the reference adds little over the books.

## Threads

```
- ACTIVE  → T-001 · do the six axes hold? (CARD.md, R-004)
- parked  → T-002 · does the reference beat a model that already knows the techniques?
            T-003 · can the recognition habit be measured (a contest problem, clean and disguised)?
- opened  → T-004 · is the dupatta's tear structural to free-hanging cloth under any surface binding?
            T-005 · does a warm-started drape settle into the same folds as a fresh one?
            T-006 · is multigrid reuse, or a faster solver?
            T-007 · do kinetic data structures cover more than "across time"?
```

## Sources

- Shypula et al. Learning Performance-Improving Code Edits (PIE). ICLR 2024. https://arxiv.org/abs/2302.07867
- Shetty et al. GSO: Challenging Software Optimization Tasks for Evaluating SWE-Agents. NeurIPS 2025. https://arxiv.org/abs/2505.23671
- SWE-fficiency: Can Language Models Optimize Real-World Repositories on Real Workloads? ICML 2026. https://icml.cc/virtual/2026/poster/66745
- Reliability of software-optimisation benchmarks (replay of 740 reference patches). arXiv 2607.01211, July 2026.
- Della Toffola, Pradel, Gross. Performance Problems You Can Fix: A Dynamic Analysis of Memoization Opportunities. OOPSLA 2015. https://github.com/lucadt/memoizeit
- Basch, Guibas, Hershberger. Data Structures for Mobile Data. SODA 1997; journal version J. Algorithms 31(1), 1999.
