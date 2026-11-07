---
id: comms-builder-stage-03
title: "Stage 03 — Audience Design"
type: stage-context
stage: 3
review-intensity: heavy
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-11-07
updated: 2026-11-07
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[comms-builder]]"
  - "[[sp-audience-mapper]]"
  - "[[audience-segment-view]]"
---

# Stage 3 — Audience Design (`CONTEXT.md`)

## Inputs

`work/01-framing-brief.md` (audience as described, comms type, lane,
whether actions or validation exist) and `work/02-context-sheet.md`
(affected services, impact, actions, conflicts) when Stage 2 ran.
`reference/audience-segment-view.md` for default segments and the view
shape. A stakeholder register for the domain, if the instance has one.

## Process

1. Start from the three default segments — application owners, technical
   owners, business users — and keep, drop, split, or add segments against
   the affected services. Name each by role, group, or distribution list;
   never by person.
2. For each segment, fill the segment view: what changes for them, what
   they must do and by when, what they can ignore, the channel (email,
   Teams post, meeting, Confluence page), and who answers their questions.
3. Mark segments that must **validate** something (e.g., an application
   team confirming its service after a change) — these feed Stage 4's
   validation tracker.
4. Ground against the stakeholder register where one exists; otherwise ask
   the user directly and record "ungrounded".
5. Resolve or escalate each conflict carried from Stage 2 with the user.
6. One-off lane: one or two segments, steps 1–2 only.

`Layer-3: TBD — skill-primer-brief filed (sp-audience-mapper)`. Until built,
run the steps above inline.

## Outputs

`work/03-audience-map.md`: a segment table (segment, identified by, what
changes, action and due date, validates? yes/no and what, channel, question
owner); grounded or ungrounded; conflicts resolved, with the resolution.

## Verify

Stage 3 → Stage 5 trace: every segment in `work/03-audience-map.md` has at
least one Stage 5 draft per touchpoint it is on, and no Stage 5 draft
addresses a segment not in the map. One-line result in the run's decision
log.

## Review

- **Reviewer:** the requester.
- **Intensity:** `heavy` — who is told what is the flow's central judgment;
  a missed segment is the most common comms failure.
- **Evidence:** the requester's confirmation of the segment table, recorded
  in `work/03-audience-map.md`.

## Data boundary

- **Max data-class this stage handles:** `internal`.
- **Sanctioned engines for this stage:** Copilot.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
