# R-016 · What the R-011 warm-start baseline named, fixed before reading Dress-1-to-3

_Written 2026-11-14 from `agents/researcher/findings/r011/answer-warm-start.md` (one fresh agent, no tools), before any of Dress-1-to-3 was read past the two sentences R-015 quoted (friction left out "to make the simulation as path-independent as possible"; each iteration starts from the previous drape because a static equilibrium doesn't depend on where it starts). After reading, each item taken from the paper is scored against this list: named, partly, or none. One baseline run, not three as in R-013, so a "none" is weaker evidence here._

| id | what the baseline named |
|---|---|
| B1 | Warm start: drape the starting cut once, then start every other drape from the settled result, changing only the rest shape |
| B2 | Rest-shape plumbing: the new flat pattern is the rest shape and the settled drape the starting positions; backwards, the folds become the cloth's natural shape |
| B3 | Vertex correspondence between cuts: warp the mesh, or look each vertex up in pattern space |
| B4 | The seams are already closed, so sewing is skipped |
| B5 | Lengthening differs from shortening: a lengthened piece is compressed, may crumple and stick against friction. A predictor x ≈ x0 + F·(u − u0), anchored at the supports, with vertices pushed out of the body; or staged changes |
| B6 | Stop on convergence (landmarks moving under ~1 mm over N frames), not after a fixed frame count |
| B7 | Measure each sensitivity against a warm run at the unchanged cut, so drift from an unsettled base cancels |
| B8 | Each least-squares step starts from the last accepted drape |
| B9 | The saving depends on where the time goes (an estimate: about 6 settle times down to 4) |
| B10 | Run the per-group drapes in parallel |
| B11 | Same answer only if there is effectively one resting shape near the start, moving smoothly with the cut: no fold flips, buckling, or contact appearing or disappearing |
| B12 | The fresh drape must land on the same shape too; check the fresh drapes' own spread |
| B13 | Both runs must have converged |
| B14 | Damping, time step and collision quality change the path, not the resting shape, only when the resting shape is unique |
| B15 | Friction at the supports gives a range of resting shapes; the warm start inherits where the base got stuck, so sensitivities of landmarks hanging from a friction support come out too small |
| B16 | Fold branches and buckling: the warm start keeps the old fold pattern |
| B17 | Contact changes (gripping, dropping off a hip, a hem reaching the floor) |
| B18 | Steps larger than the perturbations, and chained steps adding up path dependence |
| B19 | Warm-start errors lean one way: use warm starts for sensitivities, fresh drapes for the residual, with one fresh drape at the final cut |
| B20 | Tests: the null test, the rest-source test, the round trip (hysteresis), ±δ symmetry, the fresh drapes' spread, warm against fresh per group, end to end |

What the baseline did not propose, recorded so the scoring can't drift: switching friction off during the fit; any statement that a static equilibrium doesn't depend on its starting state; fixing part of the garment against slipping while friction is off.
