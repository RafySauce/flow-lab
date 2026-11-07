---
id: comms-builder-stage-02
title: "Stage 02 — Link Source Records"
type: stage-context
stage: 2
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
  - "[[sp-comms-context-linker]]"
---

# Stage 2 — Link Source Records (`CONTEXT.md`)

## Inputs

`work/01-framing-brief.md` — specifically the linked record numbers by
system, the comms type, and (for a response plan) the data rule statement.
Read access to ServiceNow and Jira as the session's capability probe
(`START-HERE.md` Step 1) found it. A one-off with no linked records skips
this stage and records the skip.

## Process

1. Probe each named source with one test read; record reachable or not.
2. For each linked record, pull only: number and link, short description,
   state, planned window (start/end, timezone), affected services or
   applications, stated customer/user impact, actions required of others,
   backout or contingency timing (time only, never steps), and owning
   group.
3. Apply the data rule to every field: exploit details, configurations, IP
   addresses, hostnames beyond service names, and control descriptions are
   dropped and replaced with "see <record number>".
4. Where a source is unreachable, ask the user to paste the record's summary
   fields; label the result "pasted, not live".
5. Flag conflicts between sources (e.g., Jira says one date, the change
   record another) for Stage 3 — never resolve them silently.

`Layer-3: TBD — skill-primer-brief filed (sp-comms-context-linker)`. Until
built, run the steps above inline.

## Outputs

`work/02-context-sheet.md`: one block per record with the fields in step 2,
each field cited to its record number; a source-status line per system
(live / pasted / skipped, with reason); a conflicts list (may be empty,
stated as "none"); and a line confirming the data rule was applied.

## Verify

Stage 2 → Stage 5 trace: every date, window, and affected service that
appears in any Stage 5 draft must trace to a cited field in
`work/02-context-sheet.md` or to the user's own words in
`work/01-framing-brief.md`. An uncited date in a draft is a defect. One-line
result in the run's decision log.

## Review

- **Reviewer:** the requester.
- **Intensity:** `light` — constrained retrieval against a fixed field list.
- **Evidence:** the requester skims the context sheet; conflicts are carried
  into Stage 3 rather than signed off here.

## Data boundary

- **Max data-class this stage handles:** `confidential` on read (security
  and incident records); `internal` on output — nothing above `internal`
  leaves this stage.
- **Sanctioned engines for this stage:** Copilot, read-only.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
