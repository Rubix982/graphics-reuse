# Glossary

_All agents append. No edits to prior entries._

- **Reuse axis**: what an entry's technique reuses: the previous step (across time), a neighbour's work (across space), an earlier run (across runs), a coarse solution (across resolutions), a result on another shape (across shapes), or work paid once for every case (across many instances).
- **Validity condition**: when a reused answer is still good enough. Section 4 of every entry.
- **Agent baseline**: what a fresh agent proposes for the repeated work with no entry (METHOD.md step 2b). An entry should carry what the baseline misses.
- **Seed-to-seed spread**: how much repeated runs of the same input differ when only the random seed changes. The yardstick for "the same answer" in a test.
- **Incremental computation**: updating a result after its inputs change without recomputing it from scratch.
- **Memoization**: storing a function's result for given inputs and returning it when the same inputs come again.
- **Kinetic data structure**: a structure kept correct while its objects move, updated only at the moments its answer can change (Basch, Guibas and Hershberger 1997).
- **Temporal coherence**: consecutive frames or steps differ little. What most reuse across time relies on.
- **Warm start**: starting an iterative solver from a previous solution instead of from scratch.
- **Refit**: updating a bounding-volume tree's boxes after its contents move, keeping the tree's structure, instead of rebuilding it.
- **The test bed**: a private Blender garment pipeline whose measurements supply the first tested entry. A separate repository; read from here, never changed from here.
- **style**: the sibling library of design knowledge for coding agents whose method this one adapts. A separate repository, public as patternbook (https://github.com/Rubix982/patternbook).
- **reuse_changes**: whether a reuse changes only the cost (the result stays exact; failure shows as slowdown) or the answer too (the result is approximate; failure shows as a wrong answer). Added after R-004.
- **Held-out test**: a test on cases not used to build the thing being tested, drawn by a fixed procedure so the tester's choice can't steer it.
