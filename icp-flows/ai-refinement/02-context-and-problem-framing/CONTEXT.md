---
id: ai-refinement-stage-02
title: "Stage 02 — Context & Problem Framing"
type: stage-context
stage: 2
review-intensity: heavy
artifact-version: "1.3"
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
  - "[[context-elicitation]]"
  - "[[platform-stakeholder-register]]"
---

# Stage 02 — Context & Problem Framing

## Inputs

| Input | Source | Required |
|---|---|---|
| Acknowledged responsibility flag | Stage 01 | Yes |
| Selected work item type + schema | Stage 01 | Yes |
| Active persona contract | Stage 01 | Yes |
| User's raw problem description / context | User | Yes |
| Screened source material + input-type tag (email request, vendor action notice, meeting minutes/notes, chat-stated requirement) | Stage 01 | No |
| Stakeholder register (role-types, "what they value most") | `../reference/platform-stakeholder-register.md` | Yes |

## Process

`Layer-3: context-elicitation` (skill spec in
`produced-skills/context-elicitation/`, `verified`)

1. **Elicit context** — use the skill's structured question sequence to draw out:
   - What problem is being solved?
   - Who is affected and how?
   - What is the business / operational value?
   - What has been tried before (if anything)?

   When screened source material accompanies the description, let its type
   (per the HUB "Common source inputs" taxonomy) steer the sequence: an email
   request or chat-stated requirement names a requester or beneficiary — start
   the stakeholder sweep there; vendor action notices and stated task lists
   are solution-shaped — elicit the underlying problem before accepting the
   actions as scope; meeting minutes may hold several candidate items — split
   them and frame one per run.
2. **Stakeholder sweep** — walk the stakeholder register and tag the entries
   whose needs or limits define this item (producers, consumers,
   constraint-setters, operators, adjacents, sponsors). Use each tagged entry's
   "what they value most" column to prompt for requirements the user hasn't
   volunteered.
3. **Challenge vague inputs** — apply the skill's pushback patterns when answers
   are too abstract. The persona's `challenge_incomplete_requirements` behavior
   drives this.
4. **Draft problem statement** — synthesize user responses into a clear problem statement.
5. **Draft business outcomes** — if the work item type is `solution_epic`, produce measurable outcomes.
   If the type is `spike`, crystallize the elicited problem into the single
   question the spike must answer (drafts `question_to_answer` — one
   answerable question; if it needs "and", recommend splitting the spike).
6. **Draft customer/business value** — produce a value statement that connects
   the problem to what the tagged stakeholders value.
7. **Confirm framing** — present the drafted fields and the stakeholder tag list
   to the user for approval before proceeding.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Confirmed problem statement | Stages 03, 04 | Plain text |
| Confirmed business outcomes (solution_epic only) | Stage 04 | Plain text |
| Confirmed question-to-answer (spike only) | Stage 04 | Plain text |
| Confirmed customer/business value | Stage 04 | Plain text |
| Stakeholder tag list (register entry # + role-type each) | Stages 03, 06 | Tagged list |
| Elicitation transcript (for audit) | Run decision log | Conversation record |

## Verify

Cross-stage trace: every field this stage confirms must be one the Stage 01
schema requires for the selected work-item type — the failure this catches is
drafting `business_outcomes` for a `feature` (which has no such field) or
skipping a required field the type demands. Second trace: every stakeholder tag
resolves to a numbered entry in `../reference/platform-stakeholder-register.md`.
Running these checks leaves a one-line result in the run's decision log.

- [ ] Problem statement is specific, not generic
- [ ] Business outcomes are measurable (solution_epic)
- [ ] Question-to-answer is a single answerable question (spike)
- [ ] Customer/business value links to the stated problem and tagged stakeholders
- [ ] Every stakeholder tag resolves to a register entry
- [ ] User explicitly confirmed each drafted field
- [ ] If source material was provided, the problem was elicited — the drafted
      problem statement is not a transcription of the request or action list
- [ ] No PII or confidential data was introduced

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy — problem framing errors cascade into every downstream
  field.
- **Evidence:** user confirmation of each drafted field in-session and a
  one-line entry in the run's decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- User-provided context may contain operational details — classify as `internal`.
- The AI must not store or log conversation content beyond session scope.
- If the user introduces PII, halt and invoke the data-safety guardrail from
  Stage 01.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
