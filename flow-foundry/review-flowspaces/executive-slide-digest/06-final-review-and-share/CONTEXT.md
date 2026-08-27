---
id: executive-slide-digest-stage-06
title: "Stage 06 — Final Review & Share"
type: stage-context
stage: 6
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

# Stage 6 — Final Review & Share (`CONTEXT.md`)

## Inputs

Stage 5's draft `.pptx` (`work/05-draft.pptx`) and Stage 4's approved
content set (`work/04-approved-content.md`) — the manager checks the styled
deck against the content they actually approved, not just against how it
looks.

## Process

The manager reads the generated deck slide by slide and confirms: every
section from Stage 4's approved content set is present and correctly
attributed, the RAG color-coding matches the approved status calls, nothing
reads as distorted or dropped by stylizing, and — if no house template was
configured — the missing-template note is present rather than silently
absent. On confirmation, the manager shares the deck directly.
`Layer-3: inline (one-off, human judgment)`.

## Outputs

The **shared `.pptx`** — the flow's terminal artifact. Once shared, it
leaves the ICP structure entirely; there is no Stage 7.

## Verify

A specific cross-stage trace check: re-run Stage 5's Verify by human eye
rather than by assuming Stage 5's own claim of completeness — every
initiative/section approved at Stage 4 must be visibly present, correctly
attributed, in the deck about to be shared. This is the same property Stage
5 already checked; Stage 6 exists because a stylizing defect that slipped
past an automated check is exactly the failure mode a heavy human gate
catches before something goes out the door. Result recorded as a one-line
entry in the run's decision log.

## Review

- **Reviewer:** the manager (this is their own review — no delegate).
- **Intensity:** `heavy` — the flow's final gate; nothing corrects a shared
  deck after the fact.
- **Evidence:** an explicit share action or confirmation, logged in the
  run's decision log.

## Data boundary

- **Max data-class this stage handles:** `internal` (inherits Stage 5's
  classification; the shared file itself may leave `internal` scope once it
  reaches its executive audience — that handoff is outside this flow's
  boundary).
- **Sanctioned engines for this stage:** Rovo or Copilot, wherever the
  manager views and shares from.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
