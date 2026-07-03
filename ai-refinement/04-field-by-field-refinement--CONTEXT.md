---
id: ai-refinement-stage-04
title: "Stage 04 — Field-by-Field Refinement"
type: stage-context
stage: 4
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
  - "[[skill-field-refinement-cadence]]"
skill-dependency: skill-field-refinement-cadence
skill-status: gap
---

# Stage 04 — Field-by-Field Refinement

## Inputs

| Input | Source | Required |
|---|---|---|
| All confirmed fields from Stages 02–03 | Stages 02, 03 | Yes |
| Work item schema (required/optional field list) | Stage 01 | Yes |
| Active persona contract | Stage 01 | Yes |
| Field definitions (summary ≤10 words, AC starters) | Source doc | Yes |

## Process

> **⚠ SKILL GAP** — `skill-field-refinement-cadence` does not yet exist.
> See `skill-demand/skill-field-refinement-cadence-brief.md`.

When the skill is built, this stage will:

1. **Determine field order** — sequence remaining required fields logically:
   - Summary first (anchors everything)
   - Acceptance criteria last (depends on all other fields)
   - Remaining fields ordered by dependency chain
2. **One field at a time** — for each field:
   a. Present the field name, its constraints (e.g., summary ≤ 10 words), and any pre-filled content from earlier stages.
   b. Draft or refine the field value.
   c. Obtain explicit user confirmation before moving to the next field.
3. **Cross-field conflict detection** — check for contradictions:
   - Due date vs. blocking dependency timelines
   - In-scope claims vs. acceptance criteria gaps
   - Type-of-work / work-category consistency (feature only)
4. **Acceptance criteria refinement** — enforce the starter pattern:
   - "Must be able to…"
   - "We will know this is done when…"
   Reframe any AC that doesn't match.
5. **Summary enforcement** — validate ≤ 10 words; rewrite if exceeded.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Complete set of refined field values | Stage 05 | Key-value pairs |
| Cross-field conflict report (if any) | User / Stage 05 | Advisory list |
| Per-field confirmation log | Decision log | Conversation record |

## Verify

- [ ] Every required field for the selected work item type has a value
- [ ] Summary is ≤ 10 words
- [ ] All acceptance criteria use approved starters
- [ ] Cross-field conflicts were checked and resolved
- [ ] Each field was individually confirmed by the user
- [ ] No PII or confidential data in any field

## Review

**Intensity: Light** — each field was already user-confirmed inline; review is a consistency scan.

Review owner: Human (Rafael or delegate)

## Data Boundary

- Field values are `internal` classification.
- Acceptance criteria may reference internal systems — acceptable at `internal`.
- No credentials, tokens, or PII in any field value.
