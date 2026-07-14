---
id: sp-field-refinement-cadence
title: "Skill Primer Brief — Field Refinement Cadence"
type: skill-primer-brief
artifact-version: "1.1"
status: living
truth-level: verified
created: 2026-07-03
updated: 2026-07-07
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.1"
data-class: public
related: ["[[ai-refinement]]"]
---

# Skill Primer Brief — Field Refinement Cadence

## Purpose

Manage the one-field-at-a-time refinement cadence for a Jira work item: field
ordering, per-field drafting with explicit confirmation, cross-field conflict
detection, and acceptance-criteria reframing. Replaces "here's the whole ticket,
look it over" reviews where field-level problems hide.

## Triggering intent

- **Fires on:** Stage 04 of the `ai-refinement` flowspace; "walk me through the
  remaining fields one at a time."
- **Does not fire on (near-misses):** eliciting problem context
  (`context-elicitation`), scope/dependency mapping (`scope-dependency-mapper`),
  or final schema validation (`workitem-validation` — that skill gates, this one
  drafts). It also doesn't reorder or rewrite fields already confirmed upstream.

## Method sketch

1. Field ordering — summary first (anchors everything), acceptance criteria last
   (depends on all other fields), the rest in schema dependency order.
2. One field at a time — present name, constraints, and pre-filled upstream
   content; draft or refine; obtain explicit confirmation before advancing
   (`confirm_each_step: true` is non-negotiable).
3. Cross-field conflict detection — due date vs. blocking dependency timelines;
   in-scope claims without matching acceptance criteria; type-of-work /
   work-category consistency (feature only); conflict axis triggered upstream
   with no decision-owner recorded.
4. AC starter reframing — rewrite criteria that don't begin "Must be able to" or
   "We will know this is done when," preserving meaning.
5. Summary enforcement — ≤ 10 words; propose meaning-preserving rewrites.

Known failure mode to guard: batching several fields into one confirmation to
save turns — the cadence *is* the accountability mechanism.

## Inputs and data boundary

Reads confirmed Stage 02–03 outputs, the work-item schema, and the field
definitions (summary limit, AC starters) from the flowspace's reference doc.
Max data-class: internal. Engines: both Rovo and Copilot.

## Demand source

`ai-refinement` flowspace, Stage 04 (Field-by-Field Refinement) — the source doc
specifies `mode: one_field_at_a_time` and `confirm_each_step: true` but no
ordering logic, no conflict detection, and no AC-reframing protocol. The stage's
`CONTEXT.md` carries this brief's id.

## Definition of done

- Presents fields in a dependency-aware order without user configuration.
- Detects at least three categories of cross-field conflict.
- Every refined item reaches Stage 05 with AC matching approved starters and a
  summary ≤ 10 words on the first pass.
