# Threads

Open questions, as a tree. One thread per entry. Statuses: open, active, answered, parked, dropped. A parked thread says what resuming it needs.

### T-001 · Do the six reuse axes hold?

**Status:** active
**Parent:** —
**Opened:** 2026-11-14
**Question:** The axes (time, space, runs, resolutions, shapes, many instances) came from about ten examples in one conversation. Does each well-known technique across graphics sort onto exactly one axis per mechanism?
**Answer:** Partly (R-004, 2026-11-14). 12 of 12 sorted cleanly, but all twelve came from the conversation that built the axes, so this only shows the axes fit their own examples. Held-out test: R-012.

### T-002 · Does the reference beat a model that already knows the techniques?

**Status:** parked
**Parent:** —
**Opened:** 2026-11-14
**Question:** As context for an AI tool, do entries with validity conditions raise the share of reuse proposals that pass a test bed's checks, compared with a model given no entries? `style`'s C-007 (an agent already followed 5 of an entry's 6 rules) is early evidence the answer could be no.
**Resume needs:** several tested entries in one test bed; the test bed has the checks (crossings, silhouette, lengths). METHOD.md step 4b.
**Answer:** — Evidence so far (R-011, 2026-11-14): on the three seed entries, a fresh agent named 11 of 18 conditions and every check, and added conditions the entries lacked. Circular, since the entries came from the same model's knowledge, but it says entries add over an agent only where they carry something from outside the model, such as the test bed's measurements.

### T-003 · Can the recognition habit be measured?

**Status:** parked
**Parent:** —
**Opened:** 2026-11-14
**Question:** Give a model a contest problem in clean form and the same problem disguised as library code, and compare how often it finds the known technique. A large drop would measure the "finding the problem" gap that the repository-level benchmarks report.
**Resume needs:** about 20 contest problems with known techniques, each rewritten as plausible library code.
**Answer:** —

### T-004 · Is the dupatta's tear structural?

**Status:** open
**Parent:** — (raised by entries/garment-transfer-surface-binding.md)
**Opened:** 2026-11-14
**Question:** Does any surface binding tear free-hanging cloth bound to distant parts of the body, or is it particular to Blender's nearest-point binding? If it is structural, the condition belongs to the whole class of techniques.
**Answer:** — Brouet et al. 2012 (R-013) has no free-hanging example; its reference points and its collision test both assume each garment vertex relates to a nearby bone, which is least likely to hold for a dupatta's free end. It does say nearest-point binding makes garments slide (Section 4.1), so part of the tear may be the binding Blender uses.

### T-010 · Should a garment moved to another body be the same garment or a graded one?

**Status:** open
**Parent:** T-002
**Opened:** 2026-11-14
**Question:** Three agent runs all assumed the same garment re-draped; Brouet et al. assume a graded garment that keeps the design. The two goals have different validity conditions and different rest shapes for any relax afterwards. The test bed's own review accepted Surface Deform as grading for the kameez and trousers, and a dupatta of a set length is plainly the same-garment case. Which does each step of the test bed actually want?
**Answer:** —

### T-005 · Does a warm-started drape settle into the same folds as a fresh one?

**Status:** open
**Parent:** — (raised by entries/warm-start-repeated-drapes.md)
**Opened:** 2026-11-14
**Question:** For cut changes of 3–8 cm, do a warm drape's landmark lengths and silhouette fall within the fresh drapes' seed-to-seed spread?
**Answer:** —

### T-006 · Is multigrid reuse, or a faster solver?

**Status:** answered
**Parent:** T-001
**Opened:** 2026-11-14
**Question:** Multigrid reuses a coarse answer as a correction but repeats no earlier work. If it doesn't fit, "across resolutions" may be two different things.
**Answer:** It fits "across resolutions" by mechanism, and it is reuse that can't change the answer (cost only). What separates it from upsampling on the same axis is whether the reuse changes the answer, which is now the `reuse_changes` field (CARD.md, R-004 result).

### T-007 · Do kinetic data structures cover more than "across time"?

**Status:** open
**Parent:** T-001
**Opened:** 2026-11-14
**Question:** Kinetic data structures are the formal frame for keeping a structure correct under motion. Do they say anything about the other axes, or is each axis its own literature?
**Answer:** —

### T-008 · Does the cost-versus-answer split predict where an entry adds most?

**Status:** open
**Parent:** T-002
**Opened:** 2026-11-14
**Question:** For reuse that changes only the cost, the condition is mostly "until it gets too slow", which an agent is likely to know. For reuse that changes the answer, the conditions are specific to the field. Do agent baselines (METHOD.md step 2b) miss more conditions on answer-changing entries than on cost-only ones?
**Answer:** — Not testable yet: R-011's three entries all change the answer (or depend), with no cost-only entry to compare, and the entries came from the same model's knowledge.

### T-009 · Is "across runs" just "across time" for an outer loop?

**Status:** open
**Parent:** T-001
**Opened:** 2026-11-14
**Question:** None of R-004's twelve techniques landed on "across runs". Inside a simulation, history is the physics; across runs, each run is meant to be independent of history, so carrying it over is an error to guard against. Is that difference enough to keep a separate axis, or does the literature treat both the same way?
**Answer:** — Evidence so far, not a decision: R-012's procedure-drawn sample (20 reuse papers from TOG speed papers) had none on "across runs", which its card counts as evidence for folding; R-015's need-chosen sample had five, all inside fitting or editing loops (T-013).

### T-011 · Does switching friction off make a fit's width sensitivities keep their sign?

**Status:** open
**Parent:** T-005
**Opened:** 2026-11-14
**Question:** Wang 2018 and Dress-1-to-3 2025 both drop friction while fitting so the drape depends only on the cut. The test bed's width sensitivities don't keep their sign across runs. Do they, with cloth-body and self-collision friction at zero and the waistband pinned, measured over the same seeds? (A test-bed spike, the user's call; R-015.)
**Answer:** — R-016: Dress-1-to-3 drops friction during the fit and fixes the bottom garment's waist loop against slipping (§6.1), but never measures what friction-off buys.

### T-012 · Is Newton's VBD or Style3D solver on one CPU core faster than Blender's cloth for a 5,000-vertex piece?

**Status:** open
**Parent:** T-005
**Opened:** 2026-11-14
**Question:** Newton runs on macOS CPU only, and Warp runs CPU kernels serially. One timed drape of one piece, exported from Blender and read back, decides whether it is worth more. (R-015.)
**Answer:** —

### T-013 · Do reuse-across-runs techniques cluster around optimisation loops?

**Status:** open
**Parent:** T-009
**Opened:** 2026-11-14
**Question:** R-004's twelve had no "across runs"; R-015's need-chosen sample had five (Wang 2018, Dress-1-to-3, Sensitive Couture, Parameter-space ReSTIR, residual path integrals), all inside fitting or editing loops. Is "across runs" the axis of outer loops, and does R-012's procedure-drawn sample find any?
**Answer:** —

### T-014 · Can Cycles' Light Groups fit a photo's light by least squares without re-rendering?

**Status:** open
**Parent:** T-001
**Opened:** 2026-11-14
**Question:** Light Groups recombine linearly in strength and colour, so a few group passes rendered once could be weighted to match a photo. Exact only for scaling, not for moving lights or changing albedo, and denoising breaks linearity. (R-015, area D; reasoned, untested.)
**Answer:** —

### T-015 · Where do exact repeats within one evaluation go?

**Status:** open
**Parent:** T-001
**Opened:** 2026-11-14
**Question:** R-012 found two speedups from computing an identical term once and sharing it (an edge-based FEM formulation, D*'s common-subexpression elimination). The premise calls exact repeats and memoization reuse, "the easy case", but all six axes describe near-repeats along some dimension. Is this a seventh axis ("within one evaluation"), out of scope by design (the premise says tools already handle exact repeats), or part of "across space"? Either answer should be written into README.md.
**Answer:** —

### T-016 · Is "across many instances" too broad to file by?

**Status:** open
**Parent:** T-001
**Opened:** 2026-11-14
**Question:** It took 12 of R-012's 20 papers: learned models, baked neural representations, precomputed tables and bases, reduced models, a precomputed Pareto front. They share "paid once, used many times" but have different validity conditions (a learned model fails off its training distribution, a precomputed transport operator when the scene moves). Would splitting it (precomputed from the problem's own data vs learned from other problems) give conditions that differ more between than within? R-010's survey is the natural place to find out.
**Answer:** —
