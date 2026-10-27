---
id: sp-servicenow-accomplishments-gatherer
title: "Skill Primer Brief — ServiceNow Accomplishments Gatherer"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
generated-by: flow-foundry
data-class: public
related: ["[[accomplishments-digest]]", "[[servicenow-ticket-ingest]]"]
---

# Skill Primer Brief — ServiceNow Accomplishments Gatherer

> Filed from a Layer-3 gap in `accomplishments-digest` 2.0, Stage 5 (Gather —
> ServiceNow). Intake record:
> `flow-foundry/backlog-flow-starters/fp-accomplishments-digest-m365-servicenow.md`.

## Purpose

Show the run-the-business work one engineer did in a review period, with
context: the incidents, change tasks, catalog tasks, and problem tasks they
resolved or closed. This replaces pulling and counting ServiceNow reports by
hand.

## Triggering intent

- `accomplishments-digest` Stage 5, with a framing brief in hand.
- "How many INCs and tasks did I close this half, and what kind?"

**Near-misses that should not trigger it:** team or service flow analysis
(`servicenow-ticket-ingest` for `statik-adoption`); comparing people; any
write or ITSM action; incident investigation.

## Method sketch

- Choose and state the source mode: live, export, or skipped.
- Attribute records using the tenant's field from
  `servicenow-attribution-capability-check.md`, applied per table.
- Read structured fields only, and page through every result. Confirm the
  count with the engineer. Map numeric state values to labels, and flag reopens.
  (These mechanics are borrowed from `servicenow-ticket-ingest`.)
- Keep **resolved/closed by** apart from **assigned at some point**, and
  never merge the two.
- Compute: counts by type, priority mix, median time to resolve by priority,
  problem-led fixes, and reopens. Group records by service or domain.
- Paraphrase short descriptions. Cite records that carry customer names,
  hostnames, or IPs by number only.
- **Failure modes to guard against:** overstating ownership through `assigned_to`; silent
  pagination truncation; any peer or team-average comparison; reading work
  notes.

## Inputs and data boundary

- **Inputs:** the Stage 1 framing brief (period, ServiceNow identity, themes)
  and the tenant's attribution field.
- **Max data-class:** `internal`. Halt on `confidential` or `restricted`.
- **Engine:** any engine sanctioned for ServiceNow reads, decided at runtime.
  Export mode works on any engine sanctioned for `internal`. Read-only always.

## Demand source

`accomplishments-digest` 2.0, Stage 5. This is a new per-person skill and
deliberately not a widening of `servicenow-ticket-ingest`. That skill is
aggregate-only and names a group, never a person, and that guarantee
protects `statik-adoption`.

## Definition of done

- The record count matches the engineer's confirmed count.
- The assigned-but-not-resolved list never leaks into the load summary.
- Median time to resolve is computed per priority, with the formula stated.
- A simulated run on a synthetic export with reassigned and reopened records
  classifies both correctly.
- Unreachable with no export produces a declared skip.
