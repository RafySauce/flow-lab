---
id: sp-executive-slide-pptx-stylizer
title: "Skill Primer Brief — Executive Slide Pptx Stylizer"
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

# Skill Primer Brief — Executive Slide Pptx Stylizer

> Filed from a Layer-3 gap in the `executive-slide-digest` flow-primer-brief
> (`flow-foundry/backlog-flow-starters/fp-executive-slide-digest.md`), Stage 5
> (Stylize to .pptx). Directly modeled on the existing
> `accomplishments-docx-stylizer` skill, swapping Word/`.docx` for
> PowerPoint/`.pptx`.

## Purpose

Apply a house PowerPoint template/branding to Stage 4's human-approved slide
content and produce a final `.pptx` — replacing the manual work of copying
approved bullet content into a slide template and reformatting it by hand —
without introducing any content beyond what Stage 4 approved.

## Triggering intent

- **Fires on:** Stage 5 of `executive-slide-digest`, given Stage 4's approved
  content set (one initiative's slide content, or a portfolio-rollup deck
  outline).
- **Does not fire on (near-misses):** drafting or synthesizing content
  (that's `sp-executive-slide-drafter`); the final human review/share (Stage
  6 stays inline, human); any PowerPoint generation unrelated to this flow's
  specific content shape (a general-purpose "make me a deck" request is a
  different, engine-native capability, not this skill).

## Method sketch

1. Read Stage 4's approved content set, preserving the section structure
   from the house `executive-slide-shape.md` content shape — the deck must
   read as the same content in a different format, never re-authored. Every
   initiative/section present in the input must appear as its own slide (or
   slide group); dropping one to fit a layout is a defect.
2. Apply the target instance's house PowerPoint template if one exists:
   title slide, per-initiative slide layout, and typography consistent with
   the source shape (status color-coding for RAG, consistent bullet
   hierarchy). If no house template has been sourced yet — an
   instantiation-time asset this design does not assume exists — apply a
   concrete clean minimal default (one title slide, one slide per
   initiative, neutral accent color for RAG status, legible body type) and
   flag the missing house template as an explicit note on the title slide,
   rather than inventing branding.
3. For single-initiative scope: one content slide (plus a lightweight title
   slide naming the initiative and period). For portfolio-rollup scope: a
   title/agenda slide, one slide per initiative in the approved order, and
   the optional closing risks/asks rollup slide if Stage 4's approved
   content included one.
4. Known failure modes to guard against: silently dropping an initiative's
   slide, merging two initiatives onto one slide to save space, introducing
   bullet content not present in Stage 4's approved set, or guessing at
   house branding when no template has been sourced.

## Inputs and data boundary

Reads: Stage 4's approved content set; the target instance's house
PowerPoint template asset, if one has been sourced. Max `data-class:
internal` (inherits Stage 4's classification; pure formatting, no new
content sourced). Engine: Copilot only, matching the `accomplishments-docx-
stylizer` precedent — file generation of this kind is not a Rovo-native
action. No Rovo adapter.

## Demand source

`executive-slide-digest` flow-primer-brief, Stage 5 — flagged gap, see
`flow-foundry/backlog-flow-starters/fp-executive-slide-digest.md`.

## Definition of done

Against a seeded approved content set (a two-initiative portfolio rollup, one
Amber with a named risk, one Green with no risks, plus a closing rollup
slide), the skill produces a `.pptx` containing: a title/agenda slide, one
slide per initiative with correct RAG color-coding and all approved bullets
present, the closing rollup slide, no content beyond what the input
contained, and — with no house template configured for this test — the
clean minimal default applied with an explicit missing-template note on the
title slide.
