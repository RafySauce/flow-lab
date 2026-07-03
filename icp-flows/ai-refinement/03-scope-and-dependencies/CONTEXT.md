---
id: ai-refinement-stage-03
title: "Stage 03 — Scope & Dependencies"
type: stage-context
stage: 3
review-intensity: light
artifact-version: "1.2"
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
  - "[[ai-refinement]]"
  - "[[scope-dependency-mapper]]"
  - "[[platform-stakeholder-register]]"
---

# Stage 03 — Scope & Dependencies

## Inputs

| Input | Source | Required |
|---|---|---|
| Confirmed problem statement | Stage 02 | Yes |
| Confirmed customer/business value | Stage 02 | Yes |
| Stakeholder tag list | Stage 02 | Yes |
| Work item type + schema | Stage 01 | Yes |
| Active persona contract | Stage 01 | Yes |
| Stakeholder register (coalitions, conflict axes, escalation rules) | `../reference/platform-stakeholder-register.md` | Yes |

## Process

`Layer-3: scope-dependency-mapper` (skill spec in
`produced-skills/scope-dependency-mapper/`, `verified`)

1. **Define in-scope** — based on the confirmed problem statement, enumerate what this work item explicitly covers.
2. **Define out-of-scope** — explicitly state what is excluded and why, to prevent scope creep.
3. **Identify dependencies** — classify each as:
   - **Blocking** — cannot proceed without resolution
   - **Informational** — awareness needed, no hard block
   Sweep the tagged stakeholders' *Adjacent* and *Constraint-setter* entries for
   dependencies the user hasn't named (integration seams and guardrails are
   where unstated dependencies live).
4. **Annotate coalition and conflict axes** — from the register: which coalition
   this item satisfies (batch those stakeholders' input; expect fast consensus)
   and which conflict axis it triggers. A triggered axis needs a named
   decision-owner and a recorded rationale before Stage 06 commits.
5. **Route unresolved conflicts** — per the register's escalation rules:
   producer ⟷ constraint-setter conflicts that can't settle peer-to-peer
   escalate to IT Leadership; "worth doing at all" conflicts escalate to
   Portfolio & Sourcing. Record the routing as an advisory, not a decision.
6. **Detect scope splitting** — if the in-scope list suggests multiple deliverables, recommend splitting into child items per the hierarchy.
7. **Identify risks** (optional for solution_epic) — flag technical, operational, or timeline risks, including any hard physical constraints surfaced by the register (e.g., Growth vs. Physical Limits).
8. **Confirm scope package** — present in-scope, out-of-scope, dependencies, annotations, and risks to the user for approval.
   For a `spike`, the confirmed scope package bounds the investigation: it
   informs `question_to_answer` and the exit criteria in Stage 04 rather than
   landing in schema fields (the spike schema carries none — see
   `../reference/work-item-schemas.md`).

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Confirmed in-scope statement | Stage 04 | Plain text |
| Confirmed out-of-scope statement | Stage 04 | Plain text |
| Classified dependency list | Stages 04, 06 | List with type tags |
| Coalition / conflict-axis annotations (+ decision-owner per triggered axis) | Stages 04, 06 | Tagged list |
| Risk list (if applicable) | Stage 04 | Plain text |
| Split recommendation (if triggered) | User decision | Advisory |
| Escalation routing (if a conflict is unresolved) | User decision | Advisory |

## Verify

Cross-stage trace: the in-scope statement must be derivable from Stage 02's
confirmed problem statement (no scope item without a corresponding problem
element), and every conflict-axis annotation must involve at least one
stakeholder from Stage 02's tag list — the failures these catch are scope creep
past the framed problem and conflict annotations invented without a tagged
party. Running these checks leaves a one-line result in the run's decision log.

- [ ] In-scope is specific and bounded
- [ ] Out-of-scope explicitly names at least one exclusion
- [ ] Every dependency is classified (blocking / informational)
- [ ] Coalition and conflict-axis annotations reference register entries
- [ ] Every triggered conflict axis has a named decision-owner or an escalation advisory
- [ ] Scope-split detection was evaluated
- [ ] User explicitly confirmed the scope package
- [ ] No PII or confidential data introduced

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — scope and dependencies are confirmable with a quick
  pass if the problem framing in Stage 02 was solid.
- **Evidence:** user confirmation of the scope package in-session and a one-line
  entry in the run's decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- Dependency references may include internal system names or team names —
  `internal` classification.
- No external system credentials or connection strings in dependency
  descriptions.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
