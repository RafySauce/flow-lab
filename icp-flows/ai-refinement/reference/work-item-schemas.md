---
id: work-item-schemas
title: "Work Item Schemas — Refinable Set (House Extension)"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.1"
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
---

# Work Item Schemas — Refinable Set

The single schema registry Stage 01 loads from. The source clipping
(`ai-refinement-hybrid.md`, `claimed`) defines only two of the five selectable
work-item types; this house-authored extension completes the set without
touching the clipping. **Authority split:** for `solution_epic` and `feature`
the clipping remains authoritative — they are transcribed here for one-stop
loading, and on any divergence the clipping wins. The `story`, `task`, and
`spike` schemas below are house extensions at `truth-level: to-review`:
operator ratification, and confirmation against the real Jira project
configuration at instantiation, are still owed (see the decision log,
`../decision-log/2026-07-03-work-item-schema-extension.md`).

## Refinable set and out-of-scope types

The hierarchy is Portfolio Epic → Solution Epic → Feature → (Story | Task |
Spike) → Sub-Task. This pipeline refines the middle five:

| Type | Refinable here | Why / where instead |
|---|---|---|
| `portfolio_epic` | No | Portfolio-level investment case, owned by Portfolio & Sourcing processes (register entry 17). The TPSO persona refines delivery work items, not portfolio cases. If selected at Stage 01, redirect. |
| `solution_epic` | Yes | Source-defined schema (clipping authoritative). |
| `feature` | Yes | Source-defined schema (clipping authoritative). |
| `story` | Yes | House extension below. |
| `task` | Yes | House extension below. |
| `spike` | Yes | House extension below. |
| `sub_task` | No | Execution breakdown created directly in Jira under an already-committed parent; carries no independent business value to elicit, so the pipeline adds nothing. If selected at Stage 01, redirect. |

## Schemas

```yaml
work_item_types:
  # --- transcribed from ai-refinement-hybrid.md (clipping authoritative) ---
  solution_epic:
    children: [feature]
    fields:
      summary: required
      problem_statement: required
      business_outcomes: required
      customer_business_value: required
      in_scope: required
      out_of_scope: required
      dependencies: required
      acceptance_criteria: required
      risks: optional
      due_date: required

  feature:
    children: [story, task, spike]
    fields:
      summary: required
      customer_business_value: required
      in_scope: required
      out_of_scope: required
      acceptance_criteria: required
      type_of_work: required
      work_category: required
      due_date: required

  # --- house extensions (to-review; operator to ratify) ---
  story:
    children: [sub_task]
    fields:
      summary: required
      customer_business_value: required
      in_scope: required
      out_of_scope: required
      acceptance_criteria: required
      due_date: required

  task:
    children: [sub_task]
    fields:
      summary: required
      customer_business_value: required
      in_scope: required
      out_of_scope: required
      acceptance_criteria: required
      type_of_work: required
      work_category: required
      due_date: required

  spike:
    children: [sub_task]
    fields:
      summary: required
      question_to_answer: required
      timebox: required
      customer_business_value: required
      acceptance_criteria: required
      due_date: required
```

## Extension field definitions

Two fields exist only in the `spike` schema; their constraints extend the
clipping's `field_definitions` block (Stage 04 refines against them, Stage 05
validates them):

```yaml
field_definitions_extension:
  question_to_answer:
    rule: exactly one answerable question — if it needs "and", split the spike
  timebox:
    rule: states an explicit bound (a duration or an end date); the timebox
      must close on or before due_date
```

## Derivation rules (how the extension fields were chosen)

Recorded so the operator can ratify the *reasoning*, not just the field lists:

1. **Pipeline invariants stay required everywhere.** Every refinable type
   requires `summary`, `customer_business_value`, `acceptance_criteria`, and
   `due_date` — Stage 02 drafts a value statement for every item, Stage 04
   enforces the summary limit and AC starters on every item, Stage 05 checks
   the due date on every item. A type missing any of these would make a stage
   contract conditionally meaningless.
2. **The feature schema is the template for its children.** `story` is
   `feature` minus the execution-classification fields; `task` keeps
   `type_of_work` and `work_category` because tasks are the pipeline's
   execution-shaped carrier (Stage 04's consistency check covers both).
3. **`dependencies` is a schema field only where the source made it one**
   (`solution_epic`). For all other types, Stage 03 still classifies
   dependencies and Stage 06 still creates the Jira issue links — the source's
   own `feature` schema establishes that dependency *links* don't require a
   dependency *text field*.
4. **A spike's scope contract is its question and timebox.** The spike schema
   deliberately carries no `in_scope`/`out_of_scope` fields: Stage 03's scope
   package still runs and bounds the investigation, but its output informs
   `question_to_answer` and `acceptance_criteria` (exit criteria) rather than
   landing in separate fields. Alternative (add both scope fields for
   uniformity) is logged for the operator.
