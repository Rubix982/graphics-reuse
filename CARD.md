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

## Live card

None open (2026-11-14). R-017 (independent re-sort of R-012) is running as a review ticket. Candidates after it: R-014, an axis survey (R-005 to R-010).

---

## Parked cards

None.

---

## Closed cards

### R-016 · Does a full reading of Dress-1-to-3 add anything to the warm-start entry over an agent?

_Opened and closed 2026-11-14 at the user's request. R-017 (an independent re-sort of R-012's abstracts) ran alongside as a review ticket, not a card._

1. **WHERE WE ARE.** `entries/warm-start-repeated-drapes.md` rests on two sources read at a distance (Catto's slides through a mirror, a continuation-methods book). R-011's agent baseline named 5 of its 6 conditions and added several. R-015 found that Dress-1-to-3 (SIGGRAPH 2025) warm-starts each iteration and states the reason.
2. **WHAT WE ARE DOING.** Read Dress-1-to-3 in full, take notes against R-016's questions with section references, rewrite the warm-start entry from them, and score the paper's items against the baseline list fixed beforehand (`agents/researcher/findings/r016/baseline-items.md`).
3. **WHY.** Whether a full reading adds to this entry beyond what an agent already says is unknown. R-013 found it did for garment transfer, as a reframe. This is the second paper read in full.
4. **WHAT IS AFFECTED.** The warm-start entry (its sources, conditions and `agent_baseline`); T-005 and T-011; the test bed's planned warm start, through `private/`.
5. **CONCLUSION IF WE DO IT.** Count the paper's items about the reuse (conditions, numbers, techniques) that the baseline named none of. If 3 or more: a full reading adds here too, and R-013's rule holds on a second paper. If 0 or 1: for this entry the agent already had what the paper says, and its value rests on measurements. If 2: inconclusive.
6. **CONSEQUENCE OF NOT DOING IT.** The warm-start entry stays written from unread sources, and the test bed's warm start would run without the one published statement of its condition.

**Result (2026-11-14): 1 item by none under the narrow reading (the 0–1 branch), 3 under the wide one. For this entry the agent already had nearly everything the paper says about warm starting; the paper adds one remedy inside the same frame.**

Of the paper's six items about the warm start, the baseline named three (start from the previous drape; the equilibrium doesn't depend on its start near one resting shape; one triangulation moved), partly named two (friction as the cause of path dependence, though not switching it off; remeshing), and named none for one: with friction off, the waist loop of the bottom garment is fixed so nothing slips (§6.1). Counting the two items about running each drape (one implicit step of 1 s; a safeguard against inverted triangles), three are by none. Notes: `agents/researcher/findings/r016/dress-1-to-3-notes.md`; scoring: `score.md` beside it. One baseline run only, so a "none" is weaker than in R-013.

