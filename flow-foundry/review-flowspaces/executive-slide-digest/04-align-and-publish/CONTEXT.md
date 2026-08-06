---
id: executive-slide-digest-stage-04
title: "Stage 04 — Align & Publish"
type: stage-context
stage: 4
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

# Stage 4 — Align & Publish (`CONTEXT.md`)

## Inputs

Stage 3's draft (`work/03-draft.md`) and Stage 1's original framing brief
(`work/01-framing-brief.md`) — the manager checks the draft against their
own original ask, not just against the draft in isolation.

## Process

The manager's own edit/approval pass: does every RAG call hold up, does the
framing still match what they meant in Stage 1, is anything missing or
overstated, does the optional ask (if any) read correctly for the intended
exec. This is the content-correctness gate — the last point at which content
can change before Stage 5 turns it into a fixed-format `.pptx`.
`Layer-3: inline (one-off, human judgment)`.

## Outputs

An **approved content set** — Stage 3's draft with the manager's edits
applied, treated from this point forward as immutable content. Lands as
`work/04-approved-content.md`.

## Verify

A specific cross-stage trace check: Stage 5's `.pptx` must contain every
initiative/section present in this stage's approved content set, and no
content beyond it. Stage 6's reviewer confirms this by comparing the shared
deck against this file directly. A dropped or invented section at Stage 5 is
the failure mode this catches. Result recorded as a one-line entry in the
run's decision log.

## Review

- **Reviewer:** the manager (this is their own review — no delegate).
- **Intensity:** `heavy` — the content-correctness gate; nothing downstream
  corrects a wrong RAG call, a missed risk, or a misstated ask once Stage 5
  has stylized it.
- **Evidence:** an explicit approval statement from the manager, logged in
  the run's decision log, before Stage 5 starts.

## Data boundary

- **Max data-class this stage handles:** `internal` (inherits Stage 3's
  classification).
- **Sanctioned engines for this stage:** Rovo or Copilot, whichever the
  manager is using.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
