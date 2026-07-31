---
id: work-item-schemas
title: "Work Item Schemas — Refinable Set (House Extension)"
type: specification
artifact-version: "1.6"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-31
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
`feature`'s field lists. **1.3** (operator feedback) simplifies `bug` from
four bug-specific custom fields down to a single standard `description`
field (steps to reproduce, expected result, actual result, severity, and
environment now fold into that one field's content instead of living as
separate custom fields) and confirms `portfolio_epic`'s field set is
unchanged — the operator affirmed it should carry every field `solution_epic`
carries, which 1.2 already implemented; see
`../decision-log/2026-07-07-bug-field-simplification-and-portfolio-epic-confirmation.md`.
**1.4** adds a cross-cutting note (see "Mandatory labels," below) that every
committed item carries the two labels defined by the `mandatory_labels` house
amendment in `ai-refinement-hybrid.md` — no `fields:` changes for any type,
since labels aren't schema fields; see
`../decision-log/2026-07-15-provenance-and-planning-labels.md`. **1.5**
updates that note: the provenance label is now `refine-ai-flow-v<version>`
(this flowspace's own `artifact-version`), replacing the static
`refine-ai-built`, and states the label's purpose (pending-review flag,
removed by the team once review is complete); see
`../decision-log/2026-07-28-provenance-label-versioning.md`. **1.6** adds a
second cross-cutting note (see "Bulk creation mode," below) recording that
bulk creation mode changes cadence only — every schema here applies per item
unchanged, and a row whose context cannot support a required field is reported
underspecified rather than padded to satisfy it; no `fields:` changes for any
type; see `../decision-log/2026-07-31-bulk-creation-mode.md`.

## Refinable set and out-of-scope types

The hierarchy is Portfolio Epic → Solution Epic → Feature → (Story | Task |
Spike | Bug) → Sub-Task. This pipeline refines seven of the eight:

| Type | Refinable here | Why / where instead |
|---|---|---|
| `portfolio_epic` | Yes | House extension below — an enterprise-wide strategic goal aligned to enterprise priorities, containing (and spanning) `solution_epic`s that can cross organizational boundaries, on a horizon of years rather than a single delivery cycle. Brought into scope 2026-07-07 (see decision log), superseding the original 2026-07-03 out-of-scope call. |
| `solution_epic` | Yes | Source-defined schema (clipping authoritative). |
| `feature` | Yes | Source-defined schema (clipping authoritative). |
| `story` | Yes | House extension below. |
| `task` | Yes | House extension below. |
| `spike` | Yes | House extension below. |
| `bug` | Yes | House extension below — peer of `story`/`task`/`spike` under `feature`; reported defect captured as summary + description + acceptance criteria, same shape discipline as every other type. |
| `sub_task` | No | Execution breakdown created directly in Jira under an already-committed parent; carries no independent business value to elicit, so the pipeline adds nothing. If selected at Stage 01, redirect. |

## Mandatory labels (cross-cutting; house extension, 2026-07-15; revised 2026-07-28)

