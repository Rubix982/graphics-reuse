---
technique: coarse-to-fine cloth
axis: across resolutions
reuse_changes: depends on the mechanism. Multigrid, cost only; upsampling, the answer.
fields: [cloth simulation, film, games]
source_docs:
  - Rasmus Tamstorf, Toby Jones, Stephen F. McCormick. Smoothed Aggregation Multigrid for Cloth Simulation. ACM Transactions on Graphics 34(6), SIGGRAPH Asia 2015. https://media.disneyanimation.com/uploads/production/publication_asset/131/asset/paper.pdf
  - Ladislav Kavan, Dan Gerszewski, Adam W. Bargteil, Peter-Pike Sloan. Physics-Inspired Upsampling for Cloth Simulation in Games. ACM Transactions on Graphics 30(4), SIGGRAPH 2011. https://users.cs.utah.edu/~ladislav/kavan11physics/kavan11physics.html
  - Rahul Narain, Armin Samii, James F. O'Brien. Adaptive Anisotropic Remeshing for Cloth Simulation. ACM Transactions on Graphics 31(6), SIGGRAPH Asia 2012. (From memory; not yet re-checked.)
also_teaches: [adaptive remeshing (Narain et al.): refine the mesh only where the cloth bends]
patterns: [coarse-to-fine, multigrid, upsampling]
agent_baseline: "R-011, 2026-11-14 (claude-opus-5-5, fresh, no tools): proposed a coarse drape followed by a short full-resolution settle, not multigrid or learned upsampling. Named 3 of 7 conditions, partly 1, missed the 3 about the mechanisms it didn't propose. Added conditions this entry lacks, chiefly that a flared garment's outline depends on its folds, and that mass and stiffness don't carry across resolution in Blender. Scoring: agents/researcher/findings/r011/score.md"
tested_in: []
---

# Coarse-to-fine cloth

**In one sentence:** Two different things share this name: coarse levels inside the solver, which reach the fine mesh's answer faster (6–8× on a fully dressed character of 371k vertices in Tamstorf et al.), and a coarse simulation with detail added afterwards, which reaches a different answer that only has to look right.

**Use for:** cloth simulations where the large-scale shape (the silhouette, where the garment hangs) costs most of the time.

## 1. Sources

Tamstorf et al. (film, Disney) build an algebraic multigrid solver for cloth that works on any mesh and handles contact constraints. Kavan et al. (games) learn linear operators from fine simulations that add mid-scale folds to a coarse simulation, on a single CPU core. Narain et al. refine the mesh only where the cloth needs it. All three read from abstracts and project pages so far.

## 2. What work is wasted

Here the waste is work done at more resolution than the answer needs, not repeated work. Iterative solvers remove small-scale error quickly and large-scale error slowly, so at full resolution the overall shape of the garment is the slowest part to converge. (This section was "What repeats" until R-004 found it didn't fit this entry or multigrid.)

## 3. The technique

Two mechanisms, kept apart because their conditions differ:

1. **Coarse levels inside the solver (multigrid).** The solver works on a hierarchy of coarser versions of the same problem. The coarse levels fix the large-scale error cheaply and the fine level fixes the rest. The answer is the fine mesh's answer, to the solver's tolerance.
2. **Coarse simulation, detail added after (upsampling).** Simulate a coarse mesh, then add mid-scale folds with a learned operator or a cheap secondary pass. The answer is the coarse silhouette plus plausible detail.

R-004 kept both on one axis. What separates them is whether the reuse changes the answer: multigrid doesn't, upsampling does (T-006, answered). They should still become two entries, one mechanism each, as METHOD.md step 3 asks.

## 4. When reuse stays valid

### Constant

- Multigrid gives the fine answer whenever it converges, so its validity is a matter of convergence and tolerance rather than approximation. (paper)

### Conditional

- Upsampling is valid when the large-scale shape is what is judged (silhouette, lengths) and the folds only need to look right. When the folds themselves are measured, the upsampled folds come from the operator, not the physics. (reasoned from the method)
- A coarse simulation has to resolve the contacts that matter. A coarse mesh can pass through or skip over thin features such as fingers or a narrow strap. (reasoned)
- Multigrid needs access to the solver. A solver you can't modify, such as Blender's, gives no way to use it. (reasoned)

### Varies

- Nothing recorded yet.

## 5. When it doesn't apply

From the methods' design; none of this has been measured here.

- Folds learned from one garment or material class may transfer poorly to another.
- Detail added after the simulation can push cloth through the body or through other cloth.
- A coarse garment can settle on a different support than the fine one would (a sleeve catching or not catching on the hand), which changes the large-scale shape as well.

## 6. The check

Against a full-resolution drape over several seeds: silhouette overlap, landmark lengths, crossings and a fold measure, each compared with the full drapes' seed-to-seed spread. Judge upsampling's silhouette and lengths separately from its folds; it can pass one and fail the other.

## 7. Tested

Untested. The test bed has quick and full quality modes; what its quick mode lowers (mesh resolution, solver steps or both) hasn't been checked from here.
