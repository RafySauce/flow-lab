---
id: sp-process-decomposition
title: "Skill Primer Brief — Process Decomposition"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[ai-refinement]]", "[[value-decomposition]]", "[[bulk-child-creation]]", "[[documentarian]]"]
---

# Skill Primer Brief — Process Decomposition

> Intake path 1 for the skill-foundry: crystallized intent, written before
> authoring starts. Filed in `skill-foundry/backlog-skill-starters/` as
> `sp-process-decomposition.md`.

## Purpose

Given a parent-level work item (or a described operational rollout) whose
work is inherently repetitive, sequential, and procedure-driven —
OS/software patch waves, certificate or credential rotations,
decommissions, disaster-recovery/failover drills, infrastructure
migrations — proposes an ordered, dependency-linked set of children
grounded in an existing (or newly elicited) runbook or procedure, for user
review, before handing each accepted child onward exactly as
`value-decomposition` does. It is the second top-down entry into the
`ai-refinement` hierarchy, alongside (never instead of) `value-decomposition`:
where that skill tailors to adaptive, incremental, stakeholder-value-sliced
work (PMBOK 7's tailoring principle), this skill tailors to predictive,
plan-driven, sequence-driven work, using PMI/PMBOK practice — not the "Value
Delivery" deck — as its grounding model. It replaces the manual practice of
hand-transcribing a runbook into a flat, unordered pile of Jira tickets, and
retires `value-decomposition`'s own step-5 "technical/project-driven
framing" exception from having to carry this entire category of work as a
one-off per-child carve-out.

## Triggering intent

**Fires on** — Stage 01 of `ai-refinement`, when the user has selected a
parent-level type (`portfolio_epic`, `solution_epic`, `feature`) and frames
its work as a repetitive, sequential, operational rollout rather than a
value-sliceable initiative:

- "We need to patch these 40 servers over the next month."
- "Help me break down this OS upgrade."
- "Decompose this migration runbook into tasks."
- "Same steps across each environment — dev, staging, then prod."
- Any parent whose grounding content is, or points at, an existing runbook,
  playbook, or step-by-step procedure document.

**Does not fire on (near-misses):**

- **Ordinary value-shaped decomposition.** A portfolio/solution epic or
  feature whose children are genuinely distinguished by stakeholder outcome,
  not execution order — stays `value-decomposition`, unaffected.
- **A single technical/infra child amid an otherwise value-shaped set.**
  `value-decomposition`'s existing step-5 exception — electing a
  technical/project-driven framing for one child within a value-shaped
  decomposition — is unaffected and stays there. This skill fires when the
  *whole parent* is process-shaped, not when one sibling among value-shaped
  children happens to be technical. This is the load-bearing boundary line
  between the two skills; a decomposition pass with a mixed set (some
  value-sliced children, one infra child) is `value-decomposition`'s job,
  not this skill's.
- **An already-decided flat task list with no sequencing or runbook shape.**
  A spreadsheet or enumerated list where the user has already decided the
  items and their content — goes straight to `bulk-child-creation`, same as
  today; this skill decides *what the sequence and structure* should be, it
  doesn't take a settled, unordered set and create it.
- **Ongoing, unscoped operational work with no bounded pass to plan.** PMI's
  operations-vs-projects distinction: this skill scopes and plans one
  bounded cycle of a recurring operational process (e.g., "the Q3 patch
  cycle"), not an open-ended adoption of an ongoing operation into the
  backlog.
- **`story`/`task`/`spike`/`bug` as the parent of a pass.** Same floor as
  `value-decomposition` — decomposition below Feature isn't this skill's
  model either.

## Method sketch

1. **Confirm and locate the grounding runbook.** Restate the parent item's
   content, then ask for or locate the procedure it's grounded in: an
   attached document, a linked page, or a described sequence of steps. If no
   runbook exists, this skill does not author one — it names the gap and
   points at the `documentarian` flowspace to produce the procedure first,
   then resumes from here. Missing content is asked for, never invented.
2. **Identify the decomposition axes** (Practice Standard for Work Breakdown
   Structures — decomposition by phase and by area/responsible-unit): the
   *stage axis* — the runbook's own phases, typically something like
   pre-check → execute → verify → rollback-contingency — and, where the
   same stage sequence repeats across a population, the *area axis* —
   server group, region, environment, or responsible team (a wave/cohort
   structure).
3. **Apply the 100% Rule as a completeness check.** Every in-scope runbook
   step maps to a proposed child, and every proposed child cites the
   runbook step it came from — flag a runbook step with no child, and flag
   a child with no runbook grounding, symmetrically. This is this skill's
   direct analog to `value-decomposition`'s vertical-slice check: a
   structural correctness gate before the set goes to the user.
4. **Propose an ordered, dependency-linked set.** Horizontal, sequence-driven
   structure is *correct and expected* here — the direct opposite of
   `value-decomposition`'s vertical-only rule. Each child names its
   relationship to its predecessor(s) using PMI's Sequence Activities
   vocabulary: Finish-to-Start as the default (most runbook steps can't
   start until the prior one finishes), Start-to-Start or Finish-to-Finish
   where steps genuinely overlap, and a dependency class — mandatory (hard
   logic: can't verify before executing), discretionary (best-practice
   ordering, not a hard constraint), or external (e.g., a vendor-owned
   maintenance window).
5. **Rolling-wave-bound the set.** Apply progressive elaboration: decompose
   the imminent cohort/wave in full step-by-step detail; represent later
   cohorts only as a milestone (a named, zero-duration marker for that
   wave's planned completion), to be elaborated in its own follow-up pass
   closer to its start. This is this skill's PMI-native analog to
   `value-decomposition`'s MVP-bounding step — it bounds the proposal
   without needing a value or MVP framing at all.
6. **Technical/procedural framing by default, with a named rollback/
   contingency child per stage sequence.** Every child is worded
   technically/procedurally — reusing the wording `value-decomposition`
   already sanctions as an elected exception, but as this skill's default
   rather than a per-item election. Every stage sequence carries an
   explicit rollback/contingency child tied to its execute step, grounded
   in PMI risk-response planning rather than left implicit.
7. **Verification-based acceptance criteria per child.** An objectively
   checkable pass/fail condition tied to the runbook step (e.g., "patch
   level confirmed via `<command>`; service confirmed running"), not a
   stakeholder-value narrative. Acceptance criteria stays a hard schema
   gate for every child's own Band 2 run, identical to every other item in
   the pipeline — decomposition, of either kind, never relaxes it.
8. **Present the full ordered/cohort/milestone set together for user
   review.** Same verdict vocabulary as `value-decomposition`: accept all,
   edit some, reject some, or stop entirely ("not ready to plan this cycle
   yet") — a stop creates nothing. No child proceeds without an explicit
   verdict.
9. **Hand off accepted children onward.** Two destinations, the user's
   choice, same as `value-decomposition`: each accepted child's own Band 2
   run (Stage 02 onward), pre-seeded with the runbook's grounding content
   and its dependency/sequence position; or, offered (never selected) when
   the accepted set is large enough that N sequential runs would be
   disproportionate — typical for repetitive work, since repetition
   usually means volume — a single bulk creation pass via
   `bulk-child-creation`, with wave-completion milestones surfaced
   alongside the batch. This skill never sets a parent link and never
   commits anything to Jira itself, identical to `value-decomposition`.

### Known failure modes to guard against

- **Inventing runbook steps instead of citing or asking.** The 100% Rule's
  other direction — content with no source is exactly as damaging here as
  an uncovered step.
- **Collapsing the area × phase structure into a flat, unordered list** —
  losing the "same steps repeat per cohort" shape the whole method exists
  to preserve.
- **Forcing the persona-value-statement format onto procedural children**,
  or, conversely, silently reusing this skill's technical framing for a
  child that's actually value-shaped (that's `value-decomposition`'s
  territory).
- **Treating verification acceptance criteria, or the rollback/contingency
  child, as optional** because the work "isn't really value work."
- **Decomposing every future wave to full depth up front**, defeating
  rolling-wave planning's whole purpose and producing the same
  disproportionate-ceremony problem `bulk-child-creation` exists to solve
  on the volume side.

## Inputs and data boundary

Reads: the parent item's confirmed Stage 02–04 field values (or its
already-committed Jira content, via read-only lookup, when decomposing a
live item); the referenced runbook/procedure document (this skill's primary
grounding source, replacing the "Value Delivery" deck for this path —
read-only, never authored here); the work-item schema registry
(`reference/work-item-schemas.md`) for the hierarchy's parent→child map and
each child type's field set.

Max data-class: internal, matching the rest of the `ai-refinement`
pipeline. Runbooks for infrastructure/OS-level work are a higher-risk
carrier (credentials, internal hostnames, network topology may appear
inline) — the same data-class screen the rest of the pipeline applies runs
before runbook content is quoted or carried into any drafted child.

Engines: Rovo and Copilot, per the employer matrix — no engine-specific
constraint identified.

## Demand source

Raised directly in operator conversation, 2026-08-01: `ai-refinement`'s only
existing top-down decomposition path, `value-decomposition`, is built
entirely around the "Value Delivery" deck's model (persona value
statements, MVP thinking, vertical-only slicing) and already carries a
one-off escape hatch in its own method step 5 — an elected
"technical/project-driven framing... for work that is inherently
sequencing-heavy or infrastructural (software/OS upgrades, hardware design
breakdowns)" (`produced-skills/value-decomposition/SKILL.md`, step 5). That
exception confirms the gap has been recognized since the skill's first
build (2026-07-15) but only ever handled as a per-child carve-out, never as
its own path with its own sequencing/cohort model. This brief proposes
graduating that carve-out into a proper sibling skill, grounded in
PMI/PMBOK practice rather than an ad hoc model, so `value-decomposition` can
keep owning genuinely value-shaped work (including the rare single
technical child within it) while this skill owns the case where the whole
parent is process-shaped.

Flowspace gap: `icp-flows/ai-refinement/` — Stage 01 currently offers
exactly one top-down decomposition path and one bottom-up bulk-creation
path; nothing recognizes "this parent's work is a repeatable operational
procedure" as its own shape.

## Definition of done

1. A 100%-Rule test proves completeness both ways: a runbook step with no
   corresponding proposed child, and a proposed child with no runbook
   grounding, are both caught and reported — neither passes through
   silently.
2. A phase-×-area test (e.g., 4 stages × 3 waves) produces a correctly
   ordered, dependency-typed set — Finish-to-Start by default, other
   relationship types and dependency classes named where they apply — not a
   flat, unordered dump.
3. A rolling-wave test shows the imminent cohort decomposed to full step
   detail and a distant cohort collapsed to a milestone only — not both
   decomposed to the same depth.
4. No child is forced into persona-value-statement format; every stage
   sequence in a live test carries an explicit rollback/contingency child.
5. Verification-based acceptance criteria is present and enforced as a
   hard, unrelaxed gate for every child, identical to every other item in
   the pipeline regardless of which decomposition path produced it.
6. A mixed-shape test proves the boundary against `value-decomposition`'s
   step-5 exception holds: a decomposition with one technical child inside
   an otherwise value-shaped set routes through that exception, not this
   skill; a decomposition where the whole parent is process-shaped routes
   here.
7. The "no runbook exists" path is exercised in a live test and correctly
   stops or redirects toward `documentarian` rather than fabricating
   procedure steps to fill the gap.
8. A "not ready to plan this cycle yet" response is honored: the run stops
   cleanly with no children created, exactly as `value-decomposition`'s own
   stop verdict.

**Open item for the operator** (carried forward, not resolved by this
brief, same treatment as `sp-value-decomposition.md`'s own open item):
whether step-ordering needs a house extension to
`icp-flows/ai-refinement/reference/work-item-schemas.md` that can express
PMI's dependency typing (relationship type — Finish-to-Start default,
Start-to-Start/Finish-to-Finish where steps overlap; class —
mandatory/discretionary/external) as first-class fields, or whether native
Jira issue-links suffice with this skill simply naming the relationship/
class per link at Stage 06's `parent_mapping_confirmation` (or a
dependency-equivalent step alongside it). Also open: whether wave-completion
milestones are represented as a lightweight Jira artifact (e.g., a
zero-point tracking issue) or purely as this skill's own presentation-layer
concept with no Jira footprint — deferred to the skill-foundry build that
develops this brief into a full spec.
