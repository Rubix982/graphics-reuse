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
**Answer:** —

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
**Answer:** —

### T-009 · Is "across runs" just "across time" for an outer loop?

**Status:** open
**Parent:** T-001
**Opened:** 2026-11-14
**Question:** None of R-004's twelve techniques landed on "across runs". Inside a simulation, history is the physics; across runs, each run is meant to be independent of history, so carrying it over is an error to guard against. Is that difference enough to keep a separate axis, or does the literature treat both the same way?
**Answer:** —
