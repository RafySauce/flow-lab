---
id: sp-audience-mapper
title: "Skill Primer Brief — Audience Mapper"
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
related: ["[[comms-builder]]", "[[platform-stakeholder-register]]"]
---

# Skill Primer Brief — Audience Mapper

> Filed from a Layer-3 gap in the `comms-builder` flowspace
> (`flow-foundry/review-flowspaces/comms-builder/`), Stage 3 (Audience Design).

## Purpose

Turn "tell the people affected by X" into named segments, each with what
changes for them, what they must do, whether they validate, and how they
are reached — so no group is missed and nobody gets a message that is not
theirs.

## Triggering intent

- **Fires on:** `comms-builder` Stage 3; standalone on "who needs to hear
  about this and what does each group need to know".
- **Does not fire on:** stakeholder mapping for requirements
  (`ai-refinement` Stages 02–03); a Kanban socialization plan
  (`statik-adoption` Stage 08); anything that needs named individuals.

## Method sketch

- Start from default segments — application owners, technical owners,
  business users — and keep, drop, split, or add against the affected
  services.
- Fill a per-segment view: what changes, action and due date, what to
  ignore, validates?, channel, question owner (shape in the flow's
  `reference/audience-segment-view.md`, descended from statik-adoption's
  per-group view).
- Ground against a stakeholder register when one exists; otherwise ask and
  mark "ungrounded".
- Identify segments by role, group, or distribution list — never a person.
- Failure modes: a generic all-hands segment that hides who must act; a
  validation need lost because nobody owns it.

## Inputs and data boundary

Framing brief and context sheet. Max `internal`. Engine: Copilot.

## Demand source

`comms-builder` Stage 3 (`03-audience-design/CONTEXT.md`).

## Definition of done

For a sample platform change, the skill produces three to five segments,
each with a concrete action or "nothing", correctly marks the validating
teams, contains no personal names, and asks rather than guesses when no
register exists.
