# Researcher tickets

### R-001 · Write up the premise dry-run

**Status:** closed
**Type:** research
**Priority:** high
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Record how the idea moved from a competitive-programming knowledge base to a reference of reuse techniques in graphics, with what each reframe broke (Premise Dry-Run moves 1, 2, 8 and 9), every number sourced, and a Threads block mirrored into `threads.md`.

**Blockers:** none

**Artifacts:**
- docs/premise.md
- threads.md

**Closed:** 2026-11-14

### R-002 · Method and entry template, adapted from `style`

**Status:** closed
**Type:** research
**Priority:** high
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Adapt the sibling `style` library's METHOD.md and entry template: problem first, primary sources covering different cases, the constant / conditional / varies sort, step 2b (check what an agent already does), conditions marked by how they are known, and a measurement against a fresh full computation in place of the blind pick.

**Blockers:** none

**Artifacts:**
- METHOD.md
- entries/_template.md

**Closed:** 2026-11-14

### R-003 · Three seed entries

**Status:** closed
**Type:** research
**Priority:** high
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Write three entries in the template's shape, one tested in part and two untested, so the format can be judged on real content: garment transfer by surface binding (measured in the test bed on 2026-11-11), warm-starting repeated drapes, and coarse-to-fine cloth. Step 2b was not run for them; that is R-011.

**Blockers:** none

**Artifacts:**
- entries/garment-transfer-surface-binding.md
- entries/warm-start-repeated-drapes.md
- entries/coarse-to-fine-cloth.md

**Closed:** 2026-11-14

### R-004 · Test the six axes on twelve known techniques

**Status:** closed
**Type:** research
**Priority:** high
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
The live card in `CARD.md`. Sort the twelve techniques listed there onto the six axes, one axis per distinct mechanism, one line per technique (its mechanisms, the axis for each, or "none fits" / "two fit" with the reason). Also note whether the template's "What repeats" section describes each naturally. If at least 10 of 12 sort cleanly, the axes stay and R-005 to R-010 unblock. If 3 or more don't, write which ones broke the axes and how, and propose revised axes. Record the result in the card and in `agents/shared/findings.md`.

**Blockers:** none

**Artifacts:**
- CARD.md → closed card R-004, with the full sort
- agents/shared/findings.md → [R-004]
- entries/_template.md (section 2 renamed "What work is wasted"; `reuse_changes` field added), the three entries, README.md, METHOD.md step 3
- threads.md (T-001 updated, T-006 answered, T-008 and T-009 opened)

**Result:** 12 of 12 sorted cleanly, but all twelve came from the conversation that built the axes, so the sort could hardly fail. Axes kept provisionally; the surveys stay blocked on a held-out test, R-012, which departs from the pre-stated branch on purpose.

**Closed:** 2026-11-14

### Survey tickets R-005 to R-010: shared description

Each survey ticket covers one axis. Following METHOD.md steps 1 to 3, including step 2b, write 5–8 entries for the axis from primary sources, marked untested unless a measurement exists. Start from the techniques the ticket lists, and add others found along the way. For each entry, note in section 1 whether *Real-Time Collision Detection* (Ericson) or *Real-Time Rendering* (Akenine-Möller et al.) already covers it, and what the entry adds. Append a summary to `agents/shared/findings.md` with a confidence level. Done when the entries exist and the summary is written. If R-012 revises the axes, each ticket is re-scoped before it starts.

### R-005 · Survey: across time

**Status:** open
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: warm starting in contact solvers (Catto 2005); refitting bounding-volume trees; sort and sweep on nearly sorted lists; temporal reprojection and temporal anti-aliasing; kinetic data structures (Basch, Guibas and Hershberger 1997).

**Blockers:** none (R-012 closed 2026-11-14: the axes hold, 18 or 20 of 20 clean)

**Artifacts:** —

**Closed:** —

### R-006 · Survey: across space

