---
id: executive-slide-digest-stage-02
title: "Stage 02 — Gather"
type: stage-context
stage: 2
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
---

# Stage 2 — Gather (`CONTEXT.md`)

## Inputs

Stage 1's framing brief (`work/01-framing-brief.md`) — specifically the
initiative(s)/keywords/epic names and the time period. Nothing else is
pre-filtered; this stage searches, it does not pre-judge what's relevant.

## Process

Run the invoking engine's own native Jira (and Confluence, where relevant)
search, keyed off Stage 1's keywords/epic names — status, recent activity,
open blockers, upcoming due dates, within the stated period. This is
deliberately inline logic, not a dedicated gatherer skill: the primer brief
considered and rejected reusing `jira-portfolio-ingest` (portfolio-shaped,
reporting overhead this flow doesn't need) and `jira-accomplishments-
gatherer` (person-scoped, wrong unit of analysis). Assignee names may surface
incidentally in returned work items; they are not the point of the query and
must not be carried into slide content unless Stage 1's framing calls for
them. `Layer-3: inline (native search; see HUB.md Known gaps for the
narrowly-scoped-skill open question)`.

## Outputs

**Gathered material**: one entry per initiative in scope, each carrying
status signals, open blockers, recent activity, and upcoming due dates found
within the period — or an explicit "no recent activity found in the gather
window" note if the search surfaced nothing. Lands as
`work/02-gathered-material.md`.

## Verify

A specific cross-stage trace check: every initiative named in Stage 1's
framing brief must have a corresponding entry in this stage's output, even
if that entry is "nothing found." Silently dropping an initiative because
the search missed it is the failure mode this catches. Result recorded as a
one-line entry in the run's decision log.

## Review

- **Reviewer:** the manager.
- **Intensity:** `light` — constrained execution against a defined query; no
  framing judgment happens here.
- **Evidence:** the gathered material is available for the manager to skim
  before Stage 3 drafts from it; no formal sign-off required at this
  boundary (that weight sits at Stage 4).

## Data boundary

- **Max data-class this stage handles:** `internal` (work-item content; may
  include other contributors' names incidentally — do not expand scope to
  their individual performance).
- **Sanctioned engines for this stage:** Rovo, per the employer's matrix, for
  native Jira/Confluence search access; note at instantiation if a
  Copilot-side integration is also sanctioned.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
