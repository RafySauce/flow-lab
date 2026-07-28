---
id: decision-2026-07-28-portfolio-rationalization-skill-batch
title: "Decision Log — Portfolio Rationalization Skill Batch Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-07-28
owner: operator
source: human+ai
data-class: public
related:
  - "[[sp-jira-portfolio-ingest]]"
  - "[[sp-portfolio-profiler]]"
  - "[[sp-objective-keyword-mapper]]"
  - "[[sp-closure-scorer]]"
  - "[[sp-disposition-packet-builder]]"
  - "[[portfolio-rationalization]]"
---

# Decision Log — 2026-07-28 — Portfolio Rationalization Skill Batch Build

**What was decided:** author all five backlog starters filed from the
`portfolio-rationalization` flowspace's Layer-3 scaffold triage —
`jira-portfolio-ingest`, `portfolio-profiler`, `objective-keyword-mapper`,
`closure-scorer`, `disposition-packet-builder` — each as an engine-neutral
`SKILL.md` plus **both** adapters, staged in `review-skills/` at
`truth-level: to-review`. **By whom:** agent, on operator instruction ("let's
build the available backlog skill starters so we can test the portfolio
rationalization flow end to end in rovo"). **What it affects:** five new
folders under `review-skills/`; the five `sp-*` primer briefs stay unchanged in
the backlog as intake records. Nothing promoted, nothing moved to
`../../produced-skills/`, nothing deployed to an engine.

**One edit outside the foundry, disclosed:** the flowspace HUB's "Known gaps"
section said "All five Layer-3 dependencies are unbuilt … no skill has been
authored." That statement became false with this batch, so the gaps paragraph
and its status table were corrected to "built — staged in `review-skills/`, not
promoted," with the on-engine gap and the open gate stated. **Nothing else in
the flowspace was touched:** the stage contracts' `Layer-3: TBD — brief filed`
lines and the HUB stage table stand as written, because those flip at
promotion, which is the operator's call. If the operator would rather the
flowspace stay frozen until promotion, revert that one section.

**Intake path:** clean for all five — each arrives from an `sp-*` primer brief
already sitting `to-review` in the backlog, filed by the flow-foundry during
the flowspace scaffold
(`flow-foundry/decision-log/2026-07-28-portfolio-rationalization-triage-and-scaffold.md`).
No foreign material, no vetting checklist run.

**Scope reading — "available" is the whole backlog here.** Unlike the
2026-07-15 documentarian batch, no starter in `backlog-skill-starters/` is
`status: dead` or deferred at filing: the folder holds exactly these five, all
`living` / `to-review`. Nothing was excluded.

**Stage 06 remains skill-less by design.** The flowspace's own Stage 06
contract declares `Layer-3: inline (one-off)` — the disposition taxonomy and
capture protocol are a human conversation with a recording discipline attached,
not an agent capability. No sixth skill was invented to fill the row.

## Notable calls

- **The corroboration rule is split across two skills, deliberately.**
  `closure-scorer` computes the count (how many of the five dimensions score
  strictly above their midpoint, and which) and **does not demote**;
  `disposition-packet-builder` enforces the demotion and states it in plain
  language in the packet. The briefs required both halves and named the split
  failure mode — computing the rule upstream and not enforcing it downstream —
  as the outcome the flow exists to prevent. Both specs name the other side of
  the split, and the scorer's worked demotion example shows the count it owes
  downstream rather than a band it must not assign.
- **Both adapters for all five — the documentarian batch's write-path split
  does not bite here.** That batch gave Rovo-only adapters to skills whose
  every write was Atlassian-side. This flow has **no write path at any stage**,
  so no adapter can be excluded on write grounds. Assignment falls back to the
  `adapter-rovo.md` rule: engine per where the invoking users work and which
  external systems the skill touches. Only Stage 01 touches an external system
  at all, and it does so read-only — so the Rovo adapters carry native Jira
  search on `jira-portfolio-ingest` and **no permitted actions whatsoever** on
  the other four, and the Copilot adapters lead with export mode where Rovo
  leads with live mode. Same spec, same logic, different primary path.
- **`objective-keyword-mapper`'s Rovo adapter carries a deployment constraint
  header, not just a data-boundary line.** The dictionary may be classified
  higher than the portfolio it maps — objective-area statements are often
  `internal` or `confidential` strategy content — so the agent must be
  published only in a tenancy sanctioned for the *dictionary's* class. This is
  the one skill in the batch whose engine routing may end up narrower than the
  rest of the flow's, and burying that in the spec body would have let it be
  missed at publish time.
- **The two hard external dependencies are stated in the specs rather than
  designed around.** `objective-keyword-mapper` halts if no instance dictionary
  exists (objective areas cannot be inferred — an invented area carries up to
  40 closure points), and `closure-scorer` states calibration status unprompted
  because the model's ramps are unratified (`close-score-model.md` §7). Both
  are operator gates before a real cycle, not build gaps: see "What is still
  needed before an end-to-end run" below.
- **Boundary/collision first pass** against the thirteen produced skills:
  `jira-portfolio-ingest` ↔ `jira-accomplishments-gatherer` is the closest pair
  (shared live-query-with-paste-degrade pattern, disjoint unit of analysis —
  portfolio vs. one engineer's own record; both name each other);
  `jira-portfolio-ingest` and `disposition-packet-builder` ↔ `jira-commit`
  (commit creates refined items and is explicitly *not* the route for bulk
  portfolio actions — both new specs say so and decline rather than routing);
  `objective-keyword-mapper` ↔ `context-elicitation` (mapping reads wording,
  elicitation improves it); `closure-scorer` ↔ `workitem-validation` (a
  completeness gate on one refined item, a different schema family and a
  different unit). Among the five themselves: disjoint by stage and by artifact
  — normalized set → profile → mapping record → scored ranking → routed pack —
  with the one shared surface, the corroboration rule, split explicitly in both
  specs. Formal collision check re-runs at the promotion gate; pre-run evidence
  in the companion entry,
  `2026-07-28-portfolio-rationalization-skill-gate-prerun.md`.

## What is still needed before an end-to-end run

Recorded here because the instruction's stated purpose was an end-to-end Rovo
test, and three of these are operator acts no build can supply:

1. **An instance objective dictionary.** Stage 03 halts without one, by design.
   The public repo carries only the mold (`AGENTS.md` rule 8).
2. **The instance status→adjustment mapping** for `closure-scorer`, recorded in
   the instance decision log; unmapped statuses score 0 and are flagged.
3. **Calibration ratification** (or an explicit decision to run provisional —
   the skills state the status either way).
4. **Five published Rovo agents** from the `adapters/rovo-agent.md` copies of
   record, plus a synthetic/`public` portfolio to test against. Promotion and
   deployment are the operator's, per `foundry-spec.md` §5.

**Next:** operator review per `foundry-spec.md` §5 — see the companion
gate-pre-run entry for what is already checked agent-side and what remains
open.
