---
id: decision-2026-07-03-communication-style-enforcement
title: "Decision Log — Communication Style Enforcement (REC-03)"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
  - "[[context-elicitation]]"
  - "[[field-refinement-cadence]]"
  - "[[jira-commit]]"
---

# Decision Log — 2026-07-03 — Communication Style Enforcement

**What was decided:** operationalize the persona contract's
`communication_style` array (precise, analytical, structured, direct) — which
the source document defined but no stage or skill referenced — as a binding
constraint on every user-facing output, not descriptive metadata. **By whom:**
agent, on operator instruction, implementing drift-analysis recommendation
REC-03. **What it affects:** `reference/ai-refinement-hybrid.md` (House
Amendment 5, the citation anchor), Stage 01 (persona activation step), Stage
05 (constraint-validation step, new checklist item), and the three skills
that produce the most user-facing text: `context-elicitation` (question
sequence, pushback, draft presentation), `field-refinement-cadence` (field
presentation, AC reframing, due-date ask), and `jira-commit` (dry-run
preview, transition offer).

## The gap this closes

DRIFT-01 in the drift analysis: the persona's four *behaviors* were loaded
and enforced (Stage 01 step 4 already listed all four), but the persona's
*communication_style* was never transcribed or checked anywhere downstream.
An agent could produce verbose, narrative, or informal output without
violating any stated contract — undermining the TPSO persona's credibility
and making Jira field content inconsistent across runs.

## Decisions and alternatives

1. **Enforcement anchor lives in the clipping, not just in stage prose.**
   Rather than adding "be precise and direct" language independently to each
   touched file, House Amendment 5
   (`reference/ai-refinement-hybrid.md`) states the rule once and every
   downstream citation points back to it — so a future reader can find the
   single source of the requirement instead of five independently-worded
   restatements. *Alternative considered:* state the rule only in Stage 01 and
   let downstream stages inherit it implicitly — rejected, since "binding on
   every stage" was exactly the property DRIFT-01 found missing when left
   implicit.
2. **Checked at Stage 05, not just stated at Stage 01.** Loading the
   persona's communication_style at intake (Stage 01) establishes intent;
   without a downstream check it would repeat DRIFT-01's failure mode of a
   stated-but-unenforced contract. Stage 05's constraint-validation step
   (already the stage that checks summary length, AC starters, and due-date
   validity) gains a parallel check for communication_style, so a violation
   is caught by the same mechanism that catches every other field-level
   drift, not left to reviewer judgment alone.
3. **Skills selected by what they generate, not blanket-applied.** Only the
   three skills with substantial user-facing text generation
   (`context-elicitation`, `field-refinement-cadence`, `jira-commit`) were
   edited; `scope-dependency-mapper` and `workitem-validation` were left
   untouched here since REC-03 named only the first three explicitly and
   their user-facing surface is comparatively thin (structured
   presentations, not open-ended drafting).

## Assumption (operator to confirm or amend)

- **E1 — "binding, not descriptive" is checkable by a human reviewer.**
  Communication-style compliance is a qualitative check (does this read as
  precise/analytical/structured/direct), not a mechanical one like word count
  — Stage 05's new checklist item relies on reviewer judgment the same way
  the AC-starter check does. Amendment path: if this proves too subjective in
  practice, consider a narrower objective proxy (e.g., banning specific hedge
  words) as a follow-up revision.
