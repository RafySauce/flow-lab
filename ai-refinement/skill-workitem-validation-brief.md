---
id: skill-workitem-validation-brief
title: "Skill Primer Brief — Work Item Validation"
type: skill-primer-brief
status: to-review
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
source: human+ai
data-class: internal
owner: rafael.torres
demanded-by: ai-refinement-stage-05
target-adapters: [rovo, copilot]
---

# Skill Primer Brief — Work Item Validation

## What This Skill Does

Performs a completeness and constraint scan on a refined work item, applies formatting
rules, and produces a structured pass/fail validation report.

## Why It's Needed

The source doc specifies formatting rules (`no_bold: true`, `no_emojis: true`) and
`jira_ready: true` but provides no:
- Scan order or priority for validation checks
- Decision tree for when to auto-correct vs. halt and ask the user
- Standard format for the validation report

## Consuming Flowspace Stage

- `ai-refinement` → Stage 05 (Validation & Formatting)

## Core Capabilities Required

1. **Completeness scan** — walk the schema's required-field list and confirm every
   field has a non-empty, non-placeholder value.
2. **Constraint validation** — check each field against its rules:
   - Summary ≤ 10 words
   - AC starters match approved patterns
   - Due date is valid and in the future
   - Dependencies reference resolvable items
3. **Formatting pass** — apply `no_bold`, `no_emojis`:
   - Strip markdown bold markers (`**text**` → `text`)
   - Remove emoji characters
   - Normalize whitespace
4. **Auto-correct vs. halt decision tree**:
   - **Auto-correct** (silent fix + log): formatting violations, minor whitespace
   - **Halt** (surface to user): missing required fields, constraint violations,
     unresolved cross-field conflicts
5. **Validation report format** — structured output with:
   - Per-field pass/fail status
   - List of auto-corrections applied
   - List of halt-level issues requiring user resolution

## Acceptance Criteria

- Must be able to catch a missing required field and halt before Jira commit.
- Must be able to auto-correct formatting without user intervention.
- We will know this is done when no work item reaches Stage 06 with a formatting
  violation or missing required field.

## Constraints

- Must not modify field *content* during auto-correct — only formatting.
- Must not introduce PII or confidential data.
- Must work on both Rovo and Copilot surfaces.
