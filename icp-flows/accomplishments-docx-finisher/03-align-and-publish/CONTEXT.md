---
id: accomplishments-docx-finisher-stage-03
title: "Stage 03 — Align & Publish"
type: stage-context
stage: 3
review-intensity: heavy
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-08
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[accomplishments-docx-finisher]]"
---

# Stage 3 — Align & Publish (`CONTEXT.md`)

## Inputs

Stage 2's draft `.docx` (`work/02-draft.docx`), Stage 1's flagged-additions
list, and the original handoff's exclusion list — all three, for direct
comparison. This stage's whole job is checking the styled document against
what was actually authorized, not reading it fresh for quality alone.

## Process

The engineer reads the styled `.docx` against three checks, in order: (1)
does every item on the handoff's exclusion list stay absent — re-confirming
what `accomplishments-digest` Stage 5 already checked once, since this is a
second pass through new hands (Copilot's) and a second surface (Word) where
something could slip back in; (2) does every Stage-1 flagged addition read as
supporting evidence, not a new claim — if any addition overstates or
introduces something not already in the source document, cut it; (3) does the
styling itself read as polished and appropriate for the intended audience, not
generic template output. This is the flow's only heavy-review stage — it
carries the full weight since it's the last human checkpoint before a file
leaves the ICP structure entirely. `Layer-3: inline (one-off, described
above)`.

## Outputs

The **final `.docx`**, shared directly with the intended audience (attached to
an email, uploaded to a promo packet system, etc.). Terminal artifact — once
shared, nothing in either flowspace consumes it further.

## Verify

A specific cross-stage trace check: the shared file's content, once diffed
against Stage 2's draft, shows only the edits the engineer explicitly made at
this stage — no untracked change between "reviewed" and "shared." Result
recorded as a one-line entry in the run's decision log — this is also the
run's closing entry for this flowspace.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `heavy` — the flow's compensating heavy-review stage (Stage
  1 deviated light per the documented U-curve exception); this is the true
  final-alignment checkpoint, "closer to debugging" than composing.
- **Evidence:** the engineer's explicit confirmation before sharing, plus the
  act of sharing itself as the record.

## Data boundary

- **Max data-class this stage handles:** `internal` (the finished file may be
  shared beyond the immediate team once published — confirm the audience
  matches the original handoff's stated audience before that happens).
- **Sanctioned engines for this stage:** Copilot for the review pass; sharing
  itself happens on whichever channel the employer's sanctioned-tool matrix
  designates for performance-review material.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
