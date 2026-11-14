_Agent baseline for entries/coarse-to-fine-cloth.md (METHOD.md step 2b). Fresh general-purpose agent, claude-opus-5-5, 2026-11-14, prompt in prompt-coarse-to-fine.md. Its answer, verbatim:_

---

I answered from my own knowledge only. I used no tools and read no files.

**The principle**

Everything the pipeline measures is a property of the cloth once it has stopped moving. So you can change anything that only affects how the cloth gets to rest: how many frames you run, where the cloth starts, how much damping there is, and how fine the mesh is on the way down. You can't change anything that affects where it ends up: total mass, stretch stiffness, rest lengths, and the body surface it touches. The shortcut fails exactly when the final shape depends on the path the cloth took. Cloth on a body does behave that way in places, because friction and contact give it more than one stable resting shape.

**First, find out where the 4–7 minutes go**

Bake one garment three ways: as normal, with self-collision off, and with a simplified body as the collider. Log the time per frame and the frame at which the cloth stops moving. With 5k-vertex pieces I'd guess that collision and self-collision cost more per frame than the spring solve. I'd also guess the fixed frame count runs well past the point where the cloth settles. Both are guesses to check, and the answers decide which lever below matters.

**What to change, in the order I'd try it**

1. **Stop when the cloth has settled, not at a fixed frame.** Track how far the fastest vertex moves per frame. Also track the measured numbers themselves (hem height, sleeve length). Stop when both have stayed under a threshold for N frames in a row. This is the lowest-risk change. It fails when the cloth creeps slowly, like a skirt sliding down the hips or a sleeve peeling off the torso. Each frame's movement is then tiny but the total drift is not, which is why the test has to watch the landmark numbers over a window of frames.

2. **Drape a coarse mesh first, then finish at full resolution.**
   - **How it works:** drape a coarser version of each piece (about twice the edge length, so about 1,250 vertices) through the falling, sewing and settling phase. Then map the result onto the full 5k mesh and run a short full-resolution settle so folds form and collisions clear.
   - **Why it can work:** gravity, stretch and contact with the body set the large-scale shape, and a coarse mesh can carry those. It can't carry folds, because a mesh can't show a fold narrower than a few edges. That is why the full-resolution settle at the end is required.
   - **Building the coarse mesh:** re-triangulate the flat pattern at the larger edge length, with the same number of vertices on both sides of each seam so sewing pairs still line up. Decimating the 3D mesh instead gives irregular triangles that stretch unevenly.
   - **Mass:** keep the total mass the same. Blender's mass setting is per vertex (worth confirming on your version), so a mesh with a quarter of the vertices needs four times the vertex mass.
   - **Stiffness:** don't assume Blender's stiffness settings behave the same at both resolutions. Calibrate on a test swatch (a rectangle hung from one edge, or a disc over a cylinder) draped at both resolutions. Adjust the coarse stiffness until its hang length and outline match the fine one.
   - **Transfer:** use something like the Surface Deform modifier, bound while both meshes are at rest. The fine mesh must start at the transferred positions but keep its own original rest lengths. If the fine solve treats the transferred shape as its rest shape, it keeps whatever stretch the coarse run had, and it will agree with the coarse result for the wrong reason. Check which shape the cloth modifier uses as rest in your setup.
   - **Penetration at transfer:** a flat coarse triangle over a curved body part dips inside it between its corners. The dip is about h²/(8R), where h is the coarse edge length and R is the radius of the body part. For h = 3 cm over an upper arm with R = 4 cm, that is about 3 mm. If the dip is larger than your collision distance, fine vertices start inside the body, so offset the transfer outward by that amount.
   - **Expected gain:** a few times faster, not ten times, because the fine settle still needs enough frames for folds to develop.

3. **Collide against a cheaper body.** Use a simplified, slightly inflated copy of the body, with regions the garment can't reach removed (head and feet for a skirt). Inflate it by the deepest point where the simplified copy falls inside the real body. Then cloth resting on the copy can't be inside the real body.
   - **The cost:** the cloth sits outward by up to that offset. This is acceptable when the offset is small next to one silhouette pixel at the photo's scale and next to your landmark tolerance.
   - **The check that doesn't change:** the final penetration test still runs against the real body.

