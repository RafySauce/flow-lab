---
id: sp-comms-drafter
title: "Skill Primer Brief — Comms Drafter"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-11-07
updated: 2026-11-07
owner: operator
source: human+ai
generated-by: flow-foundry
data-class: public
related: ["[[comms-builder]]"]
---

# Skill Primer Brief — Comms Drafter

> Filed from a Layer-3 gap in the `comms-builder` flowspace
> (`flow-foundry/review-flowspaces/comms-builder/`), Stage 5 (Draft Messages).

## Purpose

Draft every message a comms run needs — one per segment per touchpoint —
from the operator's templates or plain defaults, filled only from cited
facts, so the requester edits rather than writes from scratch. Also usable
on its own for a quick one-off email.

## Triggering intent

- **Fires on:** `comms-builder` Stage 5; standalone on "draft an email to
  <group> about <thing>".
- **Does not fire on:** sending anything; executive status narratives
  (`executive-slide-drafter`); documentation pages (`doc-drafter`).

## Method sketch

- Choose the template by touchpoint kind and channel; operator
  `template-path` wins over the flow's `default-message-templates.md`.
- Fill only from the context sheet, audience map, and framing brief; mark
  every gap `[NEEDS INPUT: …]`.
- Subject leads with the action or date; first line says whether the reader
  must act; one ask per message; plain text, voice rules from the binding.
- Re-apply the response-plan data rule to every draft.
- Standalone mode: ask for the minimum (audience, subject, date, ask) and
  produce one draft.
- Failure modes: a filled-in date that no input supports; a security
  detail slipping into a response-plan update.

## Inputs and data boundary

Upstream work files or, standalone, the user's answers. Max `internal`.
Engine: Copilot (drafts land in chat for the user to paste into Outlook or
Teams).

## Demand source

`comms-builder` Stage 5 (`05-draft-messages/CONTEXT.md`).

## Definition of done

Every draft traces each date and action to an input; missing facts appear
as markers, never inventions; an operator template is used when present and
the default otherwise; a standalone run produces a usable email from four
answers.
