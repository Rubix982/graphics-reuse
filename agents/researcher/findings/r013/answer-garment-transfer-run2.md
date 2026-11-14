_Baseline run 2 for R-013: the R-011 garment-transfer prompt (`agents/researcher/findings/r011/prompt-garment-transfer.md`), unchanged. Fresh general-purpose agent, claude-opus-5-5, 2026-11-14, no tools. Arrived after the scoring list in `brouet2012-notes.md` was written. Its answer, verbatim:_

---

Answered from my own knowledge only. I used no tools and read no files.

**Short answer**

Keep the drape that has already settled and start the new body from it. Keep the flat pattern as the cloth's rest shape. Morph the body from figure A to figure B over a few dozen frames while the cloth simulates, then let it settle. This skips the seam-closing phase and most of the fall.

The result should match a fresh drape where the cloth is held in tension against the body: shoulders, a fitted bodice, the waistband, the hips. It will drift where the cloth hangs free and its folds depend on what happened before: the dupatta, flared hems, shalwar or churidar bunching at the ankle.

Check it against how much fresh drapes differ from each other, not against a single fresh drape. A fresh drape is only one of several equally valid resting states.

**Exact savings to take first (no approximation)**

1. **Stop when the cloth has settled, not at a fixed frame count.** Log the maximum vertex speed per frame for a few drapes. If the cloth sits still for the last part of the run, a rule like "stop when max speed stays below a threshold for k frames" saves that time at no cost to accuracy. Check this first. It might be the biggest win, and it applies to the warm start too.
2. **Cache.** Key each drape on a hash of the pattern mesh, material and solver settings, body mesh and Blender version. The standard-figure step can then skip any garment it has already draped. This only helps if repeats happen.
3. **Reorder, if the pipeline allows it.** If every design's first fresh drape were on the standard figure, the standard step would be free. Every other body would then warm-start from the standard figure. A standard figure near the middle of your body range keeps every morph short.

**How the warm start works in Blender**

- **Body.** A and B need the same mesh topology (the same parametric body model) so that B can be a shape key on A. Keyframe that shape key from 0 to 1 over M frames. The body keeps its Collision modifier; Blender handles colliders that deform.
- **Garment.** The positions settled on A become the starting state, for example as a shape key set to 1. The flat pattern stays the rest state through the cloth's Rest Shape Key setting.
  - This must not go wrong. If the shape draped on A becomes the rest shape, A's stretch and sag get baked in as if they were the fabric's natural shape.
  - I'm fairly but not fully sure the stretch, shear and bending rest values all come from the rest shape key. Verify that in your Blender version.
  - The sewing edges are already near zero length, so the sewing force starts near zero.
- **Pinned vertices**, if any, must follow the morph (Surface Deform bound to the body).
- **Run** M morph frames, then settle until the stop rule fires.

**Why morph instead of projecting the garment onto B and settling**

Projection (nearest-point binding) is faster, but it leaves cloth inside the body or through other cloth layers wherever the two bodies differ. Blender's collision does not reliably recover from starting inside the body: vertices get pushed out the wrong side or stay stuck. Projection is also ambiguous under the arms and at the crotch, where a nearby surface point could be on the arm or the torso, or on either leg.

Morphing keeps collisions valid at every step, as long as the body moves less than the collision distance per substep. From 1.609 m to 1.753 m is 14.4 cm, about 9%. Spread over a few hundred substeps, that is under a millimetre per substep.

The saving is roughly (frames in a fresh drape) ÷ (morph frames + settle frames), maybe more if you can use fewer substeps without the sewing phase. I can't give you a number. Measure it.

**When it will be close to a fresh drape**

- **Only the body changes.** Pattern, material, solver and collision settings, pose, and the order layered pieces are simulated in all stay the same.
- **What touches what doesn't change.** For each girth (bust, waist, hip, thigh, ankle opening), look at ease = pattern circumference minus body circumference. For each length, look at where the hem falls relative to knee, ankle and floor. If no ease goes from loose to roughly zero and no hem crosses a landmark, the warm start should land near the fresh result.
- **The regions downstream cares about are in tension.** Cloth in tension has close to one resting shape, and both methods find it.
- **The body morph is smooth and doesn't pass through itself**, for example arms into the torso.

**When it will fail**

- **What touches what changes.** These are qualitative differences, not small errors:
  - trousers that pool on the shorter figure hang straight on the taller one;
  - a kameez that is loose over the bust on one body is tight on the other;
  - a dupatta slides off a shoulder in the fresh drape but stays on in the warm start, or the reverse.
