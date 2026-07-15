---
id: ai-refinement-stage-03
title: "Stage 03 — Scope & Dependencies"
type: stage-context
stage: 3
review-intensity: light
artifact-version: "1.4"
status: living
truth-level: verified
created: 2026-07-03
updated: 2026-07-15
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
| Selected mode (fast-track / full-interactive) | Stage 01 | Yes |
| Stakeholder-register grounding status (grounded / ungrounded) | Stage 01 | Yes |
| Stakeholder register (coalitions, conflict axes, escalation rules), if loaded | `../reference/platform-stakeholder-register.md` or a domain instance | If grounded |

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
   where unstated dependencies live) — grounded mode only; in ungrounded mode,
   ask the user directly what this item depends on and what depends on it.
4. **Annotate coalition and conflict axes.** If grounded: from the register,
   name the coalition this item satisfies (batch those stakeholders' input;
   expect fast consensus) and the conflict axis it triggers. If ungrounded
   (Stage 01's grounding check): ask the user directly whether any known
   parties or priorities are in tension over this item, and record what they
   say in the same shape (a named tension + a decision-owner) without
   pretending a coalition/axis taxonomy exists to draw from. **This step is a
   hard carve-out: it always runs interactively, in every mode.** Fast-track
   never extracts or skips it — a triggered axis needs a named decision-owner
   and a recorded rationale before Stage 06 commits, and that call is not one
   to infer from a document.
5. **Route unresolved conflicts** — per the register's escalation rules
   (grounded) or a direct question to the user about who should decide
   (ungrounded): producer ⟷ constraint-setter conflicts that can't settle
   peer-to-peer escalate to IT Leadership; "worth doing at all" conflicts
   escalate to Portfolio & Sourcing. Record the routing as an advisory, not a
   decision.
6. **Detect scope splitting** — if the in-scope list suggests multiple deliverables, recommend splitting into child items per the hierarchy.
7. **Identify risks** (optional for solution_epic and portfolio_epic) — flag technical, operational, or timeline risks, including any hard physical constraints surfaced by the register, where grounded (e.g., Growth vs. Physical Limits).
8. **Confirm scope package** — present in-scope, out-of-scope, dependencies, annotations, and risks to the user for approval.
   For a `spike`, the confirmed scope package bounds the investigation: it
   informs `question_to_answer` and the exit criteria in Stage 04 rather than
   landing in schema fields (the spike schema carries none — see
   `../reference/work-item-schemas.md`).

   **In fast-track mode:** steps 1, 2, 3, 6, and 7 (scope boundaries,
   dependencies, split detection, risks) may be drafted from the source
   material with citation, falling back to direct elicitation for anything
   not extractable with confidence. Steps 4 and 5 (coalition/conflict-axis
   annotation and escalation routing) never fast-track — see step 4's hard
   carve-out. In full-interactive mode this step is its own light-review
   checkpoint; in fast-track mode it folds into the Stage 03–05 consolidated
   checkpoint defined in Stage 05's Review section.

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
      (grounded) or the user's direct answer (ungrounded)
- [ ] Every triggered conflict axis has a named decision-owner or an escalation advisory
- [ ] Coalition/conflict-axis annotation (step 4) ran interactively regardless
      of mode — never fast-track-extracted or skipped
- [ ] Scope-split detection was evaluated
- [ ] If fast-track mode extracted any field, its source citation is in the
      transcript and the user confirmed it explicitly
- [ ] User explicitly confirmed the scope package
- [ ] No PII or confidential data introduced

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — scope and dependencies are confirmable with a quick
  pass if the problem framing in Stage 02 was solid. In full-interactive mode
  this is its own checkpoint; in fast-track mode it folds into the Stage
  03–05 consolidated draft-and-review checkpoint (see Stage 05's Review
  section, which is the canonical definition of that consolidation).
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
