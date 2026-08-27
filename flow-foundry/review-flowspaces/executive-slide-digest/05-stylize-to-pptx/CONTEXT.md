---
id: executive-slide-digest-stage-05
title: "Stage 05 — Stylize to .pptx"
type: stage-context
stage: 5
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
  - "[[executive-slide-pptx-stylizer]]"
---

# Stage 5 — Stylize to .pptx (`CONTEXT.md`)

## Inputs

Stage 4's approved content set (`work/04-approved-content.md`) — the
complete, human-approved set of initiative sections, treated as immutable
content by this stage.

## Process

Apply the target instance's house PowerPoint template if one has been
sourced — title slide, per-initiative slide layout, RAG color-coding,
consistent bullet hierarchy. If no house template exists yet, apply the
concrete clean minimal default (one title slide, one slide per initiative,
neutral accent color for RAG status, legible body type) and flag the
missing house template as an explicit note on the title slide, rather than
inventing branding. Every initiative/section present in Stage 4's input must
appear as its own slide or slide group — dropping one to fit a layout is a
defect, and merging two initiatives onto one slide to save space is the same
defect. `Layer-3: executive-slide-pptx-stylizer` (skill spec staged in
`skill-foundry/review-skills/executive-slide-pptx-stylizer/`, `to-review`).

## Outputs

A **draft `.pptx`** containing every section from Stage 4's approved content
set, styled per the house template or the clean minimal default. Lands as
`work/05-draft.pptx`.

## Verify

A specific cross-stage trace check: the count and identity of
initiatives/sections in Stage 5's `.pptx` must exactly match Stage 4's
approved content set — same initiatives, same order, nothing added or
dropped. Result recorded as a one-line entry in the run's decision log.

## Review

- **Reviewer:** the manager.
- **Intensity:** `light` — pure formatting against an already-approved
  content set; no content judgment happens here.
- **Evidence:** the draft `.pptx` is available for the manager to skim
  before Stage 6's formal final review; no formal sign-off required at this
  boundary (that weight sits at Stage 6).

## Data boundary

- **Max data-class this stage handles:** `internal` (inherits Stage 4's
  classification; pure formatting, no new content sourced).
- **Sanctioned engine for this stage:** Copilot only — file generation of
  this kind is not a Rovo-native action, matching the
  `accomplishments-docx-stylizer` precedent. No Rovo adapter.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
