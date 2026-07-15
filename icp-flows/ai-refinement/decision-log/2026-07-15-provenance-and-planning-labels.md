---
id: decision-2026-07-15-provenance-and-planning-labels
title: "Decision Log — Provenance and Planning Labels; Value-Delivery Decomposition Handoff"
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
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
  - "[[work-item-schemas]]"
  - "[[jira-commit]]"
  - "[[workitem-validation]]"
---

# Decision Log — 2026-07-15 — Provenance and Planning Labels; Value-Delivery Decomposition Handoff

**What was decided:** stamp every item this pipeline commits with
`refine-ai-built` (provenance) and, for feature-level-and-below types, a
`<team_code>-<yyyy>-q<n>` planning label (Workstream A — built in this
change); scope, ground, and defer a top-down value-delivery decomposition
capability to a follow-up build (Workstream B — designed, not built, in this
change). **By whom:** agent, on operator instruction, following a round of
clarifying questions answered 2026-07-15 (the interactive question tool
failed mid-session; questions and answers were exchanged as plain text — see
the session transcript). **What it affects:**
`reference/ai-refinement-hybrid.md` (1.1 → 1.2), Stage 01 `CONTEXT.md`
(1.7 → 1.8), Stage 05 `CONTEXT.md` (1.3 → 1.4), Stage 06 `CONTEXT.md`
(1.7 → 1.8), `reference/work-item-schemas.md` (1.3 → 1.4), the `jira-commit`
skill (1.6 → 1.7, stays `to-review`) and its adapters, the
`workitem-validation` skill (1.1 → 1.2, `verified` → `to-review`) and its
adapters, `HUB.md`, and a new skill primer brief,
`skill-foundry/backlog-skill-starters/sp-value-decomposition.md`.

## Workstream A — the change

1. **`refine-ai-built` is unconditional.** Every committed item, every type,
   every mode, carries this literal lowercase label — no exemption, no
   configuration.
2. **The planning label gates feature level and below only.** Operator
   feedback narrowed the original brief's "every item" framing: `feature`,
   `story`, `task`, `spike`, `bug` require the `<team_code>-<yyyy>-q<n>`
   label; `portfolio_epic`/`solution_epic` — multi-year/multi-quarter outcome
   horizons — are exempt from the gate (one may still be attached if a
   quarter is volunteered for them, but its absence is not checked). This
   reads directly off the value-delivery deck's own lifecycle table (the
   operator-provided "Value Delivery — Key Concepts, a 30,000ft View" deck):
   its Portfolio Epic/Solution Epic/Feature rows already treat Feature as the
   quarter-scoped delivery unit, epics as outcome-level framing above it.
3. **team_code is inferred live, not fixed at instantiation.** The original
   brief's recommended default (a static `team_code` set once in
   instantiation config) was superseded by direct operator instruction: Stage
   01 instead queries the target Jira project/space live for existing labels
   matching — or closely resembling — the `<code>-<yyyy>-q<n>` shape,
   proposes the distinct code(s) found as candidates (with the matching
   labels as rationale), and falls back to asking the user directly only if
   none exist. This mirrors the `parent_mapping_confirmation` house
   amendment's discipline exactly: query live, present candidates, the user
   confirms or overrides — never a silently-assumed value, whether from a
   config file or from the query itself.
