# R-013 · Does an entry written from a full reading add anything over an agent? Scoring

_2026-11-14. The 16 paper items listed in `brouet2012-notes.md`, fixed before runs 2 and 3 were read, against three runs of the R-011 garment-transfer prompt: run 1 (`../r011/answer-garment-transfer.md`), run 2 and run 3 (this folder). Scored by Claude. "Named" means a run states the same condition in any words; "partly" means it names the case but not the condition, or uses it for a different purpose._

## The items against the runs

| # | Paper item (short) | Run 1 | Run 2 | Run 3 | Kind |
|---|---|---|---|---|---|
| 1 | Closest-skin-point binding slides; take references orthogonal to the bone | no | partly: nearest-point projection is ambiguous under the arms and at the crotch | partly: correspondence trouble at the armpits and crotch | general |
| 2 | Shear must be allowed; deformation transfer penalises it | no | no | no | general, grading |
| 3 | Pattern scaling by height and hip, then simulation: uneven hem, baggy skirt | no | no | no | general, grading |
| 4 | Relative location: a knee-length hem stays at the knee | partly: hem against knee as a check that fit hasn't changed | partly: where the hem falls against knee and floor, as a check | the opposite goal: "the same kameez should end higher on the leg" | general, grading |
| 5 | Shape kept as normals: a flare keeps its slope, a bell's hem widens with height | no | no | no | general, grading |
| 6 | Fit kept only in tight regions; loose regions may move off the body to keep their shape | no | no | no | general, grading |
| 7 | Tight = close and facing down or sideways; fit on upward-facing areas (a belly) fails | no | no | no | method |
| 8 | Manufacturability: curvature bounded per panel, or relax fit and add darts | no | no | no | general, grading |
| 9 | Grade the pattern: output graded 2D patterns | no | no | no | general, grading |
| 10 | Re-extracted patterns: L²-stretch 1.0002–1.003 | no | no | no | method, number |
| 11 | Collisions resolved top to bottom, a few at a time, never released | no | no | no | method |
| 12 | Layers from the body outward, each finished layer treated as body | yes | yes | yes | general |
| 13 | 1–2 minutes for 5,000–12,000 triangles on a 2012 laptop CPU | no | no | no | method, number |
| 14 | Purely geometric, no simulation in the transfer | partly: geometric binding then a settle, as the cheaper option | partly: projection then a settle | partly: deform then relax, option (b) | general |
| 15 | Sensitive to the tight-region tolerance, per model source | no | no | no | method |
| 16 | Similar pose, dense correspondence, rigged characters | yes (not rigging) | yes (not rigging) | yes (not rigging) | general |

Named by at least one run: 2 (items 12, 16). Partly: 3 (items 1, 4, 14). **Named by none: 11** (items 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 15). Leaving out the five that only matter inside the paper's own method or are its own numbers (7, 10, 11, 13, 15): **6 general items named by none** (2, 3, 5, 6, 8, 9).

## Verdict against the card

The card's branch: 3 or more paper items that none of the runs names means full reading adds over an agent. Every count clears it, including the strictest one (6 general items, with partial matches not counted as added). So the branch is taken: reading in full is the rule for every entry. METHOD.md already said so after R-011; this confirms it on an entry written that way.

## What the components say

All six general items the agents missed belong to one goal: **grading**, producing an adjusted garment and pattern that keep the design on the new body. The prompt asked about the other goal, matching a fresh drape of the same pattern, and all three runs answered that goal. None of them asked whether the garment on the new body should be the same garment or a graded one. Run 3 took the same-garment goal so far as to expect the hem to ride up the leg, the opposite of what grading keeps.

Inside the prompt's own goal, the paper added nothing the agents missed outright: its one same-garment item (closest-point binding slides) was half-named twice. So the full reading added a **reframe**, which brought its criteria and numbers with it. It didn't add more conditions inside the agents' frame.

The reframe matters for the test bed. Its own verdict on its Surface Deform test was "accepted as grading" for the kameez and trousers, so grading is the goal the test bed actually has for those garments. That is the question the agents didn't raise.

It also settles the disputed relax condition. The entry said the relax after surface binding is short; R-011's agent said it has to undo the grading stretch. Both are right, about different rest shapes. Relaxing toward the **original** pattern undoes the stretch (6–7 % at the median, measured in the test bed), as the agent said. Relaxing toward a pattern re-extracted from a **graded** garment starts almost at rest: the paper's re-extracted patterns have L²-stretch 1.0002–1.003. Which rest shape is right depends on the goal, which is the same reframe again.

## What the agents had that the paper doesn't

The paper is purely geometric, so the runs covered ground it never touches: keeping the flat pattern as Blender's rest shape key (all three runs), morphing the body inside the simulation, stopping at convergence instead of a fixed frame count, caching by input hash and reordering around the standard figure, measuring the fresh drapes' own spread, catching a garment too small for the new body through strain, never chaining transfers (run 3), and fold copying biasing a dataset (run 1). For a pipeline, the paper and the agents are complementary.

## Limits

- Scored by Claude, the same model family as the agents, from a list Claude wrote. The list was fixed before runs 2 and 3 were read, but after run 1.
- The grain of the items is mine. Splitting or merging them changes the count, though not past the branch: even merging the six grading items into one "grading" item leaves the conclusion that the paper's addition was the reframe.
- One paper, one entry, three runs.
- Not yet tested: whether an agent asked about grading directly would name items 2, 3, 5, 6, 8 and 9. If it would, the paper's addition is the reframe alone. If it wouldn't, the paper adds inside its own frame too. That is R-014's question.
