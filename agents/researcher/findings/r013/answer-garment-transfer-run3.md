_Baseline run 3 for R-013: the R-011 garment-transfer prompt (`agents/researcher/findings/r011/prompt-garment-transfer.md`), unchanged. Fresh general-purpose agent, claude-opus-5-5, 2026-11-14, no tools. Arrived after the scoring list in `brouet2012-notes.md` was written. Its answer, verbatim:_

---

Answered from my own knowledge, with no tools and no files. I've given Blender option names from memory, so check them in your version.

**Short answer**

Start the new drape from the drape you already have, not from the flat pattern. Move the settled garment from body A to body B, keep the flat pattern as the cloth's rest shape, and simulate only until the cloth settles again.

This should match a fresh drape wherever the body decides the cloth's shape:
- fitted parts pulled against the body;
- cloth hanging straight down.

It will give a different but equally plausible result wherever history decides the shape, meaning cloth folded on itself and held there by friction:
- the dupatta;
- a gathered shalwar;
- the bunching at a churidar's ankle;
- the folds of a flared kameez.

To find out which case a garment is in, compare against the fresh drapes the pipeline already makes. Judge the gap against how much fresh drapes disagree with each other, not against zero.

**1. The approach**

A drape is a resting state of a fixed piece of cloth on a fixed body. The cloth is fixed by its rest shape (the pattern) and its material settings. A fresh drape and a warm start solve the same problem from different starting points. The rule is to keep the problem identical and change only where it starts.

Setup in Blender:
- **Save the A drape.** At the settled frame, use Apply as Shape Key on the cloth modifier. Keep the flat-pattern positions as the Basis.
- **Start from it.** In the new simulation, set that shape key to 1 so the cloth starts draped.
- **Keep the pattern as the rest shape.** Set Physics > Cloth > Shape > Rest Shape Key to the flat-pattern Basis. This is the step that matters most. If the draped mesh becomes the rest shape, every spring length and bending angle comes from the A drape. The cloth then keeps A's folds and stretch on body B, and you get a fast, confident, wrong answer.
- **Change nothing else.** Material, collision distances, friction, quality steps, pin groups and sewing settings should all match the fresh drape.

There are two ways to move the garment to body B:
- **(a) Morph while simulating (my default).** Give body A a shape key that turns it into body B. Animate it from 0 to 1 over some tens of frames while the cloth simulates, then hold at B until the cloth settles. As far as I know, CLO and Marvelous Designer do something like this when you swap avatars. Morph slowly: the body should move well under the collision distance per substep, or cloth passes through the body.
- **(b) Deform, then relax (faster, less robust).** Bind the settled garment to body A with a Surface Deform modifier, switch the body to shape B, then simulate until settled. The deform step scales the garment with the body. If the taller figure is mostly a scaled-up one, the kameez is briefly about 9% longer than the cloth really is, and the relax has to pull that back out. This is fine for small body changes. For large ones the starting point is far from rest, most of the saving is lost, and cloth can start inside the body or inside a lower layer.

Other points:
- **Body correspondence.** Both methods need each body vertex matched to a vertex on the other body. If both figures come from the same body generator with the same mesh, this is just a shape key. If not, you have to fit a template mesh to both bodies, and that fitting is the most likely place for the method to fail. Expect trouble at the armpits and crotch, where two body surfaces sit close together.
- **Layers.** Transfer in draping order (trousers, then kameez, then dupatta), each over the already-transferred layer below. Or morph all layers together, so no layer starts inside another.
- **Never chain transfers.** Go from a fresh drape to each target, not A to B to C. A chain piles up history, and any defect in the first drape is inherited by everything after it, such as a fold trapped under the arm or a seam caught on the shoulder. Every design passes through the standard figure, so the natural setup is one fresh drape there and a warm start to every other body.
- **Cache exact repeats.** If the same design is re-draped on the same standard figure more than once, store the result keyed on pattern, material, body mesh, simulation settings and Blender version. That reuse is exact, not an approximation.

**What it saves**

A fresh drape spends frames on three things:
- closing seams, with pieces travelling tens of centimetres and many collisions;
- falling onto the body;
- damping out the leftover motion.

The warm start skips the first two and most of the third, so its cost grows with how different the two bodies are. Before building anything, open one fresh drape's cache and see what share of frames comes after the garment has landed and the seams are closed. That share is roughly the floor the warm start can't beat. My guess is a few times faster for similar bodies, but that's untested and should be measured before you plan on it.

**2. When it is close enough, and when it fails**

The question that decides it is whether the garment has one resting state on body B or many. If it has one, both routes reach it and the warm start just arrives sooner. If it has many, each route lands on a different one, and the warm start lands on the one nearest A's drape.

Likely to match a fresh drape:
- **Fitted regions held tight against the body:** kameez shoulders, bust, armholes and upper back; trouser waist and seat; fitted sleeves.
- **Cloth hanging freely without folding on itself:** a straight kameez below the hip, straight trouser legs. Small ripples may differ.
- **Simple landmarks:** hem height above the floor, where the sleeve ends, neckline position, waistband height. On the taller figure the same kameez should end higher on the leg, and the warm start should let it ride up.
- **Moderate, smooth body changes in the same pose, with matching meshes.** Going from 1.609 m to 1.753 m is about a 9% height change. If girths grow with it, a kameez with a few centimetres of ease can go from loose to tight. That's acceptable, because tight is the well-determined case, as long as the garment still fits at all.

