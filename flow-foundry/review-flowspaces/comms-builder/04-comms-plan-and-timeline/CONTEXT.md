---
id: comms-builder-stage-04
title: "Stage 04 — Comms Plan & Timeline"
type: stage-context
stage: 4
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
  - "[[sp-comms-plan-builder]]"
  - "[[timeline-and-validation-tracker]]"
  - "[[design-system-binding]]"
---

# Stage 4 — Comms Plan & Timeline (`CONTEXT.md`)

## Inputs

`work/01-framing-brief.md` (comms type, key date), `work/02-context-sheet.md`
(window, backout timing), `work/03-audience-map.md` (segments, channels,
validation marks). `reference/comms-types-and-lanes.md` for the default
touchpoint set per type; `reference/timeline-and-validation-tracker.md` for
gantt conventions and the tracker shape; the instance's design-system
binding for color roles. Campaign lane only; a one-off skips this stage and
records the skip.

## Process

1. Lay the default touchpoint set for the comms type against the key date
   (e.g., T-14 announce, T-3 reminder, day-of, all-clear; delay/rollback
   notice held in reserve). Adjust with the user.
2. For each touchpoint: date, segments, channel, sender, and the message it
   needs (a Stage 5 draft id).
3. Build the validation tracker from segments marked "validates": what is
   validated, by which team, by when, status (default "not started").
4. Write the Mermaid `gantt` per the reference conventions; map touchpoint
   states to the binding's color roles; add the legend.
5. Render the gantt to an image where the engine can; always keep the raw
   Mermaid. Where it cannot render, say so and ship the table fallback.
6. Produce the plan in the target surface the user chose at Stage 1: chat,
   Confluence page body, or Jira comment (Jira gets the table fallback and
   a link, never Mermaid).

`Layer-3: TBD — skill-primer-brief filed (sp-comms-plan-builder)`. Until
built, run the steps above inline.

## Outputs

`work/04-comms-plan.md` (touchpoint table, validation tracker, legend, the
raw Mermaid in a fenced block, and the table fallback), `work/04-timeline.png`
when rendered, and a render-status line (rendered / raw only, with reason).

## Verify

Stage 4 → Stage 5 trace: every touchpoint row in `work/04-comms-plan.md`
names a draft id, and every one of those ids exists in `work/05-drafts.md`.
Stage 4 → Stage 2 trace: the key date on the gantt equals the window start
in `work/02-context-sheet.md`. One-line result in the run's decision log.

## Review

- **Reviewer:** the requester.
- **Intensity:** `light` — constrained execution against the default
  touchpoint set; dates and sequence get their real check at Stage 7.
- **Evidence:** the plan is available to skim; formal sign-off is Stage 7.

## Data boundary

- **Max data-class this stage handles:** `internal`.
- **Sanctioned engines for this stage:** Copilot.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
