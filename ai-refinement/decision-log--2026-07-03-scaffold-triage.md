---
id: decision-2026-07-03-scaffold-triage
title: "Decision Log — AI Refinement Scaffold Triage"
type: decision-log
created: 2026-07-03
source: human+ai
data-class: internal
owner: rafael.torres
---

# Decision Log — 2026-07-03 — Scaffold Triage

## Classification

**Input**: `AI-Refinement-Hybrid.md` (uploaded file)
**Classification**: Foreign material → primer-brief-shaped
**Rationale**: The document contains clear workflow intent with purpose, triggers, schemas,
guardrails, and a persona contract. It is structured enough to scaffold directly without
requiring an intermediate primer-brief step.

## Topology Decision

**Choice**: Two-band topology (Foundation + Per-Item Pipeline)
**Rationale**: Stage 01 (Intake & Guardrails) runs once per session and establishes the
trust boundary. Stages 02–06 form a repeatable pipeline that loops per work item.
The source doc's `triggers` and `guardrails` sections clearly separate session setup
from per-item work.

## Stage Breakdown

| Stage | Name | Intensity | Rationale |
|---|---|---|---|
| 01 | Intake & Guardrails | Heavy | Session trust boundary — guardrail miss cascades everywhere |
| 02 | Context & Problem Framing | Heavy | Problem framing errors cascade into every downstream field |
| 03 | Scope & Dependencies | Light | Confirmable with quick pass if Stage 02 was solid |
| 04 | Field-by-Field Refinement | Light | Each field is user-confirmed inline; review is consistency scan |
| 05 | Validation & Formatting | Light | Largely mechanical; review confirms report accuracy |
| 06 | Jira Commit & Close | Heavy | Commit boundary — incorrect payload creates real Jira artifacts |

## Layer-3 Triage

| Source content | Classification | Action |
|---|---|---|
| Guardrails YAML | Reference (inline) | Embedded directly in Stage 01 |
| Persona contract | Reference (inline) | Embedded directly in Stage 01 |
| Work item schemas | Reference (inline) | Embedded directly in Stage 01, referenced by 02–06 |
| Field definitions | Reference (inline) | Referenced by Stage 04 |
| Refinement workflow cadence | Gap | → `skill-field-refinement-cadence` |
| Context elicitation protocol | Gap | → `skill-context-elicitation` |
| Scope/dependency classification | Gap | → `skill-scope-dependency-mapper` |
| Validation protocol | Gap | → `skill-workitem-validation` |
| Jira API mapping | Gap | → `skill-jira-commit` |

## Skill Demand Generated

5 skill-primer-briefs filed in `skill-demand/`:
1. `skill-context-elicitation-brief.md`
2. `skill-scope-dependency-mapper-brief.md`
3. `skill-field-refinement-cadence-brief.md`
4. `skill-workitem-validation-brief.md`
5. `skill-jira-commit-brief.md`
