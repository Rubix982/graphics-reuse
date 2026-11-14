# Project: graphics-reuse

_Last updated: 2026-11-14 by O-001_

## Objective

A literature-grounded reference of reuse techniques in graphics, organised by what gets reused, where every entry says when the reused answer stays valid, how to check it, and whether it has been measured.

## Current Phase

Phase 1 — Literature. Reading and writing entries only; no tooling and no engineering.

## Active Tickets

| ID | Agent | Title | Status |
|---|---|---|---|
| R-013 | Researcher | Rewrite the garment-transfer entry from a full reading of Brouet et al. 2012 (CARD.md) | blocked: the PDF |
| R-012 | Researcher | Held-out test of the axes | parked |

## Blocked

| ID | Blocked By |
|---|---|
| R-005 to R-010 (one survey per axis) | R-012 (parked) |
| R-013 | the PDF, saved by hand to sources/ |

## Completed This Session

- O-001 · Initialize project structure
- R-001 · Write up the premise dry-run
- R-002 · Method and entry template, adapted from `style`
- R-003 · Three seed entries
- R-004 · Test the six axes on twelve known techniques (12 of 12, but not an independent test)
- R-011 · Agent baselines for the three seed entries (11 of 18 conditions named; circular; measurements are what the agent lacked)

## Next Orchestrator Action

When the PDF is in `sources/`, unblock R-013. When R-013 closes, follow its card's branch (full reading as the rule, or the README says literature entries are mainly a map for their reader), then resume R-012.
