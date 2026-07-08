---
id: sp-accomplishments-drafter
title: "Skill Primer Brief — Accomplishments Drafter"
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
related: ["[[accomplishments-digest]]"]
---

# Skill Primer Brief — Accomplishments Drafter

> Filed from a Layer-3 gap in the `accomplishments-digest` flowspace, Stage 4
> (Draft).

## Purpose

Synthesize a framing brief plus a Jira digest and a Confluence digest into
the house accomplishments-document shape — a single, theme-structured,
audience-matched, outcome-framed document ready for the engineer's own edit
pass, replacing the manual work of stitching three separate inputs into
readable prose.

## Triggering intent

- **Fires on:** Stage 4 of the `accomplishments-digest` flowspace, given all
  three of Stage 1's framing brief, Stage 2's Jira digest, and Stage 3's
  Confluence digest.
- **Does not fire on:** gathering the source digests (that's the two
  gatherer skills), the engineer's final review/edit pass (Stage 5 stays
  human, inline — this skill produces a draft, not a published document),
  or drafting any document that isn't shaped by this flow's three-input
  contract.

## Method sketch

1. Read all three inputs; do not draft from only the two digests — the
   framing brief's self-identified top items must get first placement or
   visible emphasis within their themes, not be folded in anonymously.
2. Structure output by theme/initiative (never "Jira" / "Confluence" as
   section headers — the reader shouldn't need to know the source tool).
3. Open each theme with outcome framing, then supporting detail; match
   overall length/detail to the framing brief's stated audience.
4. Carry forward every thin-coverage or signal-unavailable flag from the two
   digests as an explicit note — do not silently smooth over a gap.
5. Run the exclusion-list check: confirm nothing in the framing brief's
   exclusion list appears in the draft. Known failure mode to guard against:
   an excluded item resurfacing because it was mentioned inside a ticket or
   page the drafter pulled supporting detail from, not just the headline
   item itself.
6. Use the house shape at
   `flow-foundry/review-flowspaces/accomplishments-digest/reference/accomplishments-document-shape.md`
   as the structural template.

## Inputs and data boundary

The three Layer-4 working artifacts from Stages 1–3 of a single run. Max
`data-class: internal` (inherits the classification of its inputs; does not
independently query any external system). Engine: Rovo or Copilot — pure
synthesis of already-gathered material, so either engine sanctioned for
`internal` content is fine; no Atlassian-native-access constraint applies
here the way it does for the two gatherer skills.

## Demand source

`accomplishments-digest` flowspace, Stage 4 — flagged gap, see
`flow-foundry/review-flowspaces/accomplishments-digest/04-draft/CONTEXT.md`.

## Definition of done

Against a seeded run (a framing brief with a stated exclusion, a Jira digest,
a Confluence digest, at least one thin-coverage flag in each digest), the
drafted document: structures by theme not by source tool, gives the framing
brief's self-identified items visible emphasis, carries forward both
thin-coverage flags as explicit notes, and contains zero mentions of the
excluded item.
