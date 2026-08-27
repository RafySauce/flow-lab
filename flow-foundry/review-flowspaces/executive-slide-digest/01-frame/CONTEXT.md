---
id: executive-slide-digest-stage-01
title: "Stage 01 — Frame"
type: stage-context
stage: 1
review-intensity: heavy
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-06
updated: 2026-08-06
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[executive-slide-digest]]"
---

# Stage 1 — Frame (`CONTEXT.md`)

## Inputs

The manager's verbal ask: scope mode (single-initiative or
portfolio-rollup), the specific initiative(s)/keywords/epic name(s) in
scope, the audience, the time period, and any explicit ask or decision
needed from the exec. No prior stage; this is the flow's entry point.

## Process

Determine scope mode first — it decides whether Stage 3 drafts one slide's
content or a deck outline, and every downstream stage's Verify check depends
on getting this right up front. Confirm the initiative(s)/keywords/epic
names as concrete search terms, not a vague project name — Stage 2's native
search is keyed directly off whatever is captured here, so an imprecise term
produces an imprecise gather. Confirm audience and period. Ask explicitly
whether there's a decision or ask the exec needs to walk away with — this
becomes the optional Ask field in Stage 3's draft. `Layer-3: inline (one-off,
described above)`.

## Outputs

A **framing brief**: scope mode, the initiative(s)/keywords/epic names in
scope, audience, period, and any stated ask/decision. Lands in the run's
working folder as `work/01-framing-brief.md` (Layer-4, transient).

## Verify

A specific cross-stage trace check: Stage 3's draft's structure (one slide
vs. a deck outline) must match Stage 1's stated scope mode. A
portfolio-rollup ask drafted as a single slide (or vice versa) means Stage
1's framing wasn't carried forward — stop and re-run Stage 3 against the
correct scope mode. Result recorded as a one-line entry in the run's
decision log.

## Review

- **Reviewer:** the manager (this is their own review — no delegate).
- **Intensity:** `heavy` — direction-setting judgment; nothing downstream can
  correct a wrong scope, initiative list, or audience without redoing Stage
  2 onward.
- **Evidence:** the framing brief confirmed back to the manager in plain
  language before Stage 2 starts ("here's the scope, initiatives, audience,
  and period as I understood them — correct?").

## Data boundary

- **Max data-class this stage handles:** `internal` (the manager's own
  framing; may reference sensitive asks or decisions).
- **Sanctioned engines for this stage:** per the employer's sanctioned-tool
  matrix — Rovo or Copilot, whichever the manager is using; no data leaves
  the conversation at this stage (nothing external is queried yet).
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