Likely to differ:
- **Dupatta.** It is large and light, folds on itself, and rests on shoulders and arms by friction. A fresh drape picks one fold arrangement and the warm start keeps something close to A's. Both are physically valid, but they won't match point for point.
- **Shalwar (especially Patiala) and flared or anarkali skirts.** How many folds form, and where, has many valid answers. The warm start inherits A's.
- **Churidar ankle bunching, which fails differently in each direction.**
  - Taller to shorter: the extra length has to buckle into new bunches, and where they form is arbitrary.
  - Shorter to taller: existing bunches have to slide up the leg against friction. They can stay stuck where a fresh drape would have none.
- **Kameez side slits.** The front and back skirt panels hang separately, and which one ends up on top is history.
- **A garment too small for body B.** A fresh drape might fail to close its seams. The morph can drag a closed garment onto the bigger body and report a high-strain drape that a fresh drape would never produce. This failure is hidden unless you check strain.
- **Large or uneven body changes, pose changes such as arm angle, or a poor body correspondence.** Cloth gets dragged to the wrong place, especially at the underarm and crotch.
- **Setup errors:**
  - the rest shape taken from the draped mesh, which bakes in A's folds;
  - a morph too fast, so cloth passes through the body;
  - seams behaving differently when the simulation starts already sewn.
- **Runs stopped before settling.** Fresh drapes with a fixed frame count can have this problem too, so compare settled runs with settled runs.

"Close to a fresh drape" only means something relative to how much fresh drapes disagree with each other. Nudge the pattern pieces a few millimetres before sewing and a fresh drape's dupatta will also come out different. That spread is the baseline the warm start should be judged against.

**3. How to check**

Every run uses the same garment mesh, so each vertex is the same point of fabric in every run. That means positions and strains can be compared directly, with no matching step.

One-time calibration, which is cheap because the pipeline already produces fresh drapes on the standard figure:
1. **Identity test.** Morph A to A, so the body doesn't change, starting from A's drape. The garment should not move beyond settling noise. If it moves, the setup is wrong, most likely the rest shape or the sewing. Then do a round trip, A to B to A. Fitted regions should come back, and whatever doesn't come back shows you which regions depend on history.
2. **Baseline spread.** For a handful of designs, run 2–3 fresh drapes on B with the pieces nudged a few millimetres. If Blender gives identical results on reruns, the nudge is the only honest source of spread.
3. **Side-by-side runs.** For the next 10–20 designs through the standard-figure step, run the warm start next to the existing fresh drape. Cover each garment type (fitted kameez, flared kameez, straight trousers, shalwar, churidar, dupatta) and both directions (taller to shorter and shorter to taller).
4. **Measure per pattern piece**, because the dupatta would swamp any whole-garment average:
   - **Point-to-point distance:** median, 95th percentile and maximum.
   - **Surface-to-surface distance,** which needs no point matching. A large point distance with a small surface distance means the cloth slid or folded differently but fills the same space: fine for rendering, maybe not for print placement.
   - **Strain:** each edge's current length divided by its flat length, especially in fitted regions, since that's what fit decisions read.
   - **Body-to-cloth gap (ease)** in fitted regions.
   - **Landmarks:** hem, sleeve end, neckline, waistband, trouser hem.
   - **Penetrations** (cloth inside body, layer inside layer) and **leftover motion** in the last frames.
5. **Set the pass rule before looking at results.** For each piece, the warm-vs-fresh gap should be no larger than the fresh-vs-fresh spread at the 95th percentile. Landmarks should be within a tolerance chosen from how the drape is used downstream. There should be no penetrations, and the run should be settled. Then plot the gap against body difference to see how far the transfer can stretch before it breaks.

Checks on every garment in production, without a fresh drape:
- **Settled:** the largest per-frame vertex movement over the last ~10 frames is below a threshold.
- **No penetrations.**
- **Strain within the range fresh drapes of that garment type show.** A stuck garment usually shows up as a high-strain patch.
- **Landmarks move sensibly:** the hem height changes with the body in the expected direction and by roughly the expected amount.
- **Inside the calibrated range:** the garment type and body difference are ones the calibration covered.
- **Random audit:** one in N garments also gets a full fresh drape, logged, to catch drift.

Anything that fails falls back to a fresh drape. The worst case then costs a warm start plus a fresh drape, which is still a net saving if most garments pass.

For the dupatta and gathered pieces, decide what you need. If you only need a plausible drape for rendering, compare overall shape, hem line and strain, not point positions. If you need the fresh drape specifically, keep fresh-draping only those pieces.

Here is the claim the calibration tests, in one sentence: "On a fitted kameez moved from the 1.609 m figure to the 1.753 m figure, the warm start puts the hem, sleeve ends and neckline within X mm of where a fresh drape puts them, in a fraction of the time, and the dupatta won't match fold for fold." If X comes out larger than your tolerance, that's the result telling you not to use it for that garment type.

**Next steps, in priority order**
1. **Profile one fresh drape:** count frames before and after the garment lands. This sets the maximum possible saving and takes minutes.
2. **Check whether the two figures share the same mesh.** If they do, the morph approach is straightforward. If they don't, matching the bodies becomes the main job, so reconsider before going further.
3. **Build the morph-while-simulating warm start** with the flat pattern as rest shape, and run the identity test.
4. **Run the side-by-side comparison** on the next 10–20 designs, plus the baseline spread on a few, with the pass rule written down first.
5. **Switch over garment type by garment type** as each passes. Keep fresh drapes for types that fail, probably the dupatta and gathered trousers, with the production checks and random audits in place.

I recommend 1, then 3, then 4. Add the cache at any point if the pipeline step reruns the same designs.
