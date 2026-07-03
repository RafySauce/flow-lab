---
id: ai-refinement-stage-04
title: "Stage 04 — Field-by-Field Refinement"
type: stage-context
stage: 4
review-intensity: light
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
related:
  - "[[ai-refinement]]"
  - "[[field-refinement-cadence]]"
---

# Stage 04 — Field-by-Field Refinement

## Inputs

| Input | Source | Required |
|---|---|---|
| All confirmed fields and annotations from Stages 02–03 | Stages 02, 03 | Yes |
| Work item schema (required/optional field list) | Stage 01 | Yes |
| Active persona contract | Stage 01 | Yes |
| Field definitions (summary ≤ 10 words, AC starters) | `../reference/ai-refinement-hybrid.md` | Yes |

## Process

`Layer-3: field-refinement-cadence` (skill spec in
`skill-foundry/backlog-skill-starters/field-refinement-cadence/`, `to-review`)

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
   - Conflict axis triggered in Stage 03 with no decision-owner recorded
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
| Per-field confirmation log | Run decision log | Conversation record |

## Verify

Cross-stage trace: every value refined here must trace to a field the Stage 01
schema requires (or marks optional) for the selected type, and the scope-derived
fields (`in_scope`, `out_of_scope`, `dependencies`) must match what Stage 03
confirmed — the failure this catches is a field silently rewritten past its
confirmed upstream content. Running this check leaves a one-line result in the
run's decision log.

- [ ] Every required field for the selected work item type has a value
- [ ] Summary is ≤ 10 words
- [ ] All acceptance criteria use approved starters
- [ ] Scope fields match Stage 03's confirmed scope package
- [ ] Cross-field conflicts were checked and resolved
- [ ] Each field was individually confirmed by the user
- [ ] No PII or confidential data in any field

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — each field was already user-confirmed inline; review is
  a consistency scan.
- **Evidence:** per-field confirmation log and a one-line entry in the run's
  decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- Field values are `internal` classification; acceptance criteria may reference
  internal systems — acceptable at `internal`.
- No credentials, tokens, or PII in any field value.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