Every item this pipeline commits carries the two labels defined by the
`mandatory_labels` house amendment in `ai-refinement-hybrid.md`:
`refine-ai-flow-v<version>` (this flowspace's own `artifact-version`, e.g.
`refine-ai-flow-v1.18` — all seven refinable types, every mode; replaces the
earlier static `refine-ai-built`, not added alongside it) and, for `feature`,
`story`, `task`, `spike`, `bug` only, a `<team_code>-<yyyy>-q<n>` planning
label (`portfolio_epic`/`solution_epic` sit at a multi-year/multi-quarter
outcome horizon and are exempt from the second label's gate). The provenance
label's purpose: it flags an item as AI-produced and pending team review; the
team removes it once their review of the item is complete. These are Jira
labels, not schema fields, so no `fields:` entry changes below — Stage 01
states the provenance label (no query needed, unlike team_code) and resolves
the planning label's two components, Stage 05 runs a distinct mandatory-label
check (a warn-and-bypass gate, not a hard halt), and Stage 06 applies them at
commit. See `../decision-log/2026-07-28-provenance-label-versioning.md` (and
`../decision-log/2026-07-15-provenance-and-planning-labels.md` for the
labels' original introduction).

## Bulk creation mode (cross-cutting; house extension, 2026-07-31)

Nothing in this registry changes for bulk creation mode
(`bulk_creation_acknowledgment` in `ai-refinement-hybrid.md`), and that is the
point worth stating rather than leaving to inference: **bulk compresses
cadence, not standards.** Every schema below applies per item exactly as it
does in a single-item run — the same required-field set for the type, the same
extension field constraints, the same mandatory labels, the same formatting
rules. Acceptance criteria in particular stays a hard gate for every item in a
batch; nothing about an item arriving in a set of forty relaxes it.

What differs is only how the fields get filled and confirmed: drafted from the
provided context and confirmed per item at one batch review, rather than
elicited and confirmed per field. Where a row's context does not support a
required field, the item is reported **underspecified with that field named**
and falls out of the batch — it is never padded to satisfy the schema, because
a fabricated field passes this registry's checks exactly as well as a real one.
A mixed-type set is permitted (a feature's children may legitimately include
stories, tasks, and a spike); each row loads its own type's schema from below.
See `../decision-log/2026-07-31-bulk-creation-mode.md`.

## Schemas

```yaml
work_item_types:
  # --- house extension (to-review; operator to ratify) ---
  # Enterprise-wide strategic goal aligned to enterprise priorities; contains
  # (and can span) solution epics across organizational boundaries, on a
  # multi-year horizon. Carries the same required fields as solution_epic —
  # operator-confirmed 2026-07-07, see decision log.
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
      description: required # standard Jira field — steps to reproduce,
        # expected result, actual result, severity, and environment (where
        # known) are content within this one field, not separate fields
      customer_business_value: required
      acceptance_criteria: required
      type_of_work: required
      work_category: required
      due_date: required
```

## Extension field definitions

The `question_to_answer`/`timebox` pair exists only in the `spike` schema;
their constraints extend the clipping's `field_definitions` block (Stage 04
refines against them, Stage 05 validates them). `bug`'s `description` is a
standard Jira field, not a custom one, but carries its own content
constraint below for the same reason — Stage 04 drafts against it and Stage
05 checks it — even though the field itself isn't a registry-specific custom
field:

```yaml
field_definitions_extension:
  question_to_answer:
    rule: exactly one answerable question — if it needs "and", split the spike
  timebox:
    rule: states an explicit bound (a duration or an end date); the timebox
      must close on or before due_date
  description: # bug-specific content rule — no other current type schemas
    # this field, so this rule applies only when the selected type is `bug`
    rule: must state, as identifiable parts of the text, numbered steps to
      reproduce (no "sometimes" or "occasionally" steps), the expected
      result, and the actual result — the two results must contradict each
      other on at least one concrete point, since that contradiction is the
      bug; should also state severity (blocker | critical | major | minor)
      and environment where known, folded into the same field rather than
      tracked separately
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
6. **`portfolio_epic` mirrors `solution_epic`'s field set exactly — operator-
   confirmed, not just house-derived.** Both sit at outcome-level framing
   above the delivery hierarchy's execution types — `solution_epic` was
   already the template the clipping chose for that framing (problem
   statement, measurable business outcomes, dependencies, optional risks), so
   `portfolio_epic` reuses it rather than inventing a parallel set. This holds
   even though a portfolio epic operates at a larger scale than a solution
   epic — it can span multiple organizations and a multi-year horizon, versus
   a solution epic's narrower, typically single-organization scope — because
   the *field discipline* (a stated problem, measurable outcomes, a value
   statement, explicit dependencies, an exit condition) doesn't change with
   scale; only the content behind each field gets larger. `due_date` on a
   multi-year item reads as a target/horizon date, not a sprint-scale
   commitment, but the field stays required — the `due_date_elicitation` house
   amendment's discipline (elicited from the user, never inferred) applies
   regardless of how far out that date is. The only new thing `portfolio_epic`
   contributes structurally is its position at the top of `children` chains,
   not new field shape.
7. **`bug` carries the same three-field shape as every other type —
   summary, one content field, acceptance criteria — not a bespoke set of
   defect-specific custom fields.** The original 1.2 draft gave `bug` four
   dedicated custom fields (`steps_to_reproduce`, `expected_result`,
   `actual_result`, `severity`) plus optional `environment`, reasoning by
   analogy to `spike`'s `question_to_answer`/`timebox` custom fields (rule 4).
   Operator feedback (2026-07-07) simplified this: `bug` uses the standard
   Jira `description` field to hold the reproduction detail, expected/actual
   result, severity, and environment as prose, rather than tracking each as
   its own custom field — trading structured, individually-mappable fields
   for a smaller, more consistent schema shape (summary + description +
   acceptance criteria, same skeleton `story`/`task` already use via
   `in_scope`/`out_of_scope` in place of `description`). The content
   constraint that used to live on four separate fields now lives on
   `description` alone (see Extension field definitions, above) so Stage 04/05
   still check for it — the requirement to state reproduction steps and a
   result contradiction didn't go away, only the field boundary around it did.
