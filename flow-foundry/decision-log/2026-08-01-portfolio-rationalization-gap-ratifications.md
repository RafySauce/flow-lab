---
id: decision-2026-08-01-portfolio-rationalization-gap-ratifications
title: "Decision Log — Portfolio Rationalization: Label-Rename Ratification and Field-Completion Denominator Redesign"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[close-score-model]]"
  - "[[export-and-field-requirements]]"
  - "[[jira-portfolio-ingest]]"
  - "[[portfolio-profiler]]"
  - "[[decision-2026-07-28-portfolio-rationalization-triage-and-scaffold]]"
---

# Decision Log — 2026-08-01 — Portfolio Rationalization: Label-Rename Ratification and Field-Completion Denominator Redesign

**What was decided:** two of the four open items in `HUB.md`'s Known gaps were
operator-ratified this session; the other two (score calibration, objective
dictionary) remain open because both require real cycle data or operator
authorship that doesn't exist yet — untouched here. **By whom:** the operator,
answering directly.

## 1. Recommendation label rename — ratified

**Question:** the source taxonomy's top band was `Closed`; this design
proposed renaming it `Close (recommended)` (`close-score-model.md` §4,
proposed 2026-07-28) because `Closed` reads as a Jira status this flow cannot
actually set. Ratify or revert?

**Answer:** ratify. `Close (recommended)` stands as final, not proposed.

**Changes made:**
- `reference/close-score-model.md` §4 — naming note reworded from "awaiting
  operator ratification" to ratified, citing this entry.
- `HUB.md` Known gaps — "pending ratification" entry reworded to "ratified
  2026-08-01."

No arithmetic, band thresholds, or other model content changed — this was a
label-only ratification.

## 2. Field-completion denominator — redesigned, not just decided

**Question carried from the intake brief** (`export-and-field-requirements.md`
§4, as of 2026-07-28): the denominator for per-item field-completion
percentages was the raw column count of whatever source a cycle used. Whether
to additionally exclude always-empty system columns — comparable across
cycles, still not across Jira configurations, since a 216-column and a
90-column portfolio would still disagree on what a column even is.

**Answer given:** neither option as framed. The operator wants the denominator
built from **the required/canonical fields this flow actually reads**, not
from whatever columns happen to be in the source at all.

**Why this is stronger than either original option:** excluding always-empty
columns is still keyed to the source's own column layout, so it only ever
closes the cross-cycle comparison. Pegging the denominator to
`export-and-field-requirements.md` §2's canonical field set (Issue key through
Labels — 19 fields, all currently "used by" at least one stage) removes the
source's arbitrary structure from the arithmetic entirely: a raw export's
custom fields, workflow scaffolding, and integration metadata the flow never
reads no longer inflate or deflate the denominator, in *any* configuration.
Two cycles now denominate against the same fixed ceiling, and a completion
shift is either a real change in how thoroughly tickets are filled out, or a
visible change in which canonical fields this instance's Jira exposes at all
— never a silent artifact of the source having a different column count.

**Mechanics:** the denominator for a cycle is the count of §2's canonical
fields that Stage 01's field-mapping step actually resolves for that cycle
(≤19; fewer only when a canonical field is genuinely unmapped, which the
field-availability report already tracks). Per-item numerators are unchanged
— still populated-field count against that denominator, same rule as before.

**Changes made:**
- `reference/export-and-field-requirements.md` §4 — denominator rule rewritten
  (raw column count → resolved canonical-field count); the "open question"
  callout replaced with a resolved note pointing here. `artifact-version`
  1.1 → 1.2.
- `produced-skills/jira-portfolio-ingest/SKILL.md` — step 9 (denominator
  capture) and the export-mode header-row note (step 3) reworded; Review
  criterion 9 reworded. `artifact-version` 1.1 → 1.2. Both adapters
  (`copilot-prompt.md`, `rovo-agent.md`) updated to match and re-stamped
  `v1.2`.
- `produced-skills/portfolio-profiler/SKILL.md` — Method step 1's worked
  example and the `44 of 216` completion example updated to the
  canonical-field framing (`44 of 19`). `artifact-version` 1.1 → 1.2. Both
  adapters updated and re-stamped `v1.2`.
- `icp-flows/portfolio-rationalization/01-intake-and-source-binding/CONTEXT.md`
  (Stage 01 — step 9 and the Outputs table) and
  `02-portfolio-profiling/CONTEXT.md` (Stage 02 — Inputs table and step 1, 7)
  — same rewording, kept in lockstep with the produced skills they mirror.
- `icp-flows/portfolio-rationalization/HUB.md` — "Field-completion
  denominator, unresolved" gap entry reworded to "resolved 2026-08-01,"
  citing this entry.
- `icp-flows/portfolio-rationalization/decision-log/CONTEXT.md` — dropped the
  completion-denominator choice from the "instantiation-time decisions" list;
  it's fixed at design time now, not a per-instance call.

**What did not change:** `close-score-model.md` §3.4 (the low-field-completion
scoring ramp, 0–10 points on the resulting percentage) — the ramp's math reads
whatever percentage Stage 02/04 hand it and doesn't care how the denominator
was built, so no change was needed there.

## Status of the other two open items

Untouched by this decision, per the operator's direction — both still need
inputs this session doesn't have:

- **Score calibration** (`close-score-model.md` §7) — needs a real cycle's
  data to calibrate the ramps and band thresholds against. Still every number
  in that file is a proposal.
- **Objective dictionary** (`objective-dictionary-template.md`) — still needs
  either operator authorship or an inferred-and-confirmed instance run; the
  Stage 3 inference-and-pivot fork already handles the "nothing supplied"
  case, unchanged here.

## Notes

- This is a design-time decision on public design copy — no instance exists,
  no real portfolio data was touched, nothing ran on-engine.
- `jira-portfolio-ingest` carries `truth-level: verified` already (gated
  2026-08-01 on a simulated end-to-end run per
  `skill-foundry/decision-log/2026-08-01-portfolio-rationalization-skill-batch-promotion.md`).
  This change edits a verified skill's behavior; it does not itself re-run the
  five-point gate. The skill's on-engine test is already marked pending in
  `HUB.md` — the first on-engine run should exercise the new denominator rule
  as part of that pending test, not as an additional one.
- `portfolio-profiler` reads the denominator; it does not compute it. Its
  changes here are wording/example-only, consistent with that boundary.
