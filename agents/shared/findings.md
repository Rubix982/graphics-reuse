# Findings

_Owned by the researcher. Append-only._

## [R-001] Finding: what the premise rests on

_Date: 2026-11-14_

A knowledge base of competitive-programming tricks is already built (PIE) and aims at the wrong gap: agents mostly fail at finding where the time goes, not at knowing techniques (GSO). The reframe is a reference of reuse techniques in graphics, organised by what gets reused, with validity conditions and tested status. Full account in `docs/premise.md`.

- PIE: over 77,000 slow-to-fast C++ pairs from CodeNet; trained models beat the best human speedup on held-out contest problems.
- GSO: best agents solve under 5 % of tasks. SWE-fficiency: under 0.23× of the expert speedup.
- MemoizeIt: detecting exact repeats already works (9 opportunities in 11 Java programs, 1.04–12.93×).

Confidence: high on the cited numbers (each from the paper or its official page); medium on the premise, which rests on the untested axes (R-004).

## [R-002] Finding: `style`'s evidence applies to this library's design

_Date: 2026-11-14_

The sibling `style` library had already measured two things this library needed. Most of a source's devices are conditional (C-003: 6 of 14 facts held across a chair, drawers and a lamp), which matches "the technique is generic, the condition is specific". An unguided agent can already know most of an entry (C-007: 5 of 6 rules), and an entry's extras can make things worse. Both were adopted into METHOD.md.

- Kept: problem first, primary sources covering different cases, the constant / conditional / varies sort, step 2b, `tested_in`.
- Changed: the blind pick becomes a measurement against a fresh full computation, judged by the seed-to-seed spread.