**Status:** open
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: ReSTIR's spatial reuse (Bitterli et al. 2020); irradiance caching (Ward, Rubinstein and Clear 1988); photon mapping's density estimation; spatial denoising filters.

**Blockers:** none (R-012 closed 2026-11-14: the axes hold, 18 or 20 of 20 clean)

**Artifacts:** —

**Closed:** —

### R-007 · Survey: across runs

**Status:** open
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: warm starting and numerical continuation (Allgower and Georg 1990); adjoint and differentiable simulation, where one backward pass replaces one forward run per parameter; incremental recomputation in node-based procedural tools.

**Blockers:** none (R-012 closed 2026-11-14: the axes hold, 18 or 20 of 20 clean)

**Artifacts:** —

**Closed:** —

### R-008 · Survey: across resolutions

**Status:** open
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: multigrid for cloth (Tamstorf et al. 2015); learned upsampling (Kavan et al. 2011); adaptive remeshing (Narain et al. 2012); progressive meshes (Hoppe 1996); mipmapping and level of detail.

**Blockers:** none (R-012 closed 2026-11-14: the axes hold, 18 or 20 of 20 clean)

**Artifacts:** —

**Closed:** —

### R-009 · Survey: across shapes

**Status:** open
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: deformation transfer (Sumner and Popović 2004); design-preserving garment transfer (Brouet et al. 2012); functional maps for correspondence between shapes (Ovsjanikov et al. 2012); skinning weight transfer; motion retargeting.

**Blockers:** none (R-012 closed 2026-11-14: the axes hold, 18 or 20 of 20 clean)

**Artifacts:** —

**Closed:** —

### R-010 · Survey: across many instances

