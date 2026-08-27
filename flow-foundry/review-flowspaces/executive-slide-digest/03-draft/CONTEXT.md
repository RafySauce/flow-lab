---
id: executive-slide-digest-stage-03
title: "Stage 03 — Draft"
type: stage-context
stage: 3
review-intensity: light
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
  - "[[executive-slide-drafter]]"
---

# Stage 3 — Draft (`CONTEXT.md`)

## Inputs

Stage 1's framing brief (`work/01-framing-brief.md`) and Stage 2's gathered
material (`work/02-gathered-material.md`) — both required; drafting from the
gathered material alone loses the manager's own scope and audience framing.

## Process

Synthesize both inputs into the house `reference/executive-slide-shape.md`
content: outcome-first accomplishments, a RAG status call that names the
Stage 2 signal driving it, risks/blockers (omitted outright if none),
upcoming milestones, and an optional ask. Single-initiative scope produces
one slide's content; portfolio-rollup scope produces a full deck outline
(title/agenda, one section per initiative, an optional closing rollup).
`Layer-3: executive-slide-drafter` (skill spec staged in `skill-foundry/
review-skills/executive-slide-drafter/`, `to-review`).

## Outputs

A **draft** in the house shape — one slide's content, or a deck outline for
portfolio scope — with every thin-coverage flag from Stage 2 carried forward
explicitly rather than smoothed over. Lands as `work/03-draft.md`.

## Verify

A specific cross-stage trace check: every RAG status call in the draft must
cite the specific Stage 2 signal (a named blocker, a slipped date, an open
critical bug) that drove it. A status with no traceable Stage 2 signal is
unverifiable and must be corrected before Stage 4 review. Result recorded as
a one-line entry in the run's decision log.

## Review

- **Reviewer:** the manager.
- **Intensity:** `light` — synthesis against a defined shape and two
  upstream inputs; no new framing judgment happens here.
- **Evidence:** the draft is available for the manager to skim before Stage
  4's formal align/publish pass; no formal sign-off required at this
  boundary.

## Data boundary

- **Max data-class this stage handles:** `internal` (inherits Stage 1's and
  Stage 2's classification; no new external source touched).
- **Sanctioned engines for this stage:** Rovo or Copilot — pure synthesis, no
  Atlassian-native-access constraint applies here the way it does for Stage
  2.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
