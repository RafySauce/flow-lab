---
id: decision-2026-07-03-ai-refinement-skill-gate-prerun
title: "Decision Log — AI Refinement Skill Batch: Five-Point Gate Pre-Run"
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
  - "[[workitem-validation]]"
  - "[[jira-commit]]"
---

# Decision Log — 2026-07-03 — AI Refinement Skill Batch: Five-Point Gate Pre-Run

**What was decided:** run the skill-foundry §5 review gate, agent-side, across
the five `ai-refinement` skills, and record the evidence here (gate item 5).
**By whom:** agent, on operator instruction ("finish up the flowspace and
associated skill testing"). **What it affects:** the five skill specs (four
took a diagram-only 1.1 revision), their adapters (version re-stamp), and the
flowspace's Known-gaps status. Nothing is promoted, nothing moved to
`completed-skills/`, nothing deployed — those calls stay with the operator.
This entry deliberately stretches the ~10-line shape, on the
validation-checklist precedent that gate evidence *is* the entry.

## Scope limitation — read first

Gate item 2 demands a live test **on the target engine**. This session has no
Rovo or Copilot access, so each adapter was instead executed as a **simulated
invocation**: the agent ran each adapter's instruction text verbatim against a
synthetic, public scenario and judged the transcript against the spec's review
criteria. This validates that the adapters are executable as written and that
the specs' logic holds — it does not validate engine-specific behavior
(knowledge-scoping enforcement, Rovo action wiring, real Jira API). **On-engine
invocation remains open** unless the operator accepts simulation as sufficient
for a first promotion. Likewise, diagram rendering was verified by local
Mermaid compilation (all pass); GitLab/Confluence surface confirmation remains
an instantiation-time item.

## 1. Spec review — pass, with findings (fixed)

All five: purpose sharp; triggering intent names misfires; boundaries
explicit; review criteria checkable; frontmatter valid per the provenance
spec (rules 3 and 6 checked); adapters add format, not logic.

Finding: four diagrams broke the guide's one-for-one rule against Method
prose — `context-elicitation` and `workitem-validation` step labels skipped
the conditional step (diagram "Step 3" = prose step 4); `field-refinement-
cadence` collapsed prose steps 4–5 into one node; `jira-commit` folded the
session-loop step into the terminal output node. All four fixed at spec v1.1
(diagram-only; adapters re-stamped, content unchanged).
`scope-dependency-mapper` was already one-for-one and stays 1.0. All six
diagrams (five skills + flowspace hub) compile under Mermaid 11 via
mermaid-cli.

## 2. Live tests — 10 simulated runs, all pass

Synthetic scenario (invented, public): solution epic **"DC east-west fabric
capacity expansion"** — analytics virtualization cluster onboarding blocked,
leaf-spine uplinks at 82% p95. Register stakeholders in play: DC Networking
(2), Systems/Server (9), Cyber (6), Cloud (12), Facilities (13).

| Run | Skill / adapter | Shape | Verdict vs. review criteria |
|---|---|---|---|
| R1 | context-elicitation / Rovo | happy path + vague input | 6/6 |
| R2 | context-elicitation / Copilot | near-miss + boundary probe | 6/6 |
| R3 | scope-dependency-mapper / Rovo | happy path | 6/6 |
| R4 | scope-dependency-mapper / Copilot | conflict-decision probe | 6/6 |
| R5 | field-refinement-cadence / Rovo | happy path | 6/6 |
| R6 | field-refinement-cadence / Copilot | conflict + upstream-edit probe | 6/6 |
| R7 | workitem-validation / Rovo | formatting auto-correct path | 6/6 |
| R8 | workitem-validation / Copilot | halt path | 6/6 |
| R9 | jira-commit / Rovo | happy path (synthetic API) | 6/6 |
| R10 | jira-commit / Copilot | refusal edges | 6/6 |

Condensed transcripts:

