---
id: skill-field-refinement-cadence-brief
title: "Skill Primer Brief — Field Refinement Cadence"
type: skill-primer-brief
status: to-review
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
source: human+ai
data-class: internal
owner: rafael.torres
demanded-by: ai-refinement-stage-04
target-adapters: [rovo, copilot]
---

# Skill Primer Brief — Field Refinement Cadence

## What This Skill Does

Manages the one-field-at-a-time refinement cadence, including field ordering logic,
cross-field conflict detection, and acceptance criteria reframing.

## Why It's Needed

The source doc specifies `cadence.mode: one_field_at_a_time` and `confirm_each_step: true`
but provides no logic for:
- Which field to present first
- How to detect contradictions between fields (e.g., due date vs. blocking dependency)
- How to enforce and reframe acceptance criteria that don't match the approved starters

## Consuming Flowspace Stage

- `ai-refinement` → Stage 04 (Field-by-Field Refinement)

## Core Capabilities Required

1. **Field ordering logic** — determine the optimal sequence based on schema dependencies:
   - Summary first (anchors all other fields)
   - Acceptance criteria last (depends on scope, value, dependencies)
   - Remaining fields in dependency order
2. **Cross-field conflict detection** — identify contradictions:
   - Due date that precedes a blocking dependency's resolution date
   - In-scope claims that lack corresponding acceptance criteria
   - Type-of-work / work-category mismatches (feature only)
3. **AC starter reframing** — detect acceptance criteria that don't begin with
   "Must be able to" or "We will know this is done when" and rewrite them to match.
4. **Summary enforcement** — validate ≤ 10 words; propose rewrites that preserve
   meaning when exceeded.

## Acceptance Criteria

- Must be able to present fields in a dependency-aware order without user configuration.
- Must be able to detect at least 3 categories of cross-field conflict.
- We will know this is done when every refined work item has AC that match approved
  starters and a summary ≤ 10 words on first pass through Stage 05.

## Constraints

- Must respect `confirm_each_step: true` — never skip user confirmation.
- Must not introduce PII or confidential data.
- Must work on both Rovo and Copilot surfaces.
