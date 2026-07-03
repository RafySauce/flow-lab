---
id: ai-refinement-stage-01
title: "Stage 01 — Intake & Guardrails"
type: stage-context
stage: 1
review-intensity: heavy
artifact-version: "1.1"
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

# Stage 01 — Intake & Guardrails

## Inputs

| Input | Source | Required |
|---|---|---|
| Trigger phrase ("Run AI Refinement", "Start Refinement", "I want to refine") | User | Yes |
| Work item type selection (Solution Epic, Feature, Story, Task, Spike) | User | Yes |
| Guardrails, persona contract, work-item schemas | `../reference/ai-refinement-hybrid.md` | Yes |

## Process

`Layer-3: inline (one-off — the guardrail, persona, and schema content below is
transcribed from ../reference/ai-refinement-hybrid.md and is specific to this
flowspace)`

1. **Trigger detection** — recognize one of the defined trigger phrases.
2. **Responsibility acknowledgment** — present the responsibility notice and obtain explicit user confirmation:
   > "You, the user, are responsible for the output of this process and committing to the work it produces."
   > Policy reference: `<internal policy link — set at instantiation; redacted from this public design copy>`
3. **Data safety reminder** — state the PII / confidential-data prohibition.
4. **Persona activation** — load the `technical_product_service_owner` persona with its four behaviors:
   - Prioritize business and operational value
   - Identify risks and dependencies
   - Challenge incomplete requirements
   - Enforce measurable outcomes
5. **Work item type selection** — ask the user which item type they are refining. Load the corresponding schema from `../reference/ai-refinement-hybrid.md`:
   - `solution_epic` → children: feature; required fields: summary, problem_statement, business_outcomes, customer_business_value, in_scope, out_of_scope, dependencies, acceptance_criteria, due_date; optional: risks
   - `feature` → children: story, task, spike; required fields: summary, customer_business_value, in_scope, out_of_scope, acceptance_criteria, type_of_work, work_category, due_date
6. **Confirm setup** — echo back: persona active, item type selected, guardrails in effect. Obtain user "proceed" before advancing.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Acknowledged responsibility flag | Stage 02 | boolean |
| Selected work item type + loaded schema | Stages 02–06 | YAML schema reference |
| Active persona contract | Stages 02–06 | persona object |

## Verify

Cross-stage trace: the schema Stage 01 hands forward is the schema Stages 02–06
consume. Check that the loaded schema's required-field list matches the selected
work-item type's entry in `../reference/ai-refinement-hybrid.md` field-for-field
— the failure this catches is a downstream stage refining against a stale or
wrong-type schema. Running this check leaves a one-line result in the run's
decision log.

- [ ] Trigger phrase was matched
- [ ] Responsibility notice was displayed and explicitly acknowledged
- [ ] Data safety prohibition was stated
- [ ] Persona contract is active (all four behaviors loaded)
- [ ] Work item type is selected and its schema matches the reference doc
- [ ] User confirmed "proceed"

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy — this is the session's trust boundary; a missed
  guardrail propagates to every downstream stage.
- **Evidence:** setup confirmation echoed in the session and a one-line entry in
  the run's decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- No PII or confidential data enters the session at this stage; if it appears,
  halt per the data-safety guardrail.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
