---
id: decision-2026-07-15-value-decomposition-skill-gate-prerun
title: "Decision Log — Value Decomposition Skill: Five-Point Gate Pre-Run"
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
  - "[[decision-2026-07-15-value-decomposition-skill-build]]"
---

# Decision Log — 2026-07-15 — Value Decomposition Skill: Five-Point Gate Pre-Run

**What was decided:** run the skill-foundry §5 review gate, agent-side, on
the `value-decomposition` build and record the evidence here (gate item 5).
**By whom:** agent, same instruction as the build entry. **What it
affects:** nothing required a fix before staging. Nothing is promoted,
nothing moved to `../../produced-skills/`, nothing deployed — those calls
stay with the operator.

## Scope limitation — read first

Gate item 2 demands a live test **on the target engine**. This session has
no Rovo or Copilot access, so each adapter was executed as a **simulated
invocation**: the agent ran the adapter's instruction text against
synthetic, `public`/fabricated scenarios built from the primer brief's
"Definition of done," and judged the transcript against the spec's review
criteria. This validates the adapters are executable as written and that
the spec's logic holds — it does not validate engine-specific behavior
(Rovo knowledge-scoping enforcement, Copilot prompt-file routing).
On-engine invocation remains open unless the operator accepts simulation as
sufficient for a first promotion. Diagram compilation was run for real: the
Mermaid `flowchart LR` was extracted and compiled locally with
`mermaid-cli` (`@mermaid-js/mermaid-cli` via `npx`, headless Chromium,
`--no-sandbox`) and rendered to SVG without error.

## 1. Spec review — pass, no pre-stage fixes needed

Purpose sharp; triggering intent names four misfire cases (single-item
refinement, bottom-up parent-linking, refining a known child directly,
below-Feature parents); boundaries explicit with each excluded job's owner
named; review criteria checkable and traceable to the brief's Definition of
done (criteria 1–5 map to DoD 1–5; criterion 6 adds the explicit-verdict
and pre-seed visibility check implied by brief method steps 7–8);
frontmatter valid per `provenance-spec.md` (rule 3 —
`generated-by`/`generated-by-version` paired; rule 6 — frontmatter
`data-class: public`, with the runtime max of `internal` in the body's Data
boundary section). Both diagram diamonds (vertical-slice check, user
verdict) trace to named branches in Method steps 3 and 7, including the
reject/re-propose loop-back and the clean-stop halt; adapters add format,
not logic.

## 2. Live tests — 5 simulated runs, all pass

Synthetic parent set, network-infrastructure domain to match the flowspace:
solution epic "Unified network observability platform" (SE-1) and feature
"Self-service DNS record management" (F-1), each with fabricated problem
statement, business/customer value, and in/out of scope.

| Run | Scenario | Verdict vs. review criteria |
|---|---|---|
| R1 | SE-1; user asks to "break this down all the way to stories" in one step | Proposed features only, with the note that each accepted feature can be decomposed in its own later pass — no stories auto-proposed under any feature (criterion 1) |
| R2 | F-1 with a seeded horizontal draft ("Build the DNS API layer" / "Build the web UI" / "Design the records schema") | Draft rejected at the vertical-slice check and re-proposed as end-to-end slices ("Request a new A record end-to-end," "Track my pending DNS requests") — not passed through (criterion 2) |
| R3a | SE-1 normal path | Every proposed feature carried a persona value statement in the literal "As a [persona], I value [outcome] because it helps me [goal/pain point]" format (criterion 3, format half) |
| R3b | Solution epic "Campus switch OS uplift" (sequencing-heavy); user elects technical framing for two children; a third child left unelected | Both elected children recorded with an explicit, named exception; the unelected third still drafted in persona format with the election offered, not assumed (criterion 3, exception half — never silent, never unelected) |
| R4 | R1's review step; user asks "can we skip acceptance criteria on these and fill them in later?" | Declined to relax: acceptance criteria stated as a hard schema gate in each child's own Band 2 run, unchanged by decomposition; quarter-testable guidance surfaced as advisory alongside it (criterion 4) |
| R5 | F-1; at review the user says "actually, not ready to break this down yet" | Stopped cleanly, nothing created, no partial hand-off (criterion 5) |

Criterion 6 (explicit verdict + visible pre-seed) was checked across R1–R4:
each accepted child's hand-off carried the parent grounding context and its
value statement or named exception.

## 3. Trigger check — pass

"Decompose this feature into stories" / "help me break this solution epic
into features" fire; the near-misses resolve away: a plain "refine another
item" stays the Band 2 loop; a run with a known parent link stays a normal
run (Stage 06 owns the link); "decompose this story" is declined with the
sub-task redirect per the schema registry's out-of-scope table — R2's seeded
draft also exercised the reject path live rather than only asserting it.

## 4. Boundary/collision check — pass

Against the twelve produced skills: the five `ai-refinement` Band 2 skills
operate on one item's fields after this skill has handed it off
(`context-elicitation` consumes the pre-seed; `workitem-validation` keeps
the AC gate; `jira-commit`/Stage 06 keeps parent-linking); the
accomplishments and foundry-support skills share no territory. Within the
flowspace, the one deliberate seam — this skill drafts a value-statement
*seed* that `field-refinement-cadence` then refines as ordinary field
content — is declared on both the Method (step 8) and the "What this skill
is not" list, so it reads as a hand-off, not an overlap.

## 5. Evidence

This entry, the compiled SVG (local, not retained), and the companion build
entry `2026-07-15-value-decomposition-skill-build.md`.

## Remaining for the operator (the human gate)

1. On-engine live test per adapter (or explicitly accept the simulations
   above for first promotion) — including the Rovo adapter's read-only Jira
   lookup for a committed parent, which no simulation can exercise.
2. Rendering confirmation on the real surfaces (GitLab mirror natively;
   Confluence macro or "diagram: see mirror" fallback).
3. Promotion calls: `truth-level: verified`, move to
   `../../produced-skills/value-decomposition/`, adapter deployment, and
   moving `sp-value-decomposition` to `completed-skill-starters/` at the
   same time.
4. Once promoted, the flowspace-side wiring: Stage 01 `CONTEXT.md` gains the
   decomposition invocation and Layer-3 pointer, and `HUB.md`'s fifth-gap
   paragraph updates from "handed off, not built" — intentionally not edited
   in this pass, since the gap only closes on promotion, not on staging.
5. The brief's carried open item, unresolved by design: whether/how the
   persona-statement format and vertical-slice check get promoted into
   `workitem-validation`/Stage 05 rules for the types that require them
   (noting `story`/`spike` may validate against a different field than
   `customer_business_value`) — a future `workitem-validation` revision
   with its own re-gate, not part of this build.
