---
id: decision-2026-07-28-portfolio-rationalization-triage-and-scaffold
title: "Decision Log — Portfolio Rationalization: Triage, Sanitization, and Scaffold"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-28
updated: 2026-07-28
owner: operator
source: human+ai
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[fp-portfolio-rationalization]]"
  - "[[close-score-model]]"
  - "[[objective-dictionary-template]]"
---

# Decision Log — 2026-07-28 — Portfolio Rationalization: Triage, Sanitization, and Scaffold

**What was decided:** build a new flowspace, `portfolio-rationalization`, from
an operator description of a working four-tab Jira portfolio-analysis workbook;
stage it in `../review-flowspaces/` at `truth-level: to-review`. **By whom:**
the operator — explicit instruction this session, with the four scoping
decisions below answered directly before any authoring began (`AGENTS.md`
rule 2 / `foundry-spec.md` §1 Step 0).

## Triage classification

**Case 4 — bare conversation, no formal starter** (`foundry-spec.md` §1). The
intent arrived as a prose description of an existing workbook's four tabs
(raw Jira export → exploration → objective mapping → portfolio analysis) plus a
stated repeatable logic flow and a request to build out a missing "Recommend"
step. Workable, per the spec, but the missing structure had to be backfilled
rather than skipped: the setup questionnaire was answered into
`../backlog-flow-starters/fp-portfolio-rationalization.md` so the scaffold has
a real intake record behind it.

Not case 3 (not flowspace-worthy): this recurs on a governance cadence, spans
multiple stages with distinct review intensities, and carries reusable Layer-3
capability — a flowspace, not a single skill and not a one-off project.

## Decisions

### 1. Sanitization — objective areas ship as a mold, not content

The source description named four real organizational objective areas and real
issue keys. Neither enters this repo (`AGENTS.md` rule 8). The flowspace ships
`reference/objective-dictionary-template.md` — a domain-neutral mold for
authoring objective areas, keyword sets, weights, and thresholds — instantiated
employer-side with the real areas. This mirrors the existing precedent,
`icp-flows/ai-refinement/reference/platform-stakeholder-register-template.md`.

All worked examples use synthetic `PORT-nn` keys and an invented objective area
("Reduce Unplanned Outage Exposure"). Stage 03 accordingly carries a hard
dependency it cannot degrade around: with no dictionary, it halts rather than
inferring objective areas, because an agent that invents them produces
confident, plausible, worthless mappings.

Consequence accepted: this flowspace cannot be run from this repo alone. That
is correct — it is a design, and the strategy content it needs belongs in
tenancy.

### 2. Six stages, splitting scoring from recommending

The source logic named five phases (Ingest, Explore, Align, Rationalize,
Recommend). The scaffold uses six, with two departures from a literal
transcription:

- **Intake gets its own stage** rather than folding into profiling. The
  live-Jira-or-export binding, the data-class screen, and the field-map
  confirmation are the cycle's trust boundary; every downstream number inherits
  what this stage gets wrong and none of them can detect it. It earns a heavy
  review gate of its own.
- **Scoring and recommending are separate stages.** Scoring is constrained
  execution against a written model; recommending applies a taxonomy, enforces
  the corroboration rule, and builds routable packets. Folding them would have
  hidden the corroboration enforcement inside the scoring step, where it is
  invisible.

**Stage 03 breaks the U-curve default** (heavy in the middle) with stated
cause, recorded here because it is the scaffold's one deliberate deviation:
objective mapping feeds 40 of the model's ~100 points, is the only input
encoding organizational strategy rather than observable Jira facts, and goes
stale between planning cycles with no visible symptom.

### 3. Read-only — no Jira write-back

The flow writes nothing to Jira at any stage. Its terminal output is a
governance review pack plus an assignee-routed outreach list; owners act on
their own items outside the flow, on their own authority.

`jira-commit` was considered and explicitly **not** reused: it creates and
updates single work items from a signed-off refinement payload, which is a
different operation from bulk portfolio action. Recorded here so the collision
question is settled rather than re-asked at the gate. Whether write-back is
ever wanted is carried as open question 5 in the primer brief; adding it would
be a new skill and a Stage 06 branch, not a tweak.

### 4. Layer-3 — five gaps flagged, five briefs filed, no skills built

Per `foundry-spec.md` §4 rule 3. Stages 01–05 are each `TBD — brief filed`;
Stage 06 is an inline one-off (its disposition capture is a human conversation
with a recording discipline attached, not an agent capability, and no reusable
skill was identified). Briefs filed to `../../skill-foundry/backlog-skill-starters/`:
`sp-jira-portfolio-ingest`, `sp-portfolio-profiler`,
`sp-objective-keyword-mapper`, `sp-closure-scorer`,
`sp-disposition-packet-builder`.

No skill was authored and no adapter generated — that is a separate
skill-foundry invocation requiring its own operator go-ahead.

### 5. Recommendation label renamed — `Closed` → `Close (recommended)`

**Proposed, not minted** (`AGENTS.md` rule 7); the operator ratifies or
reverts. The source taxonomy's top band was `Closed`, which reads as a Jira
status and invites the reading that the flow already closed something — which
it structurally cannot, having no write path. The other three labels are
carried verbatim from the source taxonomy.

### 6. Corroboration rule added to the scoring model

Not present in the source description, added because the source's own stated
principle — "do not close work simply because it is old" — was otherwise
carried only as prose advice. The rule blocks the two closure bands unless at
least three of five dimensions score above their midpoint, demoting rather than
hiding an item that fails it. Without it, a 500-day-old item with no objective
match reaches 75 on two dimensions alone and the principle becomes a slogan.

Flagged as a substantive addition to the operator's logic, not a transcription
of it.

## Notes and open items

- **Score calibration is unratified and stated as such** in
  `reference/close-score-model.md` §7, in the flowspace's Known gaps, and in
  Stage 04's process (which must declare it before presenting any score). The
  ramps were inferred from five described data points, not derived from the
  workbook's formulas; they reproduce the described top-ranked item at 101
  against an observed 102. Calibration against one real cycle is an operator
  gate before first live use.
- **The field-completion denominator is captured per cycle, not fixed.** The
  source used 216 columns; column counts vary by Jira configuration and export
  settings, so a fixed denominator silently changes meaning between cycles.
  Whether to further exclude always-empty system columns remains open
  (`reference/export-and-field-requirements.md` §4).
- **Gate status:** this build has not been through the three validation gates.
  Agent-side pre-checks were run (structural completeness, Layer-3 declaration,
  contract-seam quality against the populated-vs-present standard, and a
  hand-walked logic dry-run of three synthetic items through the scoring
  model). Promotion, placement in `../../icp-flows/`, and the
  `icp-flows/CONTEXT.md` catalog row remain the operator's acts — the foundry
  never self-promotes (`AGENTS.md` rule 5, `foundry-spec.md` §5).
- **Nothing has run on-engine.** No adapter exists for any of the five skills,
  and no cycle has been executed against real portfolio data.
