---
id: decision-2026-07-03-deployment-artifacts-prepared
title: "Decision Log — Deployment Artifacts Prepared, Not Executed (REC-01/02/09/10)"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
---

# Decision Log — 2026-07-03 — Deployment Artifacts Prepared, Not Executed

**What was decided:** for the four drift-analysis recommendations that
require actually publishing to Confluence, deploying live Rovo agents, or
running validation against a live Jira instance (REC-01 Confluence
migration, REC-02 Rovo agent deployment, REC-09 on-engine validation, REC-10
Confluence page-tree structure), author operator-facing prep artifacts
instead of attempting any execution. **By whom:** agent, on operator
instruction — the operator explicitly chose "prepare artifacts, skip
execution" when asked how to handle these four recommendations, given this
session has no Confluence, Rovo, or Jira access. **What it affects:** two new
files — `reference/confluence-instantiation-guide.md` (REC-01/02/10) and
`reference/on-engine-validation-checklist.md` (REC-09) — plus `HUB.md`'s
Known gaps section and reference-material table, updated to point to both.

## Why this boundary, not a broader or narrower one

The four recommendations share a common blocker: they all require write
access to systems outside this repository (a Confluence space, a Rovo
agent-authoring surface, a live Jira project). No amount of additional
repo-side design work removes that blocker — the operator has to act on a
live system regardless of how thoroughly the checklist is written. Given
that, the highest-value contribution available in this session is making
the operator's eventual manual work as unambiguous as possible: a page-tree
structure to create, a sequenced checklist of what to verify, and a
validation matrix scoped to this flowspace's actual five refinable types and
six stages — rather than either doing nothing (leaving the operator to
reconstruct this from the drift-analysis document and the flowspace's
existing files) or attempting to simulate deployment in a way that would
produce no verifiable evidence.

## What was deliberately not done

- No Confluence pages were created; no Rovo agent definitions were
  published; no Jira project was queried or modified.
- No claim is made anywhere in the two new artifacts that any step has been
  executed — both are explicitly marked "prepared, not executed" at the top.
- `HUB.md`'s Known gaps section was updated to describe the current state
  honestly (spec-only capabilities pending on-engine validation), not to
  imply progress toward deployment that didn't happen in this session.

## Assumption (operator to confirm or amend)

- **I1 — the two artifacts belong in `icp-flows/ai-refinement/reference/`,
  not `methodology/` or `flow-foundry/`.** Both are specific to this one
  flowspace's stage structure, skills, and refinable types, not generic
  cross-flowspace method or foundry build-method — the same reasoning that
  places `work-item-schemas.md` and the stakeholder register in this
  directory rather than one level up. Amendment path: if the operator wants
  a reusable, generic version of either artifact for future flowspaces, that
  would be a separate follow-up under `flow-foundry/templates/`, not a move
  of these instance-specific files.
