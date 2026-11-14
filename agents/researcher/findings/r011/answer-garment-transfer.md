_Agent baseline for entries/garment-transfer-surface-binding.md (METHOD.md step 2b). Fresh general-purpose agent, claude-opus-5-5, 2026-11-14, prompt in prompt-garment-transfer.md. Its answer, verbatim:_

---

This answer comes from memory only, with no tools and no files. Blender field names and defaults are as I remember them and may differ slightly in your version, so check them.

## Short version

Don't start the second drape from the flat pattern. Start it from the garment that has already settled on the first body. Keep the flat pattern as the cloth's rest shape. Then morph the first body into the second **inside the simulation**, so contact and gravity push and drop the cloth into place.

That skips the expensive part of a fresh drape (closing the seams and the fall) and leaves only a local adjustment. You get the same fit as a fresh drape when:
- the two bodies share pose and mesh topology, and
- the garment stays loose, or stays tight, on both bodies.

You will not get the same folds in loose cloth. Two fresh drapes don't agree on folds either, so the check has to be against the spread of several fresh drapes, not against one.

## 0. Exact wins to check first

- **Cache.** Key each drape on a hash of the pattern mesh, fabric and solver settings, body mesh and Blender version. If the standard-figure step re-drapes designs whose inputs haven't changed, that work is pure waste, and reusing it is exact.
- **Reorder.** Every design goes through the standard figure anyway. If that drape can come first, it becomes the one fresh drape per design. Every other body is then a warm start from it, and the 11–15 minute step costs nothing extra.

## 1. The warm start in Blender

1. **Body correspondence.** Both figures need the same mesh topology, so figure B can be stored as a shape key on figure A. That is true if both come from the same parametric generator. They also need the same pose: a different arm angle is a much harder problem. If the topology differs, you need a registration step first. That is real work, so treat it as a precondition.
2. **Rest shape. This is the step that matters most.**
   - Set the garment's base positions to the settled drape on A (the last frame of the bake).
   - Store the flat pattern as a shape key and select it as the cloth's Rest Shape Key (Shape panel).
   - Without this, Blender takes spring rest lengths and bending rest angles from the starting mesh. The drape on A then becomes the cloth's natural shape: every fold turns into a remembered crease, and the stretch over hips and shoulders is silently set to zero.
   - Check it once: run the warm-start garment with zero gravity and no body. It should relax toward the flat pattern and not keep its folds.
3. **Animate the morph.** Animate the body shape key from 0 to 1 over M frames, then hold it for some frames to settle.
   - Keep fabric parameters, sewing, shrink and pins identical to the fresh drape.
   - Pinned vertices (e.g. a waistband) follow the mesh as it is before the Cloth modifier. Put a Surface Deform bound to the body above the Cloth modifier so the pins move with the morph.
4. **Morph speed and alignment.**
   - Per substep, the body surface must move less than the collision distance, or the cloth passes into the body.
   - Don't align the bodies at the feet. With feet aligned, the 14.4 cm height difference moves the shoulders 14.4 cm, and the kameez has to follow. Align near where the garments hang from: shoulders for the kameez and dupatta, waist for the trousers, roughly the waist for a whole outfit.
   - Turn on Single Sided in the body's collision settings, so a vertex that slips inside gets pushed out instead of stuck.
5. **Layering.** Transfer the garments with the same inter-garment collisions and order as the fresh pipeline (trousers, then the kameez over them, then the dupatta).
6. **Stop on convergence, not a fixed frame count.** Read the baked cache and require the largest per-vertex movement per frame, over the last ~10 frames, to be under a fraction of a millimetre. A fixed frame count is how a half-settled garment gets accepted.

**Why morph instead of mapping the garment geometrically.** The cheaper option is to bind each garment vertex to the nearest triangle of body A, evaluate it on B, then settle. That scales the garment with the body: a 9% taller figure stretches the garment about 9% along its length, but the pattern hasn't changed size. The settle then has to pull all of that back, which is large motion. Also, layers crossing in hollow regions (armpit, crotch, small of the back) produce intersections that self-collision cannot untangle. It's fine for tiny body differences. I wouldn't use it for 1.609 → 1.753.

**Expected saving.** Roughly 2–3x per piece, because a fresh drape spends much of its time, and its hardest substeps, closing seams and falling. That is a guess. Time it on five garments before building anything else.

## 2. When it matches a fresh drape and when it fails

A drape is one of many possible resting states: fabric can buckle many ways, and friction holds cloth wherever it stops. A fresh drape lands in one of them, chosen by the path the cloth took. The warm start lands in one near the drape on A. The two agree where the body decides the cloth's shape and disagree where the path does.

**Close enough when:**
- Pose and topology match, and the shape change is moderate.
- The garment keeps the same kind of fit on both bodies:
  - Ease (garment circumference minus body girth) at chest, waist and hip stays positive and similar on both.
  - No length landmark crosses a body feature: kameez hem vs knee, side-slit top vs widest hip, sleeve end vs wrist, trouser cuff vs ankle.
