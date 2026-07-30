---
id: decision-2026-07-30-value-decomposition-wiring-fix
title: "Decision Log — value-decomposition Wiring Fix"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-30
updated: 2026-07-30
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[value-decomposition]]"
---

# Decision Log — 2026-07-30 — value-decomposition Wiring Fix

**What was decided:** the `value-decomposition` skill
(`produced-skills/value-decomposition/`, spec version 1.0, `truth-level:
verified`, built 2026-07-15) was never actually referenced anywhere in the
`ai-refinement` flowspace it was built for. Its own frontmatter states
"Invoke from Stage 01," but an audit found it absent from `HUB.md`'s Stage
1 row in the Layer-3 stage table, absent from `HUB.md`'s Layer-3 reference
table entirely, and unreferenced in
`01-intake-and-guardrails/CONTEXT.md` — the skill-foundry side of the
2026-07-15 handoff closed, but the flowspace side never did. This fixes the
flowspace-side wiring only; no skill behavior changes. **By whom:** agent,
on direct operator instruction, following an operator-requested audit that
surfaced the gap. **What it affects:** `HUB.md` (1.15 → 1.17) and
`01-intake-and-guardrails/CONTEXT.md` (1.11 → 1.13). `value-decomposition`
itself is untouched — still spec version 1.0, `truth-level: verified`.

**Follow-up same day:** the operator noted that "break down" is common
everyday phrasing for the same intent as "decompose," and the initial wiring
pass's handoff text in Stage 01 only used the word "decompose." The skill's
own Triggering intent (`produced-skills/value-decomposition/SKILL.md:73`)
already used "break this ... into" as an example trigger phrase, so this was
a wording gap in the new Stage 01 text, not a skill-behavior gap. Fixed by
listing the equivalent phrasings explicitly ("decompose," "break down,"
"break this into," "split this up") everywhere the new handoff is described
— Stage 01's Layer-3 note, its step-7 handoff paragraph, its Verify
checklist item, and `HUB.md`'s stage-table cell — so the wiring doesn't read
as narrower than the skill it points to. Bumped `01-intake-and-guardrails/
CONTEXT.md` to 1.13 and `HUB.md` to 1.17 for this same-day follow-up.

## Design decisions

1. **Wire at Stage 01, step 7, not a new step.** The skill's own trigger
   ("user has selected a parent-level type and states a desire to
   decompose it") lines up exactly with Stage 01's existing step 7 (work
   item type selection) — the step already establishes the selected type
   and its schema. Adding the handoff as a paragraph inside step 7 avoided
   renumbering steps 8–12, which would have shifted internal cross-references
   (e.g., step 5's forward reference to the now-step-9 planning-label
   resolution) for a change that only needed a conditional fork after type
   selection, not a new sequential stage in the intake process.
2. **Conditional handoff, not a stage replacement.** Stage 1's Layer-3 stays
   primarily `inline`; `value-decomposition` is listed as a conditional
   fork alongside it, not a replacement Layer-3 skill, because ordinary
   single-item refinement (the default Band 2 loop) is still the common
   path through Stage 1 and must proceed unaffected when the user states no
   decomposition intent.
3. **No re-gate triggered.** This is a reference/documentation fix on the
   flowspace side — no change to `value-decomposition`'s own Method,
   Review criteria, or adapters, and no change to Stage 01's other steps —
   so `value-decomposition` keeps `truth-level: verified` and Stage 01
   keeps its existing `to-review` status (already `to-review` from prior
   gaps, unrelated to this fix) rather than triggering a new gate cycle.
4. **Table wording distinguishes Stage 1 from Stages 2–6.** Stages 2–6's
   Layer-3 reference table rows describe the skill that *is* the stage.
   Stage 1 is different — `inline` remains the stage's default path, and
   `value-decomposition` is a conditional handoff triggered only on
   explicit decomposition intent — so the new table row and stage-table
   cell wording say "conditional handoff" rather than presenting the skill
   as Stage 1's primary Layer-3, to avoid implying Stage 1 always runs
   through it.

## Remaining for the operator (the human gate)

1. Confirm the step-7 handoff wording matches how decomposition should
   actually surface during a live Stage 01 run — this was a documentation
   wiring fix, not a re-validated behavior change, and has not run on-engine.
2. Decide whether `value-decomposition`'s own frontmatter description
   ("Invoke from Stage 01") needs updating to point at the specific step
   (step 7) now that the handoff has a concrete home, or whether the
   general stage-level reference is intentional and should stay as-is.
