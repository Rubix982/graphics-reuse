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

**Status:** blocked
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: warm starting in contact solvers (Catto 2005); refitting bounding-volume trees; sort and sweep on nearly sorted lists; temporal reprojection and temporal anti-aliasing; kinetic data structures (Basch, Guibas and Hershberger 1997).

**Blockers:** R-012 (the axes may change)

**Artifacts:** —

**Closed:** —

### R-006 · Survey: across space

**Status:** blocked
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: ReSTIR's spatial reuse (Bitterli et al. 2020); irradiance caching (Ward, Rubinstein and Clear 1988); photon mapping's density estimation; spatial denoising filters.

**Blockers:** R-012 (the axes may change)

**Artifacts:** —

**Closed:** —

### R-007 · Survey: across runs

**Status:** blocked
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: warm starting and numerical continuation (Allgower and Georg 1990); adjoint and differentiable simulation, where one backward pass replaces one forward run per parameter; incremental recomputation in node-based procedural tools.

**Blockers:** R-012 (the axes may change)

**Artifacts:** —

**Closed:** —

### R-008 · Survey: across resolutions

**Status:** blocked
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: multigrid for cloth (Tamstorf et al. 2015); learned upsampling (Kavan et al. 2011); adaptive remeshing (Narain et al. 2012); progressive meshes (Hoppe 1996); mipmapping and level of detail.

**Blockers:** R-012 (the axes may change)

**Artifacts:** —

**Closed:** —

### R-009 · Survey: across shapes

**Status:** blocked
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: deformation transfer (Sumner and Popović 2004); design-preserving garment transfer (Brouet et al. 2012); functional maps for correspondence between shapes (Ovsjanikov et al. 2012); skinning weight transfer; motion retargeting.

**Blockers:** R-012 (the axes may change)

**Artifacts:** —

**Closed:** —

### R-010 · Survey: across many instances

**Status:** blocked
**Type:** research
**Priority:** medium
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
Per the shared description. Start from: precomputed radiance transfer (Sloan, Kautz and Snyder 2002); baked lighting; precomputed signed distance fields for static colliders; learned cloth simulators.

**Blockers:** R-012 (the axes may change)

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

**Status:** open
**Type:** research
**Priority:** high
**Created:** 2026-11-14
**Updated:** 2026-11-14

**Description:**
The live card in `CARD.md`. Search DBLP (or Semantic Scholar, if DBLP can't filter by venue) for ACM Transactions on Graphics papers, 2000–2025, with *fast*, *faster*, *efficient*, *accelerat-* or *real-time* in the title. Save the exact query and the full hit list in `agents/researcher/findings/r012/`. Shuffle the list with `random.Random(1114).shuffle` and sort each paper from its abstract (is the speedup reuse; if so, axis per mechanism and `reuse_changes`) until 20 reuse papers are sorted, recording every paper looked at. The branches are written in the card: at least 16 of 20 clean keeps the axes and unblocks R-005 to R-010; 5 or more misfits means revising the axes first.

**Blockers:** none

**Artifacts:** —

**Closed:** —
