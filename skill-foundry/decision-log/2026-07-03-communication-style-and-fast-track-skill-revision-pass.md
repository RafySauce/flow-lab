---
id: decision-2026-07-03-communication-style-and-fast-track-skill-revision-pass
title: "Decision Log — Communication Style + Fast-Track Skill Revision Pass"
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
  - "[[context-elicitation]]"
  - "[[scope-dependency-mapper]]"
  - "[[field-refinement-cadence]]"
  - "[[jira-commit]]"
  - "[[decision-2026-07-03-stage06-feedback-revision-pass]]"
---

# Decision Log — 2026-07-03 — Communication Style + Fast-Track Skill Revision Pass

**What was decided:** apply the drift-analysis revision pass (REC-03
communication_style enforcement, REC-05 broadened input taxonomy, REC-06
domain-configurable stakeholder register, REC-08 fast-track mode) to their
named skill specs — `context-elicitation` 1.2 → 1.3,
`scope-dependency-mapper` 1.0 → 1.1, `field-refinement-cadence` 1.2 → 1.3,
`jira-commit` 1.3 → 1.4 — regenerate all eight affected adapters, and re-run
the affected gate items, agent-side, recording the evidence here. **By
whom:** agent, on operator instruction implementing the full drift-analysis
recommendation set. **What it affects:** the four skill specs and their
eight adapters; the flowspace `HUB.md` (1.9), all six stage `CONTEXT.md`
pages, `reference/ai-refinement-hybrid.md` (1.1),
`reference/platform-stakeholder-register.md` (1.1), and the new
`reference/platform-stakeholder-register-template.md`. Nothing is deployed
to a live engine — that stays the operator's act (see
`../../icp-flows/ai-refinement/decision-log/2026-07-03-deployment-artifacts-prepared.md`).

## What changed and why, per skill

1. **`context-elicitation` 1.3.** Question-sequence steering broadened from
   four to eight source-input types; a fast-track extraction path added to
   Method step 1; pushback and confirm/present steps (3, 5) tied explicitly
   to `communication_style`; the stakeholder-sweep step (2) gained an
   ungrounded-mode conditional and is marked a hard carve-out.
2. **`scope-dependency-mapper` 1.1.** Coalition/conflict-axis annotation
   (Method step 3) gained an ungrounded-mode conditional and is marked a hard
   carve-out — the only change to this skill; it was not named in REC-03 and
   REC-08's consolidation is a Stage-CONTEXT-level change that doesn't alter
   this skill's own Method.
3. **`field-refinement-cadence` 1.3.** The largest change: the skill's
   description and Method were rewritten from "walks fields one at a time"
   (unconditional) to conditionally scoped — full-interactive mode and
   fast-track's unextractable fields still walk one at a time;
   fast-track's confidently-extracted fields are grouped for the consolidated
   checkpoint instead. Due-date elicitation (step 5) is explicitly marked a
   hard carve-out that fast-track cannot relax. AC reframing and the
   due-date ask tied to `communication_style`.
4. **`jira-commit` 1.4.** Narrowest change: dry-run preview (step 3) and
   transition offer (step 5) tied to `communication_style`. No fast-track
   changes — parent mapping was already always-interactive by design, so
   mode has no bearing on this skill.

## Scope limitation — read first

Same limitation as the two prior revision passes
(`2026-07-03-ai-refinement-skill-revision-pass.md`,
`2026-07-03-stage06-feedback-revision-pass.md`): this session has no Rovo or
Copilot access, so each regenerated adapter was executed as a **simulated
invocation** — the agent ran the adapter's instruction text verbatim against
a synthetic, public scenario and judged the transcript against the spec's
review criteria. This validates executability as written, not engine-specific
behavior. Fast-track mode in particular introduces new interaction shapes
(mode proposal with rationale, consolidated presentation, source citation)
that no prior on-engine run has ever exercised — the operator should weight
the next on-engine run's coverage of fast-track especially heavily, the same
way NEADD-1827's lesson was that simulated tests alone had not caught real
defects.

## 1. Spec re-review — pass

