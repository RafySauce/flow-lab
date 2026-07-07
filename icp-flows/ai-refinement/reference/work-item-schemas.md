---
id: work-item-schemas
title: "Work Item Schemas — Refinable Set (House Extension)"
type: specification
artifact-version: "1.2"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-07
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
(`ai-refinement-hybrid.md`, `claimed`) defines only two of the (now seven)
selectable work-item types; this house-authored extension completes the set
without touching the clipping. **Authority split:** for `solution_epic` and `feature`
the clipping remains authoritative — they are transcribed here for one-stop
loading, and on any divergence the clipping wins. The `story`, `task`, and
`spike` schemas below are house extensions at `truth-level: to-review`:
operator ratification, and confirmation against the real Jira project
configuration at instantiation, are still owed (see the decision log,
`../decision-log/2026-07-03-work-item-schema-extension.md`). **1.1** adds
`type_of_work`/`work_category` to `story` and `spike` (they were already on
`feature` and `task`) per an operator-observed defect on the first on-engine
run — see `../decision-log/2026-07-03-stage06-feedback-revision.md`; this
lands in the same to-review bundle awaiting ratification, not a separate
approval. **1.2** brings `portfolio_epic` into the refinable set (top of the
hierarchy, parent of `solution_epic`) and adds `bug` as a house-authored peer
of `story`/`task`/`spike` under `feature` — both are house extensions at
`truth-level: to-review`, same as `story`/`task`/`spike` before them; see
`../decision-log/2026-07-07-portfolio-epic-and-bug-type-extension.md`. Adding
`bug` to `feature.children` is a deliberate, documented divergence from the
clipping (whose `feature.children` still reads `[story, task, spike]`,
unedited, per the clipping's own preservation rule) — on this one point the
registry does not defer to the clipping; the divergence is a new type
addition beyond the clipping's original scope, not a disagreement about the
two source-defined schemas' own fields, so the "clipping wins on divergence"
rule in the paragraph above continues to apply only to `solution_epic` and
`feature`'s field lists.

## Refinable set and out-of-scope types

The hierarchy is Portfolio Epic → Solution Epic → Feature → (Story | Task |
Spike | Bug) → Sub-Task. This pipeline refines seven of the eight:

| Type | Refinable here | Why / where instead |
|---|---|---|
| `portfolio_epic` | Yes | House extension below — brought into scope 2026-07-07 (see decision log), superseding the original 2026-07-03 out-of-scope call. |
| `solution_epic` | Yes | Source-defined schema (clipping authoritative). |
| `feature` | Yes | Source-defined schema (clipping authoritative). |
| `story` | Yes | House extension below. |
| `task` | Yes | House extension below. |
| `spike` | Yes | House extension below. |
| `bug` | Yes | House extension below — peer of `story`/`task`/`spike` under `feature`. |
| `sub_task` | No | Execution breakdown created directly in Jira under an already-committed parent; carries no independent business value to elicit, so the pipeline adds nothing. If selected at Stage 01, redirect. |

## Schemas

```yaml
work_item_types:
  # --- house extension (to-review; operator to ratify) ---
  portfolio_epic:
    children: [solution_epic]
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
    # children extended with `bug` 2026-07-07 (house divergence from the
    # clipping's `[story, task, spike]` — see the authority-split note above)
    children: [story, task, spike, bug]
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
      type_of_work: required
      work_category: required
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
      type_of_work: required
      work_category: required
      due_date: required

  bug:
    children: [sub_task]
    fields:
      summary: required
      steps_to_reproduce: required
      expected_result: required
      actual_result: required
      severity: required
      customer_business_value: required
      acceptance_criteria: required
      type_of_work: required
      work_category: required
      due_date: required
      environment: optional
```

## Extension field definitions

Fields below exist only in the `spike` and `bug` schemas; their constraints
extend the clipping's `field_definitions` block (Stage 04 refines against
them, Stage 05 validates them):

```yaml
field_definitions_extension:
  question_to_answer:
    rule: exactly one answerable question — if it needs "and", split the spike
  timebox:
    rule: states an explicit bound (a duration or an end date); the timebox
      must close on or before due_date
  steps_to_reproduce:
    rule: a numbered sequence a third party can follow without asking a
      clarifying question — no "sometimes" or "occasionally" steps
  expected_result:
    rule: states the correct behavior, independent of the failure — must read
      as true regardless of whether the bug is ever fixed
  actual_result:
    rule: states the observed failure; must contradict expected_result on at
      least one concrete point (that contradiction is the bug)
  severity:
    rule: one of blocker | critical | major | minor — sets board triage
      priority; not the same axis as work_category
```

## Derivation rules (how the extension fields were chosen)

Recorded so the operator can ratify the *reasoning*, not just the field lists:

1. **Pipeline invariants stay required everywhere.** Every refinable type
   requires `summary`, `customer_business_value`, `acceptance_criteria`, and
   `due_date` — Stage 02 drafts a value statement for every item, Stage 04
   enforces the summary limit and AC starters on every item, Stage 05 checks
   the due date on every item. A type missing any of these would make a stage
   contract conditionally meaningless.
2. **The feature schema is the template for its children.** `story`, `task`,
   and `spike` all carry `type_of_work` and `work_category` — every refinable
   type traverses the Jira board workflow after commit, and the board's
   column-transition rules key off these two fields regardless of issue type
   (see rule 5). `story` differs from `feature`/`task` only in scope framing
   (`in_scope`/`out_of_scope`), not in board-interaction fields.
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
5. **Board-interaction fields are required wherever the board demands them,
   not wherever the source schema happened to define them.** `type_of_work`
   and `work_category` are Jira board configuration requirements for moving an
   item across workflow columns — every refinable type (`story`, `task`,
   `spike`, `bug`, in addition to `feature`) traverses that workflow once
   committed, so every refinable type requires both fields. (Operator-observed
   defect, NEADD-1827: a spike committed without them could not be
   transitioned off Backlog. See
   `../decision-log/2026-07-03-stage06-feedback-revision.md`.)
6. **`portfolio_epic` mirrors `solution_epic`'s field set exactly.** Both sit
   at outcome-level framing above the delivery hierarchy's execution types —
   `solution_epic` was already the template the clipping chose for that
   framing (problem statement, measurable business outcomes, dependencies,
   optional risks), so `portfolio_epic` reuses it rather than inventing a
   parallel set. The only new thing `portfolio_epic` contributes is its
   position at the top of `children` chains, not new field shape.
7. **`bug`'s scope contract is its reproduction triad, not `in_scope`/
   `out_of_scope`.** Same pattern as rule 4's spike carve-out: a bug is
   bounded by what actually happened (`steps_to_reproduce`, `expected_result`,
   `actual_result`), not by a scope statement written before the defect was
   understood. `severity` is required because it drives board triage
   independently of `work_category`; `environment` stays optional because not
   every defect report captures it, and its absence should not block
   refinement.
