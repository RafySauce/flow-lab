---
id: sp-accomplishments-docx-stylizer-revision
title: "Skill Primer Brief — Accomplishments Docx Stylizer 2.0 (Revision)"
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
related: ["[[accomplishments-digest]]", "[[accomplishments-docx-stylizer]]", "[[docx-minimal-default-style]]"]
---

# Skill Primer Brief — Accomplishments Docx Stylizer 2.0 (Revision)

> A revision of the verified `produced-skills/accomplishments-docx-stylizer`
> (1.0), demanded by `accomplishments-digest` 2.0, Stage 9 (Word Output).
> Intake record:
> `flow-foundry/backlog-flow-starters/fp-accomplishments-digest-m365-servicenow.md`.
> When this revision is built, the skill returns to `to-review` until it passes the gate again.

## Purpose

Style the engineer's approved accomplishments document as a `.docx`, called
directly from the digest flow. This replaces the retired
`accomplishments-docx-finisher` flow (operator decision D5: "Word styling
seems like it would be skill vs its own flow").

## Triggering intent

`accomplishments-digest` Stage 9, given Stage 8's published document.
"Make a Word version of my accomplishments." **Near-misses:** drafting or
editing content; adding evidence; styling documents of other shapes.

## Method sketch (changes from 1.0)

- **Input:** Stage 8's published document directly, replacing the
  finisher's "enriched content set with flagged additions." Drop the
  flagged-addition markers, because there is no enrichment step any more.
- **Capability check first:** confirm the running engine can write a
  `.docx`. If not, say so and stop. The published document stands.
- **Ask, never pick silently:** offer "build from the default style"
  (`accomplishments-digest/reference/docx-minimal-default-style.md` 1.1) or
  "use your own template." With a template, map the shape's elements to its
  styles, and list any mappings in the style note appendix.
- **Engine-agnostic:** remove the Copilot-only constraint.
- **Unchanged:** styling only, with no content added, removed, or reworded, and
  section order preserved.

## Inputs and data boundary

`internal`; any engine sanctioned for `internal` that can produce `.docx`,
decided at runtime.

## Demand source

`accomplishments-digest` 2.0, Stage 9; operator decisions D2 and D5.

## Definition of done

- The headings and bullet count of the `.docx` match the Stage 8 document.
- The style note appendix states which style was applied.
- The engineer was asked to choose between the default and a template.
- A simulated run with a template that lacks a heading style maps it and
  lists the mapping.
- An engine without `.docx` capability produces a clean stop, not a
  degraded file.
