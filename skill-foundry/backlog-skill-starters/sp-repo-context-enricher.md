---
id: sp-repo-context-enricher
title: "Skill Primer Brief — Repo Context Enricher"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-07-08
owner: operator
source: human+ai
generated-by: flow-foundry
data-class: public
related: ["[[accomplishments-docx-finisher]]"]
---

# Skill Primer Brief — Repo Context Enricher

> Filed from a Layer-3 gap in the `accomplishments-docx-finisher` flowspace,
> Stage 1 (Receive & Enrich).

## Purpose

Given an already human-approved accomplishments document and an explicit,
narrow, pre-authorized repo/file-access scope, pull supporting evidence
(commits, PRs, linked docs, code ownership) that reinforces — but never
extends — what the document already claims, with every addition distinctly
flagged for a later human review.

## Triggering intent

- **Fires on:** Stage 1 of `accomplishments-docx-finisher`, given a handoff
  file with a stated authorized repo/file-access scope.
- **Does not fire on:** a handoff with a blank or ambiguous scope (treat as
  no access — ask, don't infer), gathering the original accomplishments
  content (that's the two gatherer skills upstream in
  `accomplishments-digest`), or adding any claim not already present in the
  handed-off document — that's scope creep this skill must refuse, not a
  variant of its normal operation.

## Method sketch

1. Parse the handoff's authorized scope; treat blank/ambiguous as zero
   access and surface a question rather than guessing.
2. Within scope only, search for evidence tied to themes/sections already in
   the source document — commits, PRs, linked design docs, ownership records.
3. Attach found evidence to the matching theme/section, each item distinctly
   flagged (never blended silently into the original prose).
4. Known failure mode to guard against: finding something genuinely
   noteworthy that isn't already claimed in the source document and adding
   it anyway. The correct move is a separate "out-of-scope finding" note for
   the engineer to consider for a *future* run, never an addition to this
   one.

## Inputs and data boundary

The handoff file's authorized scope, plus whatever repo/file access that
scope grants — bounded explicitly, never inferred from what looks relevant.
Max `data-class: internal`, and never higher than the handoff's own
classification. Engine: Copilot (the reason this stage is Copilot-side at
all — it needs repository/file access Rovo doesn't have in this pairing).

## Demand source

`accomplishments-docx-finisher` flowspace, Stage 1 — flagged gap, see
`flow-foundry/review-flowspaces/accomplishments-docx-finisher/01-receive-and-enrich/CONTEXT.md`.

## Definition of done

Against a seeded handoff (a source document, an authorized scope covering
two of three repo areas, and a genuinely noteworthy but out-of-scope finding
planted in the third area), the skill: adds evidence only from the two
in-scope areas, flags every addition distinctly, surfaces the third-area
finding as an out-of-scope note rather than an addition, and asks rather
than guesses when tested against a second seed with a blank scope field.
