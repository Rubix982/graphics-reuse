# Card

_Template at the top, the live card below it, closed cards with their results at the bottom. One card open at a time; a card that takes more than one sitting to fill is too big._

## Template

1. **WHERE WE ARE.** The last thing established, as a number or a fact. One sentence.
2. **WHAT WE ARE DOING.** One action, stated so a second person could carry it out without asking.
3. **WHY.** What is not known now that will be known after.
4. **WHAT IS AFFECTED.** Which claims, files or numbers change if this comes back either way.
5. **CONCLUSION IF WE DO IT.** Both branches, in advance.
6. **CONSEQUENCE OF NOT DOING IT.** What breaks, stalls or stays unknown if this is skipped forever.

A card closes with a number, or with a sentence that could have come out the other way.

---

## Live card · R-012 · Do the axes hold on techniques they weren't built from?

_Opened 2026-11-14._

1. **WHERE WE ARE.** The six axes sorted 12 of 12 techniques cleanly (R-004), but all twelve came from the conversation that produced the axes, so the sort could hardly have failed.
2. **WHAT WE ARE DOING.** Draw graphics papers about speedups by a fixed procedure, and sort each one: is its speedup reuse at all; if so, which axis per mechanism, and does the reuse change only the cost or the answer too. The procedure: search DBLP (or Semantic Scholar, if DBLP can't filter by venue) for papers in ACM Transactions on Graphics, 2000–2025, whose titles contain *fast*, *faster*, *efficient*, *accelerat-* or *real-time*; save the full hit list and the exact query; shuffle it with Python's `random.Random(1114).shuffle`; go down the shuffled list sorting each paper from its abstract, until 20 papers whose speedup is reuse have been sorted. Record every paper looked at, including the ones that aren't reuse.
3. **WHY.** Whether the axes fit reuse techniques nobody chose with the axes in mind is unknown. The title words describe speed, not any kind of reuse, so they don't steer the sample toward an axis. The share of speedup papers that are reuse at all comes out as a side number.
4. **WHAT IS AFFECTED.** The axis table in `README.md`, the `axis` field in `entries/_template.md` and in the entries, and the survey tickets R-005 to R-010 (one per axis, blocked on this card).
5. **CONCLUSION IF WE DO IT.** If at least 16 of the 20 reuse papers sort cleanly (each mechanism onto exactly one axis), the axes hold beyond their own examples, and the surveys unblock. If 5 or more don't, revise the axes before writing more entries, recording which papers broke them and how. Either way, if "across runs" again gets none, that is evidence for folding it into "across time" (T-009).
6. **CONSEQUENCE OF NOT DOING IT.** The library grows under axes that are only known to fit the examples they were made from, and the surveys stay scoped by them.

**Result:** —

---

## Closed cards

### R-004 · Do the six axes hold?

_Opened and closed 2026-11-14._

1. **WHERE WE ARE.** Three entries exist (one tested in part, two untested), filed on six axes that came from about ten examples in one conversation.
2. **WHAT WE ARE DOING.** Sort the twelve techniques below onto the six axes, one axis per distinct mechanism, writing one line per technique: its mechanism or mechanisms, the axis for each, or "none fits" / "two fit" with the reason.
3. **WHY.** Whether the axes sort techniques cleanly is unknown. If they don't, every entry and every survey ticket is organised around a structure that will have to be redone.
4. **WHAT IS AFFECTED.** The axis table in `README.md`, the `axis` field in `entries/_template.md` and in the three entries, and the survey tickets R-005 to R-010 (one per axis).
5. **CONCLUSION IF WE DO IT.** If at least 10 of the 12 sort cleanly (each mechanism onto exactly one axis), keep the six axes and unblock the surveys. If 3 or more don't, revise the axes before writing more entries, and record which techniques broke them and how.
6. **CONSEQUENCE OF NOT DOING IT.** Entries pile up under axes that may not fit, and re-filing costs more with every entry. The surveys are scoped by axis, so they would be scoped wrong.

The twelve, as listed when the card opened: warm-starting contact forces (Catto, GDC 2005); refitting a bounding-volume tree; sort and sweep with insertion sort; temporal reprojection / temporal anti-aliasing; ReSTIR (Bitterli et al., SIGGRAPH 2020); irradiance caching (Ward, Rubinstein and Clear, SIGGRAPH 1988); smoothed aggregation multigrid for cloth (Tamstorf et al., SIGGRAPH Asia 2015); learned upsampling of coarse cloth (Kavan et al., SIGGRAPH 2011); deformation transfer (Sumner and Popović, SIGGRAPH 2004); design-preserving garment transfer (Brouet et al., SIGGRAPH 2012); precomputed radiance transfer (Sloan, Kautz and Snyder, SIGGRAPH 2002); kinetic data structures (Basch, Guibas and Hershberger, SODA 1997). The card also asked whether the template's "What repeats" section describes each one naturally.

**Result (2026-11-14): 12 of 12 sorted cleanly, and the test could hardly have failed.**

| # | Technique | Mechanism | Axis | "What repeats" fits? | Reuse changes |
|---|---|---|---|---|---|
| 1 | Warm-starting contact forces | the last step's contact forces start this step's solver | time | yes | depends: cost only when the problem has one solution and the solver converges; the answer too under a fixed iteration count or when there are several solutions |
| 2 | Bounding-volume tree refit | keep last frame's tree, recompute its boxes bottom-up | time | yes | cost only: queries stay correct and get slower as the boxes loosen |
| 3 | Sort and sweep, insertion sort | last frame's order starts this frame's sort | time | yes | cost only |
| 4 | Temporal reprojection / TAA | last frame's pixels, moved by motion vectors, blended into this one | time | yes | the answer: ghosting and blur when the history is stale |
| 5 | ReSTIR | (a) last frame's light samples; (b) neighbouring pixels' light samples | (a) time, (b) space | yes | depends: the unbiased form is correct on average but its reused samples are correlated; the biased form changes the answer |
| 6 | Irradiance caching | indirect light computed at sparse points and interpolated between them | space | yes | the answer: interpolation error, kept under an error estimate |
| 7 | Multigrid for cloth | coarse versions of the same problem correct the fine solve | resolutions | **no**: nothing is repeated; the fine solve is slow on large-scale error | cost only: the fine answer, to tolerance |
| 8 | Learned upsampling | (a) a coarse simulation stands in for the fine one; (b) an operator learned once from fine simulations is applied to every frame | (a) resolutions, (b) many instances | (a) **no**, (b) yes | the answer |
| 9 | Deformation transfer | carry a deformation to another mesh through a correspondence | shapes | yes | the answer |
| 10 | Garment transfer | grade the garment to the new body under pattern-making rules | shapes | yes | the answer, by design |
| 11 | Precomputed radiance transfer | light transport precomputed per object, reused under any low-frequency lighting | many instances | yes | the answer: low-frequency lighting only, static geometry |
| 12 | Kinetic data structures | keep the structure, update it only when one of its certificates fails | time | yes | cost only |

Per axis, counting mechanisms (14 from 12 techniques): time 6, space 2, runs 0, resolutions 2, shapes 2, many instances 2.

By the pre-stated branch, this keeps the axes. Reading the components says the result is weak. Every one of the twelve was an example in the README's axis table, was named earlier in the same conversation (sort and sweep, kinetic data structures), or is the paper behind one of those examples (Kavan et al., Brouet et al.). The sort tested whether the axes fit the examples they were made from, which they were always going to. The flaw was in how the card was written (by Claude, the same day): the test set should have been drawn by a procedure from a source not used to build the axes. So the axes are kept provisionally, and **the surveys stay blocked** on a held-out test (R-012). That departs from the pre-stated branch, on purpose.

Three things the sort showed anyway:

- **"Across runs" got none of the twelve.** That axis rests on the test bed's fitting loop and parameter sweeps alone. It may be "across time" for an outer loop. One difference argues for keeping it: inside a simulation, history is the physics, while across runs each run is supposed to be independent of history (a fresh run is the reference), so carrying history over is an error to guard against. That is why warm-starting across runs needs the history condition. Open as T-009.
- **"What repeats" fit 10 of 12.** Multigrid and the coarse half of learned upsampling are about work done in more detail than the answer needs, not about repeated work. Section 2 of the template is now "What work is wasted": repeated, or computed in more detail than the answer needs.
- **A second dimension cuts across all six axes: does the reuse change only the cost, or the answer too?** Cost only: 4 (refit, sort and sweep, multigrid, kinetic data structures). The answer: 6 (temporal reprojection, irradiance caching, learned upsampling, deformation transfer, garment transfer, precomputed radiance transfer). Depends on the problem: 2 (warm starting, ReSTIR). Cost-only reuse fails by getting slower: a loose refit tree makes queries slower, not wrong. Answer-changing reuse fails by giving a wrong answer, and that is where validity conditions carry content. The template now has a `reuse_changes` field. This also settles T-006: multigrid is reuse that can't change the answer, and what separates it from upsampling on the same axis is this second dimension.
