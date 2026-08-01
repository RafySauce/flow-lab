---
id: decision-2026-08-01-statik-adoption-skill-batch
title: "Decision — STATIK Adoption skill batch: build calls and collision resolution"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related:
  - "[[statik-adoption]]"
  - "[[decision-2026-08-01-statik-adoption-triage-and-scaffold]]"
---

# Decision — STATIK Adoption skill batch

## Context

Six skill-primer-briefs were filed by the `statik-adoption` flow-foundry pass and
built in the same session at operator instruction. All six are intake path 1
(clean path — crystallized intent from the flow-foundry's Layer-3 gap triage), so
no foreign-material vetting applied.

Built and staged in `review-skills/` at `truth-level: to-review`:
`fitness-and-dissatisfaction-profiler`, `demand-profiler`,
`flow-capability-analyzer`, `workflow-modeler`, `class-of-service-designer`,
`kanban-system-designer`. Each carries `SKILL.md` plus Copilot and Rovo adapters
generated from spec version 1.0.

## Decisions

### 1. Six skills, not eight — Stage 08 stays inline and Stage 01 reuses

Two of the flowspace's eight stages deliberately produced no skill:

- **Stage 01** reuses `jira-portfolio-ingest` for board binding. It already binds
  live Jira or an export, emits a normalized item set with a field-availability
  report, screens data class before typing further, and halts rather than
  auto-accepting a field map. Rebuilding it would be a collision, and the
  service-framing logic around it is genuinely flowspace-specific.
- **Stage 08** (socialization and rollout) is an inline one-off. STATIK step 8 is
  a human negotiation whose structure is specific to *this* design being
  socialized; no other flowspace would invoke it as a capability. Per
  `foundry-spec.md` §1 case 3, a capability with no reuse is not skill-worthy, and
  its structure lives as flowspace reference material instead.

### 2. Collision resolution: `demand-profiler` against `portfolio-profiler`

The sharpest collision risk in the batch — both count things on a Jira board. The
boundary is the **unit of analysis and the time dimension**, and both skills'
descriptions state it in both directions:

| | `portfolio-profiler` | `demand-profiler` |
|---|---|---|
| Unit | The item | The work item *type* |
| Question | What is in the backlog now, how well-formed? | What arrives, how often, how evenly? |
| Time | Point-in-time | Longitudinal |
| Purpose | Triage | System design |

Resolved by boundary redraw rather than merge: the two answer different questions
and a merged skill would serve neither. Both `SKILL.md` "What this skill is not"
sections name the other explicitly.

### 3. Collision resolution: `fitness-and-dissatisfaction-profiler` against
`context-elicitation`

Same technique family (structured elicitation), different altitude:
`context-elicitation` frames one *work item*'s problem context into schema-ready
fields for `ai-refinement`; this profiles one *service*'s standing fitness. Stated
in both directions. `context-elicitation` was not modified.

### 4. Collision resolution: `workflow-modeler` against `process-decomposition`

The most likely misroute in the batch, because the vocabulary overlaps almost
completely — phases, sequence, dependencies, states. The unit does not:
`process-decomposition` sequences steps *within one work item's execution*,
grounded in a runbook; `workflow-modeler` models the states *every item of a type*
passes through. Named explicitly in `workflow-modeler`'s near-misses.

Note: `process-decomposition` is itself still at `to-review` in `review-skills/`,
so neither skill in this pair has been gated. The boundary is stated but untested.

### 5. Two constraints written into every skill that touches them, not assumed

- **No per-person flow metric.** `demand-profiler` and `flow-capability-analyzer`
  both carry it as a data-boundary constraint with a stated refusal, and
  `kanban-system-designer` propagates it into the *designed system*'s metric set
  so whoever configures the board inherits it. The reasoning is stated once per
  skill rather than cross-referenced: individual flow metrics turn a Kanban
  rollout into performance management, which ends the honest reporting the
  dissatisfaction elicitation depends on.
- **Measured and estimated figures never share a column.** Carried by
  `demand-profiler` and `flow-capability-analyzer`, both of which produce figures
  in mixed-evidence runs.

### 6. Every skill is read-only

No skill in the batch has a write path, including `kanban-system-designer`, which
produces a board design but does not configure a board. This mirrors the
flowspace's own boundary and is stated in each skill's boundary section and each
Rovo adapter's permitted-actions block.

### 7. The five-point gate has **not** been run

Unlike the `ai-refinement` batch (2026-07-03), no agent-side gate pre-run was
performed here — no spec review pass, no simulated live test per adapter, no
trigger check, no boundary/collision check beyond the three resolutions recorded
above. **All five gate points remain outstanding for all six skills**, along with
deployment.

This is stated plainly rather than implied by the `to-review` status, because the
`ai-refinement` precedent means a reader could reasonably expect a pre-run to
accompany a batch build. There is none. The operator runs the gate.

## Follow-ups for the operator

1. **Run the five-point gate** on all six skills. The `Review criteria` section of
   each `SKILL.md` is written to be the live-test gate directly.
2. **Resolve the history delta** on `jira-portfolio-ingest` (triage log §7) —
   `flow-capability-analyzer`'s residency output depends on it, and through it
   every WIP limit's status as derived rather than tuned.
3. **Ratify the sufficiency floors** in the flowspace's
   `board-evidence-requirements.md` §3 before the first live run.
4. **`produced-skills/CONTEXT.md` has drifted** — 25 skill folders, 13 catalog
   rows. Flagged in the triage log; the catalog is operator-owned.
