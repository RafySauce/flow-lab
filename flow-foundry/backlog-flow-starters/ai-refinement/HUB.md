---
id: ai-refinement
title: "AI-Augmented Refinement — Jira Work Item Pipeline"
type: flowspace
artifact-version: "1.4"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.1"
data-class: public
related:
  - "[[ai-refinement-hybrid]]"
  - "[[platform-stakeholder-register]]"
  - "[[work-item-schemas]]"
---

# AI-Augmented Refinement — Jira Work Item Pipeline

This flowspace produces high-quality, Jira-ready work items through disciplined,
step-by-step refinement with explicit confirmation and accountability at every
field boundary. The pipeline enforces the Technical Product / Service Owner
(TPSO) persona — prioritizing business and operational value, identifying risks
and dependencies, challenging incomplete requirements, and enforcing measurable
outcomes across the enterprise network infrastructure domain. Requirements are
grounded in the platform stakeholder register: every work item is tagged with
the stakeholders whose needs define it, the coalition it satisfies, and the
conflict axis it triggers (see `reference/platform-stakeholder-register.md`).

One run = one fully refined work item committed to Jira.

## Stage Flow Diagram

```mermaid
flowchart LR
    subgraph F["① Foundation — set once per session"]
        style F fill:#0f172a,stroke:#475569,stroke-width:1px,color:#e2e8f0
        S1["1. Intake &amp; Guardrails<br/>review: heavy"]:::heavy
    end
    subgraph P["② Per-Item Pipeline — repeats per work item"]
        style P fill:#0f172a,stroke:#475569,stroke-width:1px,color:#e2e8f0
        S2["2. Context &amp; Problem Framing<br/>review: heavy"]:::heavy
        S3["3. Scope &amp; Dependencies<br/>review: light"]:::light
        S4["4. Field-by-Field Refinement<br/>review: light"]:::light
        S5["5. Validation &amp; Formatting<br/>review: light"]:::light
        S6["6. Jira Commit &amp; Close<br/>review: heavy"]:::heavy
    end
    S1 --> S2 --> S3 --> S4 --> S5 --> S6
    S6 -.->|"next work item"| S2

    classDef heavy fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef light fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef gap   fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

> Stages 2–6 carry their true review-intensity colors: each stage's skill
> exists as an authored spec in `skill-foundry/backlog-skill-starters/` at
> `truth-level: to-review`, and the five-point review gate has had an agent
> pre-run (spec review, simulated live test per adapter on synthetic data,
> trigger check, collision check — all passing; evidence in both foundries'
> decision logs, 2026-07-03). None is `verified` yet — on-engine live tests
> and promotion to `completed-skills/` remain the operator's call. See Known
> gaps.

## Stage table

| # | Stage | Review intensity | Max data-class | Sanctioned engines | Layer-3 |
|---|---|---|---|---|---|
| 1 | Intake & Guardrails | heavy | internal | Rovo, Copilot | inline — guardrails, persona from `reference/ai-refinement-hybrid.md`; schemas from `reference/work-item-schemas.md` (registry for all five refinable types) |
| 2 | Context & Problem Framing | heavy | internal | Rovo, Copilot | `context-elicitation` (to-review, skill-foundry backlog) |
| 3 | Scope & Dependencies | light | internal | Rovo, Copilot | `scope-dependency-mapper` (to-review, skill-foundry backlog) |
| 4 | Field-by-Field Refinement | light | internal | Rovo, Copilot | `field-refinement-cadence` (to-review, skill-foundry backlog) |
| 5 | Validation & Formatting | light | internal | Rovo, Copilot | `workitem-validation` (to-review, skill-foundry backlog) |
| 6 | Jira Commit & Close | heavy | internal | Rovo, Copilot | `jira-commit` (to-review, skill-foundry backlog) |

## Topology

- **Band ① Foundation** (Stage 1): Set once per refinement session. The user
  triggers refinement, acknowledges responsibility, confirms data-safety
  guardrails, and selects the work-item type from the hierarchy.
- **Band ② Per-Item Pipeline** (Stages 2–6): Repeats for each work item in
  the session. A run through this band takes one work item from raw context to
  a committed Jira issue. The loop-back from Stage 6 to Stage 2 fires when the
  user says "refine another item."

## Common source inputs

Operator-observed taxonomy (2026-07-03) of the raw material that most often
starts a run. All four types arrive request-shaped or solution-shaped — they
state a task or an action, not a problem — so Stage 1 screens them against the
data-safety guardrail and Stage 2's elicitation recovers the underlying problem
and value rather than transcribing the request.

| # | Input type | Typical carrier | Handling notes |
|---|---|---|---|
| 1 | Email with a direct request for support | Email thread pasted or summarized into the session | Requester maps to a stakeholder-register entry — start the Stage 2 sweep there. Emails routinely carry names and addresses: strip them before the material enters the session (Stage 1 data-safety screen). |
| 2 | Vendor details on required actions | Vendor bulletin, advisory, or notice | Third-party material — vet before ingesting. Prescribed actions are solution-shaped: elicit the internal problem and value before accepting them as scope. Stated deadlines feed `due_date`. The vendor is not a register entry — tag the internal owning stakeholder. |
| 3 | Meeting minutes, notes, or summaries | Notes pasted into the session | Multi-topic and multi-voice — may yield more than one work item (one run through Band ② each). Separate decisions from discussion; strip attributions per the data-safety screen. |
| 4 | Directly stated requirement from an engineer | Chat message ("I need to go do x, y, z to help ABC") | Task-first: the stated x/y/z are candidate scope, not the problem statement. Map the named stakeholder (ABC) to the register; elicit the problem and value before accepting the task list. |

## Surfaces

- **Primary:** Confluence — `<space set at instantiation; confirm the Mermaid
  macro is installed per the setup questionnaire, else the hub page notes
  "diagram: see mirror">`
- **Mirror:** `<internal repo>` → `flowspaces/ai-refinement/`

This public copy is the sanitized *design*; instantiation happens in employer
tenancy per `methodology/mirroring-protocol.md`. At instantiation, add the
per-stage `work/` folders (Layer-4, transient) and the `handoffs/` folder —
they are deliberately absent from this design copy because they only ever hold
per-run content.

## Run procedure

1. The user speaks a trigger phrase ("Run AI Refinement", "Start Refinement",
   "I want to refine").
2. Stage 1 activates: guardrails are presented, responsibility is acknowledged,
   and the user picks a work-item type from the refinable set — Solution Epic,
   Feature, Story, Task, or Spike. (The full hierarchy is Portfolio Epic →
   Solution Epic → Feature → Story | Task | Spike → Sub-Task; portfolio epics
   and sub-tasks are out of refinement scope and get redirected — see
   `reference/work-item-schemas.md`.)
3. Stages 2–5 walk the user through the selected work-item schema one field at
   a time, confirming each before advancing. The TPSO persona challenges
   incomplete requirements and enforces measurable outcomes throughout; the
   stakeholder register drives whose needs are elicited (Stage 2) and which
   coalition/conflict-axis annotations the item carries (Stage 3).
4. Stage 5 validates completeness against the schema and applies formatting
   rules (no bold, no emojis).
5. Stage 6 presents the finished artifact for final human approval, then
   commits it to Jira. The user may loop back to Stage 2 for the next item
   or end the session.

Human inspects at every stage boundary — that's the method, not an
inconvenience.

## Known gaps

All five skills demanded by this flowspace's Layer-3 triage are authored,
staged in `skill-foundry/backlog-skill-starters/` at `truth-level: to-review`,
and have passed an agent pre-run of the five-point review gate (2026-07-03) —
evidence in `skill-foundry/decision-log/2026-07-03-ai-refinement-skill-gate-prerun.md`;
the flowspace's own validation-checklist pre-run is in
`flow-foundry/decision-log/2026-07-03-ai-refinement-validation-prerun.md`.
Remaining gap: the human half — on-engine live tests (the pre-run's simulated
invocations are not engine runs), instantiation-time surface checks, and
operator promotion / placement in `completed-skills/`.

| Skill (spec + adapters) | Primer brief | Target stage | Status |
|---|---|---|---|
| `context-elicitation` | `sp-context-elicitation` | 2 | to-review — pre-gate run passed |
| `scope-dependency-mapper` | `sp-scope-dependency-mapper` | 3 | to-review — pre-gate run passed |
| `field-refinement-cadence` | `sp-field-refinement-cadence` | 4 | to-review — pre-gate run passed |
| `workitem-validation` | `sp-workitem-validation` | 5 | to-review — pre-gate run passed |
| `jira-commit` | `sp-jira-commit` | 6 | to-review — pre-gate run passed |

Second gap (2026-07-03): the work-item schema registry
(`reference/work-item-schemas.md`) completes type coverage — the source
clipping defined only `solution_epic` and `feature`, leaving three of the five
selectable types unrunnable. The `story`, `task`, and `spike` schemas are
house-drafted at `to-review`: the operator ratifies the field sets (and the
two proposed spike fields, `question_to_answer` and `timebox`) and confirms
them against the real Jira project configuration at instantiation. Follow-up
on ratification: add the two spike fields to `jira-commit`'s custom-field list
as a 1.2 revision. Rationale and assumptions:
`decision-log/2026-07-03-work-item-schema-extension.md`.

## Reference material (Layer-3)

| Artifact | Location | Covers |
|---|---|---|
| AI Refinement — Hybrid Definition | `reference/ai-refinement-hybrid.md` (claimed clipping) | Guardrails, persona, hierarchy, source schemas (solution_epic, feature), workflow cadence, triggers |
| Work Item Schemas — Refinable Set | `reference/work-item-schemas.md` (to-review, house extension) | Schema registry for all five refinable types; story/task/spike extensions; portfolio_epic / sub_task out-of-scope declarations; extension field constraints |
| Platform Stakeholder Register | `reference/platform-stakeholder-register.md` (claimed clipping) | Stakeholder role-types, coalitions, conflict axes, escalation routing |
| Provenance spec | `methodology/provenance-spec.md` | Frontmatter rules for all artifacts |
| Governance & Audit | `methodology/governance-and-audit.md` | Gate requirements |
