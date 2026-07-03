---
id: ai-refinement-stage-01
title: "Stage 01 — Intake & Guardrails"
type: stage-context
stage: 1
review-intensity: heavy
status: to-review
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
source: human+ai
data-class: internal
owner: rafael.torres
related:
  - "[[ai-refinement]]"
  - "[[AI-Refinement-Hybrid]]"
---

# Stage 01 — Intake & Guardrails

## Inputs

| Input | Source | Required |
|---|---|---|
| Trigger phrase ("Run AI Refinement", "Start Refinement", "I want to refine") | User | Yes |
| Work item type selection (Solution Epic, Feature, Story, Task, Spike) | User | Yes |

## Process

1. **Trigger detection** — recognize one of the defined trigger phrases.
2. **Responsibility acknowledgment** — present the responsibility notice and obtain explicit user confirmation:
   > "You, the user, are responsible for the output of this process and committing to the work it produces."
   > [Policy reference](https://mtbtools.atlassian.net/wiki/x/S4BNTgE)
3. **Data safety reminder** — state the PII / confidential-data prohibition.
4. **Persona activation** — load the `technical_product_service_owner` persona with its four behaviors:
   - Prioritize business and operational value
   - Identify risks and dependencies
   - Challenge incomplete requirements
   - Enforce measurable outcomes
5. **Work item type selection** — ask the user which item type they are refining. Load the corresponding schema from the source doc:
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

- [ ] Trigger phrase was matched
- [ ] Responsibility notice was displayed and explicitly acknowledged
- [ ] Data safety prohibition was stated
- [ ] Persona contract is active (all four behaviors loaded)
- [ ] Work item type is selected and schema is loaded
- [ ] User confirmed "proceed"

## Review

**Intensity: Heavy** — this is the session's trust boundary. A missed guardrail propagates to every downstream stage.

Review owner: Human (Rafael or delegate)

## Data Boundary

- No PII or confidential data enters the session at this stage.
- Persona contract and schemas are `internal` classification — safe for AI processing.
- The responsibility-notice link is an internal Confluence URL — do not expose externally.
