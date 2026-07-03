---
id: decision-2026-07-03-stage06-feedback-revision
title: "Decision Log — Stage 06 Feedback Revision (Flowspace Side)"
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
  - "[[work-item-schemas]]"
  - "[[jira-commit]]"
  - "[[field-refinement-cadence]]"
---

# Decision Log — 2026-07-03 — Stage 06 Feedback Revision (Flowspace Side)

**What was decided:** ratify and implement the five defects in the
operator's Stage 06 feedback package (`ai-refinement-stage06-feedback`,
operator-observed, first on-engine invocation via Rovo, produced NEADD-1827
on the Perimeter Security Services board) — the flowspace-side half of the
revision; the skill-spec half (jira-commit 1.3, field-refinement-cadence 1.2)
is logged in
`../../skill-foundry/decision-log/2026-07-03-stage06-feedback-revision-pass.md`.
**By whom:** agent, on operator instruction to implement the full feedback
package. **What it affects:** `reference/work-item-schemas.md` (1.0 → 1.1),
Stage 01 (1.3 → 1.4), Stage 04 (1.2 → 1.3), and Stage 06 (1.3 → 1.4)
CONTEXT.md pages, and the flowspace `HUB.md` (1.7 → 1.8).

## The gap this closes

The feedback package documents five operator-observed defects at the commit
boundary, none of which were caught by the prior five-point gate because
that gate ran simulated, synthetic invocations — this was the family's first
real on-engine run. Two of the five (formatting, due date) are behavioral
gaps in skill Method steps; two (parent mapping, transition offer) are
partly contract gaps — Stage 06's own CONTEXT.md never specified user
confirmation for the parent or a post-creation transition, so the skill
wasn't contradicting its contract, the contract itself was incomplete; one
(board-interaction fields) is a pure schema gap.

## Decisions and alternatives

1. **Schema fix lands in the registry, not the skills.** `type_of_work` and
   `work_category` are added to the `story` and `spike` schemas in
   `reference/work-item-schemas.md` (they were already required on `feature`
   and `task`). No skill spec needed a code change for this, since
   `jira-commit`'s field mapping and `field-refinement-cadence`'s field
   ordering both already read "every registry field for the type"
   generically — the schema *is* the single point of truth, per the
   registry's own design (`work-item-schemas` 1.0's rationale). *Alternative
   considered:* hardcode the two fields into the skills' Method prose for
   story/spike specifically — rejected, since that would duplicate what the
   registry already owns and reintroduce the exact drift (1.1's hardcoded
   custom-field list omitting spike fields) the 1.2 jira-commit revision
   fixed.
2. **Derivation rule revised, not just the field list.** The registry's
   derivation rule 2 previously read "`story` is `feature` minus the
   execution-classification fields" — no longer accurate once `story` also
   carries `type_of_work`/`work_category`. Rewritten to state the real
   invariant: every refinable type traverses the Jira board workflow, so
   every refinable type needs the fields the board's column-transition rules
   demand, independent of which fields differ for scope-framing reasons. A
   new derivation rule 5 states this explicitly, citing NEADD-1827 as the
   evidence. This keeps the registry's stated purpose intact — ratifying
   *reasoning*, not just a field list.
3. **`type_of_work`/`work_category` ripple into field-refinement-cadence's
   conflict check.** Stage 04's cross-field conflict check ("type-of-work /
   work-category consistency") was scoped to "feature and task" in its
   CONTEXT.md prose, matching the pre-1.1 registry. Updated to cover every
   type that now carries both fields — otherwise story/spike would gain the
   required fields but never get the consistency check that exists for
   exactly this reason.
4. **Parent mapping and transition offer are contract extensions, not just
   skill behavior fixes.** Per the feedback package's own framing (Defect 2,
   Defect 4): Stage 06 CONTEXT.md's Process step 2 (hierarchy linkage) and
   step 8/9 (session loop) did not specify user confirmation of the parent or
   a transition offer, so these are recorded here as contract-surface changes
   to Stage 06 itself, alongside the corresponding `jira-commit` 1.3 Method
   revisions logged in the skill-side entry. *Alternative considered:* fix
   only the skill spec and leave Stage 06's CONTEXT.md as a looser umbrella —
   rejected per the feedback package's own diagnosis that this was "a gap in
   the contract itself, not just the implementation."
5. **Stage 01's schema transcription kept in lockstep.** Stage 01 CONTEXT.md
   transcribes each type's required-field list inline (for one-stop reading
   at intake) — its story/spike bullets are updated to match the registry
   1.1 field-for-field, preserving the existing Verify check ("the loaded
   schema's required-field list matches the registry... field-for-field").

## Assumptions (operator to confirm or amend)

- **C1 — the board-required fields generalize.** This revision assumes
  `type_of_work`/`work_category` are required by the *board configuration*
  (workflow transitions) rather than by issue-type-specific screens, which is
  why they're now required uniformly across every refinable type. Amendment
  path: if the real Jira project's `story`/`spike` issue screens don't
  actually expose these fields, the registry addition should be reverted and
  the underlying board-configuration assumption revisited — this is exactly
  the kind of divergence the "confirm against the real Jira project
  configuration at instantiation" caveat (carried since `work-item-schemas`
  1.0) exists to catch.
- **C2 — this bundles into, not replaces, the existing to-review
  ratification.** The `story`/`task`/`spike` schemas were already awaiting
  operator ratification before this revision; the 1.1 field addition is one
  more item in that same pending ratification, not a separately-approved
  change.
- **C3 — parent mapping's "create new" path spawns a Band 2 run, not an
  inline sub-flow.** When the user requests a new parent at commit time, the
  contract now specifies this halts the current commit and starts a new
  Band 2 run for the parent type (per the feedback package's proposed fix).
  This assumes the operator wants a full fresh run for the parent rather than
  a lighter inline shortcut — amendment path: if that's too heavy in
  practice, a condensed "parent-only" sub-flow could be scoped later.
