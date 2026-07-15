---
id: ai-refinement-stage-02
title: "Stage 02 — Context & Problem Framing"
type: stage-context
stage: 2
review-intensity: heavy
artifact-version: "1.5"
status: living
truth-level: verified
created: 2026-07-03
updated: 2026-07-15
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
| Active persona contract (communication_style binding) | Stage 01 | Yes |
| Selected mode (fast-track / full-interactive) + rationale | Stage 01 | Yes |
| User's raw problem description / context | User | Yes |
| Screened source material + input-type tag (any of the eight HUB "Common source inputs" types) | Stage 01 | No |
| Stakeholder register (role-types, "what they value most"), if loaded | `../reference/platform-stakeholder-register.md` or a domain instance | If grounded |
| Stakeholder-register grounding status (grounded / ungrounded) | Stage 01 | Yes |

## Process

`Layer-3: context-elicitation` (skill spec in
`produced-skills/context-elicitation/`, `verified`)

1. **Elicit context** — use the skill's structured question sequence to draw out:
   - What problem is being solved?
   - Who is affected and how?
   - What is the business / operational value?
   - What has been tried before (if anything)?

   When screened source material accompanies the description, let its type
   (per the HUB "Common source inputs" taxonomy — email request, vendor action
   notice, meeting minutes/notes, chat-stated requirement, structured
   requirements document, incident/problem record, architecture/design
   artifact, or unclassified) steer the sequence: an email request or
   chat-stated requirement names a requester or beneficiary — start the
   stakeholder sweep there; vendor action notices, stated task lists, and
   structured requirements documents are solution-shaped — elicit the
   underlying problem before accepting the actions as scope; meeting minutes
   may hold several candidate items — split them and frame one per run; an
   incident/problem record is already problem-shaped — verify it names an
   affected party and a business impact rather than only a technical
   symptom; an architecture/design artifact is solution-shaped at a systems
   level — recover the problem it was drawn to solve; an unclassified
   document gets the full question sequence with no shortcuts assumed.

   **In fast-track mode:** draft the problem statement, business outcomes /
   question-to-answer, and customer/business value directly from the source
   material, citing where in the document each draft came from, instead of
   asking the four questions above one at a time. Any of the four the agent
   can't answer with reasonable confidence from the material falls back to
   being asked directly — never left blank or guessed.
2. **Stakeholder sweep** — if a stakeholder register is loaded (Stage 01's
   grounding check), walk it and tag the entries whose needs or limits define
   this item (producers, consumers, constraint-setters, operators, adjacents,
   sponsors), using each tagged entry's "what they value most" column to
   prompt for requirements the user hasn't volunteered. If Stage 01 flagged
   **ungrounded mode** (no register loaded for this domain), ask the user
   directly who is affected and what they need instead of walking a register —
   degraded but functional. **This step is a hard carve-out: it is always run
   interactively, in every mode, register or no register.** Fast-track never
   extracts or skips the stakeholder sweep — misidentifying who a work item
   affects costs more downstream than a wording tweak would.
3. **Challenge vague inputs** — apply the skill's pushback patterns when answers
   are too abstract. The persona's `challenge_incomplete_requirements` behavior
   drives this. Applies in every mode: a fast-track-extracted draft that reads
   as vague or generic gets pushed back on, not accepted because it was
   extracted rather than elicited.
4. **Draft problem statement** — synthesize user responses (or source-material
   extraction, in fast-track) into a clear problem statement.
5. **Draft business outcomes** — if the work item type is `solution_epic` or
   `portfolio_epic`, produce measurable outcomes.
   If the type is `spike`, crystallize the elicited problem into the single
   question the spike must answer (drafts `question_to_answer` — one
   answerable question; if it needs "and", recommend splitting the spike).
6. **Draft customer/business value** — produce a value statement that connects
   the problem to what the tagged stakeholders value.
7. **Confirm framing** — present the drafted fields and the stakeholder tag list
   to the user for approval before proceeding. In full-interactive mode this is
   its own checkpoint; in fast-track mode it still happens here at Stage 02 —
   the Stage 03–05 consolidation (see those stages' Review sections) does not
   reach back to fold Stage 02 in, since this stage's review stays heavy in
   every mode (see Review, below).

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Confirmed problem statement | Stages 03, 04 | Plain text |
| Confirmed business outcomes (solution_epic, portfolio_epic) | Stage 04 | Plain text |
| Confirmed question-to-answer (spike only) | Stage 04 | Plain text |
| Confirmed customer/business value | Stage 04 | Plain text |
| Stakeholder tag list (register entry # + role-type each) | Stages 03, 06 | Tagged list |
| Elicitation transcript (for audit) | Run decision log | Conversation record |

## Verify

Cross-stage trace: every field this stage confirms must be one the Stage 01
schema requires for the selected work-item type — the failure this catches is
drafting `business_outcomes` for a `feature` (which has no such field) or
skipping a required field the type demands. Second trace: in grounded mode,
every stakeholder tag resolves to a numbered entry in the loaded register
(`../reference/platform-stakeholder-register.md` or a domain instance of the
template); in ungrounded mode, every tag traces to the user's direct answer
instead. Running these checks leaves a one-line result in the run's decision log.

- [ ] Problem statement is specific, not generic
- [ ] Business outcomes are measurable (solution_epic, portfolio_epic)
- [ ] Question-to-answer is a single answerable question (spike)
- [ ] Customer/business value links to the stated problem and tagged stakeholders
- [ ] Every stakeholder tag resolves to a register entry (grounded) or an
      explicit user answer (ungrounded)
- [ ] User explicitly confirmed each drafted field
- [ ] If source material was provided, the problem was elicited — the drafted
      problem statement is not a transcription of the request or action list
      (nor, in fast-track mode, an unreviewed copy of the source text)
- [ ] If fast-track mode extracted any field, its source citation is in the
      transcript and the user confirmed it explicitly
- [ ] The stakeholder sweep (step 2) ran interactively regardless of mode —
      never fast-track-extracted or skipped
- [ ] No PII or confidential data was introduced

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy, unconditionally — problem framing errors cascade into
  every downstream field. This does not compress in fast-track mode; the
  Stage 03–05 consolidated checkpoint (Stage 05's Review section) never folds
  Stage 02 in.
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
