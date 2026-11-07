---
id: sp-comms-plan-builder
title: "Skill Primer Brief — Comms Plan Builder"
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
related: ["[[comms-builder]]", "[[sp-deck-stylizer]]"]
---

# Skill Primer Brief — Comms Plan Builder

> Filed from a Layer-3 gap in the `comms-builder` flowspace
> (`flow-foundry/review-flowspaces/comms-builder/`), Stage 4 (Comms Plan & Timeline).

## Purpose

Lay a campaign's touchpoints against its key date, produce a validation
tracker, and draw the timeline as a Mermaid gantt (rendered image plus raw
source) whose colors carry meaning — replacing the hand-built spreadsheet
and slide that usually stand in for a comms plan.

## Triggering intent

- **Fires on:** `comms-builder` Stage 4 (campaign lane); standalone on
  "build a comms timeline for this change".
- **Does not fire on:** project schedules or delivery roadmaps; a one-off
  message; exec status decks.

## Method sketch

- Apply the default touchpoint set for the comms type (flow reference
  `comms-types-and-lanes.md`), then adjust with the user.
- Each touchpoint: date, segments, channel, sender, draft id.
- Build the validation tracker from segments marked "validates".
- Write the gantt per `timeline-and-validation-tracker.md`, mapping states
  to the design-system binding's color roles; add a legend; pair each color
  with a word.
- Render to an image with the engine's own capability; always keep the raw
  Mermaid; produce a table fallback for Jira and non-rendering surfaces.
- Failure modes: a touchpoint with no draft id; a key date that disagrees
  with the source record; color as the only status signal.

## Inputs and data boundary

Framing brief, context sheet, audience map, binding config. Max `internal`.
Engine: Copilot. Open question: whether the operator's Copilot can render
Mermaid to an image; if not, raw plus table is the output.

## Demand source

`comms-builder` Stage 4 (`04-comms-plan-and-timeline/CONTEXT.md`).

## Definition of done

For a sample change-implementation campaign, the gantt parses, the key
window matches the source record date, every touchpoint has a draft id,
the tracker lists every validating segment, and swapping the binding's
color roles changes the gantt colors without editing the plan.
