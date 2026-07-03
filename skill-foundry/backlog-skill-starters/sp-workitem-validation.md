---
id: sp-workitem-validation
title: "Skill Primer Brief — Work Item Validation"
type: skill-primer-brief
artifact-version: "1.1"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.1"
data-class: public
related: ["[[ai-refinement]]"]
---

# Skill Primer Brief — Work Item Validation

## Purpose

Run a completeness and constraint scan on a refined work item, apply the
formatting rules (no bold, no emojis), and produce a structured pass/fail
validation report with a clear auto-correct vs. halt boundary. Replaces
eyeball-only "looks done" checks before Jira commit.

## Triggering intent

- **Fires on:** Stage 05 of the `ai-refinement` flowspace; "validate this work
  item," "is this Jira-ready?"
- **Does not fire on (near-misses):** drafting or improving field content
  (that's `field-refinement-cadence` — this skill never touches meaning),
  committing to Jira (`jira-commit`), or validating flowspace/skill artifacts
  (that's the foundries' own validation checklists).

## Method sketch

1. Completeness scan — walk the schema's required-field list; every field
   non-empty and non-placeholder.
2. Constraint validation — summary ≤ 10 words; AC starters match approved
   patterns; due date valid and future; dependencies reference resolvable items.
3. Formatting pass — strip `**bold**`, remove emoji, normalize whitespace.
4. Auto-correct vs. halt decision tree — auto-correct (silent fix + log):
   formatting and minor whitespace; halt (surface to user): missing required
   fields, constraint violations, unresolved cross-field conflicts.
5. Validation report — per-field pass/fail, auto-corrections applied,
   halt-level issues requiring resolution.

Known failure mode to guard: "auto-correcting" content while fixing formatting —
the skill may change markup, never meaning.

## Inputs and data boundary

Reads Stage 04's refined field set, the work-item schema, the formatting rules
from the flowspace's reference doc, and any Stage 04 conflict report. Max
data-class: internal. Engines: both Rovo and Copilot.

## Demand source

`ai-refinement` flowspace, Stage 05 (Validation & Formatting) — the source doc
specifies `no_bold`, `no_emojis`, and `jira_ready: true` but no scan order, no
auto-correct/halt boundary, and no report format. The stage's `CONTEXT.md`
carries this brief's id.

## Definition of done

- Catches a missing required field and halts before Jira commit.
- Auto-corrects formatting without user intervention, logging every correction.
- No work item reaches Stage 06 with a formatting violation or missing required
  field.
