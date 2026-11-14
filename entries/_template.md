---
technique: <named plainly, e.g. "garment transfer by surface binding">
axis: <across time | across space | across runs | across resolutions | across shapes | across many instances>
kind: <only for across many instances: computed for this problem (stale when the fixed part it was computed from changes) | fitted to examples (stale as runtime inputs leave the examples); R-018>
reuse_changes: <cost only | the answer | depends (say on what)>. Cost only: the reused result is exact and only speed is at stake, so failure shows as slowdown. The answer: the reuse approximates, so failure shows as a wrong answer, and section 4 carries the content.
fields: [<where it is used: cloth simulation, rendering, collision detection, ...>]
source_docs:
  - <author(s), title, venue, year, link. The primary source; mark anything seen second-hand>
also_teaches: [<other reuse these sources show, which may get their own entries>]
patterns: [<short kebab-case names for reusable ideas; reuse existing names where they fit>]
agent_baseline: <METHOD.md step 2b: what a fresh agent proposed with no entry, and which of section 4's conditions it named; or "not checked">
tested_in: [<project, date, card: where the reuse was measured; or empty>]
---

# <Technique, in plain words>

**In one sentence:** <a plain statement someone could observe to be false. A number beats an adjective.>

**Use for:** <the kinds of repeated work this applies to.>

## 1. Sources

<What was read, and which parts (sections, tables). One line on the setting each source was written for (games at 60 fps, offline film, CAD), since its conditions are stated for that setting.>

## 2. What work is wasted

<Work that is repeated, or computed in more detail than the answer needs, and where it shows up: which computation, how often, how long. Every number says where it came from.>

## 3. The technique

<How the reuse works, described so someone could implement it from this section and the sources. One mechanism.>

## 4. When reuse stays valid

<One bullet per condition, each marked: (paper) stated in a source, (measured) measured in a test, (reasoned) argued from the method and untested. Sorted as in METHOD.md step 1.>

### Constant

### Conditional

### Varies

## 5. When it doesn't apply

<How it fails outside those conditions and what the failure looks like. Where the sources themselves don't use it. Cases that look similar but need something else.>

## 6. The check

<The measurement that tells a valid reuse from a failed one, stated so someone could run it.>

## 7. Tested

<Where, when, on what, and the numbers. Or: "Untested.">
