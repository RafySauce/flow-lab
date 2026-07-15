---
id: custody-model
title: "Custody Model — Registry, Freshness, and the Standing Custodian"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[documentarian]]"
  - "[[doc-type-registry]]"
  - "[[documentation-standards]]"
  - "[[sp-doc-custodian]]"
---

# Custody Model — Registry, Freshness, and the Standing Custodian

The "maintain over time" half of the documentarian mandate. Stages 2 and 7
operate this model today with a human driving; it is written so a scheduled
agent-custodian can operate it tomorrow without changing the contracts —
the custodian's authority never exceeds what Stage 07 grants a human-driven
run.

## The doc-registry index

One index per governed documentation scope (typically one per Confluence
space), living as a page in that space (primary) and mirrored per
mirroring-protocol §2. One row per governed document:

| Field | Content |
|---|---|
| `id` | The document's stable id (title derives from it) |
| `doc-type` | One of the six registry types |
| `surface` | Confluence URL (+ `servicenow-pending` note where staged) |
| `owner` | The accountable human |
| `last-verified` | Date a human last confirmed the content against reality |
| `review-by` | Next due date, per the type's cadence in `documentation-standards.md` (shortened while open sections are waived) |
| `status` | `active` / `archive-candidate` / `archived` / `archive-declined (date)` / `servicenow-pending` |
| `notes` | Waived open sections outstanding (with owners); supersession pointers |

The registry is bookkeeping, not truth: the page itself is authoritative for
content, the row for custody state. A row whose page is gone, or a page whose
row is missing, is drift — a tree-audit finding.

## Freshness signals

From `documentation-standards.md`: review-by lapses (per-type cadence), dead
links past threshold, orphaned position, departed owner. Stage 02 collects
them in `tree-audit`/`modernize` modes; Stage 07 stamps the dates that make
them computable. A document is never auto-archived off a signal — signals
nominate `archive-candidate`, humans confirm (Stage 07, per item).

## Archive procedure

1. Nomination: an audit finding or a work-order archive line, with staleness
   evidence recorded.
2. Inbound-link check: pages other active documents link to get re-pointed
   first, or the archive is declined.
3. Per-item human confirmation (Stage 07 — no batch approvals; each item is
   its own yes).
4. Execution via the tenant's confirmed mechanism — fixed once per tenant at
   instantiation: archive space, archive label, or Confluence native
   archiving. **Archive, never delete.**
5. Registry row → `archived`, with supersession pointer where a replacement
   exists.

## Custody review scheduling

Every Stage 07 close records the next custody review date for the touched
scope (space or tree). That date is the trigger for the next `tree-audit`
job — custody runs on a clock, not on someone remembering. Cadence default:
quarterly per space; the operator tunes per scope.

## Operating notes for the standing custodian (future)

When agents run custody on schedule (the "agents as custodians" end state),
the same contracts hold, plus:

- **Entry point:** a scheduled custodial run enters at Stage 1 as a
  `tree-audit` job (the trigger is the recorded custody review date) and
  runs the full pipeline — it does not shortcut into Stage 7.
- **Standing constraints:** read-everything, propose-everything,
  execute-only-what-a-human-confirmed. The custodian files audit reports and
  work orders; commit and archive stay behind their existing human gates
  (Stages 6 and 7). No accumulation of standing write authority.
- **Report over silence:** a custodial run that finds nothing actionable
  still leaves its one-line decision-log entry and re-arms the next review
  date — the audit trail is the point (`governance-and-audit.md`).
- **Escalation:** registry drift (row/page mismatches), departed owners, and
  systematic staleness (a whole tree past review-by) go to the operator as
  findings, never get "fixed" unilaterally.
