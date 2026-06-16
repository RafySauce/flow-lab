---
id: task-def-lightweight-tally
title: "Delivery Manager — Lightweight Tally Task Definition"
type: specification
artifact-version: "1.0"
created: 2026-05-25
updated: 2026-05-25
status: living
truth-level: draft
domain: ai
phase: "Phase 5 — Knowledge Architecture & AI Integration"
systems:
  - hermes
tags:
  - task-definition
  - ai/agentic-harness
source: human+ai
---

# Lightweight Tally — Task Definition

## Purpose

Keep Cincinnatus oriented between synthesis runs. Surface what is accumulating in the project and flag anything that warrants attention. Does not produce durable analysis — just keeps the signal visible.

## Trigger / Cadence

**Daily.** Run at the start of the day (or at the start of a working session if daily is too frequent in practice). Start time-based; revisit cadence once real usage patterns emerge. If multiple days pass with no intake, the run still produces a line — "nothing new" is a valid observation.

## Inputs (read-only)

1. `intake/` — list files, note filenames and approximate topics
2. `corpus/` — count items, note any new additions since last pulse entry
3. `traces/` — count items, note capability distribution across recent traces
4. `review/board.md` — scan for Active cards older than 14 days with no apparent movement

## Output (one appended line)

Append one dated line to `review/pulse.md`. Create the file if it does not exist.

**Format:**
```
YYYY-MM-DD: [N] intake | [N] corpus | [N] traces ([capability breakdown if >1 type]) | [FLAGS if any]
```

**Examples:**
```
2026-05-26: 0 intake | 3 corpus | 0 traces | —
2026-06-03: 4 intake | 5 corpus | 2 traces (decide×1, draft×1) | FLAG: intake cluster (Gitea×3)
2026-06-10: 1 intake | 5 corpus | 5 traces (decide×2, draft×2, summarize×1) | FLAG: stale Active card (Frigate, 18d)
```

**Writes nothing else.** No new files. No edits to existing files except the pulse append.

## Flags to surface (in the pulse line)

| Flag | Condition |
|---|---|
| `intake cluster ([topic]×N)` | 3+ intake items sharing a topic not yet served by a project room |
| `trace cluster ([capability]×N)` | 3+ traces with the same capability since the last synthesis run |
| `stale Active card ([name], Nd)` | A board card has been Active for 14+ days with no logged movement |

If no flags, write `—` in the flags position.

## Done-condition

`review/pulse.md` has a new line dated today. The counts are accurate. Any flags are named. The task is complete when the line is written — it does not require any action on the flags. Flags are for Cincinnatus to act on; the tally just surfaces them.

## Constraints

- Writes only to `review/pulse.md` (append only)
- Does not modify `board.md`
- Does not create synthesis findings
- Does not propose new project rooms
- Does not add usefulness fields to anything
