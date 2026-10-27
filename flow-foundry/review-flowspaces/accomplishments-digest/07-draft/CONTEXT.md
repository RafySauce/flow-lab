---
id: accomplishments-digest-stage-07
title: "Stage 07 — Draft"
type: stage-context
stage: 7
review-intensity: light
artifact-version: "2.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-10-27
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[accomplishments-drafter]]"
  - "[[sp-accomplishments-drafter-revision]]"
---

# Stage 7 — Draft (`CONTEXT.md`)

## Inputs

Stage 1's framing brief (`work/01-framing-brief.md`) and Stage 6's
confirmed correlation map (`work/06-correlation-map.md`). The gather digests
are not read directly: the correlation map already carries their evidence,
grouped and confirmed by the engineer. A draft built from the map without the
framing brief loses the engineer's own narrative and reads as a tracker
export.

## Process

Synthesize the confirmed accomplishment groups into the house
accomplishments-document shape defined in
`../reference/accomplishments-document-shape.md`. Themes are the top-level
structure, never one section per source tool: the reader shouldn't have to
know which tool an accomplishment came from. Each confirmed group becomes one
outcome-framed bullet, or a short cluster of bullets, under its theme. Stage 1's
self-identified top items get first placement or visible emphasis within
their themes. Recognition from Microsoft 365 goes into the collaboration
section or under the theme it supports. It is paraphrased unless the
engineer approved a quote at Stage 6.

Draft the **Operational load** section from the correlation map's load
summary: counts with context (priority mix, median time to resolve,
problem-led fixes). Never use a bare count as a headline, and never compare
with peers. Where volume supports an outcome theme, cite it there as
evidence too. Match tone and detail level to Stage 1's stated audience.
Carry every gap flag (thin coverage, skipped or unreachable source) forward
as an explicit note rather than smoothing it over.
`Layer-3: accomplishments-drafter` (revision brief filed:
`sp-accomplishments-drafter-revision`; the verified 1.0 skill does not yet
read a correlation map or draft Operational load, so until the revision
passes the gate, those two parts run inline as described above).

## Outputs

A **draft accomplishments document**: theme-structured, outcome-framed,
audience-matched, with an Operational load section when ServiceNow ran. Stage 1's top items are
visibly represented and coverage gaps are noted rather than hidden.
Lands as `work/07-draft.md`.

## Verify

A specific cross-stage trace check: every item in Stage 1's exclusion list is
absent from this draft (the check Stage 1's own Verify field defines). This
is the stage where that check runs, since it's the first stage producing
reader-facing prose. Also confirm that every bullet traces to a confirmed
Stage 6 group (no fabricated content), and that no group the engineer dropped
at Stage 6 reappears. Result recorded as a one-line entry in the run's
decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `light`. This is synthesis against a defined shape from a map the
  engineer already confirmed, not a new judgment call. The exclusion-list check
  above is non-negotiable regardless of intensity label.
- **Evidence:** the draft is handed to the engineer for Stage 8's review; no
  separate sign-off at this boundary.

## Data boundary

- **Max data-class this stage handles:** `internal` (synthesized content
  carries forward whatever the gather stages collected, at the same
  classification).
- **Sanctioned engines for this stage:** any engine sanctioned for
  `internal` content. This stage is pure synthesis, with no new external query.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
