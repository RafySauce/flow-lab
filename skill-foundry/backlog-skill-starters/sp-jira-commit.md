---
id: sp-jira-commit
title: "Skill Primer Brief — Jira Commit"
type: skill-primer-brief
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
related: ["[[ai-refinement]]"]
---

# Skill Primer Brief — Jira Commit

## Purpose

Map a validated work item to a Jira API payload, resolve hierarchy and
dependency linkages, apply stakeholder tags as labels, execute the commit after
a dry-run preview, and manage the session loop/close decision. Replaces manual
Jira data entry from a refined draft — the step where transcription errors
undo the whole pipeline.

## Triggering intent

- **Fires on:** Stage 06 of the `ai-refinement` flowspace; "commit this item to
  Jira" — only with a signed-off Stage 05 payload in hand.
- **Does not fire on (near-misses):** validating the payload (that's
  `workitem-validation` — this skill assumes a signed-off input), bulk Jira
  imports or migrations, and editing existing issues outside a refinement run.

## Method sketch

1. Field-to-API mapping — standard fields (`summary`, `description`, `duedate`,
   `issuetype`) plus custom fields (problem_statement, business_outcomes,
   customer_business_value, in_scope, out_of_scope, type_of_work, work_category,
   acceptance_criteria), with per-instance custom-field-ID discovery.
2. Hierarchy linkage — validate the parent exists; epic link for a feature under
   a solution epic, parent link for story/task/spike under a feature.
3. Dependency linkage — blocks / is-blocked-by links for Stage 03's blocking
   dependencies.
4. Stakeholder tagging — apply stakeholder tags and coalition/conflict-axis
   annotations as Jira labels (or the instance's designated fields).
5. Dry-run preview — full payload in readable form; never commit without
   explicit approval.
6. Commit + confirm — execute the API call; return issue key and URL.
7. Session loop — "refine another" retains session context and returns to Stage
   02; "done" closes with a session summary of all created keys/URLs.

Known failure modes to guard: committing without the dry-run approval, and
silently dropping a custom field the target instance doesn't have — halt and
report instead.

## Inputs and data boundary

Reads the Stage 05 signed-off payload, Stage 03's dependency list, Stage 02's
stakeholder tags, and the hierarchy position from Stage 01. Max data-class:
internal; payloads travel only over the platform's authenticated channels; the
skill never stores or logs API credentials. Engines: both Rovo and Copilot
(Rovo natively for Atlassian actions; Copilot via sanctioned Jira integration).

## Demand source

`ai-refinement` flowspace, Stage 06 (Jira Commit & Close) — the source doc
declares `jira_ready: true` and the hierarchy but no field-to-API mapping, no
linkage protocol, and no session lifecycle. The stage's `CONTEXT.md` carries
this brief's id.

## Definition of done

- Resolves custom field IDs for the target Jira instance dynamically.
- Validates parent existence before committing a child.
- A work item commits with all fields populated, hierarchy linked, dependencies
  and labels set — in a single pass, no manual Jira field editing afterward.
- Handles API errors gracefully (field not found, parent not found, permission
  denied) without partial silent commits.
