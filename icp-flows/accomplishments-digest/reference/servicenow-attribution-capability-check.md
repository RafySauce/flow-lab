---
id: servicenow-attribution-capability-check
title: "ServiceNow Attribution Capability Check — Accomplishments Digest"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
data-class: public
related: ["[[accomplishments-digest]]", "[[sp-servicenow-accomplishments-gatherer]]"]
---

# ServiceNow Attribution Capability Check — Accomplishments Digest

**Status: prepared, not executed.** This turns the primer brief's open
question ("is `resolved_by`, `closed_by`, or `assigned_to` at closure the
right 'this was the engineer's work' signal?") into a one-time probe that an
operator runs once per ServiceNow tenant at instantiation. Stage 5 reads the
recorded answer instead of guessing every run. The model is
`confluence-activity-history-capability-check.md`.

## How to use this

Run once per ServiceNow tenant, before the first real run, and again after
any change to the tenant's incident or task workflow. Record the result as a
decision-log entry in the instantiated flowspace (not this public repo), and
point to it from Stage 5's Inputs.

## Probe steps

1. **Pick 5–10 closed records per table** (INC, CTASK, SCTASK, PTASK) where
   you know who did the work. Include at least one record that was reassigned
   and at least one that was reopened.
2. **Read the candidate fields** through the same interface Stage 5 will use
   (live connector, or the export report): `resolved_by`, `closed_by`, and
   `assigned_to` as of closure.
3. **Compare with what you know.** Which field names the person who
   actually did the work most reliably? Tables often differ. Incidents
   commonly carry `resolved_by`, while tasks may only have `closed_by` or
   `assigned_to`.
4. **Check the time-to-resolve fields.** Confirm that `opened_at` and
   `resolved_at`/`closed_at` are populated, and whether a state-history
   table is readable. Without it, reopens are inferred from the reopen count
   field only.
5. **Record one attribution field per table** using the table below.

## Decision table

| Finding for a table | Attribution field | What Stage 5 does |
|---|---|---|
| `resolved_by` populated and accurate | `resolved_by` | Counts records resolved by the engineer. |
| No `resolved_by`; `closed_by` accurate | `closed_by` | Counts records closed by the engineer, and notes that closer may differ from fixer. |
| Only `assigned_to` at closure is reliable | `assigned_to` at closure | Counts these records, but labels them "assigned at closure" in the digest so the load summary doesn't overstate ownership. |
| No field is reliable | none | Excludes the table from volume. Records may still appear as evidence when another source links them. The gap is noted. |

## What this does not resolve

This probe does not change the never-merge rule: records assigned at some
point but resolved by someone else are always kept separate. It also doesn't
sanction an engine. Live access depends on the employer's tool matrix, and
export mode is the fallback.
