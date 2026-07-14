---
id: fp-weekly-status-report
title: "Flow Primer Brief — Weekly Status Report (EXEMPLAR)"
type: flow-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-02
updated: 2026-07-02
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.0"
data-class: public
related: []
---

# Flow Primer Brief — Weekly Status Report

> **EXEMPLAR.** A deliberately generic, sanitized worked example of a filled-in primer brief — the kind of small, genuinely recurring workflow that makes a good *first* flowspace. Use it as a reading model, then write your own against the template.

## Purpose

Produce the weekly status report for a team: gather the week's signal from Jira and Confluence, synthesize it into the standard report shape, and publish after owner review. Recurs weekly; currently ~90 minutes of manual assembly.

## Trigger and cadence

Every Thursday, ahead of the Friday status meeting. One run per week.

## Stage sketch

| # | Stage | What happens | Review intensity (est.) |
|---|---|---|---|
| 1 | Frame | Owner sets the week's emphasis: what matters this week, what to foreground, any sensitivities | heavy |
| 2 | Gather | Pull the week's completed/slipped items, decisions, and risks from Jira and Confluence into a working digest | light |
| 3 | Draft | Synthesize the digest into the standard report template (wins / progress / risks / asks) | light |
| 4 | Align & publish | Owner reviews against stage-1 framing, edits, signs off, publishes to the status page | heavy |

## Data profile

Internal project data throughout (`data-class: internal` for instances — this exemplar is `public` because it carries no real content). No customer PII expected; if a week's content includes any, stage 2's boundary escalates and the run is flagged.

## Layer-3 inventory

- Stage 2: candidate skill gap — a **status-signal gatherer** (Rovo agent: query Jira/Confluence for the week's delta). Likely `sp-` brief.
- Stage 3: candidate skill gap — a **report drafter** (prompt-file skill: digest → house report shape).
- Stages 1 and 4: human judgment, inline.

## Surfaces

Primary: team Confluence space, `Status Reports` page tree. Mirror: internal repo `flows/weekly-status-report/`.

## Open questions

- Does the Friday meeting want a delta-only view or a full-state view? (Changes stage 3's output shape — resolve before scaffolding.)
