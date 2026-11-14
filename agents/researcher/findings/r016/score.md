# R-016 · Dress-1-to-3's items against the R-011 warm-start baseline

_Scored 2026-11-14, after reading the paper, against the list fixed before reading (`baseline-items.md`). One baseline run (R-011's), not three as in R-013. Named = the baseline says it; partly = the baseline says part of it; none = the baseline doesn't say it._

## Items about the warm start itself

| id | the paper's item | section | baseline |
|---|---|---|---|
| P1 | Each iteration's drape starts from the previous iteration's result | §6.1, Eq. 17 | named (B1, B8) |
| P2 | Why that's allowed: the static equilibrium doesn't locally depend on its starting state (zero Jacobian with respect to it) | §6.1 | named (B11, B14: one resting shape near the start; path settings don't matter only then) |
| P3 | Friction is switched off during the fit, "to make the simulation as path-independent as possible" | §6.1 | partly (B15 names friction as the cause of path dependence; switching it off isn't proposed) |
| P4 | With friction off, the bottom garment is held by fixing its waist boundary loop | §6.1 | **none** |
| P5 | Correspondence across iterations by construction: one triangulation, moved through fixed harmonic coordinates | §5.1.2, §6.5 | named (B3: "warp the existing mesh") |
| P6 | When the mesh must change, re-triangulating the settled drape can put cloth through cloth or body, so the chain is broken: the new mesh is pulled back to the initial pattern, re-fitted from the start, then relaxed to the new rest shape | §6.5 | partly (B3 suggests interpolating in pattern space; B5 knows cloth starting inside the body is a problem, in another context) |

## Items about each iteration's drape (they apply to a fresh drape too)

| id | the paper's item | section | baseline |
|---|---|---|---|
| P7 | Each drape is one implicit step of 1 s with an intersection-free solver, reaching near-static equilibrium directly | §6.1 | **none** (B6 proposes stopping on convergence instead) |
| P8 | An update that inverts rest triangles makes the next drape fail; a least-squares safeguard on negative areas runs after updates that come close | §6.4 | **none** |

Not counted, since they aren't about the reuse: the static target approximates garments in motion (§9.4); stiffness fitted with the pattern (§6.1); the shrunken waist rest shape that makes friction grip in the first drape (§5.4); curvature parameters frozen in a first stage because they are more sensitive (§6.1). All are recorded in the notes.

## Count and branch

- About the warm start: 3 named, 2 partly, **1 none** → the card's 0–1 branch: for this entry the agent already had nearly everything the paper says about warm starting.
- With the two items about each iteration's drape: **3 none** → the 3-or-more branch.

The card asked for "items about the reuse". Read narrowly, the paper adds one idea the agent didn't have: switch friction off during the fit and pin the waist so nothing slips. The agent had named friction as the problem, not this remedy. Read widely, it adds two techniques for running each drape in the loop. Both readings are reported. Neither is a reframe like R-013's. Here the agent and the paper share a frame, and the paper adds a remedy inside it.

What the paper doesn't have that the baseline did: rest-shape plumbing (B2), lengthening against shortening (B5), measuring sensitivities against a warm run at the unchanged cut (B7), parallel drapes (B10), warm drapes for sensitivities and fresh ones for the residual (B19), and the cheap tests (B20). And neither has measured a warm drape against fresh ones.
