---
id: skill-scope-dependency-mapper-brief
title: "Skill Primer Brief — Scope & Dependency Mapper"
type: skill-primer-brief
status: to-review
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
source: human+ai
data-class: internal
owner: rafael.torres
demanded-by: ai-refinement-stage-03
target-adapters: [rovo, copilot]
---

# Skill Primer Brief — Scope & Dependency Mapper

## What This Skill Does

Takes a confirmed problem statement and value context, then produces structured
in-scope, out-of-scope, dependency, and risk outputs for Jira work items.

## Why It's Needed

The source doc's schema requires `in_scope`, `out_of_scope`, and `dependencies` as
required fields, but provides no taxonomy for dependency classification, no protocol
for detecting when scope should be split into child items, and no risk identification
framework.

## Consuming Flowspace Stage

- `ai-refinement` → Stage 03 (Scope & Dependencies)

## Core Capabilities Required

1. **Scope boundary generation** — derive in-scope and out-of-scope statements from
   confirmed problem context.
2. **Dependency classification taxonomy**:
   - **Blocking** — work cannot proceed without resolution
   - **Informational** — awareness needed, no hard block
3. **Scope-split detection** — recognize when in-scope covers multiple distinct
   deliverables and recommend hierarchy decomposition per the work item hierarchy.
4. **Risk identification** — flag technical, operational, and timeline risks
   (optional for solution_epic, not required for feature).

## Acceptance Criteria

- Must be able to classify every dependency as blocking or informational.
- Must be able to detect when a single work item's scope should be split into children.
- We will know this is done when the skill produces in_scope, out_of_scope, and
  dependencies fields that pass Stage 05 validation without rework.

## Constraints

- Must respect the persona's `identify_risks_and_dependencies` behavior.
- Must not introduce PII or confidential data.
- Must work on both Rovo and Copilot surfaces.
