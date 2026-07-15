---
id: sp-accomplishments-docx-stylizer
title: "Skill Primer Brief — Accomplishments Docx Stylizer"
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
related: ["[[accomplishments-docx-finisher]]"]
---

# Skill Primer Brief — Accomplishments Docx Stylizer

> Filed from a Layer-3 gap in the `accomplishments-docx-finisher` flowspace,
> Stage 2 (Stylize to Word).

## Purpose

Apply a house Word template/branding to an enriched accomplishments content
set and produce a final `.docx` — replacing the manual work of copy-pasting
Confluence content into Word and reformatting it by hand — while preserving
Stage 1's flagged-addition markers so the human reviewer can still tell what
was enriched versus original.

## Triggering intent

- **Fires on:** Stage 2 of `accomplishments-docx-finisher`, given Stage 1's
  enriched content set.
- **Does not fire on:** enriching content (that's `sp-repo-context-enricher`),
  the final human review/share (Stage 3 stays inline, human), or any
  Word-document generation unrelated to this flow's specific content shape.

## Method sketch

1. Read the enriched content set, preserving section/theme structure from
   `accomplishments-digest`'s house document shape
   (`flow-foundry/review-flowspaces/accomplishments-digest/reference/accomplishments-document-shape.md`).
2. Apply the target instance's house Word template if one exists; if not,
   fall back to a clean minimal default (consistent heading hierarchy, one
   accent color at most, legible body type) and flag the missing house
   template as a note rather than inventing house branding.
3. Carry Stage 1's flagged-addition markers into the output in a
   still-identifiable form (a distinct character style, or a trailing
   "Enrichment notes" appendix) — styling must never erase that
   traceability.
4. Known failure mode to guard against: producing visually polished output
   that silently drops a section, merges flagged additions into
   indistinguishable body text, or introduces content not present in the
   input.

## Inputs and data boundary

Stage 1's enriched content set; the target instance's house Word template
asset, if one has been sourced (instantiation-time dependency, not assumed
to exist in this design). Max `data-class: internal` (inherits Stage 1's
classification; pure formatting, no new content sourced). Engine: Copilot.

## Demand source

`accomplishments-docx-finisher` flowspace, Stage 2 — flagged gap, see
`flow-foundry/review-flowspaces/accomplishments-docx-finisher/02-stylize-to-word/CONTEXT.md`.

## Definition of done

Against a seeded enriched content set (three themes, two flagged additions,
no house template configured), the skill produces a `.docx` containing all
three themes, both flagged additions still identifiable as such, a note
about the missing house template, and no content beyond what the input
contained.
