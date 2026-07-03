---
id: ai-refinement-stage-06
title: "Stage 06 — Jira Commit & Close"
type: stage-context
stage: 6
review-intensity: heavy
artifact-version: "1.2"
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
  - "[[jira-commit]]"
---

# Stage 06 — Jira Commit & Close

## Inputs

| Input | Source | Required |
|---|---|---|
| Validated + formatted work item payload | Stage 05 | Yes |
| User sign-off confirmation | Stage 05 | Yes |
| Work item type + hierarchy position | Stage 01 | Yes |
| Classified dependency list | Stage 03 | Yes |
| Stakeholder tags + coalition / conflict-axis annotations | Stages 02, 03 | Yes |
| Parent item reference (if creating a child) | User | If applicable |

## Process

`Layer-3: jira-commit` (skill spec in
`skill-foundry/backlog-skill-starters/jira-commit/`, `to-review`)

1. **Field-to-API mapping** — translate the refined field key-value pairs into Jira API field IDs:
   - Standard fields: summary, description, due date, issue type
   - Custom fields: problem_statement, business_outcomes, customer_business_value, in_scope, out_of_scope, type_of_work, work_category, acceptance_criteria, question_to_answer, timebox (spike — map or create at instantiation per the registry)
2. **Hierarchy linkage** — resolve parent-child relationships:
   - If creating a feature under a solution epic: set epic link
   - If creating a story/task/spike under a feature: set parent link
   - Validate that the parent exists in Jira
3. **Dependency linkage** — create Jira issue links for blocking dependencies identified in Stage 03.
4. **Stakeholder tagging** — apply the Stage 02 stakeholder tags and Stage 03
   coalition / conflict-axis annotations as Jira labels (or the instance's
   designated fields), so the item is taggable per the stakeholder register's
   usage rules.
5. **Dry-run preview** — present the full API payload to the user in a readable format before committing.
6. **Commit** — execute the Jira create/update API call.
7. **Confirm success** — return the created issue key and URL to the user.
8. **Session loop decision**:
   - "Refine another" → loop back to Stage 02 with session context retained
   - "Done" → close session, produce session summary

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Created Jira issue key + URL | User | Link |
| API response confirmation | Run decision log | JSON |
| Session summary (if closing) | User / audit | Structured summary |

## Verify

Cross-stage trace: the committed payload must match Stage 05's signed-off
payload field-for-field (nothing altered between sign-off and commit), and
every blocking dependency from Stage 03's classified list must appear as a Jira
issue link — the failures these catch are post-sign-off mutation and dropped
dependency links. Running these checks leaves a one-line result in the run's
decision log.

- [ ] All required Jira fields are mapped (no unmapped required fields)
- [ ] Committed payload matches the Stage 05 signed-off payload
- [ ] Parent item exists in Jira (if hierarchy linkage applies)
- [ ] Every Stage 03 blocking dependency has a Jira issue link
- [ ] Stakeholder tags / annotations applied as labels
- [ ] Dry-run preview was shown and user approved
- [ ] Jira API returned success (issue key received)
- [ ] User was offered loop/close decision

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy — this is the commit boundary. An incorrect API payload
  creates real Jira artifacts that require manual cleanup.
- **Evidence:** the approved dry-run preview, the API response captured in the
  run's decision log, and the returned issue key.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- Jira API payloads contain `internal` data — transmitted over authenticated, encrypted channels only.
- Issue keys and URLs are `internal` — shareable within the organization.
- API credentials are handled by the platform (Rovo/Copilot) — never included in flowspace artifacts.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
