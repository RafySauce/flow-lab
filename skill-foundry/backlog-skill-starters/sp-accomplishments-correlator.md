---
id: sp-accomplishments-correlator
title: "Skill Primer Brief — Accomplishments Correlator"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
generated-by: flow-foundry
data-class: public
related: ["[[accomplishments-digest]]"]
---

# Skill Primer Brief — Accomplishments Correlator

> Filed from a Layer-3 gap in `accomplishments-digest` 2.0, Stage 6
> (Correlate). Intake record:
> `flow-foundry/backlog-flow-starters/fp-accomplishments-digest-m365-servicenow.md`.

## Purpose

Turn several source digests into one set of accomplishment groups, where each
group is one piece of work with all of its evidence. Then present the groups
for the engineer to confirm. This replaces the manual cross-referencing that
otherwise turns one fix into three bullets, or loses the link between an
incident and the thanks it earned.

## Triggering intent

- `accomplishments-digest` Stage 6, with the gather digests in hand.
- "Tie my tickets, emails, and incidents together into accomplishments."

**Near-misses that should not trigger it:** drafting prose
(`accomplishments-drafter`); deduplicating a backlog
(`portfolio-rationalization`); correlating anyone's evidence but the
engineer's own.

## Method sketch

- Match on hard identifiers first (INC/CHG/PRB/PTASK numbers, Jira keys,
  page links, file references).
- Then match on Stage 1 themes, labeled `inferred`.
- Keep everything else as a singleton. Never merge on similarity alone; flag
  a "possible duplicate" instead.
- Attach ServiceNow load context as evidence to the groups it supports, and carry the
  load summary through whole.
- Present the groups with top items first. Record the engineer's merges,
  splits, drops, and quote choices.
- **Failure modes to guard against:** over-merging; dropping an entry; letting an
  inferred match look as strong as an identifier match.

## Inputs and data boundary

- **Inputs:** the Stage 1 framing brief, plus whichever of the four digests
  ran, including declared skips.
- **Max data-class:** `internal`. No external queries.
- **Engine:** any engine sanctioned for `internal`.

## Demand source

`accomplishments-digest` 2.0, Stage 6. The operator chose a separate,
heavy-review stage (D3, D6). A skill rather than inline logic, because
identifier matching across sources is reusable beyond this flow.

## Definition of done

- Count in equals count out across all digests: each entry is grouped once
  or dropped by the engineer.
- Every match carries its basis (identifier, inferred, or singleton).
- Every top item maps to a group or an accepted "narrative only" flag.
- A simulated run with one incident present in three sources yields exactly
  one group, and a run with two look-alike incidents yields two groups plus
  a duplicate flag.
