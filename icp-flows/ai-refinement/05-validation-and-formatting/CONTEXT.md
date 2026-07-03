---
id: ai-refinement-stage-05
title: "Stage 05 — Validation & Formatting"
type: stage-context
stage: 5
review-intensity: light
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
  - "[[workitem-validation]]"
---

# Stage 05 — Validation & Formatting

## Inputs

| Input | Source | Required |
|---|---|---|
| Complete set of refined field values | Stage 04 | Yes |
| Work item schema (required/optional fields) | Stage 01 | Yes |
| Formatting rules (no bold, no emojis) | `../reference/ai-refinement-hybrid.md` | Yes |
| Cross-field conflict report (if any) | Stage 04 | If exists |

## Process

`Layer-3: workitem-validation` (skill spec in
`produced-skills/workitem-validation/`, `verified`)

1. **Completeness scan** — walk the schema's required-field list and confirm every field has a non-empty value.
2. **Constraint validation** — check each field against its constraints:
   - Summary ≤ 10 words
   - AC starters match approved patterns
   - Due date is a valid future date
   - Dependencies reference real items (if Jira-linked)
   - Spike only: question_to_answer is a single question; timebox states an
     explicit bound closing on or before the due date
     (`../reference/work-item-schemas.md`, extension field definitions)
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
| Validation report | User / run decision log | Structured pass/fail |
| User sign-off confirmation | Stage 06 | Boolean |

## Verify

Cross-stage trace: the validated payload's field set must equal Stage 04's
refined field set (no field added, dropped, or content-changed by the
formatting pass — formatting alters markup only), and every required field in
the Stage 01 schema must appear in the payload — the failure this catches is
the validator silently rewriting content or a required field lost between
stages. Running this check leaves a one-line result in the run's decision log.

- [ ] Every required field passes completeness check
- [ ] All constraints pass (summary length, AC format, date validity)
- [ ] No bold or emoji characters remain in any field
- [ ] Auto-corrections are logged in the validation report and touch formatting only
- [ ] Any halt-level issues were surfaced and resolved with the user
- [ ] User explicitly signed off on the final payload

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — validation is largely mechanical; review confirms the
  report is accurate.
- **Evidence:** the validation report itself plus a one-line entry in the run's
  decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- Validated payload is `internal` — ready for Jira but not for external sharing.
- Validation report may reference field values — same `internal` classification.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
