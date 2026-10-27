---
id: accomplishments-digest-stage-05
title: "Stage 05 — Gather — ServiceNow"
type: stage-context
stage: 5
review-intensity: light
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[sp-servicenow-accomplishments-gatherer]]"
  - "[[servicenow-ticket-ingest]]"
---

# Stage 5 — Gather — ServiceNow (`CONTEXT.md`)

## Inputs

Stage 1's framing brief (`work/01-framing-brief.md`): the period, the top
items and themes, the exclusion list, the engineer's ServiceNow user
identity, and the capability-probe result saying whether this engine can
reach ServiceNow live, or whether the engineer will supply an export
instead. Also needed is the tenant's attribution field: which field marks a
record as the engineer's own work (`resolved_by`, `closed_by`, or
`assigned_to` at closure). This is set once per tenant per
`../reference/servicenow-attribution-capability-check.md`. Independent of
Stages 2–4; it can run in parallel.

## Process

Choose the source mode explicitly and state it: **live** (read-only query
through the engine's sanctioned ServiceNow capability), **export** (the
engineer supplies a report export of the same tables), or **skipped**
("ServiceNow not reachable and no export supplied"). Skipped is a declared
gap, not a silent absence.

Read, for the period: incidents (INC), change tasks (CTASK), catalog tasks
(SCTASK), and problem tasks (PTASK) attributed to the engineer by the
tenant's attribution field. Read **structured fields only**: number, type,
priority, state, opened and resolved/closed timestamps, the attribution
field, assignment group, short description, and parent problem/change
links. Do not read work-note or comment bodies by default. Page through every
result and confirm the count against what the engineer expects. Map numeric
`state` values to their labels. Flag reopened records.

Keep two sets apart and never merge them: records **resolved or closed by**
the engineer, and records **assigned to them at some point** but resolved by
someone else. Only the first set counts as the engineer's volume.

Compute the load context: count by type, priority mix, median time to
resolve by priority, problem tasks that led to a permanent fix (a linked
change or a closed problem), and reopen count. Then group records by the
service or problem domain (the assignment group's service or the configuration item class)
so Stage 6 can match them to themes. Short descriptions are paraphrased.
Any record whose short description carries a customer name, hostname, or IP
is cited by number only.
`Layer-3: TBD — brief filed (sp-servicenow-accomplishments-gatherer)`.

## Outputs

A **ServiceNow digest** with three parts:

1. A **load summary**: counts by type, priority mix, median time to
   resolve, problem-led fixes, and reopens. This is the source for the
   Operational load section.
2. **Records grouped by service or domain**, each with number, type,
   priority, a paraphrased one-liner, and any linked problem/change.
3. The **assigned-but-not-resolved list**, kept separate, plus the source
   mode used and the attribution field applied.

Lands as `work/05-servicenow-digest.md`.

## Verify

A specific cross-stage trace check. The digest's record count matches the
count the engineer confirmed (or the export's row count). Every Stage 1 top
item that plausibly maps to operational work appears in the digest, or is
flagged "not found in ServiceNow — narrative only." No record from the
assigned-but-not-resolved list is counted in the load summary. Result
recorded as a one-line entry in the run's decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `light`. This is constrained execution against a defined
  query, field set, and arithmetic.
- **Evidence:** the digest, available for the engineer to skim before
  Stage 6.

## Data boundary

- **Max data-class this stage handles:** `internal`. Incident records
  routinely carry customer references and hostnames, which is why only
  structured fields are read and sensitive short descriptions are cited by
  number only. If a record surfaces `confidential` or `restricted` content,
  halt and re-scope. Assignment groups and other people's names appear only as
  context. **No peer comparison:** never compare the engineer's volume
  with a colleague's or with a team average.
- **Sanctioned engines for this stage:** whichever engine the employer's
  sanctioned-tool matrix allows to read ServiceNow, decided at runtime by the
  Stage 1 capability probe. Export mode works on any engine sanctioned for
  `internal`. **Read-only always:** no ITSM action is ever taken.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
