---
id: decision-2026-07-03-work-item-schema-extension
title: "Decision Log — AI Refinement Work-Item Schema Extension"
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
  - "[[work-item-schemas]]"
---

# Decision Log — 2026-07-03 — Work-Item Schema Extension

**What was decided:** complete the flowspace's work-item type coverage by
house-authoring the three missing schemas (`story`, `task`, `spike`) and
declaring `portfolio_epic` and `sub_task` out of refinement scope. **By whom:**
agent, on operator instruction ("build the rest of the flow"); all artifacts
emitted at `to-review` — nothing promoted. **What it affects:** Stage 01's
schema-loading step (the previous dead-end), Stages 02/04/05/06's
type-conditional handling, `HUB.md`, and the new
`reference/work-item-schemas.md`.

## The gap

Stage 01 offers five selectable types (Solution Epic, Feature, Story, Task,
Spike) and the hierarchy names seven, but the source clipping defines schemas
for only `solution_epic` and `feature`. A run selecting Story, Task, or Spike
had no schema to load at Stage 01 step 5 — every downstream stage contract
reads "the Stage 01 schema," so the pipeline was unrunnable for three of its
five advertised types.

## Decisions and alternatives

1. **Extension registry beside the clipping, not inside it.** The clipping is
   `claimed` foreign material captured as-is; editing it would destroy its
   evidentiary value. New schemas live in `reference/work-item-schemas.md`
   (`type: specification`, house-authored), which transcribes the two source
   schemas for one-stop loading and declares the clipping authoritative for
   them on any divergence. *Alternative considered:* leave Stage 01 loading
   from two documents with no registry — rejected: the split-source rule would
   then live only in stage prose, invisible to validation.
2. **Refinable set = the middle five.** `portfolio_epic` (portfolio investment
   case — Portfolio & Sourcing territory, consistent with the skill family's
   "not a portfolio tool" boundary) and `sub_task` (execution breakdown under
   a committed parent; no independent value to elicit) are declared
   out-of-scope with a redirect at Stage 01. *Alternative considered:* schema
   all seven — rejected: it would extend the pipeline past what the TPSO
   persona and the source doc's own selection framing support.
3. **Field derivation is rule-based, not invented per type** — see the
   registry's "Derivation rules": pipeline invariants (summary, value, AC,
   due date) required everywhere; `story`/`task` derived from `feature`;
   `dependencies` a field only where the source made it one; spike scope
   contract = question + timebox.
4. **Skills left untouched.** All five skill specs read "the schema from
   Stage 01" generically, so extension schemas flow through — except
   `jira-commit`'s Method step 1, which enumerates custom fields and does not
   list the spike's `question_to_answer`/`timebox`. Its step already routes
   custom fields through per-instance field-ID discovery, so this is a doc
   gap, not a behavior gap. Deliberately not edited: the 2026-07-03 pre-gate
   evidence references spec version 1.1, and reopening a passed gate for two
   list items is worse than logging the follow-up. **Follow-up:** when the
   operator ratifies the spike schema, add both fields to `jira-commit`'s
   custom-field list (and adapters) as a 1.2 revision.

## Assumptions (operator to confirm or amend)

- **B1 — Spike carries no `in_scope`/`out_of_scope`.** The question + timebox
  are its scope contract; Stage 03's scope package informs them rather than
  landing in fields. Amendment path: add both fields for cross-type
  uniformity if the real Jira spike screen has them.
- **B2 — Task carries `type_of_work`/`work_category`; story does not.** Tasks
  are the execution-shaped carrier. Amendment path: mirror whatever the real
  Jira project's field screens require per issue type.
- **B3 — Two new field names are proposed** (`question_to_answer`,
  `timebox`); they must be mapped to (or created as) custom fields at
  instantiation, per `jira-commit`'s discovery step.
- **B4 — Relationship to prior assumption A4** (structure-correction log,
  "no new required fields were invented"): A4 still holds for the two
  source-defined schemas, which are untouched. The extension schemas invent
  fields *only* in the clearly-separated house registry, on explicit operator
  instruction to complete the flow.
