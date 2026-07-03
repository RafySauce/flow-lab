---
id: ai-refinement-stage-05
title: "Stage 05 — Validation & Formatting"
type: stage-context
stage: 5
review-intensity: light
status: to-review
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
source: human+ai
data-class: internal
owner: rafael.torres
related:
  - "[[ai-refinement]]"
  - "[[skill-workitem-validation]]"
skill-dependency: skill-workitem-validation
skill-status: gap
---

# Stage 05 — Validation & Formatting

## Inputs

| Input | Source | Required |
|---|---|---|
| Complete set of refined field values | Stage 04 | Yes |
| Work item schema (required/optional fields) | Stage 01 | Yes |
| Formatting rules (no bold, no emojis) | Source doc | Yes |
| Cross-field conflict report (if any) | Stage 04 | If exists |

## Process

> **⚠ SKILL GAP** — `skill-workitem-validation` does not yet exist.
> See `skill-demand/skill-workitem-validation-brief.md`.

When the skill is built, this stage will:

1. **Completeness scan** — walk the schema's required-field list and confirm every field has a non-empty value.
2. **Constraint validation** — check each field against its constraints:
   - Summary ≤ 10 words
   - AC starters match approved patterns
   - Due date is a valid future date
   - Dependencies reference real items (if Jira-linked)
3. **Formatting pass** — apply the `no_bold`, `no_emojis` rules:
   - Strip `**bold**` markers
   - Remove emoji characters
   - Normalize whitespace and list formatting
4. **Auto-correct vs. halt decision tree**:
   - **Auto-correct**: formatting violations, minor whitespace — fix silently and note in report
   - **Halt**: missing required fields, constraint violations, unresolved cross-field conflicts — present to user for resolution
5. **Validation report** — produce a structured pass/fail report for user review.
6. **User sign-off** — user confirms the validated, formatted work item is ready for Jira commit.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Validated + formatted work item payload | Stage 06 | Key-value pairs (clean) |
| Validation report | User / decision log | Structured pass/fail |
| User sign-off confirmation | Stage 06 | Boolean |

## Verify

- [ ] Every required field passes completeness check
- [ ] All constraints pass (summary length, AC format, date validity)
- [ ] No bold or emoji characters remain in any field
- [ ] Auto-corrections are logged in the validation report
- [ ] Any halt-level issues were surfaced and resolved with user
- [ ] User explicitly signed off on the final payload

## Review

**Intensity: Light** — validation is largely mechanical; review confirms the report is accurate.

Review owner: Human (Rafael or delegate)

## Data Boundary

- Validated payload is `internal` — ready for Jira but not for external sharing.
- Validation report may reference field values — same `internal` classification.
