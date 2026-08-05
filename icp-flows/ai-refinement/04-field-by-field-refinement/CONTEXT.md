---
id: ai-refinement-stage-04
title: "Stage 04 — Field-by-Field Refinement"
type: stage-context
stage: 4
review-intensity: light
artifact-version: "1.6"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-08-05
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
| Active persona contract (communication_style binding) | Stage 01 | Yes |
| Selected mode (fast-track / full-interactive) | Stage 01 | Yes |
| Selected creation mode (bulk / single-item) + normalized item set | Stage 01 | Yes |
| Field definitions (summary ≤ 10 words, AC starters) | `../reference/ai-refinement-hybrid.md` | Yes |
| House amendment: due-date elicitation rule | `../reference/ai-refinement-hybrid.md` | Yes |
| Extension field constraints (question_to_answer, timebox) | `../reference/work-item-schemas.md` | If type is spike |

## Process

`Layer-3: field-refinement-cadence` (skill spec in
`produced-skills/field-refinement-cadence/`, `verified`)

1. **Determine field order** — sequence remaining required fields logically:
   - Summary first (anchors everything)
   - For a spike: question_to_answer immediately after summary (every other
     field serves answering it)
   - Acceptance criteria next-to-last (depends on all other fields)
   - Due date always last (elicited only after acceptance criteria exist, so
     the user has a concrete effort reference to commit against; a spike's
     timebox is elicited alongside it)
   - Remaining fields, between summary and acceptance criteria, ordered by
     dependency chain

   **In fast-track mode**, this ordering governs presentation, not
   elicitation sequence: fields the agent can draft with confidence from the
   source material are grouped and presented together, with citations, as
   part of the Stage 03–05 consolidated checkpoint (Stage 05's Review
   section); only fields it can't confidently draft — plus `due_date`, always
   (step 5 is a hard carve-out) — enter the one-at-a-time queue below, in the
   stated order.
2. **One field at a time** — for each field that wasn't confidently
   extracted in fast-track mode (or for every field, in full-interactive
   mode):
   a. Present the field name, its constraints (e.g., summary ≤ 10 words), and any pre-filled content from earlier stages.
   b. Draft or refine the field value.
   c. Obtain explicit user confirmation before moving to the next field.

   `confirm_each_step: true` is non-negotiable for whichever fields reach
   this step — fast-track changes which fields arrive pre-drafted for the
   consolidated checkpoint, never whether a field gets an individual,
   explicit confirmation somewhere in the run.
3. **Cross-field conflict detection** — check for contradictions:
   - Due date vs. blocking dependency timelines
   - In-scope claims vs. acceptance criteria gaps
   - Type-of-work / work-category consistency (every type that carries both
     fields — feature, task, story, spike)
   - Timebox closes on or before the due date (spike only)
   - Conflict axis triggered in Stage 03 with no decision-owner recorded
4. **Acceptance criteria refinement** — enforce the starter pattern:
   - "Must be able to…"
   - "We will know this is done when…"
   Reframe any AC that doesn't match.
5. **Due-date elicitation — hard carve-out, every mode, no exception.** Never
   auto-generate or infer the due date, in full-interactive or fast-track.
   Present the confirmed acceptance criteria as an effort reference, then ask
   the user directly for a committed completion date. A stated deadline in
   source material (e.g., a vendor advisory's expiration, or a date mentioned
   in a structured requirements document) is surfaced as a reference point
   only — the user still confirms explicitly; a date being present in the
   source document is extraction of a reference, not a substitute for the
   user's commitment. For a spike, obtain the timebox at the same time and
   validate it closes on or before the confirmed due date. This is the
   flowspace's `due_date_elicitation` house amendment
   (`../reference/ai-refinement-hybrid.md`) — the rule fast-track mode is not
   permitted to relax.
6. **Summary enforcement** — validate ≤ 10 words; rewrite if exceeded.

**In bulk creation mode**, this stage folds into `bulk-child-creation`'s
batch-draft pass (Band ③). State the substitution plainly, because it is the
largest compression in the mode and the one the Stage 01 acknowledgment exists
to cover: **per-field confirmation is replaced by per-item review of the
presented set.** Each item's required fields are drafted from its row content
and the batch's shared grounding, and the user's verdict lands on the item as a
whole at the Band ③ review rather than field by field.

