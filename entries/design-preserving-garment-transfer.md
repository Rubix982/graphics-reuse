---
technique: design-preserving garment transfer (grading the garment and its pattern to the new body)
axis: across shapes
reuse_changes: the answer, by design. The garment and its pattern come out graded to the new body, a different garment that keeps the design.
fields: [garment modelling, pattern grading, character pipelines]
source_docs:
  - Rémi Brouet, Alla Sheffer, Laurence Boissieux, Marie-Paule Cani. Design Preserving Garment Transfer. ACM Transactions on Graphics 31(4), SIGGRAPH 2012. DOI 10.1145/2185520.2185532. HAL hal-00695903v1. Read in full 2026-11-14; notes in agents/researcher/findings/r013/brouet2012-notes.md
also_teaches: [as-2D-as-possible deformation through transformation gradients (Section 5.1), collision resolution by gradually added equality constraints (Section 5.3), pattern extraction with ABF++ (Section 5.5), garment transfer by surface binding (entries/garment-transfer-surface-binding.md)]
patterns: [grade-not-stretch, relative-location, normal-preservation, layers-inside-out]
agent_baseline: "R-013, 2026-11-14 (claude-opus-5-5, fresh, no tools; three runs of the R-011 garment-transfer prompt): no run proposed grading or asked whether the garment should be graded. Of 16 paper items, 2 named, 3 partly, 11 by none, 6 of those general. The agents' frame was the same garment re-draped. Scoring: agents/researcher/findings/r013/score.md"
tested_in: []
---

# Design-preserving garment transfer

**In one sentence:** Grading a garment of 5,000–12,000 triangles to a body of different proportions takes 1–2 minutes of geometric optimisation on a 2 GHz laptop CPU of 2012, with no simulation, and the patterns re-extracted from the result are stretched by at most 0.3 % (L²-stretch 1.0002–1.003).

**Use for:** moving a garment to another body when what's wanted there is **the same design, graded to fit**: hems at the same body landmarks, the same flare, the same fit where it was tight. Not for showing the same cut of cloth hanging on a different person; for that, see the warm start and surface binding in `garment-transfer-surface-binding.md`. The test bed's verdict on its own Surface Deform test, "accepted as grading" for the kameez and trousers, says grading is what the test bed wants for those garments.

## 1. Sources

Brouet et al. 2012, read in full. Setting: virtual characters for film and games, offline, on a 2012 laptop CPU. Validated by a fashion designer's judgement against the criteria of traditional grading, and by sewing a real dress for a doll from transferred patterns (Section 6, Fig. 11). All of its examples are garments worn on the body: dresses, skirts, tunics, overalls, trousers, tops, ruffled layers.

## 2. What work is wasted

