---
id: comms-builder-stage-01
title: "Stage 01 — Frame & Triage"
type: stage-context
stage: 1
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
  - "[[comms-types-and-lanes]]"
---

# Stage 1 — Frame & Triage (`CONTEXT.md`)

## Inputs

The requester's ask in their own words, plus whatever they can give of:
subject, audience described in plain words, key date (change window, go-live,
deadline, or "as soon as possible" for a response plan), and any linked
record numbers (change, incident, CVE/vulnerability record, Jira key).
`reference/comms-types-and-lanes.md` supplies the type list, the lane rule,
and the default touchpoint set per type. Nothing from a prior run is
assumed.

## Process

1. Restate the ask in one sentence and confirm it.
2. Ask only for what is missing: subject, audience, key date, linked
   records, and whether people must *do* anything (act, validate, attend).
3. Propose a **comms type** — awareness, action required, change
   implementation, or response plan — and name the signal that drove it.
4. Propose a **lane** — one-off or campaign — against the three campaign
   signals in `reference/comms-types-and-lanes.md` (many stakeholders;
   application-team validation needed; multi-stakeholder project). State
   which signals fired. The user confirms or overrides; record an override
   with its reason.
5. For a response plan, state the data rule (impact, timing, actions only)
   before anything is gathered.
6. Flag an exec status-deck ask as belonging to `executive-slide-digest` and
   offer to route there instead.
7. Record whether the instance has a design-system binding and a template
   folder set (`reference/design-system-binding.md`); if not, say the run
   will use plain defaults.

`Layer-3: inline (one-off, described above)` — human judgment, steered by
the reference rules.

## Outputs

`work/01-framing-brief.md`: subject (one sentence); comms type with its
driving signal; lane with the campaign signals that fired or did not, and
any user override with reason; audience as described by the user; key date
(or "ASAP" with an update cadence for a response plan); linked record
numbers by system; whether actions, validation, or an implementation event
exist (each yes/no); binding and template-folder status; the data rule
statement when the type is response plan.

## Verify

Stage 1 → Stage 8 trace: the lane and comms type recorded in
`work/01-framing-brief.md` must match the lane and type stated in Stage 8's
delivered pack header, unless Stage 7 logged an upgrade from one-off to
campaign. A mismatch without that log line means a stage ran under the wrong
lane. One-line result in the run's decision log.

## Review

- **Reviewer:** the requester (the person who owns getting this comms out).
- **Intensity:** `heavy` — type and lane set everything downstream, and
  over-communicating costs as much trust as under-communicating.
- **Evidence:** the requester's explicit confirmation of type and lane,
  recorded in `work/01-framing-brief.md`.

## Data boundary

- **Max data-class this stage handles:** `internal`.
- **Sanctioned engines for this stage:** Copilot.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