4. **Start from a previous drape, if your drapes are related.** This applies to the same garment on many bodies, several sizes, or a fitting loop that re-drapes after small parameter changes. Start from the previous result instead of the flat pattern. In a fitting loop this may be the largest saving of all. It is also where path-dependence bites hardest: the loop can settle on a resting shape that a drape from scratch would never reach.

**What I wouldn't do:** turn self-collision off early and on at the end. Once two layers of cloth have passed through each other, Blender's self-collision (as far as I know) has no step that separates them back onto the right sides. The crossing survives into the final mesh. This is only safe for garments where no two layers touch on the way down.

**When it gives the same answer, and when it doesn't**

It agrees when there is effectively only one resting shape, and that shape is set by things the shortcut keeps. That is typical of fitted or stretched garments. It is also typical of hems and sleeves that hang freely from a clear support like the shoulders or a waistband. Hem height then comes from fabric length, weight and stretch, which survive both the coarse mesh and early stopping.

It fails in four situations:
- **The outline depends on the folds.** A flared or circle skirt is held out partly by its folds, and so is a cowl neck. A coarse mesh makes fewer, stiffer folds, so the outline changes, not just the wrinkles.
- **Friction allows more than one resting shape.** Examples are a sleeve resting against the torso versus hanging free, or a loose dress caught on the hips. A different path can end in a different one.
- **The fold measure itself.** Where folds sit depends on history, and how narrow they can be depends on mesh resolution. At best the shortcut keeps the total amount of folding, never the position of individual folds. Even that only holds if the fine settle runs long enough for the cloth to buckle.
- **Layered cloth.** Any crossing between layers during the cheap phase is permanent.

One caveat about the reference: if your current full drape is still moving at its last frame, it is the wrong target. An early-stopped run that has truly settled could disagree with it because the full drape is the one that's off.

**How to check whether it worked on a given garment**

1. **Measure how much the full drape disagrees with itself.** Run it 3–5 times with tiny changes: shift the starting position by a millimetre or two, or use one more or one fewer quality step. The spread of each metric across these runs is your noise floor. Without it you can't tell "the shortcut changed the answer" from "the answer is this sensitive anyway". The fold measure especially will vary between full runs.
2. **Check that the full drape has settled.** Plot hem height, sleeve length and the fold measure against frame number.
3. **Compare the cheap drape with the full one.** Compute every metric the pipeline uses. Compare the cheap result directly against the full drape (silhouette overlap with the full drape's silhouette, not only with the photo). It passes when, for every metric, the cheap-vs-full difference is inside the full-vs-full spread. Set these thresholds before you look at the results.
4. **Treat penetration as a hard pass/fail.** It must be zero on the final full-resolution mesh, against the real body (not the simplified one) and between all cloth pieces.
5. **When it fails, find out where.** Both final meshes have the same vertices, so a per-vertex distance map shows where they differ. Large differences at folds are expected. Large differences at a hem or sleeve end mean the large-scale shape broke. Also compare how stretched the edges are in each mesh. If the cheap run shows almost no stretch where the full run is stretched, the fine stage used the wrong rest shape.
6. **Check the decisions, not just the numbers.** If the pipeline decides something (which size fits, pass or fail against the photo), check that those decisions agree across a batch of garments. Small metric shifts that never flip a decision may not matter.

In production, run the cheap checks on every drape (the settling test and the real-body penetration test). Re-run a random few percent with full drapes to catch garment types where the shortcut starts to drift.

**What to do first**
1. Profile one garment and check whether the full drape has settled by its last frame. This takes about an hour and tells you which lever matters.
2. Add the stop-when-settled rule. It has the smallest risk, and it may be the whole win if the frame count is padded.
3. Build the self-disagreement check on 3–5 representative garments: one fitted, one flared, one layered.
4. Try the coarse-then-fine approach on the fitted garment first, where it is most likely to hold, and on the flared one second, where it is most likely to fail.

My recommendation is to do 1 and 2 before anything else, and only try coarse-then-fine if they don't save enough.
