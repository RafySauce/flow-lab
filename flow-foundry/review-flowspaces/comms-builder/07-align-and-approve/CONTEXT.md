---
id: comms-builder-stage-07
title: "Stage 07 — Align & Approve"
type: stage-context
stage: 7
review-intensity: heavy
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
---

# Stage 7 — Align & Approve (`CONTEXT.md`)

## Inputs

Every work artifact the run produced: `work/01-framing-brief.md` through
`work/06-meeting-pack.md` (whichever the lane ran), including the open
`[NEEDS INPUT]` list from `work/05-drafts.md` and the render-status line
from `work/04-comms-plan.md`.

## Process

1. Present the pack in reading order: framing, audience map, plan and
   timeline (campaign), drafts, meeting pack.
2. Walk the requester through four checks against Stage 1's framing: right
   segments, right asks, right dates, nothing sensitive.
3. Resolve every open `[NEEDS INPUT]` marker with the requester's own text,
   or record it as deliberately left open.
4. Apply edits the requester asks for; re-run the affected Verify traces
   (Stage 2 → 5 for facts, Stage 4 → 5 for ids).
5. Offer a one-off → campaign upgrade if the review surfaces more segments
   or a validation need; on yes, log it and re-enter at Stage 4.
6. If the instance has a house comms approval step, route the pack there
   and record who approved.

`Layer-3: inline (one-off, described above)` — human judgment.

## Outputs

`work/07-approval.md`: the approved pack version, a line per check (pass /
edited, with what changed), resolved and deliberately open markers, any
lane upgrade, and the approver(s) with date.

## Verify

Stage 7 → Stage 3 trace: the approved drafts address exactly the segments in
the final `work/03-audience-map.md`, after any edits made here. One-line
result in the run's decision log.

## Review

- **Reviewer:** the requester; the house comms approver where the instance
  has one.
- **Intensity:** `heavy` — the content-correctness gate before anything
  leaves the flow.
- **Evidence:** `work/07-approval.md` with approver and date.

## Data boundary

- **Max data-class this stage handles:** `internal`.
- **Sanctioned engines for this stage:** Copilot.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
