---
id: decision-2026-07-15-value-decomposition-skill-build
title: "Decision Log — Value Decomposition Skill Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
data-class: public
related:
  - "[[sp-value-decomposition]]"
  - "[[ai-refinement]]"
---

# Decision Log — 2026-07-15 — Value Decomposition Skill Build

**What was decided:** author the `sp-value-decomposition` backlog starter —
the Workstream B handoff from
`icp-flows/ai-refinement/decision-log/2026-07-15-provenance-and-planning-labels.md` —
as an engine-neutral `SKILL.md` plus Rovo and Copilot adapters, staged in
`review-skills/value-decomposition/` at `truth-level: to-review`. **By
whom:** agent, on operator instruction ("let's implement the value
decomposition skill piece"). **What it affects:** one new folder under
`review-skills/`; the `sp-value-decomposition` primer brief stays unchanged
in the backlog as the intake record. Nothing promoted, nothing moved to
`../../produced-skills/`, nothing deployed.

**Intake path:** clean — the starter is a primer brief filed same-day by the
`ai-refinement` flowspace's Workstream B handoff, built from an
operator-answered clarifying-question set. No foreign material, no vetting
checklist run. (The "Value Delivery — Key Concepts, a 30,000ft View" deck
the brief grounds on is operator-provided material living in employer
tenancy; the spec carries the deck's key concepts it depends on — persona
value statements, MVP thinking, Hamburger Method slicing, quarter-testable
acceptance criteria — rather than referencing an artifact this public repo
cannot hold.)

## Notable calls

- **Both adapters built.** The brief names Rovo and Copilot as the
  sanctioned set with no engine-specific constraint, same as the rest of
  `ai-refinement` — so both adapters exist, mirroring the five Band 2
  skills, rather than the Copilot-only pattern used where a brief names one
  engine as the reason the skill exists.
- **The "not ready" stop is modeled once, available throughout.** The brief
  places the user's "not ready to decompose this level yet" option in both
  its method steps 2 and 7; the spec models it as the review decision's stop
  verdict (one diagram branch) with prose making the same clean stop
  available at any earlier point — one behavior, not two subtly different
  stops.
- **`feature` → children widened to the registry's full child set, framed.**
  The brief's method sketch says "`feature` → stories," but its own
  persona-statement exceptions name `bug` and `task` as possible children —
  so the spec reads `feature` → stories, with `task`/`spike`/`bug` allowed
  only where a proposed child genuinely is one, per
  `reference/work-item-schemas.md`. Stories stay the value-carrying default.
- **Quarter-testable stays advisory; validation promotion stays open.** The
  brief's open item (promoting the persona-statement format and
  vertical-slice check into `workitem-validation`/Stage 05 rules) is
  deliberately not resolved here: the spec states both as generation-time
  heuristics and names the promotion as an open operator decision. Extending
  `workitem-validation` would be its own revision with its own re-gate.
- **No flowspace edits in this pass.** Stage 01's `CONTEXT.md` and `HUB.md`
  still describe the decomposition capability as handed off, not built —
  accurate until promotion. Wiring the skill into Stage 01 (an invocation
  line in its Process, a Layer-3 pointer, and the HUB fifth-gap update) is
  flowspace-side work owed at promotion, not at staging — same sequencing as
  the 2026-07-14 batch's item 5.
- **Boundary/collision first pass** against the twelve produced skills: the
  close neighbors are `context-elicitation` (elicits one item's context —
  this skill pre-seeds that run, it doesn't run it) and Stage 06's
  parent-linking inside `jira-commit` (this skill never sets a parent link).
  No territory overlap found; formal check re-runs at the five-point gate —
  pre-run evidence in the companion entry,
  `2026-07-15-value-decomposition-skill-gate-prerun.md`.

**Next:** operator review per `foundry-spec.md` §5 (see the companion
gate-pre-run entry for what's already checked agent-side and what remains).