Confidence: high that the evidence exists (style's own cards); medium that it transfers, since style's tests were one brief per arm with one judge, in a different domain.

## [R-003] Finding: three seed entries

_Date: 2026-11-14_

One entry tested in part, two untested. The tested one, garment transfer by surface binding, shows the pattern the reference is built around: body-hugging pieces carried in 1.2 s against about 6 minutes for a drape, and the free-hanging dupatta tore.

- Transfer: edges 1.06–1.07× at the median, 1.22–1.30× at the 95th percentile; dupatta 4.9× at the 95th percentile with 96 points inside the body.
- Coarse-to-fine names two mechanisms with different validity: multigrid reaches the same answer faster; upsampling reaches a different answer that only has to look right.
- The template's "What repeats" section fits coarse-to-fine poorly; carried into R-004.

Confidence: high on the measured transfer numbers (the test bed's record of 2026-11-11); low on the two untested entries' conditions, which are reasoned from the methods.

## [R-004] Finding: the axes fit their own examples, and a second dimension matters more

_Date: 2026-11-14_

Twelve techniques sorted onto the six axes, 12 of 12 cleanly (14 mechanisms: time 6, space 2, runs 0, resolutions 2, shapes 2, many instances 2). The result is weak: all twelve came from the conversation that produced the axes, so the sort could hardly fail. Axes kept provisionally; surveys blocked on a held-out test (R-012). Full table in `CARD.md`.

- "Across runs" got none of the twelve (T-009).
- The template's "What repeats" fit 10 of 12; renamed "What work is wasted" (repeated, or done in more detail than needed).
- Whether the reuse changes only the cost or the answer too cuts across every axis: cost only 4, the answer 6, depends 2. Cost-only reuse fails by slowing down; answer-changing reuse fails by giving a wrong answer, which is where validity conditions carry content. Added as `reuse_changes`.

Confidence: high on the sort itself (each technique's mechanism is standard); low on what it says about the axes, because the test set wasn't independent of them; medium on the cost-versus-answer split, which is a property of each technique rather than of the axes, but rests on these twelve.

## [R-011] Finding: an agent already knows what the seed entries say; the measurements are what it lacks

_Date: 2026-11-14_

Three fresh agents, given each seed entry's wasted work with no hint of the technique, named 11 of the entries' 18 conditions, partly named 3, disputed 1 and missed 3, and named every check. The misses were all about mechanisms the agent didn't propose (multigrid, learned upsampling). Each answer also had conditions the entry lacked. Scoring and the verbatim answers: `agents/researcher/findings/r011/`.

- Circular: the entries were written by the same model from abstracts and memory, so the agent was always going to know most of them. METHOD.md step 2b now says so.
- What only an entry carried was the test bed's measurements. The agent guessed 9 % stretch where the test bed measured 6–7 % at the median and 22–30 % at the 95th percentile.
- One reasoned condition is disputed: the entry says the relax after surface binding is short, the agent says it has to undo the grading stretch. Only a timed relax settles it.
- Two agents independently named the cloth's rest shape as the main thing to get right when restarting from a settled drape.
- The coarse-to-fine baseline named a condition that matters for flared garments: their outline depends on their folds, so a coarse mesh changes the silhouette.

Confidence: high that the counts are as scored (answers saved verbatim); low on what they say about entries in general, given the circularity and one run per entry; medium that entries add over an agent mainly through measurements and full reading, which is what the result points to but hasn't shown on an entry written that way.

## [R-013] Finding: a full reading added a reframe, not more conditions inside the agents' frame

_Date: 2026-11-14_

Brouet et al. 2012 read in full; 16 items from it, fixed before two of three baseline runs were read, scored against three runs of the garment-transfer prompt. 2 named, 3 partly, 11 by none, 6 of them general. That clears the card's branch, so reading in full is the rule. All six general items belong to grading (adjust the garment and pattern to the new body, keeping the design), a goal the prompt didn't pose and no run raised. Inside the agents' frame (match a fresh drape of the same pattern) the paper added nothing they missed outright. Full scoring: `agents/researcher/findings/r013/score.md`.

- New entry: `entries/design-preserving-garment-transfer.md`, the first written from a full reading.
- The test bed's own review accepted its Surface Deform result as grading for the kameez and trousers, so the reframed question is the one the test bed has for those garments.
- The relax dispute was two rest shapes: toward the original pattern the relax undoes the stretch (6–7 % at the median), toward a re-extracted graded pattern it starts almost at rest (L²-stretch 1.0002–1.003).
- The agents covered ground the paper doesn't (it is purely geometric): Blender's rest shape key, morphing the body inside the simulation, stopping at convergence, caching, measuring the fresh drapes' own spread.

Confidence: high that the paper says what the notes say (page-referenced, checkable by the user); medium on the counts, since the scorer is the same model family and the item grain is the scorer's; low that the result holds beyond one paper and one entry.

## [R-015] Finding: for a drape-in-the-loop garment fit on a laptop with no CUDA, recent papers give strategies more than solvers

_Date: 2026-11-14_

Four areas of 2023–2026 graphics literature were searched by saved queries: learned cloth (47 candidates), fast and GPU cloth solvers (34), differentiable cloth and inverse garment fitting (44), and rendering (about 60). Each candidate was recorded with what it reuses, its code and licence, and whether it runs without CUDA. The headline speedups in every area are GPU numbers on NVIDIA hardware, and almost none of the code runs on a 16 GB Apple Silicon machine. What transfers is mostly conditions and strategies that need no code. Two garment-fitting papers seven years apart (Wang 2018; Li et al. 2025, Dress-1-to-3) both switch friction off while fitting, so that the drape depends only on the cut. Wang runs short inner drapes and a full one every 32 outer steps, backing off when the cost hasn't dropped. Dress-1-to-3 starts each iteration's drape from the previous one, because a static equilibrium doesn't depend on where the drape starts, which is the validity condition `entries/warm-start-repeated-drapes.md` marks as untested. Open code that runs here: Newton (Apache-2.0; Vertex Block Descent, Offset Geometric Contact, and a Style3D solver that builds rest shapes from 2D pattern panels), on macOS CPU only, where Warp runs CPU kernels serially, so its speed is unknown until timed; and HOOD (MIT), plausibly on CPU, but its rest shape is a 3D mesh and it has no cloth-on-cloth contact. Raw notes: `agents/researcher/findings/r015/`.

- Card branch taken: at least one method addresses one of the three costs with open code that runs without CUDA (Newton), and several techniques can be rebuilt inside Blender: friction off with the waistband pinned; inexact inner drapes with a periodic full one; earlier drapes and sensitivities blended by moving least squares (Sensitive Couture, 2011); GarmentCodeData's settling rule (at most 1.5 % of vertices moving more than 0.04 cm between frames).
- No paper in the window measures whether a garment sensitivity keeps its sign across runs. DiffCloth (2022) ranks contact-set changes as the worst source of jumps in cloth gradients, and on a bumpy one-parameter problem evolution strategies beat L-BFGS-B.
- No neural cloth simulator takes a flat sewing pattern as its rest shape, none models sewing the seams closed, and nothing in the window uses a network's drape as the start for a physical solver (the one example is Shao et al. 2020). On CPU, HOOD's one third-party timing is 0.75–1.0 s per frame at 4.4k vertices (phone CPUs), so the large speedups are GPU claims.
- Rendering: nothing fits a sheer fabric's transmission from an ordinary photo, and Tang et al. 2024 argue a reflection-only view can't. The reuse usable on the Mac is Cycles' own (Light Groups, Persistent Data, a fixed seed), with no published measurements. Blender 4.5's glTF exporter writes sheen and transmission but nothing for diffuse transmission.
- Across runs: this sample has several reuse-across-runs techniques (Wang 2018, Dress-1-to-3, Sensitive Couture, Parameter-space ReSTIR, residual path integrals), against none of R-004's twelve. The sample was chosen by need, a fitting loop, so it doesn't count as evidence for the axes (T-009, R-012).
- Checked against primary sources by the orchestrator: GarmentCodeData's rule (arXiv HTML), Dress-1-to-3's friction sentence and its 2 h on an RTX 3090 (arXiv HTML), HOOD's MIT licence, Newton's "macOS (CPU only)" (README), Warp's "kernels launched on CPU devices will be executed in serial" (runtime guide). Other numbers came through the agents' reads, many via WebFetch extracts, and must be re-checked before they go into an entry.

Confidence: high that the headline speedups don't transfer to the constraints (each paper states its hardware); medium on the per-candidate code verdicts (read from repos, nothing run); low on any speed on this machine (nothing was timed).
