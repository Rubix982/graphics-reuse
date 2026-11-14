_Agent baseline for entries/warm-start-repeated-drapes.md (METHOD.md step 2b). Fresh general-purpose agent, claude-opus-5-5, 2026-11-14, prompt in prompt-warm-start.md. Its answer, verbatim:_

---

This answer comes from memory. I didn't open any files or check Blender's documentation, so treat the Blender details I mark below as things to check.

## What to reuse

A drape is really a search for the shape the cloth comes to rest in, where gravity, the fabric's stretch and bend, and contact with the body balance. Moving a control 3–8 cm moves that resting shape only a little. Draping from scratch pays again for the large motion (closing the seams, the fall) just to reach a point a few cm from one you already have.

So: drape the starting cut from scratch once and keep the settled result. Start every other drape from that result. Change only the cloth's rest shape, meaning the new flat pattern, and keep the settled positions as the starting point. Then let it settle again.

**Doing it in Blender**

- **Which shape is which.** The rest shape must be the new flat pattern and the starting positions must be the settled drape. As I remember it, Blender takes rest lengths from the mesh at the start frame unless a rest shape key is set (Cloth > Shape; `ClothSettings.rest_shape_key` in Python). So:
  - write the settled drape into the Basis;
  - put the new cut's flat pattern in a shape key at value 0;
  - point the rest shape key at it.

  Getting this backwards is the main plumbing bug. If the rest shape comes from the draped positions, the folds become the fabric's natural shape and it then sags further. I believe the bending rest angles also come from the rest key, but check that.
- **Vertex correspondence.** If your pattern generator re-meshes every cut, the vertices no longer match between cuts. Either warp the existing mesh to the new outline (fine for 3–8 cm on a 5,000-vertex piece), or look each vertex up in pattern space and interpolate. Warping is simpler.
- **Seams.** They are already closed in the starting state, so the sewing phase is skipped entirely.
- **Shortening vs lengthening.** Shortening a piece leaves it stretched, and it pulls up into place. Lengthening leaves it compressed. The extra length may crumple where it is and then get stuck against friction instead of sliding down. Two fixes:
  - A predictor. Move each draped vertex by its pattern displacement, stretched and turned the way the drape has stretched and turned that bit of fabric: x ≈ x0 + F·(u − u0). Anchor the pattern change at the supported part (shoulders, waistband), so a sleeve made 4 cm longer starts with its cuff 4 cm lower. Push any vertex that ends up inside the body back out, because Blender doesn't reliably recover cloth that starts inside a collider.
  - Apply the change in 2–3 stages, with a short settle between them.

  Try without either first.
- **Stopping rule.** Stop when every landmark has changed less than about 1 mm over the last N frames, not after a fixed frame count. Average over the last few frames if collisions jitter.
- **Sensitivity reference.** Measure each sensitivity against a warm-started run at the unchanged cut, settled for the same number of frames, not against the baseline. If the baseline wasn't fully settled, both runs keep drifting by the same amount and the drift cancels.
- **Least-squares steps.** Start each step from the last accepted drape.

**How much it saves**

I can't tell from here; it depends on where the 4–7 minutes go.
- If most of it is sewing and the fall, a warm settle could be a small fraction of a drape.
- If most of it is the slow final creep, the saving is smaller. Suppose settling were one slow exponential decay to a 1 mm tolerance. Starting 5 cm away instead of 50 cm would then cut it from about 6 decay times to about 4.

Log the landmarks per frame on one scratch drape and you'll know. That log may also show your drapes running well past the point where the landmarks stopped moving. In that case the convergence stopping rule alone is a large win, and it moves the answer by no more than the tolerance you pick.

**Parallel runs**

The per-group drapes are independent of each other. Running them as parallel `blender -b` processes gives identical answers in less wall-clock time, if you have spare cores. There's no accuracy risk, so it's worth doing either way.

## When it gives the same answer

Both runs end in some resting shape for the new cut, and they agree when it's the same one. That needs four things:

1. **One resting shape that moves smoothly.** There is effectively one resting shape near the start, and it moves smoothly as the cut changes across the perturbation. No fold flips, no buckling, no contact appearing or disappearing.
2. **Scratch lands there too.** The scratch drape at the new cut would land on that same shape. This is the condition that's easy to miss. A warm start can follow its own drape perfectly and still disagree because the scratch drape picked a different fold pattern. If small irrelevant changes to the scratch setup (placing the pieces 1 cm differently) move the landmarks, then scratch isn't a single answer either.
3. **Both runs converged.** A run stopped mid-settle remembers where it started.
4. **Path-only settings don't matter.** Damping, time step and collision quality change the path but not the resting shape, and that holds only when the resting shape is unique (condition 1).