Three things do not move:

- **`confirm_each_step` is satisfied at item granularity, not abandoned.** No
  item is created without an explicit verdict covering it (accept / edit /
  reject), and a stop creates nothing. What changes is the unit of
  confirmation, not whether confirmation happens.
- **Anti-fabrication replaces the elicitation queue.** In single-item mode, a
  field the agent cannot draft enters the one-at-a-time queue at step 2. In
  bulk mode there is no queue: when a row's detail runs out, the item is
  reported **underspecified with the specific missing fields named**, and the
  user supplies detail, drops the row, or routes it into a full Band ② run.
  Nothing is padded into apparent completeness — at batch volume an invented
  field is indistinguishable from a drafted one at review time.
- **Constraints are unchanged.** Summary ≤ 10 words, approved AC starters,
  cross-field conflict detection, and the spike timebox rule apply per item
  exactly as below. Acceptance criteria remains a hard gate for every item;
  bulk compresses cadence, never standards.

**Due date in bulk mode** (step 5's carve-out, narrowed to batch scope by the
`bulk_creation_acknowledgment` amendment and nowhere else): the anchor is the
**parent's** due date where the set sits beneath one carrying it, stated as
such — the parent's commitment is what the children serve. A user-supplied
sheet's per-row due-date column is **user-committed** and used as given,
because the user authored the sheet. Absent both, one date is elicited
explicitly for the batch after the drafted acceptance criteria are visible as
an effort reference. A date the agent derives from prose remains a reference
point only, never a commitment — that part of the rule does not narrow.

**Context-budget marker.** Per the `session_budget_checkpoint` house amendment
(`../reference/ai-refinement-hybrid.md`), self-query and state context-window
usage at this stage's exit: "Stage 04 — context remaining: ~<percent>%."
Informational only at 50%; an escalating quality-degradation advisory at 60%
and 70%; past 80%, stop proposing further stages and produce the handoff
defined in `../reference/session-continuation-handoff.md` instead of
proceeding.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Complete set of refined field values | Stage 05 | Key-value pairs |
| Cross-field conflict report (if any) | User / Stage 05 | Advisory list |
| Per-field confirmation log | Run decision log | Conversation record |

## Verify

Cross-stage trace: every value refined here must trace to a field the Stage 01
schema requires (or marks optional) for the selected type, and the scope-derived
fields (`in_scope`, `out_of_scope`, `dependencies` — where the selected schema
carries them; a spike carries none) must match what Stage 03 confirmed — the
failure this catches is a field silently rewritten past its confirmed upstream
content. Running this check leaves a one-line result in the
run's decision log.

- [ ] Every required field for the selected work item type has a value
- [ ] Summary is ≤ 10 words
- [ ] All acceptance criteria use approved starters
- [ ] Scope fields match Stage 03's confirmed scope package (where the schema
      carries them)
- [ ] Question-to-answer and timebox meet their extension constraints (spike)
- [ ] Due date traces to an explicit user commitment made after acceptance
      criteria were presented — never fabricated or defaulted, in any mode
- [ ] Cross-field conflicts were checked and resolved
- [ ] Each field was individually confirmed by the user — either inline
      (full-interactive, or fast-track fallback) or as part of the Stage
      03–05 consolidated checkpoint (fast-track extracted fields); in bulk
      mode, every item carries an explicit accept/edit verdict at the Band ③
      review, which is where `confirm_each_step` lands at item granularity
- [ ] Fast-track-extracted fields carry a source citation in the transcript
- [ ] In bulk mode, no item was padded past its available grounding — rows
      whose detail ran out are reported as underspecified with the specific
      missing fields named, never filled with plausible-sounding content
- [ ] In bulk mode, the due date traces to the parent's date, a user-supplied
      sheet column, or an explicit batch elicitation — never to a date the
      agent derived from prose
- [ ] No PII or confidential data in any field
- [ ] Context-remaining marker was stated at stage exit, with the correct
      threshold advisory (or handoff, past 80%) attached if usage warranted it

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — each field was already user-confirmed, inline or at
  the consolidated checkpoint; review is a consistency scan. In
  full-interactive mode this stage's confirmation is its own checkpoint; in
  fast-track mode it folds into the Stage 03–05 consolidated checkpoint (see
  Stage 05's Review section).
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
