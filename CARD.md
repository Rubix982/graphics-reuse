# Card

_Template at the top, the live card below. One card open at a time; a card that takes more than one sitting to fill is too big._

## Template

1. **WHERE WE ARE.** The last thing established, as a number or a fact. One sentence.
2. **WHAT WE ARE DOING.** One action, stated so a second person could carry it out without asking.
3. **WHY.** What is not known now that will be known after.
4. **WHAT IS AFFECTED.** Which claims, files or numbers change if this comes back either way.
5. **CONCLUSION IF WE DO IT.** Both branches, in advance.
6. **CONSEQUENCE OF NOT DOING IT.** What breaks, stalls or stays unknown if this is skipped forever.

A card closes with a number, or with a sentence that could have come out the other way.

---

## Live card · R-004 · Do the six axes hold?

_Opened 2026-11-14._

1. **WHERE WE ARE.** Three entries exist (one tested in part, two untested), filed on six axes that came from about ten examples in one conversation.
2. **WHAT WE ARE DOING.** Sort the twelve techniques below onto the six axes, one axis per distinct mechanism, writing one line per technique: its mechanism or mechanisms, the axis for each, or "none fits" / "two fit" with the reason.
3. **WHY.** Whether the axes sort techniques cleanly is unknown. If they don't, every entry and every survey ticket is organised around a structure that will have to be redone.
4. **WHAT IS AFFECTED.** The axis table in `README.md`, the `axis` field in `entries/_template.md` and in the three entries, and the survey tickets R-005 to R-010 (one per axis).
5. **CONCLUSION IF WE DO IT.** If at least 10 of the 12 sort cleanly (each mechanism onto exactly one axis), keep the six axes and unblock the surveys. If 3 or more don't, revise the axes before writing more entries, and record which techniques broke them and how.
6. **CONSEQUENCE OF NOT DOING IT.** Entries pile up under axes that may not fit, and re-filing costs more with every entry. The surveys are scoped by axis, so they would be scoped wrong.

**The twelve**, chosen to span rendering, simulation, collision and geometry, and to include a few that may break the axes:

1. Warm-starting contact forces (Catto, GDC 2005)
2. Refitting a bounding-volume tree instead of rebuilding it
3. Sort and sweep with insertion sort on a nearly sorted list (collision broad phase)
4. Temporal reprojection / temporal anti-aliasing
5. ReSTIR (Bitterli et al., SIGGRAPH 2020), which reuses light samples across neighbouring pixels and across frames
6. Irradiance caching (Ward, Rubinstein and Clear, SIGGRAPH 1988)
7. Smoothed aggregation multigrid for cloth (Tamstorf et al., SIGGRAPH Asia 2015)
8. Learned upsampling of coarse cloth (Kavan et al., SIGGRAPH 2011)
9. Deformation transfer (Sumner and Popović, SIGGRAPH 2004)
10. Design-preserving garment transfer (Brouet et al., SIGGRAPH 2012)
11. Precomputed radiance transfer (Sloan, Kautz and Snyder, SIGGRAPH 2002)
12. Kinetic data structures (Basch, Guibas and Hershberger, SODA 1997)

Also note, for each, whether the template's section 2 ("What repeats") describes it naturally. The coarse-to-fine entry suggests it may not for every axis.

**Result:** —
