---
id: decision-2026-07-03-ai-refinement-skill-batch
title: "Decision Log — AI Refinement Skill Batch Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
data-class: public
related: ["[[ai-refinement]]"]
---

# Decision Log — 2026-07-03 — AI Refinement Skill Batch Build

**What was decided:** author the five skills demanded by the `ai-refinement`
flowspace's Layer-3 triage — `context-elicitation`, `scope-dependency-mapper`,
`field-refinement-cadence`, `workitem-validation`, `jira-commit` — each as an
engine-neutral `SKILL.md` plus Rovo and Copilot adapters, staged in
`backlog-skill-starters/` at `truth-level: to-review`. **By whom:** agent, on
operator instruction; nothing promoted, nothing deployed. **What it affects:**
the skill-foundry backlog and the flowspace's Layer-3 pointers (gap → referenced
skill).

**Intake path:** clean — all five arrive from `sp-*` primer briefs filed by the
flow-foundry's demand loop; no foreign material, so no vetting checklist run.

**Alternatives considered:** leaving the briefs unfilled (rejected — the
operator asked for the underlying skills); one mega-skill driving stages 2–6
(rejected — boundary discipline: elicit / scope / draft / gate / commit are
distinct territories, and the gate (`workitem-validation`) and the writer
(`jira-commit`) especially must not share a boundary with the drafting skills).

**Notable calls:**
- Skill ids drop the `skill-` prefix the flowspace originally used, matching the
  house `sp-<slug>` → `<slug>/SKILL.md` pattern; flowspace contracts updated.
- Copilot surface: prompt file for all five (command-shaped triggering intent
  per the adapter's rule of thumb), not custom agents.
- Write actions: only `jira-commit` gets any (create/update issue, create issue
  link, minimum set) — the other four specs don't state that they write, so
  their Rovo adapters carry no write actions.
- The stakeholder register (`platform-stakeholder-register`, claimed clipping in
  the flowspace's `reference/`) is consumed read-only by `context-elicitation`
  (stakeholder sweep) and `scope-dependency-mapper` (coalition/conflict-axis
  annotation, escalation routing).
- Boundary/collision first pass against the seeded backlog briefs
  (`sp-intake-triage-assistant`, `sp-provenance-stamper`, `sp-contract-reviewer`,
  `sp-mirror-drift-checker`): no territory overlap found — those serve the
  foundries' own pipeline, these serve a work-item refinement run. Formal
  collision check re-runs at the five-point promotion gate.

**Next:** operator review per foundry-spec §5 — spec review, live test per
adapter on synthetic data, trigger check, collision check, evidence entry —
then human placement in `completed-skills/` and adapter deployment.
