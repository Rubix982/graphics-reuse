# R-018 · The blind classification, the bar, and the orchestrator's classification

_2026-11-14. The test is the blind agent's classification (`blind-kinds.md`: a fresh agent, claude-opus-5-5, no web, given only the 15 abstracts and the class definitions). The orchestrator's (`orchestrator-kinds.md`) was committed before the blind result was seen._

| # | blind | orchestrator |
|---|---|---|
| 5 | A | A |
| 6 | B | B |
| 8 | A | A |
| 18 | B | B |
| 20 | B | B |
| 33 | B | B |
| 40 | C | C |
| 41 | unclear | unclear |
| 47 | A | A |
| 48 | **A** | **both** |
| 50 | A | A |
| 53 | A | A |
| 55 | A | A |
| 56 | B | B |
| 58 | B | B |

- **The test:** the blind classification puts 13 of 15 clearly in A or B (A 7, B 6), against a bar of 12, with at least 3 in each. **The two-kinds branch is taken.**
- **Agreement:** 14 of 15. The one difference is rank 48 (a reduced deformable model per domain): A for the blind agent, "both" for the orchestrator, whose 12 sat exactly on the bar.
- **The line, in the blind agent's words:** a model fitted to one scene or subject is A "where the runtime input is a view, a light or an edit", and B where it is "a pose, motion, expression or state". So what separates the kinds is the input that varies at runtime, not where the precomputed work came from. In A, the varying input is something the precomputation was built to be independent of (lights over a fixed scene, views of a baked field, palette edits over one image). In B, the varying input is the thing the model was fitted over, so its validity is how well the examples covered it.
- **Outside both:** rank 40, precomputed correction vectors that depend on nothing in the problem (a table about the method), and rank 41, whose abstract doesn't say what its Pareto frontiers are computed from. Both classifiers agree on these.
