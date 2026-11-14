# R-011 · Agent baselines for the three seed entries: scoring

_2026-11-14. Three fresh general-purpose agents (claude-opus-5-5), no tools, prompts in this folder, answers saved verbatim beside them. Scored by Claude against each entry's sections 4–6, as written before the agents ran. A condition counts as named if the answer states the same condition in any words; "partly" if it names the case but not the mechanism, or the mechanism in a different form._

## Read this first

The entries were written by the same model, from paper abstracts and its own knowledge, on the same day. Most of what they say came from what that model already knew, so an agent of that model naming it was expected. As with R-004, the test can't do what it looks like it does. What it can show is the part of each entry that came from outside the model: the test bed's measurements, and anything read in a source in full. So far that is only the measurements.

## Garment transfer by surface binding

**Technique.** The agent proposed something else first: start from the settled garment, keep the flat pattern as the rest shape, and morph body A into body B inside the simulation. It also proposed two exact wins: cache drapes by a hash of their inputs, and drape on the standard figure first so it becomes the one fresh drape per design. It considered surface binding and rejected it for a 1.609 → 1.753 m gap.

| Entry condition (section 4–5) | Entry's mark | Baseline |
|---|---|---|
| Binding stretches the garment with the body; it comes out graded, not the same garment | measured | named ("a 9% taller figure stretches the garment about 9% along its length") |
| Valid only where the garment lies close to the body; free-hanging cloth tears | measured | partly: named the dupatta as the worst case, for path dependence, not the tearing |
| Needs a correspondence when the meshes' numbering differs | measured | named (same topology or a registration step first) |
| The relax afterwards is short when the binding is close | reasoned | **disputed**: "The settle then has to pull all of that back, which is large motion" |
| A fixed-size garment comes out resized | reasoned | named (the pattern hasn't changed size) |

Checks (section 6): points inside the body, edge stretch, crossings, comparison with several fresh drapes within their spread. All four named.

Count: 3 named, 1 partly, 1 disputed, 4 of 4 checks.

What only the entry had: the measured numbers (1.2 s against about 6 minutes; edges 1.06–1.07× at the median and 1.22–1.30× at the 95th percentile; the dupatta 4.9× with 96 points inside). The agent guessed 9 % stretch and a 2–3× saving.

Conditions the baseline named that the entry lacks:
- Keep the flat pattern as the cloth's rest shape, or the drape on A becomes its natural shape (folds turn into creases, stretch silently set to zero). Test: zero gravity, no body, it should relax toward flat.
- Align the bodies where the garment hangs from (shoulders, waist), not at the feet.
- Morph speed: the body surface must move less than the collision distance per substep.
- A pattern too small for B: a fresh drape fails visibly; the warm result looks like a tight fit and **hides a garment that can't be worn**. Check ease before simulating.
- Direction: a shrinking body goes worse than a growing one.
- Warm results copy folds from the source drape, which biases a dataset of drapes.
- Report metrics per region; per-vertex distance overstates error when cloth slides, so pair it with surface-to-surface distance.

## Warm-starting repeated drapes

**Technique.** Proposed this technique, unprompted.

| Entry condition (section 4–5) | Entry's mark | Baseline |
|---|---|---|
| The change between runs is small | reasoned | named ("moves smoothly as the cut changes across the perturbation") |
| The two cuts' meshes correspond, directly or through pattern coordinates | reasoned | named (warp the mesh, or look each vertex up in pattern space) |
| Cloth has many resting shapes; a warm start finds the nearest | reasoned | named, more sharply ("Scratch lands there too… the condition that's easy to miss") |
| History dependence across rounds | reasoned | named ("chaining three steps adds up the path dependence") |
| Sensitivity drapes warm-started from one base share its folds, so responses come out too small | reasoned | named ("sensitivities for landmarks that hang from a friction support to come out too small") |
| A large change saves little | reasoned | partly: said the saving depends on where the time goes, with an estimate (about 6 settle time constants down to 4) |

Check: warm against fresh over several runs, within their spread. Named, with four more tests.

Count: 5 named, 1 partly.

What only the entry had: nothing beyond the test bed's numbers it quotes in section 2, which were in the prompt.

Conditions the baseline named that the entry lacks:
- The rest shape again: the new flat pattern as the rest shape key, the settled drape as the starting positions.
- Shortening and lengthening differ: a lengthened piece is compressed and can crumple and stick against friction. A predictor x ≈ x0 + F·(u − u0), or staged changes.
- Measure each sensitivity against a warm run at the unchanged cut, so drift from an unsettled base cancels.
- Use warm starts for sensitivities and fresh drapes for the residual: one fresh drape at the start, one at the final cut, and the second becomes the new base if the warm chain drifted.
- Cheap tests: the null test (warm at the unchanged cut moves nothing), the rest-source test, the round trip (hysteresis), ±δ symmetry (contact changes).

## Coarse-to-fine cloth

**Technique.** Proposed a coarse drape, mapped onto the full mesh, then a short full-resolution settle. It didn't mention multigrid or learned upsampling. It ranked stopping at convergence and a cheaper collider first.

| Entry condition (section 4–5) | Entry's mark | Baseline |
|---|---|---|
| Multigrid gives the fine answer; validity is convergence and tolerance | paper | missed |
| Upsampling is valid when the large-scale shape is judged, not when folds are measured | reasoned | named, and went further: the outline itself can depend on folds |
| A coarse mesh has to resolve the contacts that matter | reasoned | partly: a flat coarse triangle dips inside a curved body part by about h²/(8R) |
| Multigrid needs access to the solver | reasoned | missed |
| Learned folds may transfer poorly across garments | reasoned | missed (it proposed no learned operator) |
| Detail added after can push cloth through the body or other cloth | reasoned | named (crossings during the cheap phase are permanent) |
| A coarse garment can settle on a different support | reasoned | named (a sleeve against the torso or hanging free) |

Check: against several full drapes within their spread, judged per metric. Named.

Count: 3 named, 1 partly, 3 missed. All three misses are about the two mechanisms the agent didn't propose.

What only the entry had: multigrid as a route to the same answer, and the split between the two mechanisms.

Conditions the baseline named that the entry lacks:
- **A flared garment's outline depends on its folds.** A coarse mesh makes fewer, stiffer folds, so the silhouette changes as well as the wrinkles. For a flared gharara this is the case that matters.
- Mass and stiffness don't carry across resolution in Blender: vertex mass is per vertex (scale it), and stiffness has to be calibrated on a swatch at both resolutions.
- The fine stage must keep its own rest lengths, or it inherits the coarse stretch and agrees for the wrong reason.
- The full drape used as the reference must itself have settled.
- Self-collision switched off early and back on later doesn't undo crossings.

## Result

Across the three entries the baseline named 11 of 18 conditions, partly named 3, disputed 1 and missed 3. It named every check. All three misses came from one entry and concern mechanisms the agent didn't propose. In each case it also named several conditions the entry lacks.

Read with the caveat above, this says three things:

1. The seed entries are under-written. A five-minute answer from the same model is more complete than entries written from abstracts.
2. What an entry adds over the agent is what came from outside the model. Here, that's the test bed's measurements: the agent guessed 9 % stretch where the test bed measured 6–7 % at the median and 22–30 % at the 95th percentile.
3. The dispute on the relax is worth keeping. The entry's reasoned condition (a short relax) and the agent's reasoned objection (pulling back the grading stretch is large motion) can't both be right, and only a measurement settles it.

On T-008: all three entries change the answer (or depend), and the agent still named most of their conditions. There is no cost-only entry to compare, and the circularity applies, so this neither supports nor sinks T-008.
