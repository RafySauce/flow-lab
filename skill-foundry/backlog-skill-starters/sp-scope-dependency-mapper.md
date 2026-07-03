---
id: sp-scope-dependency-mapper
title: "Skill Primer Brief — Scope & Dependency Mapper"
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
related: ["[[ai-refinement]]", "[[platform-stakeholder-register]]"]
---

# Skill Primer Brief — Scope & Dependency Mapper

## Purpose

Turn a confirmed problem statement and value context into structured in-scope,
out-of-scope, dependency, and risk outputs — annotated with the stakeholder
coalition the item satisfies and the conflict axis it triggers. Replaces scope
sections written as afterthoughts and dependencies discovered mid-build.

## Triggering intent

- **Fires on:** Stage 03 of the `ai-refinement` flowspace; "map the scope and
  dependencies for this item."
- **Does not fire on (near-misses):** eliciting the problem itself (that's
  `context-elicitation`), drafting the remaining schema fields (that's
  `field-refinement-cadence`), or portfolio-level prioritization — this skill
  scopes one work item, it doesn't rank the backlog.

## Method sketch

1. Scope boundary generation — derive in-scope and out-of-scope statements from
   the confirmed problem context.
2. Dependency classification taxonomy — every dependency is **blocking** (cannot
   proceed without resolution) or **informational** (awareness only); sweep the
   register's *Adjacent* and *Constraint-setter* entries for unnamed dependencies.
3. Coalition / conflict-axis annotation — per the register's usage rules: name
   the coalition the item satisfies (batch their elicitation) and the conflict
   axis it triggers; a triggered axis needs a named decision-owner and rationale.
4. Escalation routing — unresolved producer ⟷ constraint-setter conflicts route
   to IT Leadership; "worth doing at all" conflicts route to Portfolio & Sourcing.
   Routing is an advisory; the skill never decides the conflict.
5. Scope-split detection — recognize when in-scope covers multiple deliverables
   and recommend hierarchy decomposition.
6. Risk identification — technical, operational, timeline (optional for
   solution_epic), including hard physical constraints (e.g., Growth vs.
   Physical Limits is non-negotiable, not a tradeoff).

Known failure mode to guard: classifying every dependency as blocking (inflates
critical paths) or none (hides them) — the taxonomy exists to force the call.

## Inputs and data boundary

Reads Stage 02 outputs (problem statement, value, stakeholder tags), the
work-item schema, and the platform stakeholder register. Max data-class:
internal. Engines: both Rovo and Copilot.

## Demand source

`ai-refinement` flowspace, Stage 03 (Scope & Dependencies) — the source schema
requires `in_scope`, `out_of_scope`, and `dependencies` but provides no
dependency taxonomy, no split-detection protocol, and no risk framework. The
stage's `CONTEXT.md` carries this brief's id.

## Definition of done

- Every dependency in the output is classified blocking or informational.
- Detects when a single item's scope should split into children.
- Coalition and conflict-axis annotations resolve to register entries, and every
  triggered axis carries a decision-owner or an escalation advisory.
- Produced `in_scope`, `out_of_scope`, and `dependencies` fields pass Stage 05
  validation without rework.
