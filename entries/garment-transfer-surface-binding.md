---
technique: garment transfer by surface binding
axis: across shapes
reuse_changes: the answer, by design. The garment comes out graded to the new body.
fields: [cloth simulation, garment modelling, character pipelines]
source_docs:
  - Robert W. Sumner, Jovan Popović. Deformation Transfer for Triangle Meshes. ACM Transactions on Graphics 23(3), SIGGRAPH 2004.
  - Rémi Brouet, Alla Sheffer, Laurence Boissieux, Marie-Paule Cani. Design Preserving Garment Transfer. ACM Transactions on Graphics 31(4), SIGGRAPH 2012. https://hal.archives-ouvertes.fr/hal-00695903v1
  - Blender manual, Surface Deform and Mesh Deform modifiers.
also_teaches: [pattern grading as constrained optimisation (Brouet et al.), cage-based deformation (Mesh Deform)]
patterns: [transfer-then-relax, bind-to-surface]
agent_baseline: not checked
tested_in: [a private test bed, 2026-11-11, its own notes. The transfer only]
---

# Garment transfer by surface binding

**In one sentence:** Carrying a settled kameez and trousers from a 1.609 m figure to a 1.753 m one took 1.2 s against about 6 minutes for a fresh drape, and their edges came out stretched by 6–7 % at the median and 22–30 % at the 95th percentile.

**Use for:** a garment already draped on one body that is needed on another body of similar shape.

## 1. Sources

Sumner and Popović give the general method: carry a deformation from one mesh to another through a correspondence between them. Brouet et al. are specific to garments and treat transfer as pattern grading. They turn a pattern-maker's grading rules into geometric requirements (keep the design, keep proportions, keep the fit) and solve for the transferred garment as a constrained optimisation, several layers at once. Neither paper has been read in full for this entry; what is said of them here comes from their abstracts. The measurement is the test bed's own record.

## 2. What work is wasted

A garment that has already settled on one body is draped again from its flat pattern on another. In the test bed an A-pose drape takes about 4–7 minutes (its run records, 2026-11-09 and 2026-11-10), and one export step drapes every garment again on the standard figure: 11.5 and 14.4 minutes for two designs, with its gate, export and checks (the test bed's own notes).

## 3. The technique

Bind each point of the draped garment to the nearby surface of the body it was draped on, then move the binding to the new body; the garment follows in one step. In Blender this is the Surface Deform modifier. Mesh Deform is the version with a cage, a coarse closed mesh around the body. The full technique as intended is transfer, then a short relax under the cloth solver, so the garment settles under gravity on the new body.

Brouet et al. is the better-founded version of the same move: it grades the garment on purpose, under a pattern-maker's rules, where surface binding grades it as a side effect of following the body.

## 4. When reuse stays valid

### Constant

Constant here means it follows from how the method works; there is one measurement so far.

- The transfer costs one evaluation of the binding, however long the drape took. (measured: 1.2 s against about 6 minutes)
- Surface binding stretches the cloth with the body and doesn't keep the garment's lengths. What it produces is the garment graded to the new body. (measured: edges 1.06–1.07× at the median, 1.22–1.30× at the 95th percentile. paper: Brouet et al. frame transfer as grading)

### Conditional

- Valid only where the garment lies close to the surface it is bound to. (measured: kameez and trousers carried with 1 and 0 points inside the new body; the dupatta's free end tore)
- When the two bodies' meshes don't share numbering, the binding has to go through a correspondence (nearest point, or a proper map), not through vertex index. (measured: the two bodies shared their point count, but only 0.4 % of points were within 1 cm by index)
- The relax afterwards should be short when the binding is close, because the carried shape is already near rest. (reasoned, untested)

### Varies

- Nothing recorded yet.

## 5. When it doesn't apply

- Free-hanging cloth bound to distant parts of the body tears. In the test bed the dupatta's free end stretched to 4.9× its edge length at the 95th percentile, with 96 points inside the new body; it needs its own drape. Whether this holds for any surface binding or only for Blender's is T-004.
- A garment of fixed size (a dupatta of a set length) comes out resized with the body.
- When the same garment, unchanged, has to hang on the new body, the transfer gives the wrong answer by design. Only the relax afterwards could recover it, and that is untested.

## 6. The check

- Garment points inside the new body: want 0.
- Edge lengths on the new body against the original: the median and 95th-percentile ratio.
- Cloth crossing cloth: want 0 (the test bed's crossing check).
- Against a full re-drape on the new body, over several seeds: landmark lengths and silhouette within the re-drapes' seed-to-seed spread. Not yet run.

## 7. Tested

A private test bed, 2026-11-11. A-pose garments carried by Surface Deform from the standard figure (1.609 m) to a registered figure (1.753 m) in 1.2 s, against about 6 minutes for an A-pose drape. Each standard point went to the nearest point of the other body in one frame.

- Kameez and trousers: 1 and 0 points inside the new body; edges 1.06–1.07× at the median, 1.22–1.30× at the 95th percentile. Accepted in the test bed as grading.
- Dupatta: torn (95th percentile 4.9×, 96 points inside).

Not tested: the relax afterwards, and the comparison against a full re-drape.