4. **Enforcement is warn-and-bypass, not a hard halt.** Both labels are
   checked at Stage 05 as a new, distinct mandatory-label check (separate
   from schema completeness, since labels aren't schema fields). A missing or
   malformed label warns the user with the specific defect and offers an
   explicit override to proceed uncorrected — the one check in Stage 05's
   gate that isn't a hard stop. This is a deliberate softer tier than the
   existing halt/auto-correct split: governance/traceability labels
   shouldn't block an otherwise-ready item from an operator who consciously
   accepts the gap, but the gap must never pass silently — every bypass is
   named in the validation report and re-surfaced (not silently resolved) in
   Stage 06's dry-run preview.
5. **The planning quarter is session-scoped with a per-item override.**
   Elicited once at Stage 01 ("What quarter do you plan to do this work?"),
   normalized from free text to the canonical `<yyyy>-q<n>` form, applied to
   every gated item by default; Stage 06's dry-run preview offers a per-item
   override for the rare item that targets a different quarter than the
   session default.
6. **Acceptance criteria stays a hard gate, unaffected by any of the
   above.** The operator explicitly reaffirmed this while answering the
   Workstream B questions (see below) — recorded here because it bears on
   how the mandatory-label warn-bypass tier is scoped: the softer
   enforcement is specific to the two new labels, never generalized to any
   existing schema-required field.

## Decisions and alternatives

1. **Live inference over fixed config for `team_code`.** *Alternative
   considered (and originally recommended):* a static `team_code` set once
   in an instantiation config, asked only if unset. *Rejected* by direct
   operator instruction in favor of a live query — the flowspace already has
   a proven query-then-confirm mechanism (`parent_mapping_confirmation`);
   reusing it for a label avoids introducing a second "trust config blindly"
   pattern alongside the existing "always confirm live state" one. **Owed:**
   the query's fuzzy-match tolerance ("existing labels that match or are
   close to the format") isn't fully specified — see Assumptions, below.
2. **Planning-label gate scoped to feature-and-below, not "every item."**
   *Alternative considered:* gate all seven refinable types uniformly (the
   original brief's framing). *Rejected*: operator feedback narrowed this to
   where it's actually meaningful — quarter-scale planning fits Feature and
   its children; it doesn't fit a portfolio/solution epic's multi-year
   horizon. `refine-ai-built` stays universal because provenance (was this
   AI-refined?) is a fact about every item regardless of horizon; the
   planning quarter is not.
3. **Warn-and-bypass over a hard halt.** *Alternative considered (and
   originally recommended):* Stage 05 halts sign-off on any missing/malformed
   label, identical to a missing schema field. *Rejected* by direct operator
   instruction: enforce, but warn and allow an explicit bypass. This is a new
   halt tier for Stage 05 — previously a strict two-way auto-correct/halt
   split — introduced deliberately narrowly (only the mandatory-label check
   moves into it; every other check keeps its existing tier).
4. **`workitem-validation` demotes from `verified` to `to-review`.** This is
   the first behavior change to this skill since its initial promotion
   (2026-07-03) — it had stayed `verified` through every other flowspace
   revision to date. Consistent with how every other touched skill/artifact
   in this flowspace has been demoted on a genuine behavior change (see the
   2026-07-07 decision logs), this is an honest gap, not a simulated pass:
   the new mandatory-label check and its warn-bypass tier have not run
   on-engine.

## Assumptions (operator to confirm or amend)

- **D1 — Live-query fuzzy-match tolerance is unspecified.** The operator
  asked for inference from "existing labels that match or are close to the
  format" — this decision reads that as tolerating different separators and
  casing (e.g. `DDI_2026_Q4`, `ddi-2026-Q4`) but does not fix an exact
  matching algorithm. Amendment path: ratify a specific tolerance (or an
  explicit non-goal — e.g., "case-insensitive, hyphen-only") at
  instantiation, once the real target project's existing label conventions
  are visible.
- **D2 — `portfolio_epic`/`solution_epic` exemption is a gate exemption, not
  a prohibition.** The amendment text allows attaching a planning label to an
  epic-level item if the user volunteers a quarter for it; Stage 01 does not
  proactively ask for one at that level. Amendment path: if the operator
  wants epics to also carry an informational (ungated) quarter by default,
  Stage 01's elicitation step would need a second, softer prompt for those
  two types — not built here, since the operator's answer ("really only
  matters for features") reads as opt-in, not opt-out.
- **D3 — Warn-and-bypass is scoped to exactly one check.** This decision
  deliberately does not extend the new tier to any other Stage 05 check
  (e.g., due date, AC starters). Amendment path: if operator experience shows
  another check would benefit from a bypass tier, that is a new decision, not
  an implicit extension of this one.

## Workstream B — value-delivery decomposition (handoff, not built)

Per operator instruction, this change implements Workstream A only. The
value-delivery decomposition capability — reading the operator-provided
"Value Delivery — Key Concepts, a 30,000ft View" deck (Stakeholder Persona
Value Statements, MVP thinking, the Hamburger Method's vertical-vs-horizontal
slicing, and the deck's Portfolio Epic/Solution Epic/Feature lifecycle table)
against the flowspace's current bottom-up-only hierarchy — is captured as a
skill primer brief for a future skill-foundry build, not implemented now.

**Answers gathered 2026-07-15, carried into the primer brief:**

- **Scope now:** Workstream A only, in this change; Workstream B is a
  follow-up.
- **Depth:** one hierarchy level per decomposition pass (e.g. Solution Epic →
  Features), agent proposes and discusses with the user, defaulting to
  one-level-per-pass; the user may also say they aren't ready to decompose
  this level yet and stop with nothing created.
- **Deck concepts → validation, not just heuristics:** the persona
  value-statement format should be *validated* (not just drafted-to) for
  `portfolio_epic`, `solution_epic`, `feature`, `story`, and `spike` — noting
  that for `story` and `spike` the value content may need to be checked
  against a different field than `customer_business_value` in practice.
  Features (and, by extension, similarly technical work) may elect a more
  technical/project-driven framing instead of the persona-statement format
  when the underlying work is inherently sequencing-heavy (software/OS
  upgrades, hardware design breakdowns) — `bug` and `task` are already
  accepted as technically worded and need no exception. Acceptance criteria
  remains a hard gate for every work item regardless of framing.
- **Integration point:** a new produced skill (`value-decomposition`),
  invoked from Stage 01 when the user indicates a desire to do a full
  decomposition of the selected parent-level item.

Full detail: `skill-foundry/backlog-skill-starters/sp-value-decomposition.md`.
This brief is intake, not a spec — the skill-foundry still owes it a full
`SKILL.md`, adapters, and a gate pass before it can run.
