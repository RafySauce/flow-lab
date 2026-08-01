---
id: decision-2026-08-01-process-decomposition-brief
title: "Decision Log — Process Decomposition Brief (handoff, not built)"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[value-decomposition]]"
  - "[[bulk-child-creation]]"
  - "[[sp-process-decomposition]]"
---

# Decision Log — 2026-08-01 — Process Decomposition Brief (handoff, not built)

**What was decided:** capture a second top-down decomposition path for
`ai-refinement` — repetitive, sequential, procedure-driven work (OS/software
patch waves, credential/cert rotations, decommissions, DR/failover drills,
infra migrations) — as a skill primer brief,
`skill-foundry/backlog-skill-starters/sp-process-decomposition.md`. Nothing
was built: no skill spec, no Stage 01 wiring, no `work-item-schemas.md`
change. **By whom:** agent, on direct operator instruction, following a
conversation about adding a project-management output option for work that
doesn't fit `value-decomposition`'s value-delivery mindset. **What it
affects:** the new primer brief; this decision-log entry; a short gap-log
note in `HUB.md` pointing at the brief (no stage-table or wiring change).

## The gap this names

`value-decomposition` (`produced-skills/value-decomposition/SKILL.md`) is
`ai-refinement`'s only top-down decomposition path, and it is built entirely
around the operator-provided "Value Delivery" deck: persona value
statements, MVP thinking, the Hamburger Method's vertical-only slicing,
quarter-testable acceptance criteria. That model already carries a one-off
escape hatch in its own method step 5 — an elected "technical/
project-driven framing instead of the persona-statement format... for work
that is inherently sequencing-heavy or infrastructural (software/OS
upgrades, hardware design breakdowns)." The exception has existed since the
skill's first build (2026-07-15) and confirms the gap was already visible
then — but it was only ever handled as a per-child carve-out inside a
value-shaped method, never as its own path with its own sequencing/cohort
model.

The operator's framing in conversation: this work "doesn't fit the value
delivery mindset of value decomposition" — it's highly repetitive, sequenced,
and usually already has an associated runbook or documentation. That is a
different *shape* of work, not a harder instance of the same shape, and
PMI/PMBOK practice supplies a grounding model for it that doesn't require
forcing persona/MVP/vertical-slice language onto procedural steps.

## Scope and boundary decided

1. **A sibling skill, not an extension of `value-decomposition`.** The
   deciding factor mirrors the reasoning that split `bulk-child-creation` out
   from `value-decomposition` on 2026-07-31: the two skills solve genuinely
   different problems — deciding *what the children of a value-sliceable
   parent should be* versus deciding *how a known procedure decomposes into
   an ordered, dependency-linked set*. Bolting a second model onto
   `value-decomposition`'s single method would have made every step
   conditional on which framing applies.
2. **The boundary line is drawn at the whole-parent level.**
   `value-decomposition`'s existing step-5 exception keeps owning the case
   where *one* child within an otherwise value-shaped decomposition is
   technical. The new skill owns the case where the *whole parent* is
   process-shaped. This line is stated explicitly in both the near-miss list
   (new brief) and, when the new skill is eventually built, should be
   cross-referenced back into `value-decomposition`'s own boundary section so
   neither skill silently expands into the other's territory.
3. **Grounding source is PMI/PMBOK practice, not an ad hoc model.** Named
   explicitly in the brief: PMBOK 7's tailoring principle (as the rationale
   for two decomposition skills existing at all) and the predictive/adaptive
   life-cycle spectrum (as the license for horizontal/sequential children,
   the opposite of `value-decomposition`'s vertical-only rule); the Practice
   Standard for Work Breakdown Structures' decomposition-by-phase and
   decomposition-by-area, plus its 100% Rule, as the structural axes and
   completeness check; Sequence Activities / Precedence Diagramming Method
   dependency typing (Finish-to-Start default; mandatory/discretionary/
   external classes) as the vocabulary for the ordered set; rolling wave
   planning as the direct PMI-native analog to `value-decomposition`'s
   MVP-bounding step; risk-response planning as the source of the mandatory
   rollback/contingency child; milestones for cross-cohort visibility; and
   the lessons-learned practice as the mechanism that closes the loop back
   into the grounding runbook via `documentarian`, keeping this genuinely
   repeatable rather than re-derived each cycle. Full detail:
   `skill-foundry/backlog-skill-starters/sp-process-decomposition.md`.
4. **Operations vs. projects, stated as an explicit non-goal.** PMI's own
   distinction between a project (temporary, unique result) and operations
   (ongoing, repetitive) is used to bound the skill: it scopes and plans one
   bounded pass of a recurring operational process, it does not adopt an
   ongoing operation permanently, and it does not replace any separate
   change-management/ITSM system of record — where one exists, this skill's
   output feeds it rather than substituting for it.
5. **Scope now:** brief only, filed for a future skill-foundry build — no
   spec, no Stage 01 handoff wiring, no schema change. This mirrors exactly
   how `value-decomposition` itself was staged from the "Workstream B"
   section of `2026-07-15-provenance-and-planning-labels.md`: brief first,
   full `SKILL.md` and Stage 01 wiring later, as a separate, deliberate act.

## Assumptions (operator to confirm or amend)

The session that produced this brief was non-interactive — clarifying
questions on deliverable shape, placement relative to `ai-refinement`, and
output shape were asked and went unanswered. The brief proceeds on the
repo's own default conventions rather than a confirmed operator choice:

- **Placement:** a third Stage 01 conditional handoff, sibling to
  `value-decomposition` and `bulk-child-creation` — reusing the existing
  hierarchy/Jira machinery rather than a standalone flowspace outside
  `ai-refinement`. Amendment path: if repetitive/runbook work turns out not
  to want the Jira epic/feature/story hierarchy at all, this placement
  should be revisited before the skill-foundry builds a full spec.
- **Output shape:** sequenced Jira work items via the same `jira-commit`
  path every other `ai-refinement` output takes, not a standalone
  runbook/checklist artifact. Amendment path: if the operator's real need is
  closer to what `documentarian` produces (a durable procedure document with
  Jira items as a thin tracking layer), the brief's Method sketch would need
  rework before a build.
- **Dependency representation** (schema extension vs. native Jira
  issue-links) and **milestone representation** (a lightweight Jira artifact
  vs. presentation-layer only) are left as open items in the brief itself,
  not decided here — same treatment `sp-value-decomposition.md` gave its own
  open item on validation promotion.
