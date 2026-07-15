---
id: sp-jira-accomplishments-gatherer
title: "Skill Primer Brief — Jira Accomplishments Gatherer"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-08
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
data-class: public
related: ["[[accomplishments-digest]]"]
---

# Skill Primer Brief — Jira Accomplishments Gatherer

> Filed from a Layer-3 gap in the `accomplishments-digest` flowspace, Stage 2
> (Gather — Jira).

## Purpose

Pull an engineer's closed/resolved Jira work within a stated date range and
turn it into a theme-grouped, outcome-framed digest — replacing the manual
work of scrolling a Jira activity view and re-writing ticket titles as
achievements by hand.

## Triggering intent

- **Fires on:** Stage 2 of the `accomplishments-digest` flowspace, given a
  confirmed period and engineer identity from Stage 1; also standalone on
  "pull my closed work for <period>" or "summarize what I shipped this
  quarter."
- **Does not fire on:** drafting the final document (that's
  `sp-accomplishments-drafter`), pulling another person's activity for
  evaluative purposes (out of scope — this skill gathers one's own record,
  not a manager building a review from someone else's tickets without their
  involvement), or open-ended Jira reporting unrelated to accomplishments
  framing (that's ordinary Jira/JQL use, not this skill).

## Method sketch

1. Query closed/resolved items where the engineer was assignee or primary
   driver, within the stated date range, across their known project(s)/board(s).
2. Cluster results by theme (feature area, initiative, problem domain) —
   not by issue type, sprint, or status.
3. For each theme, reframe from ticket titles/summaries to outcome language
   ("shipped X, which enabled Y") with ticket keys kept as traceable
   citations, not display text.
4. Flag any theme where result volume looks thin — a signal for the drafting
   stage to lean on narrative, not a gap to silently smooth over.
5. Known failure mode to guard against: treating ticket count as the
   headline metric. The digest is themes-with-outcomes; counts are backing
   evidence at most.

## Inputs and data boundary

Jira project/board access scoped to the engineer's own work; a date range;
the engineer's Jira account identity. Max `data-class: internal` — ticket
content may name other engineers as collaborators; the skill must not expand
scope to characterizing their individual performance. Engine: Rovo strongly
preferred if the employer's sanctioned-tool matrix requires Jira-native
access to keep this data inside Atlassian; confirm at instantiation whether
a Copilot-side Jira integration is also sanctioned.

## Demand source

`accomplishments-digest` flowspace, Stage 2 — flagged gap, see
`flow-foundry/review-flowspaces/accomplishments-digest/02-gather-jira/CONTEXT.md`.

## Definition of done

Against a seeded set of an engineer's closed tickets spanning at least three
themes and one deliberately thin theme (1–2 tickets), the skill's output
groups correctly by theme, reframes every item in outcome language (no bare
ticket-title copy), flags the thin theme explicitly, and every Stage-1
self-identified top item that maps to Jira work appears in the output or is
explicitly marked not found.
