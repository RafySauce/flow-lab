---
id: sp-confluence-contribution-gatherer
title: "Skill Primer Brief — Confluence Contribution Gatherer"
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

# Skill Primer Brief — Confluence Contribution Gatherer

> Filed from a Layer-3 gap in the `accomplishments-digest` flowspace, Stage 3
> (Gather — Confluence & Collaboration).

## Purpose

Pull an engineer's authored/co-authored Confluence pages and available
collaboration signal (review comments, mentions) within a stated date range,
framed as scope/leadership evidence rather than a page-title list —
replacing the manual work of remembering which docs one wrote and digging
through page history.

## Triggering intent

- **Fires on:** Stage 3 of the `accomplishments-digest` flowspace, given a
  confirmed period from Stage 1; also standalone on "what docs did I write
  this quarter" or "pull my Confluence contributions for <period>."
- **Does not fire on:** drafting the final document (that's
  `sp-accomplishments-drafter`), gathering another person's contributions for
  evaluative purposes (out of scope), or general Confluence search/reporting
  unrelated to accomplishments framing.

## Method sketch

1. Query pages authored or substantially co-authored by the engineer within
   the date range.
2. Separately, where the platform exposes it, gather collaboration signal:
   review comments given, page mentions, cross-team contributions.
3. Group by initiative (mirroring the Jira gatherer's theme grouping) and
   frame each as scope or leadership evidence ("drove the design for X,"
   "wrote the postmortem that changed Y's on-call process"), not a bare
   page-title list.
4. Before presenting the collaboration-signal slice, check whether the
   target Confluence instance actually exposes comment/mention history at
   usable granularity. If not, narrow to authored-pages-only and say so
   explicitly — a known failure mode to guard against is presenting a thin,
   incomplete collaboration slice as if it were comprehensive.

## Inputs and data boundary

Confluence space access scoped to the engineer's own contributions; a date
range; the engineer's Confluence identity. Max `data-class: internal` — pages
may name co-authors or reviewers; the skill must not quote review comments in
ways that read as evaluating a colleague rather than the engineer's own work.
Engine: Rovo strongly preferred if the employer's sanctioned-tool matrix
requires Confluence-native access; confirm at instantiation whether a
Copilot-side integration is also sanctioned.

## Demand source

`accomplishments-digest` flowspace, Stage 3 — flagged gap, see
`flow-foundry/review-flowspaces/accomplishments-digest/03-gather-confluence/CONTEXT.md`.

## Definition of done

Against a seeded set of an engineer's authored pages spanning at least two
initiatives, plus a synthetic case where comment/mention history is
unavailable, the skill's output groups correctly by initiative, frames each
entry as scope/leadership evidence (not a title list), and correctly falls
back to an explicit "collaboration signal unavailable" note rather than
fabricating or overstating collaboration evidence in the unavailable case.
