---
id: decision-2026-07-07-bug-field-simplification-and-portfolio-epic-confirmation
title: "Decision Log — Bug Field Simplification and Portfolio Epic Field Confirmation"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-07
updated: 2026-07-07
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[work-item-schemas]]"
  - "[[2026-07-07-portfolio-epic-and-bug-type-extension]]"
---

# Decision Log — 2026-07-07 — Bug Field Simplification and Portfolio Epic Field Confirmation

**What was decided:** simplify `bug`'s schema from four bug-specific custom
fields down to a single standard `description` field (plus `summary` and
`acceptance_criteria`), and confirm — no schema change needed — that
`portfolio_epic` already carries every field `solution_epic` carries, per the
operator's stated characterization of a portfolio epic as an enterprise-wide
strategic goal that can span organizations and years, containing solution
epics. **By whom:** agent, on direct operator feedback to the same-day
`2026-07-07-portfolio-epic-and-bug-type-extension.md` decision.
**What it affects:** `reference/work-item-schemas.md` (1.2 → 1.3), Stage 01
and Stage 06 `CONTEXT.md`, `reference/on-engine-validation-checklist.md`, and
the `jira-commit` and `field-refinement-cadence` skill specs and their
adapters.

## The feedback

> "the bug should have a summary statement (required), a description (which
> can include the items you described including environment), and clear
> acceptance criteria."
>
> "portfolio epics contain solution epics that can span organizations. they
> are strategic goals aligned to enterprise priorities that can span years.
> they should have all of the same required fields that solution epics have."

## Decisions and alternatives

1. **`bug` drops `steps_to_reproduce`, `expected_result`, `actual_result`,
   `severity`, and `environment` as separate schema fields; adds
   `description` (a standard Jira field, not a custom one).** The 1.2 draft
   reasoned by analogy to `spike`'s two custom fields
   (`question_to_answer`/`timebox`) and gave `bug` four required fields plus
   one optional — defensible in isolation, but the operator's explicit
   instruction is narrower: three fields, one of them a catch-all. Taking the
   instruction literally, `description` is the natural home for the
   catch-all content, since it is already a standard Jira field every issue
   type has, and the registry already treats standard fields (`summary`,
   `description`, `due_date`, `issuetype`) as directly mapped without
   per-instance custom-field discovery (`jira-commit` Method step 1). This
   also *simplifies* `jira-commit`'s field-mapping and `field-refinement-
   cadence`'s conflict-detection logic, since there's no longer a
   custom-field discovery step or a cross-field comparison unique to `bug` —
   only a within-field content check on `description`. *Alternative
   considered:* keep `severity` as a separate required field even after
   folding the rest into `description`, since severity is often a real,
   board-filterable Jira field in practice, distinct from free-text content —
   rejected in favor of following the operator's instruction literally
   (three fields); flagged as an assumption below for the operator to
   override if board-level severity filtering turns out to matter in
   practice.
2. **The `description` field keeps a content constraint, not a blank check.**
   Even though `steps_to_reproduce`/`expected_result`/`actual_result` are no
   longer separate fields, the requirement that a bug report actually
   contain reproduction steps and a stated contradiction between expected and
   actual behavior didn't disappear — dropping it entirely would let a vague
   one-line "description" pass Stage 05 validation. The registry's Extension
   field definitions section keeps a `description` rule (scoped explicitly
   to `bug`, since no other current type schemas that field) requiring the
   same content, now as parts of one field's prose instead of four fields'
   values. `field-refinement-cadence`'s Method step 3 conflict check was
   rewritten from a cross-field comparison to a within-field one accordingly.
3. **`portfolio_epic` needed no schema change** — 1.2 already gave it
   `solution_epic`'s exact field set (see that decision log's rule 6 /
   derivation rule 6). What the operator's message adds is *characterization*
   the schema didn't previously state explicitly: portfolio epics can span
   organizations and operate on a multi-year horizon, as distinct from a
   solution epic's narrower scope. This is documentation enrichment, not a
   field-list change: the registry's schema table, YAML comment, and
   derivation rule 6 were expanded to state this explicitly (so a future
   reader doesn't have to infer it from field-list similarity alone), and
   Stage 01's type-selection rationale prompt was updated so the
   agent-proposed rationale can distinguish "reads as a portfolio-level,
   cross-org, multi-year goal" from "reads as a solution epic's narrower
   outcome-level framing" when both are plausible from source material.

## Assumptions (operator to confirm or amend)

- **D1 — `severity` is not a separately tracked field.** If the target Jira
  project's board relies on a structured severity field for triage/filtering
  (rather than reading it out of free-text description), the amendment path
  is to re-add `severity` as its own required field while keeping
  `steps_to_reproduce`/`expected_result`/`actual_result`/`environment`
  folded into `description` — a partial reversal, not a full one, since the
  operator's instruction was explicit about summary + description +
  acceptance criteria being the shape, and severity is arguably a
  triage/classification field in the same family as `type_of_work`/
  `work_category` rather than narrative content.
- **D2 — `description`'s content rule is guidance Stage 04/05 apply, not a
  machine-parseable structured format.** Unlike `steps_to_reproduce` as its
  own field (which Stage 05 could check was non-empty), `description`'s
  completeness now depends on the field actually containing three
  identifiable parts (steps, expected, actual) within prose — a subtler
  check than "field is non-empty." This is the tradeoff of the
  simplification the operator asked for; flagged so it doesn't get missed as
  a silent quality regression during Stage 05 validation.
- **D3 — Portfolio epic's `dependencies` field takes on more weight at
  cross-org scale** (assumption C1 from the prior decision log already
  covers `dependencies` as a field-level question; this note is about
  content, not schema). A portfolio epic spanning organizations likely
  surfaces dependencies Stage 03's stakeholder-register sweep doesn't
  reach (the register is currently scoped to a single domain/organization
  instance). No schema or process change made here — flagged for the
  operator to consider whether Stage 03's grounding needs a cross-org
  extension when `portfolio_epic` is selected, separate from this decision.