- **Friction keeps the history.**
  - Large body to small: the freed slack folds wherever it happens to be. In a fresh drape it falls and spreads out.
  - Small body to large: friction can stop the cloth sliding over the body, so strain bunches (above the bust, at the hips) instead of spreading evenly.
  - Cloth gets caught in hollows: under the arms, the crotch, between the thighs, under the bust.
  - Two fixes to test: lower the collision friction during the morph and restore it for the settle, or give the cloth a short kick (a brief wind or gravity pulse) before settling.
- **Layers.** Kameez over trousers and dupatta over kameez are a risk. Cloth-on-cloth collision is less robust than cloth-on-body, and layers pressed together at the waist can pass through each other. Keep the fresh pipeline's order. If the dupatta is the problem, drape it fresh on top of a warm-started kameez and trousers.
- **Large body changes.** Far enough from the old resting state, you lose the speed gain and keep the risk. There is a break-even distance; find it by testing.
- **A different pose** is a separate problem. Don't mix it into this one.

**How to check whether it worked on a given garment**

The trap is comparing the warm start with one fresh drape and calling every difference an error. In free-hanging cloth, fold positions move between fresh drapes when the inputs change slightly.

1. **Measure the noise floor.**
   - Pick 10–20 validation designs covering fitted and flared kameez, shalwar and churidar, and a few dupatta styles.
   - Drape each fresh on B three times with tiny changes, such as moving the starting placement by about 1 mm or changing the substep count.
   - Before that, check whether two identical runs give identical output. If they don't, that variation is already a floor.
   - How much these fresh drapes differ from each other is what "close enough" means.
2. **Warm-start A→B** on the same designs.
3. **Pass/fail checks.** Run these on every warm start in production too. Any failure means falling back to a fresh drape.
   - No garment vertex inside the body.
   - No cloth-through-cloth triangle intersections.
   - Seams closed: sewing edge length below a tolerance.
   - Settled: max vertex speed below a threshold for k frames.
   - Maximum edge stretch (length ÷ flat-pattern length) within the range fresh drapes reach.
4. **Comparison metrics by region**: shoulders, bust, waist, hips, sleeves, hem, dupatta. The pattern mesh is the same, so vertex-to-vertex matching is free.
   - **Fit:** gap between each garment vertex and the body, and stretch per edge. These should match closely where the cloth is in tension.
   - **Shape:**
     - per-vertex distance (mean, 95th percentile, max), which is strict about fold positions;
     - a surface distance such as Chamfer, which tolerates folds sliding;
     - hem height and circumference;
     - silhouette overlap from front, side and back renders.
   - **Energy:** approximate stretch + bending + gravity energy from positions and rest lengths. If the warm start's energy is clearly higher, it is stuck in a worse resting state, such as a trapped fold. Similar energy with different folds means it found an equally valid state.
5. **Write the decision rule before looking.** Accept a garment type when every check passes and each warm-vs-fresh metric falls within the fresh-vs-fresh spread.
   - I'd expect fitted pieces to pass and the dupatta and flared hems to fail on fold-sensitive metrics.
   - Whether that matters depends on what the standard-figure drape is for. If it feeds fit or measurement, the body gap and stretch are the metrics. If it feeds images, folds matter visually, but a fresh drape's folds are also arbitrary, so "within the fresh spread" is the fair bar.
6. **Cheap flags per garment in production** (no fresh drape needed):
   - predict whether what touches what will change between A and B: any ease reaching zero, any hem crossing a landmark;
   - kick and re-settle; if the shape moves a lot, it was trapped in an unstable state;
   - optionally, warm-start from two different source bodies; if the results disagree, that region depends on history, so drape it fresh.
7. **Spot audit.** Also drape a random ~5% of garments fresh and log the metrics. Garment types missing from the validation set will show up there.

A plain claim that could turn out false: "On these garments, the warm-started drape differs from a fresh one by no more than two fresh drapes differ from each other, everywhere except the dupatta."

I'd skip a learned drape predictor (neural garment models) for now. It needs training data for each garment family and has the same checking problem.

**Next steps, in priority order**

1. Measure frames simulated against frames until settled in a few fresh drapes. If there's slack, the stop rule is free speed.
2. Prototype the morph warm start on 3 designs: one fitted kameez with shalwar, one flared, one with a dupatta. Run 1.609→1.753 m and the reverse, with the noise-floor comparison. This gives the real speedup and shows which garment parts are safe.
3. Add input-hash caching.
4. Then decide whether to reorder the pipeline around the standard figure.

I recommend 1 and 2 first. Step 1 has no accuracy cost, and step 2 is the only way to learn whether the warm start's errors stay inside the noise floor for your garments.