**Status:** split
**Split into:** R-018, R-019
**Reason:** 5–8 entries, each read in full with its own agent baseline (R-013's rule), don't fit one sitting; and R-012 and R-017 put two-thirds of reuse papers on this axis, so whether it holds one kind of reuse or two decides how its entries are filed (T-016).
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: precomputed radiance transfer (Sloan, Kautz and Snyder 2002); baked lighting; precomputed signed distance fields for static colliders; learned cloth simulators.

**Blockers:** none (R-012 closed 2026-11-14: the axes hold, 18 or 20 of 20 clean)

**Artifacts:** —

**Closed:** —

### R-011 · Agent baseline for the three seed entries

**Status:** closed
**Type:** research
**Priority:** low
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
METHOD.md step 2b, skipped when the seed entries were written. For each of the three seed entries, give one fresh agent (no access to this repository) a description of the repeated work from the entry's section 2, with no mention of the technique, and ask how it would avoid redoing the work and when that would be safe. Save each prompt verbatim in `agents/researcher/findings/r011/` before running. Record in each entry's `agent_baseline` which techniques the agent proposed and which of section 4's conditions it named. Done when all three headers are filled.

**Blockers:** none

**Artifacts:**
- agents/researcher/findings/r011/ (three prompts, three verbatim answers, score.md)
- the three entries' `agent_baseline` headers; the disputed relax condition in entries/garment-transfer-surface-binding.md
- METHOD.md step 2b (the circularity note, read sources in full)

**Result:** The baseline named 11 of 18 conditions, partly 3, disputed 1 and missed 3 (all about mechanisms it didn't propose), named every check, and added conditions the entries lacked. Circular, because the entries came from the same model's knowledge. What only the entries carried was the test bed's measurements.

**Closed:** 2026-11-14

### R-012 · Held-out test of the axes

**Status:** closed
**Type:** research
**Priority:** high
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
The live card in `CARD.md`. Search DBLP (or Semantic Scholar, if DBLP can't filter by venue) for ACM Transactions on Graphics papers, 2000–2025, with *fast*, *faster*, *efficient*, *accelerat-* or *real-time* in the title. Save the exact query and the full hit list in `agents/researcher/findings/r012/`. Shuffle the list with `random.Random(1114).shuffle` and sort each paper from its abstract (is the speedup reuse; if so, axis per mechanism and `reuse_changes`) until 20 reuse papers are sorted, recording every paper looked at. The branches are written in the card: at least 16 of 20 clean keeps the axes and unblocks R-005 to R-010; 5 or more misfits means revising the axes first.

**Blockers:** none

**Parked:** 2026-11-14, for R-013. **Unparked:** 2026-11-14, at the user's request. DBLP's API answered with a bot check, so the source is Semantic Scholar, the card's fallback; the procedure was fixed in `agents/researcher/findings/r012/procedure.md` before the list was drawn.

**Artifacts:**
- agents/researcher/findings/r012/procedure.md (fixed before the list was drawn)
- agents/researcher/findings/r012/draw.py, raw.json, hits.csv, shuffled.csv (the sample: 354 papers)
- agents/researcher/findings/r012/abstracts.py, abstracts.jsonl (abstracts for the first 100 in shuffled order)
- agents/researcher/findings/r012/sorted.md (every paper looked at, with its verdict and the abstract's words)

**Result:** 18 of 20 clean (strict) or 20 of 20 (lenient): the keep branch either way, so R-005 to R-010 unblock. "Across many instances" took 12 of 20, "across runs" and "across shapes" none. See CARD.md.

**Closed:** 2026-11-14

### R-013 · Rewrite the garment-transfer entry from a full reading of Brouet et al. 2012

**Status:** closed
**Type:** research
**Priority:** high
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
The live card in `CARD.md`. Read Rémi Brouet, Alla Sheffer, Laurence Boissieux, Marie-Paule Cani, "Design Preserving Garment Transfer", ACM Transactions on Graphics 31(4), 2012 (DOI 10.1145/2185520.2185532), in full. Write notes against the six questions (the grading requirements and which are hard constraints; how points are matched between bodies; whether and how long they simulate after transfer; layers; loose, free-hanging cloth; results and limitations) with page or section references, in `agents/researcher/findings/r013/brouet2012-notes.md`. Rewrite `entries/garment-transfer-surface-binding.md` from the notes, every condition marked (paper, with page), (measured) or (reasoned). Run the R-011 garment-transfer prompt (`agents/researcher/findings/r011/prompt-garment-transfer.md`), unchanged, twice more as fresh agents with no tools, saving the answers verbatim. Score per the card's branches: count the entry's paper-sourced conditions and numbers that none of the three runs named.

**Blockers:** the paper's PDF. HAL, the ACM Digital Library and the SIGGRAPH archive all refuse automated downloads (checked 2026-11-14). It has to be saved by hand as `sources/brouet2012.pdf` (git-ignored, as in `style`). Resolved 2026-11-14: saved by hand, 12 pages.

**Artifacts:**
- agents/researcher/findings/r013/brouet2012-notes.md (notes against the six questions; the 16 scoring items, fixed before runs 2 and 3 were read)
- agents/researcher/findings/r013/answer-garment-transfer-run2.md, -run3.md (verbatim), score.md
- entries/design-preserving-garment-transfer.md (new: the paper describes a different mechanism)
- entries/garment-transfer-surface-binding.md (the paper's conditions; the relax dispute settled as a question of rest shape)

**Result:** 11 of 16 paper items named by none of the three runs, 6 of them general; the branch is taken (reading in full is the rule). All six general items belong to grading, a goal the prompt didn't pose and no run raised, so the addition was a reframe. R-014 tests whether the paper also adds inside its own frame.

**Closed:** 2026-11-14

### R-014 · Does the paper add anything inside its own frame?

**Status:** open
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
R-013 found that what Brouet et al. 2012 added over three agent runs was a reframe: grading the garment instead of re-draping the same one. Test whether it adds anything when the agent is asked about grading directly. Write a prompt that keeps R-011's garment-transfer setting (Blender, kameez, trousers, dupatta, 1.609 and 1.753 m figures) but asks how to produce a version of the garment graded to the second body, one that keeps the design, and how to check it, without naming any technique or criterion. Save it verbatim in `agents/researcher/findings/r014/` before running, then run it as three fresh agents with no tools and save each answer verbatim. Score against the six general items R-013's runs missed (items 2, 3, 5, 6, 8 and 9 in `agents/researcher/findings/r013/brouet2012-notes.md`), with the branches written in CARD.md before the runs. If the runs name most of the six, the paper's addition was the reframe alone; if they name few, it adds inside its frame too.

**Blockers:** none

**Artifacts:** —

**Closed:** —

### R-015 · Recent graphics literature for the test bed's measured problems

**Status:** closed
**Type:** research
**Priority:** high
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
The live card in `CARD.md`, at the user's request (2026-11-14): research graphics literature from recent years on AI, optimisation, GPU and model rendering, aimed at where the private test bed wants to use it. Four areas, each searched separately for 2023–2026 papers (2022 only where everything later builds on it, marked): (A) learned and neural cloth: draping, dynamics, detail added after simulation; (B) fast cloth solvers and GPU simulation, with or without contact guarantees; (C) differentiable cloth simulation and inverse garment fitting: gradients of a drape with respect to pattern parameters, image to sewing pattern; (D) model rendering: differentiable and neural rendering, inverse rendering of fabric and light, texture from photos. Each area saves its exact queries and every candidate looked at in `agents/researcher/findings/r015/<area>.md`, with venue and year, the work reused or avoided (axis and `reuse_changes`), code and licence, whether it runs without CUDA on a 16 GB Apple Silicon machine, the numbers it reports with their hardware, and whether the source was read past its abstract. The selection is by need, so the axis sort here is a record, not a test of the axes (R-012 stays parked). The mapping to the test bed's own write-ups stays in `private/` (git-ignored), since the test bed is private.

**Blockers:** none

**Artifacts:**
- agents/researcher/findings/r015/a-learned-cloth.md, b-fast-solvers.md, c-differentiable-fitting.md, d-rendering.md (queries, every candidate, the best few in depth, gaps)
- agents/shared/findings.md → [R-015]
- private/r015-map.md (git-ignored: the mapping to the test bed's own write-ups)
- agents/researcher/findings/r015/agent-reports.md (the four agents' final replies, verbatim)
- agents/researcher/findings/r015/verification.md (claims re-checked against primary sources; where the downloaded sources went; what was left out)
- sources/r015/ (git-ignored: 18 papers as PDF and text, and the pages behind specific claims)
- private/r015-briefs.md (git-ignored: the four briefs, verbatim)

**Result:** The card's first branch: Newton runs here without CUDA (CPU, speed untimed), and friction-off fitting, inexact inner drapes and cached sensitivities can be rebuilt inside Blender. Next full reading: R-016.

**Closed:** 2026-11-14

### R-016 · Read Dress-1-to-3 in full and rewrite the warm-start entry from it

**Status:** closed
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Read Xuan Li et al., "Dress-1-to-3: Single Image to Simulation-Ready 3D Outfit with Diffusion Prior and Differentiable Physics", ACM TOG / SIGGRAPH 2025 (arXiv 2502.03449), in full, with notes against these questions, each with a section reference: why each iteration's drape may start from the previous one (the static-equilibrium argument) and what breaks it; what removing friction does and doesn't buy, and how slip is prevented (the pinned waist loop); how many iterations and what each costs; how flipped triangles, remeshing and penetration are handled; what the method can't recover (new pattern pieces, loose garments). Save the notes in `agents/researcher/findings/r016/`. Then rewrite `entries/warm-start-repeated-drapes.md` with every condition marked (paper, with section), (measured) or (reasoned), and list what the paper says about friction as a condition of the entry. Before reading, fix the scoring items against the R-011 warm-start baseline answer (`agents/researcher/findings/r011/`), as R-013 did.

**Blockers:** none (open on arXiv)

**Artifacts:**
- agents/researcher/findings/r016/baseline-items.md (the R-011 baseline's 20 items, fixed before reading)
- agents/researcher/findings/r016/dress-1-to-3-notes.md (notes against the five questions, with sections)
- agents/researcher/findings/r016/score.md (8 paper items against the baseline)
- entries/warm-start-repeated-drapes.md (rewritten)
- sources/r016/li2025-dress-1-to-3.txt (git-ignored: the paper's text from arXiv HTML)

**Result:** 1 item by none narrowly (the pinned waist with friction off), 3 widely; the paper adds a remedy, not a reframe, and doesn't test the warm start.

**Closed:** 2026-11-14

### R-017 · An independent re-sort of R-012's abstracts

**Status:** closed
**Type:** review
**Priority:** high
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
R-012's sorter wrote the axes. A fresh agent, given only the first 60 abstracts in R-012's shuffled order and R-012's sorting rules (procedure.md steps 4–9, with the README's axis table and its cost-or-answer paragraph), sorts all 60 without seeing R-012's verdicts, its result or its decisions made during sorting. It writes `agents/researcher/findings/r017/resort.md`. Compare: (a) agreement on reuse or not, over papers both judged; (b) agreement on axis, over papers both call reuse; (c) the card's statistic on the second sorter's own first 20 reuse papers. Written before the run: if the second sorter's first 20 has at least 16 clean, R-012's keep verdict doesn't depend on who sorted. If fewer, R-012 is re-opened with an RCA and its verdict is stated as sorter-dependent. Either way, the per-axis counts and T-015/T-016 are compared.

**Blockers:** none

**Artifacts:**
- agents/researcher/findings/r017/resort.md (the second sorter's verdicts on all 60, with the cases the rules didn't settle)
- agents/researcher/findings/r017/comparison.md (agreement and components)

**Result:** The second sorter's first 20 had 19 clean, so R-012's keep verdict doesn't depend on the sorter. Same reuse verdict on 47 of 48 jointly judged papers (κ 0.96) under R-012's lenient reading, 45 of 48 (κ 0.87) under the strict one; same axes on 18 of 18. Many instances 13 of 20 for both.

**Closed:** 2026-11-14

### R-018 · Does "across many instances" hold two kinds of reuse?

**Status:** closed
**Type:** research
**Priority:** high
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Child of R-010; the live card in CARD.md (T-016). The 15 papers that either R-012 or R-017 placed on "across many instances" (R-012 ranks 5, 6, 8, 18, 20, 33, 40, 41, 47, 48, 50, 53, 55, 56, 58) are classified by what makes their reused work go stale. The classes are fixed in the card: (A) computed for this problem, (B) fitted to examples, (C) neither, or "unclear". A fresh agent does it blind from the abstracts and the class definitions alone, writing `agents/researcher/findings/r018/blind-kinds.md`; the orchestrator's own classification, done in parallel, is the comparison, not the test. Branch as in the card.

**Blockers:** none

**Artifacts:**
- agents/researcher/findings/r018/orchestrator-kinds.md (committed before the blind result was seen)
- agents/researcher/findings/r018/blind-kinds.md (the test)
- agents/researcher/findings/r018/comparison.md

**Result:** 13 of 15 clearly A or B (A 7, B 6), against a bar of 12; two kinds. Agreement with the orchestrator 14 of 15. A `kind` field added to the template for this axis.

**Closed:** 2026-11-14

### R-019 · Write the entries for "across many instances"

**Status:** open
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Child of R-010; R-010's shared description applies (5–8 entries from primary sources, each read in full per R-013, with METHOD.md step 2b and the Ericson / Real-Time Rendering note). Start from: precomputed radiance transfer (Sloan, Kautz and Snyder 2002); baked lighting; precomputed signed distance fields for static colliders; learned cloth simulators (HOOD, from R-015). File each by R-018's answer. Cut into one ticket per entry when started, since one entry with a full reading and a baseline is about one sitting.

**Blockers:** none (R-018 closed 2026-11-14: file each entry with `kind`, computed for this problem or fitted to examples)

**Artifacts:** —

**Closed:** —
