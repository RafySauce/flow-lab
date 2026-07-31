---
id: decision-2026-07-29-portfolio-rationalization-dictionary-inference-and-pivot
title: "Decision Log — Portfolio Rationalization: Dictionary Inference, Confirmation Gate, and Current-State-Analysis Pivot"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-29
updated: 2026-07-29
owner: operator
source: human+ai
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[portfolio-rationalization-stage-03]]"
  - "[[portfolio-rationalization-stage-03p]]"
  - "[[objective-dictionary-template]]"
  - "[[close-score-model]]"
  - "[[decision-2026-07-28-portfolio-rationalization-triage-and-scaffold]]"
---

# Decision Log — 2026-07-29 — Portfolio Rationalization: Dictionary Inference, Confirmation Gate, and Current-State-Analysis Pivot

**What was decided:** soften Stage 03's hard halt into a tiered resolution —
attempt inference, gate it behind explicit operator confirmation, and pivot
to a new terminal deliverable (Stage 3P, Current State Analysis) rather than
halting when nothing gets confirmed. **By whom:** the operator — explicit
instruction this session (`AGENTS.md` rule 2 / `foundry-spec.md` §1 Step 0).
This remains foundry revision work on a `to-review` design; nothing is
promoted, and nothing has run on-engine.

## Reconciling with 2026-07-28's decision #1

That entry recorded a deliberate call: "Stage 03 accordingly carries a hard
dependency it cannot degrade around: with no dictionary, it halts rather
than inferring objective areas, because an agent that invents them produces
confident, plausible, worthless mappings."

**What stays true:** an agent must never invent an objective area and have
it become load-bearing without a human standing behind it. That guarantee is
unchanged and this decision does not weaken it.

**What changes:** the *shape* of what happens when no dictionary exists.
Decision #1 treated absence as a dead end (halt). This decision treats it as
a fork: attempt to earn a dictionary through inference plus an explicit
human confirmation gate — which preserves the original guarantee, since
nothing invented becomes load-bearing without the operator owning it — and
if that fork also fails, do honest, lower-claim descriptive work (the
Current State Analysis) instead of nothing. The prior halt was a reasonable
default when the only alternative was silent invention; a confirmed-or-else
gate removes that tradeoff.

## Changes made

1. **`03-objective-mapping/CONTEXT.md`** — step 3's flat halt replaced with
   three tiered steps (attempt inference → present for confirmation → pivot
   if unconfirmed and no dictionary exists), with the rest of the process
   renumbered. Inference is capped structurally: every inferred term tops
   out at weight 2, so High confidence is unreachable for an
   inferred-and-confirmed dictionary by construction, not by discipline
   alone.
2. **`reference/objective-dictionary-template.md` §9 (new)** — the inference
   method itself: an evidence floor (≥15% of items carry
   Component/Label/Epic Link), a cluster floor (≥5 items or 5% of the
   portfolio), a term-frequency-in-cluster-vs-outside test, the weight cap,
   and a rule that candidate area names come from the tag itself, never an
   invented strategic phrase. Synthetic worked fragment only, per the
   existing `PORT-nn` convention — no real content enters this repo.
3. **`03p-current-state-analysis/CONTEXT.md` (new stage)** — the pivot
   target. Descriptive only: portfolio shape, age/staleness, field
   completion, and non-scored structural groupings carried from Stages
   01–02, with an explicit "what this does not do" section (no score, no
   band, no packet, no outreach list). Terminates the cycle standalone —
   does not hand off to Stage 06, whose disposition taxonomy presumes a
   recommendation to react to.
4. **`HUB.md`** — added the flowspace's first documented branch: a diamond
   after Stage 3, per `flow-foundry/references/flow-diagram-guide.md`'s
   allowance for a genuine, documented topology split (house palette hex
   values reused verbatim, no new colors invented). Stage table, Run
   procedure, and the "Objective dictionary does not exist yet" Known-gap
   entry updated to describe the fork.
5. **`04-rationalization-scoring/CONTEXT.md`, `05-recommendation-and-packet/CONTEXT.md`,
   `reference/close-score-model.md`** — a dictionary-provenance **caveat**
   threaded through scoring and packets, deliberately **not** a scoring-model
   change. The model's ramps are already unratified and calibration is an
   operator-only gate (§7); adding an uncalibrated provenance discount would
   stack a second unproven number on the first — the same failure mode the
   original hard-halt existed to prevent, just relocated into the scoring
   arithmetic. A caveat matches the model's existing pattern (Summary-only
   mapping, low-confidence staleness, unmapped status, unknown due date — all
   append-only flags, never silent point adjustments). Added item 6 to §7's
   calibration list, flagging this as an open question for a real cycle to
   answer, not one to guess at now.

## Flagged, not silently resolved

**`stage: "3p"` provenance-spec deviation.** `methodology/provenance-spec.md`
requires `stage` to be an integer on `type: stage-context`. Stage 3P's real
position — "3-and-a-branch" — isn't one. `03p-current-state-analysis/CONTEXT.md`
carries `stage: "3p"` as a deliberate, named exception. The operator should
either ratify this as a one-off or resolve it with a small
`provenance-spec.md` amendment (e.g., permitting a string `stage` id for
documented branch stages) — not something a foundry pass decides unilaterally
(`AGENTS.md` rule 7: propose structure, don't mint it).

**`skill-foundry/review-skills/objective-keyword-mapper/SKILL.md` is now
stale against this contract.** Confirmed by direct read: its description
("Halts if no dictionary exists — objective areas are never inferred"), its
mermaid diagram's `Halt` node, Method step 3, its "Grounding rules" section,
and its Definition-of-done all still encode the pre-2026-07-29 hard-halt
behavior. This was **not** edited in this pass — skill edits are a separate
skill-foundry invocation (`AGENTS.md` rule 1/2), and this decision only had a
confirmed go-ahead for the flowspace. **Open follow-up:** if the five staged
skills are promoted before `objective-keyword-mapper` is brought in line with
Stage 03's new contract, the stage contract and its own Layer-3 skill will
disagree — the operator should not let that happen silently. A skill-foundry
pass to update `objective-keyword-mapper/SKILL.md` (description, diagram,
Method, grounding rules, Definition-of-done) is recommended before that
skill's gate is re-run or it is promoted.

## Notes

- This build has not been through the three validation gates
  (`foundry-spec.md` §5) as a fresh pass — the existing Known-gaps entries
  from 2026-07-28 (unratified calibration, pending label rename, unresolved
  completion denominator, unpromoted skills) are unchanged by this decision
  except where noted above.
- Nothing has run on-engine. No adapter exists yet for the inference method
  or the Stage 3P contract.
- All frontmatter-bumped files (`HUB.md`, `03-objective-mapping/CONTEXT.md`,
  `04-rationalization-scoring/CONTEXT.md`,
  `05-recommendation-and-packet/CONTEXT.md`,
  `reference/objective-dictionary-template.md`,
  `reference/close-score-model.md`) moved `artifact-version` 1.0 → 1.1,
  `updated: 2026-07-29`. `03p-current-state-analysis/CONTEXT.md` is new at
  `1.0`.