**Where it fails, most likely first:**

- **Friction at the supports.** With friction there isn't one resting shape. There's a range of shapes that all stay put. The warm start inherits wherever the baseline got stuck on the shoulders, waist or hips. Say the new cut "wants" to slide 1 cm down the shoulder but friction holds it. Warm start reports no change in hem height, while scratch lets it settle lower. I'd expect sensitivities for landmarks that hang from a friction support to come out too small.
- **Fold branches and buckling.** Sleeve bunching at the wrist, trouser break at the shoe. The warm start stays on the old fold pattern, and scratch may pick another.
- **Contact changes.** Tightening until the cloth grips the body, loosening until it drops off a hip, or the hem reaching the floor.
- **Steps bigger than the perturbations.** A 10–15 cm least-squares step is further outside the safe range than a 3 cm perturbation, and chaining three steps adds up the path dependence.
- **Plumbing.** The rest shape read from the wrong place, the predictor pushing vertices into the body, lost vertex correspondence, or an unconverged baseline.

**What this means for the design**

Warm-start errors all lean one way. It measures how the drape you already have responds, while scratch measures the difference between two independent drapes, fold switches included. That makes warm starts good for sensitivities: less noise, and later maybe smaller perturbations (keep 3–8 cm while comparing). For the final residual you want what a fresh drape gives.

An approximate sensitivity only costs a worse step direction, and damped least squares tolerates moderate error. A wrong residual makes the fit claim a match it doesn't have. So spend scratch drapes on the residual:

1. Drape the starting cut from scratch.
2. Get sensitivities and least-squares steps from warm starts.
3. Drape the final cut from scratch once.

If that last drape's landmarks match the warm estimate within tolerance, you're done. If not, the warm chain drifted, and that scratch drape becomes the baseline for another round, so nothing is wasted.

## How to check on a given garment

First set a tolerance per landmark from what the fit can resolve, such as the photo measurement error.

**Plumbing checks (cheap, warm starts only):**
1. **Null test.** Warm start at the unchanged cut. Every landmark should move less than the tolerance. If they move, the baseline wasn't settled or the rest shape is wrong. Fix that before anything else.
2. **Rest-source test.** Warm start with gravity and the body turned off. The pieces should relax toward flat. If they keep their draped folds, the rest shape came from the draped positions.
3. **Round trip.** Go from p0 to p0+δ and back to p0, warm each time. Landmarks should return to baseline within tolerance. If they don't, that control has hysteresis (friction or a fold branch), and warm starts aren't safe for it.
4. **±δ symmetry.** The response to +δ should be about minus the response to −δ. A large asymmetry means a contact change or buckling inside the range.

Tests 3–4 also tell you how far from baseline warm starts stay trustworthy. You can cap the least-squares step at that distance.

**Against scratch (once per garment type, not every fit):**
5. **Scratch noise.** Drape the same perturbed cut from scratch 2–3 times with something irrelevant changed (placement shifted 1 cm, different substeps). The spread between them is the noise of the reference.
6. **Per control group.** Compare warm vs scratch landmarks at the perturbed cut, and their sensitivity columns. It passes if the difference is within the scratch-vs-scratch spread or the tolerance, whichever is larger. Where it fails, compare which vertices touch the body in each run and look at the folds. Disagreement at shoulders or waist points to friction; a flipped fold points to branching.
7. **End to end.** Run the whole fit both ways, drape both final cuts from scratch, and compare their landmark errors against the photo. This is the test that matters. It passes if the warm fit's final cut is no worse than the scratch fit's by more than the tolerance. Tests 5–6 are there to explain a failure here.

**Every fit:**
8. **Final scratch drape.** Do the final scratch drape described above, and log warm-predicted vs scratch landmarks each time. That gives you a running record of whether the approach holds on that garment.

## Action items

1. **Log landmarks per frame on one scratch drape.** It shows whether a stopping rule alone gets most of the saving, and how much warm starting could add. It costs one drape and carries no risk.
2. **Run the per-group drapes in parallel.** Same answers, less time.
3. **Build the warm start.** Rest shape key, tests 1–2, stop-on-convergence, and the final scratch verification drape.
4. **Run tests 3–7 on one garment you know well.** If test 7 passes, adopt it. If it fails, tests 3–6 tell you whether the cause is friction, fold branching or plumbing, and whether to limit warm starts to some controls.
5. **Add the predictor or staged changes only if lengthening runs look wrong.**

I'd do 1 and 2 now, then 3 and 4 on that one garment before trusting warm starts more widely.
