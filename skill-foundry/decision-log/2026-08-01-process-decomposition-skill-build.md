---
id: decision-2026-08-01-process-decomposition-skill-build
title: "Decision Log — process-decomposition Skill Build"
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
  - "[[process-decomposition]]"
  - "[[sp-process-decomposition]]"
  - "[[ai-refinement]]"
  - "[[value-decomposition]]"
  - "[[bulk-child-creation]]"
---

# Decision Log — 2026-08-01 — process-decomposition Skill Build

**What was decided:** build `process-decomposition` from the primer brief
filed the same day, and stage it in `review-skills/` at
`truth-level: to-review`, per `foundry-spec.md` §§2–4. **By whom:** agent, on
direct operator instruction ("let's build the skill starter in the
backlog"). **Triage classification:** skill-primer-brief — clean path. The
brief (`backlog-skill-starters/sp-process-decomposition.md`) already carried
crystallized Purpose, Triggering intent, a nine-step Method sketch, known
failure modes, inputs/data boundary, and a Definition of done; this build
transcribes it into the engine-neutral spec and adapters without re-opening
the exploration recorded in
`icp-flows/ai-refinement/decision-log/2026-08-01-process-decomposition-brief.md`.

The brief stays in `backlog-skill-starters/` as the intake record, per
`foundry-spec.md` §4 — it moves to `completed-skill-starters/` only at
promotion, alongside the skill itself. This log records the build decisions
only; the flowspace-side rationale for the gap this skill closes lives in
the flowspace decision log linked above.

## Build decisions

1. **Scope held to the foundry's own job.** This pass authors the spec,
   adapters, and staging move (`foundry-spec.md` §§2–4) and stops there. It
   does **not** wire a third Stage 01 conditional handoff into
   `icp-flows/ai-refinement/01-intake-and-guardrails/CONTEXT.md` or `HUB.md`
   — that flowspace-side wiring is a distinct act, and precedent supports
   treating it as one: `value-decomposition` itself was built 2026-07-15 and
   sat unwired in Stage 01 for two weeks before the wiring gap was closed
   separately on 2026-07-30 (the flowspace's own "Ninth gap"). Wiring
   `process-decomposition` into Stage 01/HUB.md — a third branch alongside
   `value-decomposition` and `bulk-child-creation` in step 7's decomposition
   handoff, plus a stage-table and Known-gaps entry — is flagged as the next
   owed step, not performed here.

2. **The spec carries the near-miss it is most likely to fail**, same
   house practice as `bulk-child-creation`'s build: the boundary against
   `value-decomposition`'s own step-5 exception is stated in both
   Triggering intent's near-misses and the "What this skill is not"
   section, because it is the one line a careless build could blur — one
   technical child in a value-shaped set stays `value-decomposition`'s job;
   a whole process-shaped parent is this skill's.

3. **Both of the brief's open items resolved now, not left open.** The
   brief explicitly deferred "whether step-ordering needs a house extension
   to `work-item-schemas.md`... or whether native Jira issue-links
   suffice" and "whether wave-completion milestones are represented as a
   lightweight Jira artifact... or purely presentation-layer" to "the
   skill-foundry build that develops this brief into a full spec" — i.e.,
   this one. Resolved both toward the lighter-weight option:
   - **Dependencies: native Jira issue-links, no schema extension.** The
     skill names the relationship type (Finish-to-Start default,
     Start-to-Start/Finish-to-Finish where steps overlap) and dependency
     class (mandatory/discretionary/external) per link; Stage 06's
     `parent_mapping_confirmation` (or a dependency-equivalent step
     alongside it) remains the only mechanism that creates the link, same
     division of labor as the parent link itself. Rejected alternative: a
     first-class `dependency_type`/`dependency_class` field pair on the
     registry, by analogy to `spike`'s `question_to_answer`/`timebox`
     extension — rejected because it would require operator ratification
     and a Jira project-configuration check *before* this skill could even
     be tested, and `work-item-schemas.md`'s own derivation rule 3 already
     establishes that dependency *links* don't require a dependency *text
     field* for any other type in the registry (`solution_epic` is the one
     exception, and only because the source schema made it one).
   - **Milestones: presentation-layer only, no Jira footprint.** A
     wave-completion milestone lives in this skill's proposal and the
     handoff context, never as a created Jira artifact. Rejected
     alternative: a zero-point tracking issue — rejected for the same
     reason as above (no registry entry exists for a milestone type, and
     inventing one is a schema-authority decision this skill's own
     boundary list explicitly disclaims) and because it would mean the
     skill commits something to Jira, breaking the "never commits anything
     itself" invariant it otherwise shares word-for-word with
     `value-decomposition`.
   - Both are logged as reversible defaults, not permanent rulings — if the
     operator's on-engine review finds native issue-links or
     presentation-only milestones insufficient, that becomes a registry
     change proposed through the normal ratification path, not a silent
     skill-side workaround.

4. **Collision check, run at authoring time — one sibling touched.**
   `value-decomposition`'s "What this skill is not" gained a new entry
   ("Not the process decomposer") stating the same whole-parent-vs.-single-
   child line from the other direction, its own boundary otherwise
   untouched (step 5's exception is explicitly reaffirmed, not narrowed).
   Bumped 1.1 → 1.2 and both adapters regenerated with a matching refusal
   case — the same pattern `bulk-child-creation`'s build used on
   `jira-commit` (1.9 → 1.10) the day it was built, done here at staging
   time rather than deferred to promotion, per the operator instruction
   captured in the brief's own decision log that this cross-reference
   "should be" added "when the new skill is eventually built."
   `bulk-child-creation` and `documentarian` were checked and need no
   change: the former's boundary already reads "a set that already arrived
   decided" broadly enough to cover a flat procedural list without
   amendment; the latter is only ever a redirect target here (`this skill
   does not author a runbook`), never a peer with overlapping territory.

5. **Adapters add format, not logic.** Both are mechanical translations of
   the nine Method steps plus the "Dependency and milestone representation"
   sub-section. Rovo and Copilot both carry the same refusal set — declining
   into `value-decomposition`, `bulk-child-creation`, or the Band 2/Jira
   Commit/validation skills as appropriate — matching `value-decomposition`'s
   own adapters' refusal-list pattern rather than inventing a new shape.

## Five-point gate — status

Not run. Per `foundry-spec.md` §5 the gate is the operator's, and this build
stops at staging. Owed for promotion:

1. **Spec review** — purpose, triggering intent (including the near-misses),
   boundaries, review criteria, and Flow Diagram one-for-one with Method
   prose, with Mermaid rendering confirmed on GitLab.
2. **Live test per adapter** on `public`/synthetic data — a synthetic
   runbook with an explicit phase × area shape (e.g., 4 stages × 3 waves)
   would exercise the 100%-Rule check, the rolling-wave split, and the
   rollback-child requirement in one pass; a second run with no runbook
   supplied would exercise the `documentarian` redirect.
3. **Trigger check** — fires on a process-shaped whole parent; does *not*
   fire on ordinary value-shaped decomposition, a single technical child
   inside a value-shaped set, a flat already-decided list, or an
   open-ended unscoped operation.
4. **Boundary/collision check** — re-verified against `value-decomposition`
   1.2's new cross-reference and `bulk-child-creation`'s unchanged boundary.
5. **Promotion** — moving the folder to `produced-skills/`, moving the
   primer brief to `completed-skill-starters/`, and bumping both to
   `verified`. Stage 01/HUB.md wiring (build decision 1, above) is a
   separate, still-owed act, whether it happens before or alongside
   promotion.

Nothing here has run on-engine.
