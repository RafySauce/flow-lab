---
id: ai-refinement-stage-06
title: "Stage 06 — Jira Commit & Close"
type: stage-context
stage: 6
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
  - "[[skill-jira-commit]]"
skill-dependency: skill-jira-commit
skill-status: gap
---

# Stage 06 — Jira Commit & Close

## Inputs

| Input | Source | Required |
|---|---|---|
| Validated + formatted work item payload | Stage 05 | Yes |
| User sign-off confirmation | Stage 05 | Yes |
| Work item type + hierarchy position | Stage 01 | Yes |
| Parent item reference (if creating a child) | User | If applicable |

## Process

> **⚠ SKILL GAP** — `skill-jira-commit` does not yet exist.
> See `skill-demand/skill-jira-commit-brief.md`.

When the skill is built, this stage will:

1. **Field-to-API mapping** — translate the refined field key-value pairs into Jira API field IDs:
   - Standard fields: summary, description, due date, issue type
   - Custom fields: problem_statement, business_outcomes, customer_business_value, in_scope, out_of_scope, type_of_work, work_category, acceptance_criteria
2. **Hierarchy linkage** — resolve parent-child relationships:
   - If creating a feature under a solution epic: set epic link
   - If creating a story/task/spike under a feature: set parent link
   - Validate that the parent exists in Jira
3. **Dependency linkage** — create Jira issue links for blocking dependencies identified in Stage 03.
4. **Dry-run preview** — present the full API payload to the user in a readable format before committing.
5. **Commit** — execute the Jira create/update API call.
6. **Confirm success** — return the created issue key and URL to the user.
7. **Session loop decision**:
   - "Refine another" → loop back to Stage 02 with session context retained
   - "Done" → close session, produce session summary

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Created Jira issue key + URL | User | Link |
| API response confirmation | Decision log | JSON |
| Session summary (if closing) | User / audit | Structured summary |

## Verify

- [ ] All required Jira fields are mapped (no unmapped required fields)
- [ ] Parent item exists in Jira (if hierarchy linkage applies)
- [ ] Dependency links target valid Jira issues
- [ ] Dry-run preview was shown and user approved
- [ ] Jira API returned success (issue key received)
- [ ] User was offered loop/close decision

## Review

**Intensity: Heavy** — this is the commit boundary. An incorrect API payload creates real Jira artifacts that require manual cleanup.

Review owner: Human (Rafael or delegate)

## Data Boundary

- Jira API payloads contain `internal` data — transmitted over authenticated, encrypted channels only.
- Issue keys and URLs are `internal` — shareable within the organization.
- API credentials are handled by the platform (Rovo/Copilot) — never included in flowspace artifacts.
