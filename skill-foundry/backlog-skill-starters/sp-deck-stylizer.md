---
id: sp-deck-stylizer
title: "Skill Primer Brief — Deck Stylizer"
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
related: ["[[comms-builder]]", "[[executive-slide-digest]]", "[[executive-slide-pptx-stylizer]]", "[[design-system-binding]]"]
---

# Skill Primer Brief — Deck Stylizer

> Filed from a Layer-3 gap in the `comms-builder` flowspace
> (`flow-foundry/review-flowspaces/comms-builder/`), Stage 6 (Meeting Materials).
> Generalizes `executive-slide-pptx-stylizer` (staged in
> `skill-foundry/review-skills/`, to-review), which this brief does not
> change.

## Purpose

Turn approved deck content into a styled `.pptx` driven by a
**design-system binding** instead of a hard-coded house template, so every
flow that produces a deck — `comms-builder` now, `executive-slide-digest`
later — looks consistent and an operator swaps their design system by
editing one config, not a skill.

## Triggering intent

- **Fires on:** `comms-builder` Stage 6 with approved meeting deck content;
  later, `executive-slide-digest` Stage 5 once the operator decides to switch.
- **Does not fire on:** drafting deck content (the calling stage does
  that); styling emails or pages; a general "make me a deck" request.

## Method sketch

- Read the binding (flow reference `design-system-binding.md`; the contract
  moves into this skill when built): themes for present vs. read, type
  family, color roles, deck template path.
- Apply the deck template if set; otherwise build from the binding's tokens;
  otherwise fall back to the neutral default with a visible note.
- Never add, drop, or reword approved content; flag overflow instead of
  cutting.
- Check every text-on-fill pair at 4.5:1; status color always paired with a
  word.
- Failure modes: content drift during layout; a binding value that fails
  contrast silently used.

## Inputs and data boundary

Approved deck content (Markdown outline), binding config, optional `.pptx`
template. Max `internal`. Engine: Copilot.

## Demand source

`comms-builder` Stage 6 (`06-meeting-materials/CONTEXT.md`); generalization
requested by the operator (decision D2 option C, 2026-11-06).

## Definition of done

The same content styled under two different bindings produces two decks
that differ only in styling; the neutral default runs with no config; a
contrast-failing binding value is reported, not used; the content
round-trips with no change against the approved outline. A migration note
for `executive-slide-digest` Stage 5 is written but not applied.
