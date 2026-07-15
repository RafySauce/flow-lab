---
id: sp-doc-custodian
title: "Skill Primer Brief — Doc Custodian"
type: skill-primer-brief
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
related: ["[[documentarian]]", "[[custody-model]]"]
---

# Skill Primer Brief — Doc Custodian

## Purpose

Operate the custody model's bookkeeping at documentarian Stage 07: doc-
registry index rows, freshness and review-by stamping, per-item-confirmed
archive execution, and custody-review scheduling. This is the skill the
"agents as custodians of the documentation platforms" end state grows from —
which is exactly why its authority is bounded now: it executes only what a
human confirmed, and its standing-run mode proposes rather than acts.

## Triggering intent

- **Fires on:** documentarian Stage 07, once per job after the per-document
  loop drains; and (future) as the executing skill of a scheduled `tree-audit`
  custodial run's close.
- **Does not fire on:** deciding what to archive (audit findings nominate,
  Stage 03 plans, the human confirms per item — this skill executes and
  records); committing document content (`confluence-page-commit`);
  provenance frontmatter on mirror artifacts (`provenance-stamper`,
  referenced separately); deleting anything, ever.

## Method sketch

- Registry rows per the custody-model shape: id, doc-type, surface, owner,
  last-verified, review-by, status, notes — one row touched per document the
  job committed; waived open sections noted with shortened review-by.
- Review-by page properties set per the type's cadence in
  `documentation-standards.md`.
- Archive execution: per-item human confirmation presented with staleness
  evidence and inbound-link check; execution via the tenant's confirmed
  mechanism; **archive, never delete**; declined items become
  `archive-declined` registry notes.
- Record the next custody review date for the touched scope — the trigger
  for the next scheduled tree-audit.
- Job summary reconciling the work order line-for-line (committed / waived /
  struck / archived / declined).
- Failure modes to guard: committed pages missing registry rows (the
  untracked-document failure this flow exists to prevent); batch-approving
  archives; "cleaning up" declined archive candidates on a later run without
  a fresh confirmation.

## Inputs and data boundary

Receives Stage 06's committed-page list and the confirmed work order; reads
and writes the doc-registry index page and target pages' custody properties;
executes confirmed archive moves. Max data-class: `internal`. Engine:
**Rovo** — all writes are Atlassian-side.

## Demand source

Documentarian flowspace, Stage 07 (`07-custody-and-close/CONTEXT.md`) —
Layer-3 gap flagged at scaffold triage
(`flow-foundry/review-flowspaces/documentarian/decision-log/2026-07-15-scaffold-triage.md`).
The custody model's standing-custodian operating notes
(`reference/custody-model.md`) are this skill's future-mode constraints.

## Definition of done

On a seeded job close (two committed pages, one archive line confirmed, one
archive line declined): both pages get registry rows with correct review-by
dates (one shortened for a waived open section), the confirmed archive
executes via the configured mechanism with its confirmation recorded, the
declined line becomes an `archive-declined` note, nothing is deleted, the
next custody review date is recorded, and the job summary reconciles all
work-order lines with zero unaccounted entries.