All four specs' Method sections and Flow Diagrams remain one-for-one (no
diagram changes were required by this pass — the new behavior fits within
each skill's existing node structure as conditional branches inside existing
steps, not new steps requiring new diagram nodes, except
`field-refinement-cadence` where steps 1 and 2's prose grew substantially but
the diagram's two corresponding nodes still describe the same decision
points). Frontmatter valid per the provenance spec on all four. Adapter
tables and headers stamped 1.3/1.1/1.3/1.4 on all eight regenerated adapters
— no version skew.

## 2. Live tests — 4 simulated runs, all pass

Scenario family continues the prior passes' synthetic DC east-west fabric
expansion; run numbering continues from R18.

| Run | Skill / adapter | Shape | Verdict vs. review criteria |
|---|---|---|---|
| R19 | context-elicitation / Rovo | fast-track, structured requirements doc input, ungrounded-mode fallback | 9/9 |
| R20 | field-refinement-cadence / Copilot | fast-track, extracted fields + due-date carve-out | 9/9 |
| R21 | scope-dependency-mapper / Rovo | ungrounded-mode conflict-axis annotation | 7/7 |
| R22 | jira-commit / Copilot | communication_style check on dry-run preview + transition offer | 9/9 |

- **R19** — a synthetic structured requirements document (a one-page "PRD"
  for a DC fabric capacity increase) was fed in with Stage 01 having proposed
  fast-track mode. The adapter drafted problem_statement and
  customer_business_value with citations to specific PRD sections; the
  stakeholder sweep still ran as a fully interactive walk of the register
  (confirmed in transcript — no extraction attempted there) even though the
  PRD named two stakeholders. A second run of the same scenario with no
  register loaded correctly fell into ungrounded mode and asked the user
  directly instead of referencing register entries.
- **R20** — continuing R19's scenario in fast-track: summary, customer value,
  and acceptance-criteria drafts arrived pre-filled with citations at a single
  presentation; the due date was still elicited as its own interactive
  question after acceptance criteria were shown, per the hard carve-out — the
  adapter did not attempt to extract a date from the PRD's "target Q3"
  language, correctly treating it as a reference point only.
- **R21** — a scenario with no stakeholder register loaded for the domain
  (a hypothetical facilities-management flowspace instantiation). The adapter
  asked the user directly whether any tensions existed, recorded a
  user-stated conflict with a named decision-owner, and did not invent a
  coalition or axis name — matching the ungrounded-mode conditional.
- **R22** — re-ran a jira-commit dry-run preview and transition-offer
  exchange with an intentionally verbose draft passed in from an upstream
  stage; the adapter's own preview and offer language stayed precise and
  direct as required, and the review checklist's new communication_style
  item was checked against the transcript.

## 3. Trigger check — pass

None of the four revisions add a new fire condition. Fast-track mode is
selected upstream at Stage 01 and handed to each skill as an input; it does
not change any skill's own trigger phrase or near-miss boundaries.

## 4. Boundary/collision check — pass

Re-inspected all four against their neighbors: `context-elicitation`'s
fast-track extraction does not encroach on `scope-dependency-mapper`'s
territory (it drafts problem/value fields only, never scope or dependencies).
`field-refinement-cadence`'s consolidation does not encroach on
`workitem-validation`'s gate (the consolidated checkpoint is a user
confirmation step, not a validation verdict — Stage 05 still owns pass/fail).
`jira-commit`'s parent-mapping behavior is unchanged by this pass, confirming
mode has no bearing on Stage 06 as designed.

## 5. Evidence

This entry. Flowspace-side sync recorded in `ai-refinement` HUB (1.9) and all
six stage `CONTEXT.md` pages.

## Remaining for the operator (the human gate)

1. On-engine live test per adapter for all four revised skills, per
   `../../icp-flows/ai-refinement/reference/on-engine-validation-checklist.md`
   — weighted especially heavily for fast-track mode, which has never run on
   any engine in any form.
2. Redeployment of all eight regenerated adapters, superseding whatever was
   published from the prior versions (per
   `../../icp-flows/ai-refinement/reference/confluence-instantiation-guide.md`).
3. Confirm the target Jira project's board configuration still matches what
   `jira-commit` assumes (unchanged by this pass, but worth re-confirming at
   the same time as the above).
