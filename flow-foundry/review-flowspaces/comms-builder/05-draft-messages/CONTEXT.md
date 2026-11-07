---
id: comms-builder-stage-05
title: "Stage 05 — Draft Messages"
type: stage-context
stage: 5
review-intensity: light
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
  - "[[sp-comms-drafter]]"
  - "[[default-message-templates]]"
---

# Stage 5 — Draft Messages (`CONTEXT.md`)

## Inputs

`work/03-audience-map.md` (segments, what changes, actions, channel,
question owner); `work/04-comms-plan.md` touchpoint rows with draft ids
(campaign) or the single touchpoint from `work/01-framing-brief.md`
(one-off); `work/02-context-sheet.md` for cited facts. Templates from the
operator's `template-path` (binding config) or, if unset, from
`reference/default-message-templates.md`.

## Process

1. For each (segment, touchpoint) pair, pick the matching template by
   touchpoint kind and channel.
2. Fill only from cited inputs: dates, windows, services, actions, contact.
   Anything the inputs lack becomes a visible `[NEEDS INPUT: …]` marker,
   never an invented fact.
3. Write subject lines that lead with the action or the date
   ("Action needed by 14 Nov: …"); keep body text plain — no visual
   styling, since recipients' clients strip it. Follow the binding's voice
   rules if set.
4. For a response plan, re-apply the data rule to each draft.
5. Number each draft with its id from Stage 4 (or `D1` for a one-off).

`Layer-3: TBD — skill-primer-brief filed (sp-comms-drafter)`. Until built,
run the steps above inline. The skill is also invocable standalone for a
quick single message outside this flow.

## Outputs

`work/05-drafts.md`: one block per draft — id, segment, channel, send date,
sender, subject, body — plus a list of every open `[NEEDS INPUT]` marker by
draft id, and which template source was used (operator folder or default).

## Verify

Stage 5 → Stage 2 trace: every factual claim (date, window, service, action)
in a draft cites back to `work/02-context-sheet.md` or
`work/01-framing-brief.md`; for a response plan, no draft contains a field
the data rule drops. One-line result in the run's decision log.

## Review

- **Reviewer:** the requester.
- **Intensity:** `light` — template filling from fixed inputs.
- **Evidence:** drafts are available to skim; open markers are resolved at
  Stage 7.

## Data boundary

- **Max data-class this stage handles:** `internal`.
- **Sanctioned engines for this stage:** Copilot.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
