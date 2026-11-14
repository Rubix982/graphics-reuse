---
technique: warm-starting repeated drapes
axis: across runs
fields: [cloth simulation, simulation inside fitting and optimisation loops, rigid-body contact solvers]
source_docs:
  - Erin Catto. Iterative Dynamics with Temporal Coherence. Game Developers Conference, 2005. (Slides seen through a third-party mirror; the paper itself not yet read.)
  - Eugene L. Allgower, Kurt Georg. Numerical Continuation Methods: An Introduction. Springer, 1990.
also_teaches: [warm starting across time steps (Catto), which belongs under "across time"]
patterns: [warm-start, continuation]
agent_baseline: not checked
tested_in: []
---

# Warm-starting repeated drapes

**In one sentence:** Untested hypothesis: when a fitting loop changes a garment's cut by a few centimetres per round, starting each drape from the previous round's settled garment instead of the flat pattern gives landmark lengths within the fresh drapes' seed-to-seed spread, in less time.

**Use for:** loops that simulate the same garment many times with small changes between runs: fitting a cut to a photo, estimating how landmarks respond to each control, parameter sweeps.

## 1. Sources

Catto's talk is about rigid-body contact in games. Contact forces solved in one time step are cached and used to start the next step's solver, matched contact by contact. That is reuse across time; using it across runs is the move this entry makes. Allgower and Georg give the mathematical frame: follow a solution as a parameter changes, using each solution as the starting guess for the next. Neither has been read in full for this entry.

## 2. What repeats

In the test bed, the length fit drapes the garment once at the base cut, once per group of controls to estimate how each landmark responds (each control moved 3–8 cm), then once per step of the solve, at most 3 steps (its fitting code). Every drape starts from the flat pattern: pieces placed around the body, seams closed, cloth fallen (the stages in each drape's log). An A-pose drape takes about 4–7 minutes, and the fitting loop as a whole took 27–35 minutes on the runs with a dupatta (the test bed's run records, 2026-11-10).

## 3. The technique

Start the next drape from the last settled garment, carried onto the new cut, then simulate until it settles again. If the cut change only moves existing points of the pattern, positions carry over directly. If it remeshes the pattern, they have to be carried by pattern coordinates first.

## 4. When reuse stays valid

### Constant

- The starting state has to be close to a resting state of the new problem for the warm start to save time. (paper: the premise of both sources)

### Conditional

- The change between runs is small relative to the garment. (reasoned, untested; 3–8 cm on a garment about a metre long is the case to test)
- The meshes of the two cuts correspond, directly or through pattern coordinates. (reasoned)
- The wanted answer is a resting shape near the old one. Cloth has many resting shapes (fold patterns, which side of a contact a panel ends up on). A warm start finds the one nearest its start, which need not be the one a fresh drape finds. (reasoned, untested; T-005)

### Varies

- Nothing recorded yet.

## 5. When it doesn't apply

- History dependence: the warm drape keeps folds or contacts from the previous cut that a fresh drape wouldn't have, so the result depends on the order of rounds as well as on the cut.
- Inside a finite-difference estimate, warm-starting every sensitivity drape from the same base drape would make them share its folds, and the estimated response could come out smaller than a fresh drape's. (reasoned, untested)
- A large cut change moves the garment far from its old state; the warm start then saves little or slows the settle.

## 6. The check

Drape the same cut both ways, warm from the previous round and fresh from the flat pattern, over several seeds. The reuse is valid at the precision that matters if the warm drape's landmark lengths and silhouette fall within the fresh drapes' seed-to-seed spread and its crossings stay at their level. Record the time saved beside it.

## 7. Tested

Untested.
