---
id: ai-refinement-stage-03
title: "Stage 03 — Scope & Dependencies"
type: stage-context
stage: 3
review-intensity: light
status: to-review
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
source: human+ai
data-class: internal
owner: rafael.torres
related:
  - "[[ai-refinement]]"
  - "[[skill-scope-dependency-mapper]]"
skill-dependency: skill-scope-dependency-mapper
skill-status: gap
---

# Stage 03 — Scope & Dependencies

## Inputs

| Input | Source | Required |
|---|---|---|
| Confirmed problem statement | Stage 02 | Yes |
| Confirmed business value | Stage 02 | Yes |
| Work item type + schema | Stage 01 | Yes |
| Active persona contract | Stage 01 | Yes |

## Process

> **⚠ SKILL GAP** — `skill-scope-dependency-mapper` does not yet exist.
> See `skill-demand/skill-scope-dependency-mapper-brief.md`.

When the skill is built, this stage will:

1. **Define in-scope** — based on the confirmed problem statement, enumerate what this work item explicitly covers.
2. **Define out-of-scope** — explicitly state what is excluded and why, to prevent scope creep.
3. **Identify dependencies** — classify each as:
   - **Blocking** — cannot proceed without resolution
   - **Informational** — awareness needed, no hard block
4. **Detect scope splitting** — if the in-scope list suggests multiple deliverables, recommend splitting into child items per the hierarchy.
5. **Identify risks** (optional for solution_epic) — flag technical, operational, or timeline risks.
6. **Confirm scope package** — present in-scope, out-of-scope, dependencies, and risks to user for approval.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Confirmed in-scope statement | Stage 04 | Plain text |
| Confirmed out-of-scope statement | Stage 04 | Plain text |
| Classified dependency list | Stage 04 | List with type tags |
| Risk list (if applicable) | Stage 04 | Plain text |
| Split recommendation (if triggered) | User decision | Advisory |

## Verify

- [ ] In-scope is specific and bounded
- [ ] Out-of-scope explicitly names at least one exclusion
- [ ] Every dependency is classified (blocking / informational)
- [ ] Scope-split detection was evaluated
- [ ] User explicitly confirmed the scope package
- [ ] No PII or confidential data introduced

## Review

**Intensity: Light** — scope and dependencies are confirmable with a quick pass if the problem framing in Stage 02 was solid.

Review owner: Human (Rafael or delegate)

## Data Boundary

- Dependency references may include internal system names or team names — `internal` classification.
- No external system credentials or connection strings in dependency descriptions.