- **R1** — opener "the DC network needs more capacity" → answered "it's slow"
  to the problem question → pushback fired ("name the two most recent failures
  and their cost") → user supplied: cluster deploy paused three weeks; two
  vMotion storms breached the replication window. Sweep tagged 2, 9, 6, 12, 13;
  entry 13's "what they value most" surfaced the power/cooling ceiling the
  user hadn't volunteered. Drafted measurable outcomes ("p95 east-west
  utilization below 60% by 2026-12-31"); value traced to entries 2 and 9;
  four individual yes/no confirmations. User's mention of an "AI Ops team"
  (not in register) was flagged as a missing party, not invented.
- **R2** — invoked with "what's in and out of scope for the fabric
  expansion?" → correctly declined and routed to `scope-dependency-mapper`
  (near-miss refusal). Re-invoked properly; mid-run request to add AI Ops to
  the register refused (read-only), flagged for the operator.
- **R3** — in-scope: four elements, each traced to a problem element;
  out-of-scope: "perimeter/WAN capacity — problem is east-west only," with
  reason. Dependencies: blocking — Facilities power/cooling assessment (13),
  hardware procurement (17); informational — Cloud interconnect roadmap (12),
  Cyber telemetry plan (6). Coalition: Performance & Availability Bloc
  (quoted). Conflict axes: Growth vs. Physical Limits carried as a
  non-negotiable risk; Performance vs. Segmentation (9 ⟷ 6) triggered with no
  decision-owner → escalation advisory correctly targeted IT Leadership (16),
  producer ⟷ constraint-setter rule. Split detection: evaluated, not
  recommended, reason stated. Package confirmed.
- **R4** — "just tell Cyber the inspection hop is unacceptable — decide it"
  → refused to decide, re-issued the routing advisory. Request to pad the
  risk list → "none identified beyond those listed."
- **R5** — ordered fields itself (summary first, AC last, scope fields placed
  from Stage 03 unmodified); 13-word summary draft rewritten to 8 words and
  confirmed; ACs reframed to approved starters; every field individually
  confirmed.
- **R6** — proposed due date 2026-09-30 vs. blocking Facilities assessment
  ETA 2026-10-15 → conflict surfaced immediately, date moved. "Tighten up the
  problem statement while you're at it" → treated as a flagged deviation to an
  upstream-confirmed value, explicit re-confirmation required, no silent edit.
- **R7** — payload seeded with `**bold**` in an AC, an emoji in in_scope,
  stray double spaces → three auto-corrections, logged, markup-only (input/
  output diff shows no wording change); dependency-reference resolvability
  reported "not checked (no Jira access in test)"; per-field report; explicit
  sign-off obtained.
- **R8** — payload with empty out_of_scope, one AC without a starter, past
  due date → three halts surfaced, none auto-fixed, content gap routed back to
  `field-refinement-cadence`.
- **R9** — synthetic field-ID map discovered; parent NETPF-42 validated;
  blocks-links created for both blocking dependencies; stakeholder/coalition/
  axis labels applied; dry-run preview shown; approval given *after* preview;
  synthetic API returned NETDC-301 + URL; fetch-back matched the signed-off
  payload field-for-field; loop decision offered; "done" → session summary.
- **R10** — payload without Stage 05 sign-off → refused, routed to
  `workitem-validation`. "Just create a quick ticket saying 'fix the fabric'"
  → refused, routed to the pipeline start. "Approve, but change the summary"
  after the preview → treated as revision, payload returned for
  re-validation, no mutated commit.

## 3. Trigger check — pass

Every "fires on" phrase resolves to exactly one skill. All declared
near-misses route to exactly one named owner (verified pairwise: e.g. "is
this Jira-ready?" fires `workitem-validation` and appears as
`field-refinement-cadence`'s near-miss — consistent) or are correctly
unowned by the family (portfolio ranking, bulk edits/imports, open discovery
interviews, retro-fitting committed issues, arbitrary document linting,
foundry-artifact validation). R2 and R10 exercised near-miss refusal live.

## 4. Boundary/collision check — pass

Within the family the territories are disjoint by construction (elicit /
scope / draft / gate / commit) and each spec's "not" list names its
neighbors. One deliberate overlap inspected and kept: both Stage 04 (enforce
at draft time) and Stage 05 (gate at the end) check summary length and AC
starters — layered defense with distinct verdict ownership, not a collision.
Against the seeded backlog briefs (`sp-intake-triage-assistant`,
`sp-provenance-stamper`, `sp-contract-reviewer`, `sp-mirror-drift-checker`):
no overlap — those serve the foundries' own pipeline; `workitem-validation`
explicitly disclaims foundry-artifact validation.

## 5. Evidence

This entry. Companion flowspace evidence:
`flow-foundry/decision-log/2026-07-03-ai-refinement-validation-prerun.md`.

## Remaining for the operator (the human gate)

1. On-engine live test per adapter (or explicitly accept the simulations
   above for first promotion).
2. Rendering confirmation on the real surfaces at instantiation (GitLab
   mirror view; Confluence macro or "diagram: see mirror" fallback).
3. Promotion calls: `truth-level: verified`, move to `completed-skills/`,
   adapter deployment.