Making the garment again for each new body. It took an experienced artist three hours to make the woman's outfit in the paper's Fig. 1 (patterns, placement, simulation, iteration; Section 1). Re-draping the same pattern on the new body is fast by comparison, but "produces a result that looks like a person wearing someone else's wrong size garment" (Section 2). In the test bed, one export step re-drapes every garment on the standard figure: 11.5 and 14.4 minutes for two designs (the test bed's own notes).

## 3. The technique

1. **Proportional scaling** (Section 4). Each garment vertex is tied to a point on a skeleton bone and to the skin point where the bone-to-vertex segment leaves the body, preferring directions orthogonal to the bone (σ = 0.1). On the new body, the vertex goes to the corresponding skin point plus the same offset. Vertices between two bones (between the legs, under the arms) get two references, blended.
2. **Shape-preserving optimisation** (Section 5). Minimise E = E_shape + E_rl + E_fit: keep each triangle's normal, letting it stretch and shear within its own plane ("as-2D-as-possible"); keep relative location (weight 0.5 inside loose regions, 1000 along borders, seams and tight regions); keep tight triangles at their distance from the body (weight 1000). Alternate an update of each triangle's target transformation with a linear solve for positions, the solver started from the previous positions. Converges; 6 iterations for a tunic without collisions (Fig. 7).
3. **Collisions** (Section 5.3), the one hard constraint: each vertex stays farther from its bone than the skin. Added top to bottom, two at a time, never removed.
4. **Layers** (Section 5.4): from the body outward, each finished layer treated as part of the body.
5. **Patterns** (Section 5.5): cut the result at the source's seams and flatten with ABF++. Darts that are no longer needed close and are dropped.

## 4. When reuse stays valid

### Constant

- No physics: the result is a geometric grading, and cloth mechanics are ignored. The authors show the design survives a later simulation in other poses, but give no measurement of that. (paper: Sections 3.1, 6, 7)
- The graded garment is almost unstretched relative to its own new pattern (L²-stretch 1.0002–1.003). So simulating it with the new pattern as the rest shape should start almost at rest. (paper for the number, Section 5.5; reasoned for the consequence, untested)

### Conditional

- The two bodies need a similar pose, a dense correspondence between them, and an animation skeleton each; the output is only as good as the correspondence. (paper: Sections 3.2, 6) The test bed's two bodies share their point count but not their numbering. (measured: 0.4 % of points within 1 cm by index, the test bed 2026-11-11)
- Grading keeps relative location: a knee-length hem stays at the knee and a waistline on the waist, whatever the height. That is right only when the pipeline wants a graded garment. (paper: Section 3.1)
- Shape is kept as surface normals, not distances: a flare keeps its slope, so a bell's hem widens in proportion to height. This bears on flared pieces such as a gharara. (paper: Section 3.1)
- Fit is kept only in tight regions, which are triangles close to the body and facing down or sideways. Enforcing fit on upward-facing areas (a belly) raises curvature and looks wrong; relaxing it everywhere also fails (Fig. 8). (paper: Section 5.2)
- Proportional shear has to be allowed. Methods that penalise shear, deformation transfer among them, can't express grading. (paper: Section 2)
- Each panel's curvature has to stay low enough to cut it from flat cloth. Graders relax fit or add darts when the body's curvature grows. (paper: Section 3.1)

### Varies

- Nothing recorded yet.

## 5. When it doesn't apply

- When the same garment has to appear on the new body (one product on different people, a dupatta of a set length): grading gives a different garment by design.
- Free-hanging cloth such as a dupatta isn't in the paper's examples. The method ties every vertex to a bone through a segment that should cross the skin once, and tests collisions along that segment ("in theory the garment can intersect other areas on the skin, this had not happened in practice", Section 5.3). A dupatta's free end, hanging away from the body or across an arm, is where that is most likely to break. (reasoned; T-004)
- Different poses, and meshes that aren't manifold. (paper: Sections 3.2, 6)
- The tight-region tolerance has to be adjusted per model source, because models differ in their smallest garment-to-body offset. (paper: Section 6)
- The tight-region rule assumes upward-facing tight areas come from the body, not the design; it can't tell bra seaming from a bust. (paper: Section 5.2)
- Cheaper alternatives the paper shows failing: scaling the patterns by the change in height and hip circumference, then simulating, gives an uneven hem and a baggy skirt (Fig. 3); skinning-based transfer leaves artifacts along silhouettes (Fig. 13).

## 6. The check

- The paper's: a fashion designer judging the output against grading criteria; making a real garment from the graded patterns (Fig. 11); the L²-stretch of the re-extracted patterns.
- For the test bed (reasoned, not yet run): landmarks measured against body features (hem against knee, sleeve end against wrist) on both bodies; no garment points inside the body; no cloth crossing cloth after layering; and a drape from the graded pattern compared with the geometric result within the test bed's seed-to-seed spread. The last one tests whether the grading survives physics, which the paper shows only by eye.

## 7. Tested

Untested in the test bed. The paper's own figures (Table 1): 11 s to 199 s per garment, 3 to 81 iterations, 0 to 67 collisions resolved; runtime driven mostly by the number of collisions.
