# graphics-reuse

A reference of reuse techniques in graphics, drawn from the literature. Each entry says what work gets repeated, how some field avoids repeating it, when the reused answer is still good enough, and whether that has been measured.

Started 2026-11-14. Phase 1 is literature only: reading papers and writing entries. No tooling yet.

The method is adapted from `style`, a sibling repository that collects design knowledge for coding agents. The two make entries the same way (problem first, primary sources, the conditions written down, checked against what an agent already does) and test them differently: `style` uses a blind pick by a judge, this library a measurement against a fresh full computation. See [`METHOD.md`](METHOD.md).

## Organised by what gets reused

The same reuse patterns turn up in rendering, simulation, geometry processing and CAD, so entries are filed by what they reuse rather than by subfield:

| Axis | What is reused | Examples |
|---|---|---|
| across time | the previous frame or step | warm-starting a solver, refitting a bounding-volume tree, temporal reprojection |
| across space | a neighbour's work | ReSTIR's spatial reuse, irradiance caching |
| across runs | an earlier run with slightly different inputs | repeated drapes in a fitting loop, parameter sweeps |
| across resolutions | a coarse solution | multigrid, coarse-to-fine cloth |
| across shapes | a result on another shape or body | deformation transfer, garment transfer |
| across many instances | work paid once and reused for every case | precomputed radiance transfer, learned models |

These six came from about ten examples and haven't been tested yet. Testing them is the open card ([`CARD.md`](CARD.md)).

## Reading an entry

Each entry in `entries/` follows [`entries/_template.md`](entries/_template.md). Its header names the axis, the sources, `agent_baseline` (what a fresh agent proposed with no entry, or "not checked") and `tested_in` (where the reuse was measured, or empty). Every condition in section 4 is marked with how it is known: stated in a paper, measured, or reasoned from the method and untested.

## Entries so far

| Entry | Axis | tested_in |
|---|---|---|
| [Garment transfer by surface binding](entries/garment-transfer-surface-binding.md) | across shapes | a private test bed, 2026-11-11 (the transfer; not the relax) |
| [Warm-starting repeated drapes](entries/warm-start-repeated-drapes.md) | across runs | — |
| [Coarse-to-fine cloth](entries/coarse-to-fine-cloth.md) | across resolutions | — |

## Layout

```
entries/<technique>.md   the reference (template: entries/_template.md)
METHOD.md                how an entry is made and tested
CARD.md                  the open card
threads.md               open questions, as a tree
docs/premise.md          how the idea got here, and what each reframe broke
plan.md, agents/         project tracking: tickets, shared findings, glossary
CHANGELOG.md             one line per closed ticket, per session
```
