---
id: ai-refinement-stage-06
title: "Stage 06 — Jira Commit & Close"
type: stage-context
stage: 6
review-intensity: heavy
artifact-version: "1.4"
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
| Candidate parent items (queried live from the target instance) | Jira (via native lookup) | If applicable |
| Confirmed parent choice (confirm / skip / create-new) | User | If applicable |

## Process

`Layer-3: jira-commit` (skill spec in
`produced-skills/jira-commit/`, `verified`)

1. **Field mapping, registry-driven, format-translated** — translate the
   refined field key-value pairs into Jira field IDs, the field set read from
   the selected type's schema in `../reference/work-item-schemas.md`:
   - Standard fields: summary, description, due date, issue type
   - Custom fields (per the type's registry schema): problem_statement, business_outcomes, customer_business_value, in_scope, out_of_scope, type_of_work, work_category, acceptance_criteria, question_to_answer, timebox (spike — map or create at instantiation per the registry)
   - Format-translation gate: convert the payload's Markdown structure
     (headings, bullet lists, code blocks) into the target platform's native
     markup — Atlassian Document Format (ADF) for Jira Cloud — before mapping
     any rich-text field. Raw Markdown syntax landing in a Jira field is a
     defect; Stage 05's "no bold, no emojis" pass does not translate
     structural markup, so this stage owns the translation.
2. **Hierarchy linkage** — resolve parent-child relationships. Parent mapping
   is default behavior for every type this stage commits except
   `portfolio_epic` (out of pipeline scope) and `solution_epic` (top of the
   refinable set — no parent within scope):
   - Query the target instance for existing candidates of the appropriate
     parent type (features under the selected solution epic; the epic's
     existing features for a story/task/spike).
   - Present the candidates to the user (key, summary, status) and obtain
     one of: confirm a specific parent, skip (no parent yet), or request a
     new parent be created (spawns a new Band 2 run for that type; this
     commit resumes once the new parent exists).
   - If creating a feature under a solution epic: set epic link. If creating
     a story/task/spike under a feature: set parent link. Set the link only
     after the user's explicit confirmation — never from an unconfirmed
     Stage 01 hierarchy position.
   - Validate that the parent exists in Jira.
3. **Dependency linkage** — create Jira issue links for blocking dependencies identified in Stage 03.
4. **Stakeholder tagging** — apply the Stage 02 stakeholder tags and Stage 03
   coalition / conflict-axis annotations as Jira labels (or the instance's
   designated fields), so the item is taggable per the stakeholder register's
   usage rules.
5. **Dry-run preview** — present the full payload to the user in its
   translated, rendered form (native markup, not raw Markdown source) before
   committing.
6. **Commit** — execute through the engine's native Jira capabilities first
   (Rovo built-in create/update issue and issue-link actions); the sanctioned
   Jira integration is the fallback for engines without them (Copilot).
7. **Confirm success** — return the created issue key and URL to the user.
8. **Offer status transition** — ask whether to move the item to In Progress
   (or the board's equivalent active status); execute via the engine's native
   Jira capabilities on confirmation, leave the default status on decline.
9. **Session loop decision**:
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
payload field-for-field, aside from format translation (nothing of substance
altered between sign-off and commit), and every blocking dependency from
Stage 03's classified list must appear as a Jira issue link — the failures
these catch are post-sign-off content mutation and dropped dependency links.
Running these checks leaves a one-line result in the run's decision log.

- [ ] All required Jira fields are mapped (no unmapped required fields)
- [ ] Committed payload matches the Stage 05 signed-off payload (content
      unchanged; only markup was translated to the platform's native format)
- [ ] No raw Markdown syntax (heading markers, list markers, code fences)
      remains in any committed field
- [ ] For applicable types, candidate parents were presented and the user
      explicitly confirmed, skipped, or requested a new parent — never a
      silently-carried-forward hierarchy position
- [ ] Parent item exists in Jira (if hierarchy linkage applies)
- [ ] Every Stage 03 blocking dependency has a Jira issue link
- [ ] Stakeholder tags / annotations applied as labels
- [ ] Dry-run preview was shown in rendered (native-markup) form and user approved
- [ ] Jira API returned success (issue key received)
- [ ] User was offered the post-commit status transition (accept or decline
      recorded)
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
