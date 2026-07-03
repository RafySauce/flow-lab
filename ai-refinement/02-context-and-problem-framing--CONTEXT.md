---
id: ai-refinement-stage-02
title: "Stage 02 — Context & Problem Framing"
type: stage-context
stage: 2
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
  - "[[skill-context-elicitation]]"
skill-dependency: skill-context-elicitation
skill-status: gap
---

# Stage 02 — Context & Problem Framing

## Inputs

| Input | Source | Required |
|---|---|---|
| Acknowledged responsibility flag | Stage 01 | Yes |
| Selected work item type + schema | Stage 01 | Yes |
| Active persona contract | Stage 01 | Yes |
| User's raw problem description / context | User | Yes |

## Process

> **⚠ SKILL GAP** — `skill-context-elicitation` does not yet exist.
> See `skill-demand/skill-context-elicitation-brief.md`.

When the skill is built, this stage will:

1. **Elicit context** — use a structured question sequence to draw out:
   - What problem is being solved?
   - Who is affected and how?
   - What is the business / operational value?
   - What has been tried before (if anything)?
2. **Challenge vague inputs** — apply pushback patterns when answers are too abstract.
   The persona's `challenge_incomplete_requirements` behavior drives this.
3. **Draft problem statement** — synthesize user responses into a clear problem statement.
4. **Draft business outcomes** — if the work item type is `solution_epic`, produce measurable outcomes.
5. **Draft customer/business value** — produce a value statement that connects to the problem.
6. **Confirm framing** — present the drafted fields to the user for approval before proceeding.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Confirmed problem statement | Stage 04 (field refinement) | Plain text |
| Confirmed business outcomes (solution_epic only) | Stage 04 | Plain text |
| Confirmed customer/business value | Stage 04 | Plain text |
| Elicitation transcript (for audit) | Decision log | Conversation record |

## Verify

- [ ] Problem statement is specific, not generic
- [ ] Business outcomes are measurable (solution_epic)
- [ ] Customer/business value links to the stated problem
- [ ] User explicitly confirmed each drafted field
- [ ] No PII or confidential data was introduced

## Review

**Intensity: Heavy** — problem framing errors cascade into every downstream field.

Review owner: Human (Rafael or delegate)

## Data Boundary

- User-provided context may contain operational details — classify as `internal`.
- AI must not store or log conversation content beyond session scope.
- If user introduces PII, halt and invoke data-safety guardrail from Stage 01.