Read with R-013, reading in full added a reframe there and a remedy here, and both were things the test bed can act on (grading; friction off during the fit, T-011). The baseline also had six things the paper lacks: rest-shape plumbing, lengthening against shortening, sensitivities measured against a warm drape at the unchanged cut, parallel drapes, warm drapes for sensitivities with fresh ones for the residual, and cheap tests. The paper never compares warm drapes to fresh ones, so the entry stays untested. `entries/warm-start-repeated-drapes.md` was rewritten with every condition marked: (paper, section), or (reasoned, with R-011's baseline named where it came from).

### R-012 · Do the axes hold on techniques they weren't built from?

_Opened 2026-11-14. Parked the same day for R-013, unparked and closed the same day at the user's request (after R-015). Run as written, except that DBLP answered with a bot check, so the source is the card's named fallback, Semantic Scholar (`agents/researcher/findings/r012/procedure.md`)._

1. **WHERE WE ARE.** The six axes sorted 12 of 12 techniques cleanly (R-004), but all twelve came from the conversation that produced the axes, so the sort could hardly have failed.
2. **WHAT WE ARE DOING.** Draw graphics papers about speedups by a fixed procedure, and sort each one: is its speedup reuse at all; if so, which axis per mechanism, and does the reuse change only the cost or the answer too. The procedure: search DBLP (or Semantic Scholar, if DBLP can't filter by venue) for papers in ACM Transactions on Graphics, 2000–2025, whose titles contain *fast*, *faster*, *efficient*, *accelerat-* or *real-time*; save the full hit list and the exact query; shuffle it with Python's `random.Random(1114).shuffle`; go down the shuffled list sorting each paper from its abstract, until 20 papers whose speedup is reuse have been sorted. Record every paper looked at, including the ones that aren't reuse.
3. **WHY.** Whether the axes fit reuse techniques nobody chose with the axes in mind is unknown. The title words describe speed, not any kind of reuse, so they don't steer the sample toward an axis. The share of speedup papers that are reuse at all comes out as a side number.
4. **WHAT IS AFFECTED.** The axis table in `README.md`, the `axis` field in `entries/_template.md` and in the entries, and the survey tickets R-005 to R-010 (one per axis, blocked on this card).
5. **CONCLUSION IF WE DO IT.** If at least 16 of the 20 reuse papers sort cleanly (each mechanism onto exactly one axis), the axes hold beyond their own examples, and the surveys unblock. If 5 or more don't, revise the axes before writing more entries, recording which papers broke them and how. Either way, if "across runs" again gets none, that is evidence for folding it into "across time" (T-009).
6. **CONSEQUENCE OF NOT DOING IT.** The library grows under axes that are only known to fit the examples they were made from, and the surveys stay scoped by them.

**Result (2026-11-14): 18 of 20 clean under the strict reading, 20 of 20 under the lenient one, so the keep branch either way. The axes hold beyond their own examples, and R-005 to R-010 unblock.**

The source was Semantic Scholar, since DBLP answered with a bot check; 354 TOG papers passed the title filter. Going down the list shuffled with seed 1114: 53 papers looked at, 2 without an abstract and 2 whose abstracts don't say where the speed comes from, so 49 judged, 20 of them reuse (41 %). Every verdict quotes its abstract (`agents/researcher/findings/r012/sorted.md`). The two readings differ on one kind of saving the procedure hadn't anticipated: an identical term computed once and shared within one evaluation (common subexpressions; ranks 1 and 52). The library's premise calls exact repeats reuse, but no axis holds them, so under the strict reading they are misfits. Under the lenient reading they are out of scope, and the sample runs to rank 55 (T-015).

The components say more than the count. "Across many instances" took 12 of the 20 papers (learned models, baking, precomputed tables and bases, reduced models), and "across runs" and "across shapes" took none, so the sort is clean partly because one axis is broad (T-016). "Across runs" got none again, which the card counts as evidence for folding it into "across time" (T-009). R-015's need-chosen sample had five, all inside fitting or editing loops (T-013), so the axis may be rare in speed papers and common in optimisation loops. Weaknesses: the sorter wrote the axes, and an independent sort of the same 55 abstracts would measure agreement (not done); Semantic Scholar's coverage of TOG wasn't checked against DBLP.

### R-015 · Does any recent method serve the test bed's largest measured costs under its constraints?

_Opened and closed 2026-11-14, at the user's request._

1. **WHERE WE ARE.** The library's four entries rest on papers from 2005 to 2015. The test bed's own profile puts nearly all of a fitting run's time in drapes, much of it in drapes that never settle, and it runs on a 16 GB Apple Silicon machine with no CUDA, using open code only.
2. **WHAT WE ARE DOING.** Search four areas of 2023–2026 graphics literature (learned cloth; fast and GPU cloth solvers; differentiable cloth and inverse garment fitting; differentiable and neural rendering for garments) by saved queries, and record for every candidate what it reuses, its code and licence, whether it runs without CUDA, and its reported numbers with their hardware. Details in R-015's ticket.
3. **WHY.** Whether any recent method addresses the test bed's largest measured costs (drape time, drapes that never settle, the drapes spent measuring a fit's sensitivities) and can run under its constraints is unknown. The library has nothing after 2015.
4. **WHAT IS AFFECTED.** The next full readings (new R- tickets), `threads.md`, and `private/`'s mapping to the test bed. No entry changes until a paper is read in full (R-013's rule). The test bed itself isn't touched.
5. **CONCLUSION IF WE DO IT.** If at least one method addresses one of the three costs, has open code, and runs without CUDA (or its technique can be rebuilt inside Blender), it becomes the next paper read in full and a spike candidate for the test bed. If none does, the test bed's speed work stays on its own path (fail-fast, warm starts), the survey stands as a map, and the reason each method fails the constraints is recorded.
6. **CONSEQUENCE OF NOT DOING IT.** The library stays pre-2016, and the test bed may rebuild what recent papers already solved.

