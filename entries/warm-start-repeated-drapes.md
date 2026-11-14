---
technique: warm-starting repeated drapes
axis: across runs
reuse_changes: depends. Cost only when the drape has one resting shape near its start; the answer too when it has several (friction, fold branches, contact changes), as cloth usually does (T-005).
fields: [cloth simulation, simulation inside fitting and optimisation loops, garment pattern fitting, rigid-body contact solvers]
source_docs:
  - Xuan Li, Chang Yu, Wenxin Du, Ying Jiang, Tianyi Xie, Yunuo Chen, Yin Yang, Chenfanfu Jiang. Dress-1-to-3 — Single Image to Simulation-Ready 3D Outfit with Diffusion Prior and Differentiable Physics. ACM Transactions on Graphics, SIGGRAPH 2025. arXiv 2502.03449v2. Read in full 2026-11-14; notes in agents/researcher/findings/r016/dress-1-to-3-notes.md
  - Erin Catto. Iterative Dynamics with Temporal Coherence. Game Developers Conference, 2005. (Slides seen through a third-party mirror; not read.)
  - Eugene L. Allgower, Kurt Georg. Numerical Continuation Methods — An Introduction. Springer, 1990. (Not read.)
also_teaches: [a static drape as one implicit step of 1 s with an intersection-free solver (Dress-1-to-3 §6.1), holding a bottom garment up in a first drape by shrinking the waist's rest shape so friction grips (§5.4), refitting after a remesh (§6.5), warm starting across time steps (Catto), which belongs under "across time"]
patterns: [warm-start, continuation, friction-off-while-fitting]
agent_baseline: "R-011, 2026-11-14 (claude-opus-5-5, fresh, no tools): proposed this technique unprompted and named 5 of the entry's 6 conditions, partly the sixth, with several more (agents/researcher/findings/r011/score.md). R-016 scored Dress-1-to-3 against that answer: of the paper's 6 items about the warm start, 3 named, 2 partly, 1 by none (the pinned waist that friction-off needs); with the paper's 2 items on running each drape, 3 by none (agents/researcher/findings/r016/score.md)."
tested_in: []
---

# Warm-starting repeated drapes

**In one sentence:** A published garment-fitting loop (Dress-1-to-3, SIGGRAPH 2025) starts every iteration's drape from the previous one and switches friction off to make that valid, but nobody has measured, there or in the test bed, whether a warm drape lands within fresh drapes' seed-to-seed spread.

**Use for:** loops that simulate the same garment many times with small changes between runs: fitting a cut to a photo, estimating how landmarks respond to each control, parameter sweeps.

## 1. Sources

Dress-1-to-3 (read in full) fits a sewing pattern to images generated from one photo. Each iteration drapes the current pattern statically on a fixed body with a differentiable Codimensional IPC simulator, then updates the pattern's Bézier curves and the cloth's global stretching and bending stiffness by gradient. Every iteration starts from the previous iteration's drape, and friction is left out during the fit (§6.1). It reports about 10 minutes of setup and up to 2 hours of fitting on one RTX 3090 (§8), but no iteration count, and no comparison of warm against fresh drapes. Catto's talk (rigid-body contact in games) caches each step's contact forces to start the next step's solver, which is reuse across time. Allgower and Georg give the frame: follow a solution as a parameter changes, each solution starting the next. Neither of those two has been read.

## 2. What work is wasted

In the test bed, the length fit drapes the garment once at the base cut, once per group of controls to estimate how each landmark responds (each control moved 3–8 cm), then once per step of the solve, at most 3 steps (its fitting code). Every drape starts from the flat pattern: pieces placed around the body, seams closed, cloth fallen (the stages in each drape's log). An A-pose drape takes about 4–7 minutes, and the fitting loop as a whole took 27–35 minutes on the runs with a dupatta (the test bed's run records, 2026-11-10).

## 3. The technique

Start the next drape from the last settled garment, with the new cut as the cloth's rest shape, and simulate until it settles again.

- Keep one triangulation across the loop and move it, so points correspond by construction. Dress-1-to-3 moves a fixed triangulation through fixed harmonic coordinates of its boundary samples (§5.1.2).
- Switch friction off during the fitting drapes and hold what would slip: Dress-1-to-3 fixes the waist loop of the bottom garment (§6.1). Drape the final cut with friction on (reasoned).
- When the mesh has to change, break the chain and re-drape, as Dress-1-to-3 does (§6.5); don't interpolate the settled drape onto the new mesh.

## 4. When reuse stays valid

### Constant

- The starting state has to be close to a resting state of the new problem for the warm start to save time. (paper: the premise of Catto and of Allgower and Georg, neither read; Dress-1-to-3 relies on it without measuring the saving)
- A static equilibrium doesn't locally depend on where the drape starts, which is what allows the start to be the previous drape. (paper: Dress-1-to-3 §6.1, stated as the zero Jacobian of the simulated state with respect to the initial state, for its gradients) "Locally" carries the weight: it holds only near one resting shape (below).

### Conditional

- There is one resting shape near the start, and it moves smoothly with the cut: no fold flips, no buckling, no contact appearing or disappearing. (reasoned; named by R-011's agent baseline; Dress-1-to-3's "locally")
- Friction gives a range of resting shapes, and a warm drape inherits wherever the previous one got stuck. Landmarks hanging from a friction support then respond too little. (reasoned; R-011's baseline) Switching friction off during the fit makes the drape "as path-independent as possible". (paper: Dress-1-to-3 §6.1) How path-independent is not measured there; contact, and so folds, stay. (reasoned)
- With friction off, a bottom garment slides down unless something holds it. Dress-1-to-3 fixes the waist boundary loop. (paper: §6.1) In its first drape, before the fit, it does the opposite: it shrinks the waist's rest shape so friction grips while the body moves into pose. (paper: §5.4)
- The new cut must be the rest shape and the settled drape the starting positions. The other way round, the folds become the cloth's natural shape. (reasoned; R-011's baseline; in Blender, the cloth's rest shape key)
- The two cuts' meshes correspond. Moving one triangulation keeps them so (paper: §5.1.2). Re-triangulating a settled drape can put cloth through cloth or body, because collision handling relied on the old mesh (paper: §6.5, for an intersection-free solver). Blender's solver isn't intersection-free, but it recovers poorly from cloth that starts inside a collider. (reasoned; R-011's baseline)
- Lengthening is harder than shortening: a lengthened piece starts compressed, and can crumple and stick instead of sliding down. (reasoned; R-011's baseline, which suggests moving each point by its pattern displacement through the drape's local deformation, or staging the change)
- A cut update that inverts rest triangles makes the next drape fail; Dress-1-to-3 runs a least-squares safeguard on negative triangle areas after updates that come close. (paper: §6.4)

### Varies

- Nothing recorded yet.

## 5. When it doesn't apply

- History dependence: the warm drape keeps folds or contacts from the previous cut that a fresh drape wouldn't have, so the result depends on the order of rounds as well as on the cut. Friction-off reduces this; it doesn't remove it. (reasoned)
- Inside a finite-difference estimate, sensitivity drapes warm-started from one base share its folds, and the response can come out smaller than a fresh drape's. R-011's baseline suggests measuring each response against a warm drape at the unchanged cut, and keeping fresh drapes for the residual. (reasoned, untested)
- A large cut change moves the garment far from its old state; the warm start then saves little or slows the settle. (reasoned)
- A change of mesh: the chain has to be broken and the garment draped again. (paper: Dress-1-to-3 §6.5)
- A target that isn't at rest (a garment photographed in motion, or held): a static drape only approximates it, warm or fresh. (paper: Dress-1-to-3 §9.4)

## 6. The check

Drape the same cut both ways, warm from the previous round and fresh from the flat pattern, over several seeds. The reuse is valid at the precision that matters if the warm drape's landmark lengths and silhouette fall within the fresh drapes' seed-to-seed spread and its crossings stay at their level. Record the time saved beside it. Run it with friction on and off during the fit (T-011), since friction is the published reason a warm drape can differ. R-011's baseline adds cheap checks before that: a warm drape at the unchanged cut should move no landmark (the null test); going there and back should return the landmarks (hysteresis); responses to +δ and −δ should be about opposite (contact changes).

## 7. Tested

Untested here, and untested in Dress-1-to-3, which uses the warm start without comparing it to fresh drapes.
