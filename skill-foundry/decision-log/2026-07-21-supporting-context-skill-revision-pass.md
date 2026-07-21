---
id: decision-2026-07-21-supporting-context-skill-revision-pass
title: "Decision Log — Supporting-Context Research Skill Revision Pass"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-21
updated: 2026-07-21
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[context-elicitation]]"
  - "[[scope-dependency-mapper]]"
  - "[[decision-2026-07-21-supporting-context-research]]"
---

# Decision Log — 2026-07-21 — Supporting-Context Research Skill Revision Pass

**What was decided:** apply the `supporting_context_research` house
amendment (see
`../../icp-flows/ai-refinement/decision-log/2026-07-21-supporting-context-research.md`)
to its two named skill specs — `context-elicitation` 1.4 → 1.5 and
`scope-dependency-mapper` 1.2 → 1.3 — regenerate all four affected adapters,
and pre-run the affected gate items agent-side, recording the evidence here.
**By whom:** agent, on operator instruction. **What it affects:** the two
skill specs and their four adapters; flowspace-side sync in `HUB.md` (1.13),
Stages 01–03 `CONTEXT.md`, and `reference/ai-refinement-hybrid.md` (1.3).
Both skills move `verified` → `to-review` pending the operator gate re-run.
Nothing is deployed to a live engine.

## What changed and why, per skill

1. **`context-elicitation` 1.5.** Input-type steering broadened from eight
   to nine types (adds the precedent-shaped prior-completed-work record;
   row 7 now names SAD, HLD/LLD, ADR, data model, topology diagram
   explicitly). Method step 2's stakeholder sweep gains document-seeded
   candidate prompts from architecture material — cited,
   propose-not-decide; the sweep's hard carve-out is unchanged. The skill
   reads Stage 01's supporting-context set, research record, and work-focus
   classification, and names not-found gaps (e.g., no SAD) instead of
   inventing missing context. New review criterion 10.
2. **`scope-dependency-mapper` 1.3.** Method step 2 additionally sweeps
   architecture material's integration seams for candidate dependencies
   (cited, user-confirmed). Method step 4 mines prior completed
   same-type/same-area processes for risks encountered and duration
   reference, precedent-checked with the user. Step 3's hard carve-out
   (coalition/conflict-axis, always interactive) is unchanged. New review
   criterion 8.

The other three flowspace skills are untouched: the research step lives in
Stage 01's inline Layer-3 (no skill), and Stages 04–06 consume already-
confirmed fields, not the document set.

## Scope limitation — read first

Same limitation as every prior revision pass: this session has no Rovo or
Copilot access, so each regenerated adapter was executed as a **simulated
invocation** — the agent ran the adapter's instruction text against a
synthetic, public scenario and judged the transcript against the spec's
review criteria. This validates executability as written, not
engine-specific behavior. The research step itself (Confluence/Jira search)
could not be exercised at all — no Confluence or Jira exists in this
session — so the simulated runs cover *consumption* of a supporting-context
set, not its *acquisition*. The operator should weight the next on-engine
run's coverage of the acquisition path especially heavily.

## 1. Spec re-review — pass

Both specs' Method sections and Flow Diagrams remain one-for-one — the new
behavior lands as conditional branches inside existing steps (no new
diagram nodes required). Frontmatter valid per the provenance spec on both.
Adapter tables and headers stamped 1.5/1.3 on all four regenerated adapters
— no version skew.

## 2. Live tests — 2 simulated runs, both pass

Scenario family continues the synthetic DC east-west fabric expansion; run
numbering continues from R22.

| Run | Skill / adapter | Shape | Verdict vs. review criteria |
|---|---|---|---|
| R23 | context-elicitation / Rovo | supporting-context set with a synthetic SAD + a not-found HLD, grounded mode | 10/10 |
| R24 | scope-dependency-mapper / Copilot | SAD integration-seam sweep + prior completed same-type refresh record | 8/8 |

- **R23** — a synthetic SAD (three integration points: IPAM feed, monitoring
  export, firewall policy engine) accompanied the fabric-expansion scenario,
  with the research record noting "HLD: not found." The adapter used the
  three integration points as cited candidate prompts during the register
  walk (each proposed, two confirmed by the user, one rejected), and named
  the missing HLD when the user asked about migration sequencing — eliciting
  that context instead of inventing it. No extraction was attempted in the
  sweep.
- **R24** — the same scenario's supporting-context set added a closed
  synthetic Jira item for a prior fabric refresh in the same DC hall. The
  adapter surfaced two candidate dependencies from the SAD's seams (one
  classified blocking, one informational, both cited and user-confirmed),
  mined the prior record for a risk actually encountered (optic
  incompatibility) with a citation, and asked the user to confirm the
  precedent's conditions still held before carrying its duration reference
  into the risk discussion. Scope was not copied forward.

## 3. Trigger check — pass

Neither revision adds a fire condition. The supporting-context set, research
record, and work-focus classification are Stage 01 inputs handed to each
skill; no trigger phrase or near-miss boundary changes.

## 4. Boundary/collision check — pass

`context-elicitation`'s document-seeded sweep prompts stay inside problem
framing (stakeholder candidates, "tried before") and never draft scope or
dependencies — no encroachment on `scope-dependency-mapper`. The mapper's
seam sweep and precedent mining produce scope-package content only — no
encroachment on `field-refinement-cadence` (placement) or
`workitem-validation` (gating). The acquisition step itself belongs to
Stage 01 inline, not to either skill — neither spec gained a search
capability, only consumption of an already-screened set.

## 5. Evidence

This entry. Flowspace-side sync recorded in `ai-refinement` HUB (1.13,
sixth Known-gaps entry) and Stages 01–03 `CONTEXT.md`.

## Remaining for the operator (the human gate)

1. On-engine live test per adapter for both revised skills — weighted
   toward the acquisition path (Confluence/Jira search, scope confirmation,
   widening), which no simulated run could exercise.
2. Redeployment of the four regenerated adapters, superseding the prior
   versions.
3. The instantiation-guide and validation-checklist extensions named in the
   flowspace-side log (REC-02 knowledge scoping, REC-09 research-step
   checks) before the first live run.