**Result (2026-11-14): yes, the first branch, but by strategies more than by solvers.** One open codebase runs here without CUDA and addresses drape time: Newton (Apache-2.0; VBD, Offset Geometric Contact, a Style3D solver that takes 2D pattern panels as rest shapes), on macOS CPU only, with Warp's CPU kernels serial, so whether it beats Blender's solver on a 5,000-vertex piece is unknown until timed (T-012). The rest of what addresses the three costs is technique that can be rebuilt inside Blender without code: friction off while fitting, with the waistband pinned (Wang 2018; Dress-1-to-3 2025), aimed at drapes that depend on more than the cut (T-011); short inner drapes with a full one every 32 steps and backtracking (Wang 2018); earlier drapes and sensitivities blended by moving least squares (Sensitive Couture 2011). Neural simulators don't fit the constraints or the loop: none takes a flat pattern as its rest shape, and their speedups are GPU numbers.

Next paper read in full: Dress-1-to-3 (R-016). It is recent, on arXiv, and a published instance of `entries/warm-start-repeated-drapes.md` that states the entry's validity condition. Per-area notes: `agents/researcher/findings/r015/`; summary: `agents/shared/findings.md` [R-015]. The mapping to the test bed stays in `private/`.

### R-013 · Does an entry written from a full reading add anything over an agent?

_Opened and closed 2026-11-14._

1. **WHERE WE ARE.** A fresh agent named 11 of the seed entries' 18 conditions (R-011); the entries were written from abstracts by the same model, and what only they carried was the test bed's measurements.
2. **WHAT WE ARE DOING.** Read Brouet et al. 2012 in full, rewrite `entries/garment-transfer-surface-binding.md` from that reading with every condition marked and page-referenced, and compare it against three runs of R-011's garment-transfer baseline prompt, unchanged: the saved answer and two new runs.
3. **WHY.** Whether an entry built from a full reading carries anything an agent doesn't is unknown, and the library's value as agent context depends on it.
4. **WHAT IS AFFECTED.** The garment-transfer entry; METHOD.md step 2b; T-002; whether Phase 1's literature entries are worth writing as agent context or only as a map for their reader.
5. **CONCLUSION IF WE DO IT.** Count the entry's conditions and numbers taken from the paper that none of the three baseline runs named. If 3 or more: full reading adds over an agent, and reading in full becomes the rule for every entry. If 0 or 1: even a fully read entry adds little as agent context, its value as agent context rests on measurements, and the README says the literature entries are mainly a map for their reader. If 2: inconclusive; repeat with a second paper.
6. **CONSEQUENCE OF NOT DOING IT.** The library's claim to help an agent stays untested, and R-012 would test how to file entries whose value is unknown.

**Result (2026-11-14): 11 of 16 paper items were named by none of the three runs, 6 of them general. Branch taken: reading in full is the rule. The addition came as a reframe.**

The paper describes a different mechanism from surface binding, so the reading produced a new entry, `entries/design-preserving-garment-transfer.md`, and added the paper's conditions to the surface-binding entry (one mechanism per entry, METHOD.md step 3). The 16 items were fixed in `agents/researcher/findings/r013/brouet2012-notes.md` before runs 2 and 3 were read. Against the runs: 2 named, 3 partly, 11 by none. Leaving out the five items that only matter inside the paper's own method, 6 general items were named by none. Every count clears the branch's 3. Full table: `agents/researcher/findings/r013/score.md`.

Reading the components changes what the number means. All six general items belong to grading, an adjusted garment and pattern that keep the design on the new body. The prompt asked about matching a fresh drape of the same pattern, and none of the three runs asked whether the garment should be graded instead. Inside that same-garment frame the paper added nothing the agents missed outright. So the full reading added a different question, with its criteria and numbers; it didn't add conditions inside the agents' frame. The test bed's own verdict on Surface Deform, "accepted as grading" for the kameez and trousers, says the reframed question is the one the test bed has. The same reframe settles the disputed relax: toward the original pattern it undoes the stretch, toward a re-extracted graded pattern it starts almost at rest (L²-stretch 1.0002–1.003).

Not settled: whether an agent asked about grading directly would name the six items. That's R-014.

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
