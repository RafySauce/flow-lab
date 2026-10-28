---
id: accomplishments-digest-stage-09
title: "Stage 09 — Word Output"
type: stage-context
stage: 9
review-intensity: light
artifact-version: "2.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-10-28
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[accomplishments-docx-stylizer]]"
  - "[[docx-minimal-default-style]]"
---

# Stage 9 — Word Output (`CONTEXT.md`)

> Optional, additional terminal stage. Stage 8 already produces a complete,
> published, human-approved document, and that publish does not wait on this
> stage. This stage runs only when the engineer also wants a styled Word
> version, for example for a promo packet. It replaces 1.x's "Handoff to
> Copilot" stage and the companion `accomplishments-docx-finisher` flow
> (operator decision 2026-10-27: Word styling is a skill, not a flow).

## Inputs

Stage 8's **published** accomplishments document. It never takes the Stage 7
pre-review draft, so only human-approved content ever gets styled. Stage 1's
framing brief is also an input (audience, exclusion list). Optionally, the
engineer supplies a Word template (`.dotx` or a styled `.docx`).

## Process

1. **Capability check.** Confirm that the running engine can produce a
   `.docx`. If it can't, say so plainly and stop. The published Stage 8
   document remains the deliverable, and the engineer can re-run this stage
   on an engine that can.
2. **Ask before stylizing.** Offer the engineer two choices:
   **build from the default style** (`../reference/docx-minimal-default-style.md`)
   or **use a template they provide**. Never pick silently.
3. **Stylize.** Apply the chosen style to the approved content. Styling
   only: no content is added, removed, or reworded, and section and theme
   order is preserved. If a provided template lacks a style the document
   shape needs, map it to the nearest style and list the mapping in an
   appendix. Don't invent branding.

`Layer-3: accomplishments-docx-stylizer` (2.0 revision, `to-review`, staged
in `skill-foundry/review-skills/accomplishments-docx-stylizer/`; until 2.0 passes the gate,
the verified 1.0 in `produced-skills/` applies with steps 1 and 2 run inline).

## Outputs

A **styled `.docx`** of the Stage 8 document, named
`<engineer>-accomplishments-<period>.docx`, with a style note in its
appendix (default or template, plus any style mappings). Lands in the run's
working folder and is shared by the engineer.

## Verify

A specific cross-stage trace check: the `.docx`'s headings and bullet count
match Stage 8's published document one-for-one, and nothing on Stage 1's
exclusion list appears. If they differ, styling changed the content: fix
and re-run. Result recorded as a one-line entry in the run's decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `light`. This is mechanical styling of already-approved content,
  with the content judgment already made at Stage 8. The engineer opens the
  `.docx` and confirms it reads the same before sharing.
- **Evidence:** the engineer's style choice (default or template) and the
  Verify result, both in the run's decision log.

## Data boundary

- **Max data-class this stage handles:** `internal` (inherits Stage 8's
  published document).
- **Sanctioned engines for this stage:** any engine sanctioned for
  `internal` content that can produce a `.docx`, decided at runtime by step 1.
  No longer locked to Copilot.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
