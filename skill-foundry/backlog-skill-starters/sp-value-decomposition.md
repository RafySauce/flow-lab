---
id: sp-value-decomposition
title: "Skill Primer Brief — Value Decomposition"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.1"
data-class: public
related: ["[[ai-refinement]]"]
---

# Skill Primer Brief — Value Decomposition

> Intake path 1 for the skill-foundry: crystallized intent, written before authoring starts. Filed as `sp-value-decomposition.md`.

## Purpose

Given a parent-level work item (`portfolio_epic`, `solution_epic`, or
`feature`) already selected or committed in the `ai-refinement` flowspace,
propose candidate children one hierarchy level down — grounded in the
operator-provided "Value Delivery — Key Concepts, a 30,000ft View" deck's
model (Stakeholder Persona Value Statements, MVP thinking, the Hamburger
Method's vertical-vs-horizontal slicing, and quarter-testable acceptance
criteria) — for user review, before handing each accepted child into its own
Band 2 refinement run. Replaces the manual, ad-hoc practice of decomposing an
epic into features (or a feature into stories) by memory or spreadsheet.

## Triggering intent

- **Fires on:** at Stage 01 of `ai-refinement`, when the user selects a
  parent-level type (`portfolio_epic`, `solution_epic`, `feature`) and states
  a desire to do a full decomposition of it into its children — "help me
  break this solution epic into features," "decompose this feature into
  stories."
- **Does not fire on (near-misses):** ordinary single-item refinement (the
  default Band 2 loop, bottom-up parent-linking via Stage 06's
  `parent_mapping_confirmation` — unaffected by this skill and still the only
  path when the user isn't asking for a decomposition); refining one
  already-known child directly (a normal run with a parent link, not a
  decomposition); `story`/`task`/`spike`/`bug` as the *parent* of a
  decomposition pass — the deck's lifecycle table stops applying at Feature,
  so decomposing below Feature isn't this skill's model without a follow-up
  revision and a fresh look at whether the deck's concepts still apply that
  far down.

## Method sketch

1. Confirm the parent item and its content (problem statement,
   business/customer value, in/out of scope) as the decomposition's
   grounding context.
2. **One level per pass, user-driven.** Propose candidate children for the
   immediate next level down only (`portfolio_epic` → solution epics;
   `solution_epic` → features; `feature` → stories) — never cascade multiple
   levels unprompted. Discuss the proposed set with the user; the user may
   also say they aren't ready to decompose this level yet and stop with
   nothing created.
3. **Vertical-slice check.** Frame every proposed child as an end-to-end unit
   of stakeholder value (the deck's Hamburger Method), not a technical-layer
   split (UI/backend/database) — explicitly reject and re-propose a
   horizontally-sliced draft rather than passing it through.
4. **MVP-bounded set.** Apply MVP thinking to bound the proposal: the
   smallest set of children that deliver meaningful, incremental value, not
   maximal upfront decomposition.
5. **Persona Value Statement per child**, in the deck's literal format ("As
   a [persona], I value [outcome] because it helps me [goal/pain point]") —
   except:
   - `bug` and `task` are already accepted as technically worded; no format
     expectation applies to them.
   - The user may explicitly elect a technical/project-driven framing
     instead — for sequencing-heavy or infrastructure work (software/OS
     upgrades, hardware design breakdowns) where the persona-statement format
     doesn't fit the work's nature — recorded as an explicit, named
     exception per item, never silently substituted.
6. For `feature`-level children, surface the deck's quarter-testable
   expectation (acceptance criteria achievable/testable within a quarter) as
   guidance during user review — see "Open item," below, on whether this
   becomes a hard validation rule later.
7. Present the full candidate set together for user review: accept all, edit
   some, reject some, or stop ("not ready to decompose this level yet") with
   no children created.
8. Each accepted child becomes its own Band 2 run (Stage 02 onward),
   pre-seeded with the parent's context and the drafted value statement (or
   the technical-framing exception, if elected). This skill never sets a
   parent link itself — the normal per-item run still goes through Stage
   06's `parent_mapping_confirmation` for that.

**Known failure modes to guard:** proposing a horizontal slice and not
catching it (the vertical-slice check must genuinely reject, not
rubber-stamp); cascading levels without being asked; forcing the
persona-value-statement format onto genuinely technical/sequencing-driven
work without offering the technical-framing exception; treating acceptance
criteria as optional or soft for a proposed child — it stays a hard gate,
identical to every other item, and decomposition never relaxes it.

## Inputs and data boundary

Reads: the parent item's confirmed Stage 02–04 field values (or its
already-committed Jira content, if decomposing a live item); the
"Value Delivery — Key Concepts, a 30,000ft View" deck's key concepts
(persona value statements, MVP thinking, Hamburger Method vertical/horizontal
slicing, quarter-testable acceptance criteria) as grounding reference
material. Max data-class: internal, matching the rest of the `ai-refinement`
pipeline. Engines: Rovo, Copilot — the same sanctioned set as the rest of
`ai-refinement`; no engine-specific constraint identified yet.

## Demand source

`icp-flows/ai-refinement`'s stated model (`HUB.md`: "one run = one fully
refined work item," hierarchy realized only bottom-up at Stage 06) has no
top-down decomposition capability — confirmed by reading the whole flow,
2026-07-15. Grounded in the operator-provided value-delivery deck, whose
Portfolio Epic/Solution Epic/Feature lifecycle table maps directly onto this
gap. See
`icp-flows/ai-refinement/decision-log/2026-07-15-provenance-and-planning-labels.md`
§"Workstream B — value-delivery decomposition (handoff, not built)" for the
full clarifying-question answer set this brief is built from.

## Definition of done

The operator can judge a built skill acceptable when:

1. A scripted two-level test proves one-level-per-pass is real: requesting a
   Solution Epic decomposition proposes features only — it does not also
   auto-propose stories under those features.
2. A seeded horizontal-slice draft (e.g., "database layer," "API layer," "UI
   layer" as proposed children) is caught and rejected, not passed through.
3. Both the persona-value-statement format and the technical-framing
   exception are exercisable in a live test; the exception is always
   explicit and named, never a silent default, and never available to
   `feature` without the user electing it.
4. Acceptance criteria remains a hard, ungated-by-nothing requirement for
   every proposed child — no test shows it relaxed or skipped because the
   item came from a decomposition pass rather than direct refinement.
5. The user's "not ready to decompose this level yet" response is honored —
   a live test shows the skill stopping cleanly with no children created.

**Open item for the operator (carried from the intake discussion, not
resolved by this brief):** whether/how the persona-value-statement format and
the vertical-slice check eventually become `workitem-validation`/Stage 05
validation rules (enforced at the gate) rather than this skill's own
generation-time heuristics (advisory only). The intake discussion leaned
toward "validate for the types that require it" — `portfolio_epic`,
`solution_epic`, `feature`, `story`, `spike` — noting that for `story` and
`spike` the value content may need to be checked against a different field
than `customer_business_value` in practice. That promotion is deliberately
deferred to the skill-foundry build that develops this brief into a full
spec, not decided here.
