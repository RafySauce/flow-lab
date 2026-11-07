---
id: comms-builder-stage-06
title: "Stage 06 — Meeting Materials"
type: stage-context
stage: 6
review-intensity: light
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-11-07
updated: 2026-11-07
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[comms-builder]]"
  - "[[sp-deck-stylizer]]"
  - "[[design-system-binding]]"
---

# Stage 6 — Meeting Materials (`CONTEXT.md`)

## Inputs

`work/01-framing-brief.md` (implementation event: yes), `work/02-context-sheet.md`
(window, backout timing, owning groups), `work/03-audience-map.md`
(segments that attend or validate), `work/04-comms-plan.md` (validation
tracker, key date). The instance's design-system binding and deck template,
if set. Runs only on a campaign with an implementation event; otherwise
skipped and the skip recorded.

## Process

1. Draft the **run-of-show**: timed steps from start to all-clear, with the
   owning group per step, go/no-go checkpoints, and the backout decision
   time (time only, no technical steps).
2. Draft the **bridge-call agenda**: purpose, roles (lead, scribe, comms
   sender, validators by segment), checkpoint calls, how validation results
   are reported, and the all-clear or delay criteria.
3. Draft a **short deck** (opener, what is changing and when, roles,
   validation asks by segment, checkpoints, contacts) as content.
4. Style the deck through the design-system binding; with no binding, use
   the neutral default.

`Layer-3: TBD — skill-primer-brief filed (sp-deck-stylizer)` for step 4;
steps 1–3 inline (one-off to this flow).

## Outputs

`work/06-meeting-pack.md` (run-of-show table, bridge agenda, deck content
outline) and `work/06-implementation-deck.pptx` when styled, with a line
naming the binding used (instance system or neutral default).

## Verify

Stage 6 → Stage 4 trace: every validation row in the Stage 4 tracker
appears as a checkpoint or validator role in the run-of-show or agenda, and
the run-of-show start time equals the key date in `work/04-comms-plan.md`.
One-line result in the run's decision log.

## Review

- **Reviewer:** the requester, plus the implementation lead if different.
- **Intensity:** `light` — assembled from approved upstream content.
- **Evidence:** reviewed together with the whole pack at Stage 7.

## Data boundary

- **Max data-class this stage handles:** `internal`.
- **Sanctioned engines for this stage:** Copilot.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
