---
id: sp-executive-slide-drafter
title: "Skill Primer Brief — Executive Slide Drafter"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-06
updated: 2026-08-06
owner: operator
source: human+ai
generated-by: flow-foundry
data-class: public
related: ["[[executive-slide-digest]]"]
---

# Skill Primer Brief — Executive Slide Drafter

> Filed from a Layer-3 gap in the `executive-slide-digest` flow-primer-brief
> (`flow-foundry/backlog-flow-starters/fp-executive-slide-digest.md`), Stage 3
> (Draft).

## Purpose

Synthesize Stage 2's gathered Jira/Confluence material and Stage 1's framing
into the house exec-slide content shape — replacing the manual work of a
manager rereading raw tickets and rewriting them into slide language by hand.
Its hardest job is the same discipline `accomplishments-drafter` already
enforces for a different audience: outcome first, ticket second, and a
defensible status call rather than a guessed one.

## Triggering intent

- **Fires on:** Stage 3 of `executive-slide-digest`, given Stage 2's gathered
  Jira/Confluence material and Stage 1's stated scope, audience, and framing.
- **Does not fire on (near-misses):** gathering the source material itself
  (Stage 2, inline native search — not this skill's job); the human
  align/approve pass (Stage 4 stays inline, human); drafting an individual
  contributor's own accomplishments for a performance review (that's
  `accomplishments-drafter` — different audience, different content shape,
  different unit of analysis: initiative status vs. one person's work).

## Method sketch

1. Read Stage 2's gathered material and Stage 1's framing (scope mode,
   audience, time period, any explicit ask). Determine scope mode
   (single-initiative vs. portfolio-rollup) before drafting — it decides
   whether the output is one slide's content or a deck outline.
2. For each initiative in scope, draft into the house shape: Title, Status
   (RAG + one-line why), Headline (business-outcome framed), Key
   accomplishments (2–4 outcome-first bullets), Risks/Blockers (0–3, omit
   the section if none), Upcoming milestones (1–3, dated), optional Ask.
3. **Outcome first, ticket second** — "Shipped X, which unblocks Y" beats
   "Closed 12 tickets in the Foo epic." Ticket counts are supporting
   evidence, never the headline. This is the same authoring discipline
   `accomplishments-document-shape.md` states for its own audience; apply it
   here for an executive audience instead of a performance-review one.
4. **The RAG call must be defensible from the gathered material** — a
   blocked dependency, a slipped due date, or an open critical bug drives
   Amber/Red; the drafted status line names which signal drove the call, so
   Stage 4's human reviewer can check it rather than take it on faith.
5. For portfolio-rollup scope, emit a deck outline: a title/agenda slide,
   one section per initiative in the shape above, and an optional closing
   slide rolling up risks/asks across initiatives.
6. **Gaps stay visible.** If Stage 2's material is thin for a given
   initiative (e.g., no recent activity found), say so in that initiative's
   content rather than padding it to look complete — a fabricated
   accomplishment or an invented milestone date is a worse failure than a
   visibly thin slide.
7. Known failure modes to guard against: reverting to ticket-listing under
   time pressure; asserting a RAG status the gathered material doesn't
   support; inventing a milestone date or metric not present in the source
   material; silently dropping the Risks section instead of omitting it
   deliberately when it's genuinely empty.

## Inputs and data boundary

Stage 2's gathered Jira/Confluence material; Stage 1's scope, audience, time
period, and framing; the house `executive-slide-shape.md` content-shape
reference (authored when `executive-slide-digest` is scaffolded, per that
flow's Layer-3 inventory). Max `data-class: internal` (inherits Stage 2's
classification — work-item content, no new external source touched). Engine:
Rovo, Copilot both — drafting from already-gathered material is not
engine-specific the way live search is.

## Demand source

`executive-slide-digest` flow-primer-brief, Stage 3 — flagged gap, see
`flow-foundry/backlog-flow-starters/fp-executive-slide-digest.md`.

## Definition of done

Against a seeded gather output covering two initiatives (one with a clear
blocker, one with clean recent progress and no risks), the skill produces
draft content for both in the house shape, with: the blocked initiative
correctly called Amber or Red with the blocking signal named, the clean
initiative's Risks section omitted (not shown empty), every accomplishment
bullet outcome-framed rather than ticket-framed, and no milestone date or
metric appearing that wasn't present in the seeded input.
