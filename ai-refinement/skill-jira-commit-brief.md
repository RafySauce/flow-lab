---
id: skill-jira-commit-brief
title: "Skill Primer Brief — Jira Commit"
type: skill-primer-brief
status: to-review
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
source: human+ai
data-class: internal
owner: rafael.torres
demanded-by: ai-refinement-stage-06
target-adapters: [rovo, copilot]
---

# Skill Primer Brief — Jira Commit

## What This Skill Does

Maps validated work item field values to Jira API payloads, resolves hierarchy and
dependency linkages, executes the commit, and manages the session loop/close decision.

## Why It's Needed

The source doc specifies `jira_ready: true` and defines the work item hierarchy but
provides no:
- Field-to-Jira-API-field-ID mapping (especially for custom fields like problem_statement,
  business_outcomes, type_of_work, work_category)
- Hierarchy linkage resolution protocol (how to find/validate the parent epic or feature)
- Session lifecycle management (loop back to Stage 02 or close)

## Consuming Flowspace Stage

- `ai-refinement` → Stage 06 (Jira Commit & Close)

## Core Capabilities Required

1. **Field-to-API mapping** — translate refined field names to Jira REST API field IDs:
   - Standard: `summary`, `description`, `duedate`, `issuetype`
   - Custom: `problem_statement`, `business_outcomes`, `customer_business_value`,
     `in_scope`, `out_of_scope`, `type_of_work`, `work_category`, `acceptance_criteria`
   - Must support discovery of custom field IDs per Jira instance
2. **Hierarchy linkage resolution**:
   - Given a parent reference (key or summary), validate it exists in Jira
   - Set the appropriate link type (epic link, parent link) based on hierarchy level
3. **Dependency linkage** — create Jira issue links (blocks/is-blocked-by) for
   dependencies classified as blocking in Stage 03
4. **Dry-run preview** — present the full payload in human-readable format before commit
5. **Commit execution** — call Jira create or update API
6. **Session loop management**:
   - "Refine another" → retain session context (guardrails, persona), return to Stage 02
   - "Done" → produce session summary with all created issue keys/URLs

## Acceptance Criteria

- Must be able to resolve custom field IDs for the target Jira instance dynamically.
- Must be able to validate parent item existence before committing a child.
- We will know this is done when a work item can be committed to Jira with all fields
  correctly populated, hierarchy linked, and dependencies set — in a single pass
  without manual Jira field editing afterward.

## Constraints

- Must present a dry-run preview — never commit without user approval.
- Must handle API errors gracefully (field not found, parent not found, permission denied).
- Must not store or log API credentials.
- Must not introduce PII or confidential data.
- Must work on both Rovo and Copilot surfaces.