- What you care about is fit: where the cloth touches, how much ease there is, strain, hem/sleeve/slit positions and overall outline. This covers the bodice, shoulders, sleeves and waistband well.

**Fails or diverges:**
1. **The kind of fit changes.**
   - If girth grows in proportion to height (it often doesn't, which is why you check), 9% on an 88 cm chest is about 8 cm. That is roughly the ease of a fitted kameez, so a garment that is loose on A may have none on B.
   - The dangerous case is a pattern too small for B. A fresh drape fails visibly: seams don't close, or the cloth stretches badly. The warm start grows the body inside an already-closed garment and produces what looks like a tight fit. **It hides a garment that can't be worn.**
   - A pattern too large for B changes where the garment is held up (neckline slipping off a shoulder, waistband sliding). Friction can keep the warm result up where a fresh drape would slide down.
2. **Path-dependent parts.**
   - The dupatta is the worst: long free cloth whose end position depends on placement and friction, and which can land on the other side of an arm.
   - Kameez side-slit panels can overlap or separate differently.
   - Shalwar gathers vary.
   - Churidar ankle bunching: going tall to short, the extra length has to bunch by compression, a different mechanism from a fresh drape.
   - In all of these, the folds are inherited from A.
3. **Direction matters.** A growing body pushes the cloth, and contact decides where it goes, which is predictable. A shrinking body leaves slack that has to buckle into new folds while friction holds things in place. Expect B smaller than A to go worse, and high-friction fabrics to be worse.
4. **Mechanical failures:** cloth passing into the body because the morph was too fast, intersections locked in, the garment not settled, pins not following the body.
5. **Pose difference or poor body correspondence.**

**A side effect error numbers won't show.** If these drapes are used as data, warm results copy their folds from the source drape. Drapes of one design on different bodies then become correlated in a way fresh drapes aren't. That's fine for a picture, but it biases a dataset.

## 3. How to check it on a given garment

**Reference.** One fresh drape is not a stable reference. Run 3–5 fresh drapes on B, each with a change that should make no difference: pattern placement shifted 2–3 mm, one extra quality step, a slight rotation. The spread between them is the noise floor. The warm start passes if its distance to each fresh drape is no larger than the largest fresh-to-fresh distance. Use the maximum, since you only have a few pairs.

**Metrics.** Report them per region (shoulders/bodice, sleeves, skirt panels, waistband, legs, cuffs, dupatta). Never use one number for the whole garment: a good bodice and a bad skirt average out to "fine".
- **Per-vertex distance**, warm vs fresh. It's free because the garment mesh is identical. Report median and 95th percentile. It overstates error when cloth has slid along the body, so also compute:
- **Surface-to-surface distance** (Chamfer or Hausdorff). Large per-vertex distance with small surface distance means sliding, not a change in shape.
- **Gap map:** distance from body B to the garment, and overlap of the contact regions (gap under ~2 mm). This is the fit.
- **Strain against the flat pattern:** per-edge stretch, 99th percentile and maximum. This catches leftover pre-stretch and the hidden too-small case.
- **Landmarks in mm:** hem height (front, back, sides), slit top, sleeve end vs wrist, neckline, waistband height, cuff height.
- **Outline overlap** of front, side and back orthographic renders, for loose regions where folds legitimately vary.
- **Hard fails regardless of the rest:** vertices inside the body, more intersecting triangle pairs than the fresh drapes had, not converged.

**Calibrate once.** Use 20–30 designs covering fitted and flared kameez, shalwar, churidar and dupatta styles, crossed with body pairs of various size gaps in both directions. Plot each metric, as a multiple of the noise floor, against height change, girth change and ease change. That tells you which garment types and size gaps pass, and how much time is actually saved.

**On every warm result in production** (no fresh drape needed):
- **Before simulating:** check ease and landmark crossings from the pattern and body measurements.
- **After simulating:** check penetration, intersections, convergence, and that strain is within the range fresh drapes show.
- Anything outside the calibrated range, or failing a check, goes to a fresh drape.

**Audit.** Fresh-drape a random 5–10% of warm results and keep comparing, so drift from new styles, new figures or a new Blender version shows up.

**Visual lineup.** Render 4 fresh drapes and 1 warm one, and ask someone who knows these garments to pick the odd one out. If they can't beat chance, it passes for visual use.

**Fold copying, for dataset use.** Compute a wrinkle field per vertex in pattern space: the garment minus a smoothed copy of itself, or curvature. Correlate the A drape with the B warm result, and the A drape with a B fresh drape. If the warm correlation is clearly higher, folds are being copied.

## What I'd do first

1. **Check the cache and reorder wins.** About an hour, and the saving is exact.
2. **Prototype on 5 garments with one body pair (1.609 → 1.753).** Confirm the Rest Shape Key behaves as described, time it, and compare each result against 3 fresh drapes. This tells you whether the speed and accuracy are worth building the rest.
3. **If kameez and trousers pass, build the pre-simulation ease check and the post-run checks.** Keep the dupatta on fresh drapes until it passes separately.

I'd do 1 now and 2 next; 3 depends on what 2 shows.
