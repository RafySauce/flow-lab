---
id: sp-accomplishments-drafter-revision
title: "Skill Primer Brief — Accomplishments Drafter 2.0 (Revision)"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
generated-by: flow-foundry
data-class: public
related: ["[[accomplishments-digest]]", "[[accomplishments-drafter]]"]
---

# Skill Primer Brief — Accomplishments Drafter 2.0 (Revision)

> A revision of the verified `produced-skills/accomplishments-drafter` (1.0),
> demanded by `accomplishments-digest` 2.0, Stage 7 (Draft). Intake record:
> `flow-foundry/backlog-flow-starters/fp-accomplishments-digest-m365-servicenow.md`.
> When this revision is built, the skill returns to `to-review` until it passes the gate again.

## Purpose

Keep the drafter's job the same (one theme-structured, outcome-framed,
audience-matched draft), but take the confirmed correlation map as its
input instead of two raw digests, and add the Operational load section.

## Triggering intent

`accomplishments-digest` Stage 7, given the framing brief and Stage 6's
confirmed correlation map. The near-misses are unchanged: gathering, correlating
(`accomplishments-correlator`), and the engineer's final edit.

## Method sketch (changes only)

- **Inputs:** the framing brief plus `work/06-correlation-map.md`, replacing
  the Jira and Confluence digests. Each confirmed group becomes a bullet or
  a short bullet cluster under its theme. Dropped groups never reappear.
- **Recognition:** goes into the collaboration section or under its theme,
  paraphrased unless the map records an engineer-approved quote.
- **Operational load:** drafted from the map's load summary as context
  (priority mix, median time to resolve, problem-led fixes), never as a bare
  count headline and never with a peer comparison. Omitted when ServiceNow
  was skipped.
- **Gaps:** skipped or unreachable sources join the Notes section.
- **Unchanged:** top-item emphasis, the exclusion-list check across the full
  draft, audience matching, and no fabricated content.

## Inputs and data boundary

`internal`; any engine sanctioned for `internal`; no external queries.

## Demand source

`accomplishments-digest` 2.0, Stage 7. Operator decisions D3 (separate
Correlate stage) and D4 (Operational load section plus counts in themes).

## Definition of done

- Every bullet traces to a confirmed group.
- The exclusion-list check passes.
- Operational load appears only when ServiceNow ran, and reads as context.
- A simulated run where the map holds one group with evidence from three
  sources yields one bullet, not three.
- The 1.0 review criteria that still apply continue to pass.
