---
id: accomplishments-digest-stage-01
title: "Stage 01 — Frame"
type: stage-context
stage: 1
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
  - "[[accomplishments-digest]]"
---

# Stage 1 — Frame (`CONTEXT.md`)

## Inputs

The engineer's verbal statement of: the review period (start/end dates, or a
named cycle e.g. "H1 2026 self-assessment"), the audience (manager only, promo
committee, skip-level), and — if known — a short list of what they personally
consider their top 3–5 contributions this period. No prior stage; this is the
flow's entry point.

## Process

Ask, don't assume: confirm the period as concrete dates (not "this year"),
confirm the audience (it changes tone and detail level in Stage 4), and
elicit the engineer's own read on impact before any tracker data is pulled —
this ordering matters, because framing set *after* seeing the Jira/Confluence
digest tends to anchor on whatever the tools happened to surface rather than
what the engineer actually thinks mattered. Also ask what to explicitly
exclude (a project that got cancelled, a sensitive reorg, anything not meant
for this audience). `Layer-3: inline (one-off, described above)`.

## Outputs

A **framing brief**: period (start date, end date), audience, a 3–5 item list
of self-identified top contributions (one sentence each, in the engineer's own
words), and an exclusion list. Lands in the run's working folder as
`work/01-framing-brief.md` (Layer-4, transient).

## Verify

A specific cross-stage trace check: Stage 4's draft must be able to point back
to every item in Stage 1's exclusion list and confirm none of it appears in
the synthesized document. If Stage 4 can't produce that confirmation, Stage 1's
exclusion list wasn't carried forward — stop and re-run the carry-through
before drafting continues. Result recorded as a one-line entry in the run's
decision log.

## Review

- **Reviewer:** the engineer (this is their own review — no delegate).
- **Intensity:** `heavy` — direction-setting judgment; nothing downstream can
  correct a wrong period, audience, or exclusion list without redoing the
  gather stages.
- **Evidence:** the framing brief itself, confirmed back to the engineer in
  plain language before Stage 2 starts ("here's the period, audience, and
  your top items as I understood them — correct?").

## Data boundary

- **Max data-class this stage handles:** `internal` (the engineer's own
  self-assessment framing; may reference sensitive exclusions).
- **Sanctioned engines for this stage:** per the employer's sanctioned-tool
  matrix — Rovo or Copilot, whichever the engineer is using; no data leaves
  the conversation at this stage (nothing external is queried yet).
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
