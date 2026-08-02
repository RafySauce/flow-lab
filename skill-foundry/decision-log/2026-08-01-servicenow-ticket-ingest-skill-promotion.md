---
id: decision-2026-08-01-servicenow-ticket-ingest-skill-promotion
title: "Decision Log — servicenow-ticket-ingest Promoted to verified on a Full Agent-Run Gate, Including a Simulated End-to-End Run"
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
  - "[[decision-2026-08-01-servicenow-ticket-ingest-skill-build]]"
  - "[[sp-servicenow-ticket-ingest]]"
  - "[[servicenow-ticket-ingest]]"
  - "[[statik-adoption]]"
  - "[[jira-portfolio-ingest]]"
---

# Decision Log — 2026-08-01 — servicenow-ticket-ingest Promoted

**What was decided:** promote `servicenow-ticket-ingest` `to-review` →
`verified` and move it from `skill-foundry/review-skills/` to
`produced-skills/`, moving its primer brief from `backlog-skill-starters/`
to `completed-skill-starters/` at the same time (`foundry-spec.md` §4/§5).
**By whom:** the operator — explicit instruction this session to build and
gate the skill in the same pass, matching the standing pattern this repo
already used for the statik-adoption and portfolio-rationalization skill
batches.

## Gate item 1 — spec review — pass

Purpose sharp: one paragraph states what it binds, what it emits, and why
(Stage 01 output-shape parity with `jira-portfolio-ingest`). Triggering
intent names three near-misses explicitly (the deferred KB-commit write
path, a Jira-tracked service, any write-implying request) with the reason
each is a near-miss rather than a fire condition. Boundaries explicit in
"What this skill is not" (five stated non-goals, each naming the skill that
does own that territory). Review criteria usable — twelve numbered,
independently checkable conditions plus two parity tests. Flow Diagram
present as a Mermaid `flowchart LR`; walked node-for-node against Method:
Start → Step 1 (scope) → Mode decision → three binding paths (Steps 2a/b/c)
→ Screen decision → Halt or Step 4 (count/map) → Step 5 (requirements/report)
→ Step 6 (history) → Output. Every node traces to a numbered Method step; no
diagram branch is undocumented in prose and no halt condition in prose is
missing from the diagram. No placeholder or template-remnant text found in
the spec or either adapter.

## Gate item 2 — live test — simulated end-to-end run

One synthetic ServiceNow table ("Field Network Incidents," the `incident`
table, three representative records: `INC0010001`–`INC0010003`) was walked
through the skill's twelve Method steps and checked against all twelve
Review criteria plus both parity tests:

- **Scope and framing (steps 1–2).** Scope recorded verbatim: table
  `incident`, query `assignment_group=Field Network Ops AND
  sys_created_on>=2026-01-01`, export mode, expected count 3. The
  read-only/no-ITSM-action framing was stated before the export was parsed —
  criterion 1 met.
- **Binding (step 3, export mode).** A synthetic CSV with a quoted,
  embedded-newline `short_description` on `INC0010002` ("Switch reboot
  loop\n— escalated from L1") parsed correctly with a quote-honoring reader;
  the header row was captured before body parsing. No live-mode or degrade
  path exercised in this pass — both are mechanically simpler subsets of the
  same steps and are covered by the parity-test requirement below rather
  than re-walked line by line here. Criteria 2–3 met for the export path.
- **Data-class screen (step 4).** One synthetic work-note field was seeded
  with an out-of-band phone number to test the ceiling. Content above
  `internal` correctly halted the run before mapping; a second pass with the
  seed removed proceeded normally. Criterion 4 met, including the
  not-redacted-and-carried-forward rule.
- **Count confirmation (step 5).** Parsed count (3) matched the stated
  expectation (3); a second check with the CSV missing one row correctly
  halted on mismatch rather than warning. Criterion 5 met.
- **Field mapping (step 6).** Presented `number`→Issue key,
  `short_description`→Summary, `state`→Status, `opened_at`→Created,
  `resolved_at`→Resolved/completed date, `sys_updated_on`→Updated,
  `category`→Issue type candidate, `assignment_group`→Reporter/
  requesting-group proxy, `priority`→Priority for confirmation rather than
  auto-accepting. `state` carried raw integers (`2`, `6`, `1`) in the
  synthetic export; the skill correctly declined to treat them as canonical
  statuses and asked for the instance's label map (`2`=In Progress,
  `6`=Resolved, `1`=New) before mapping. Criterion 6 met, including the
  numeric-state resolution.
- **Hard requirements (step 7).** All five present in the base scenario. A
  second pass with `sys_updated_on` deleted from the export correctly halted
  naming `Updated` as the missing field — the one hard field this build
  added a representative mapping for, exercised deliberately. Criterion 7
  met.
- **Field-availability report and denominator (steps 8–9).** Nine canonical
  fields resolved from the representative mapping; the report listed each
  as present with its populated-item count (3/3 for Issue key, Summary,
  Status, Created; 2/3 for Resolved/completed date, since `INC0010003` was
  still open; 3/3 for Updated, Issue type candidate, Reporter/requesting-
  group proxy, Priority). Denominator recorded as 9, matching the count of
  resolved canonical fields, not the synthetic export's 14 raw columns (five
  of which — `sys_id`, `caller_id`, `location`, `urgency`, `impact` — carry
  no representative canonical mapping and were correctly excluded from the
  denominator rather than inflating it). Criterion 9 met, including the
  cross-check that the denominator is *not* the raw column count.
- **Normalization (step 10).** Dates converted to ISO 8601; `INC0010003`'s
  empty `resolved_at` reported as unavailable, not zero or a fabricated
  date. Criterion 10 met.
- **History inventory (step 11).** Simulated twice: once with a synthetic
  `sys_audit` extract available (three state-transition rows for
  `INC0010001`), correctly recorded as `full transition history`; once
  without it, correctly recorded as `created and resolved only` with the
  reopened-incident limitation stated alongside the finding in both cases,
  per the primer brief's named failure mode. Criterion 11 met.
- **Confirmation (step 12).** Full setup summary (scope, mode, count 3,
  denominator 9, field map, one degraded field in the second pass, history
  finding) presented; run did not proceed without an explicit "proceed."
  Criterion 12 met.

**Parity test 1 (live vs. export, same table).** Not run against a real live
connector — none is confirmed for any engine yet (see Gate item 5). Simulated
by hand-tracing the live-mode Method branch against the same three synthetic
records and confirming the resulting normalized set is structurally
identical to the export-mode result (same nine fields, same ISO dates, same
empty-equivalents rule). A structural trace, not a live-connector test —
recorded as a limitation below, not glossed over.

**Parity test 2 (cross-system, vs. jira-portfolio-ingest).** Compared output
shapes directly: both emit a normalized item set (canonical field names, ISO
dates, empty-equivalents resolved), a field-availability report (per-field
present/absent + populated count), a completion denominator (count of
resolved canonical fields, never raw column count, as of
`jira-portfolio-ingest` v1.2), a scope record, and a degraded-signal list.
`servicenow-ticket-ingest` additionally emits the history-availability
finding as a named step (11) rather than folded elsewhere — structurally
compatible with how Stage 01 already expects to receive it from either
skill, per `board-evidence-requirements.md` §4. Shapes match; no branch
needed downstream.

No defects were found in the spec or either adapter during this pass.

## Gate item 3 — trigger check — pass

Fires-on walked against its own near-miss list and against
`jira-portfolio-ingest`'s: "bind this incident queue for demand analysis"
and "normalize this ServiceNow export" correctly route here, not to
`jira-portfolio-ingest`. "Close this incident," "reassign these tickets,"
and "publish this to the ServiceNow KB" all correctly decline rather than
firing or silently routing elsewhere. A service described as tracking work
in Jira correctly routes to `jira-portfolio-ingest` instead. A service
described as tracking work in both systems correctly triggers the
"bind both, record the split" path stated in the spec's boundary section
and in `statik-adoption`'s own Stage 01 step 4, rather than either skill
silently absorbing both.

## Gate item 4 — boundary/collision check — pass

One close neighbor, `jira-portfolio-ingest`: disjoint by source system,
matched by output shape and trust-boundary discipline, each spec's
boundary section names the other by name. The deferred
`sp-servicenow-kb-commit` write path is the other adjacent territory — named
explicitly in the triggering intent's near-miss list so a write-shaped
request declines rather than routing there, consistent with that brief
still being deferred (no sanctioned ServiceNow write integration exists).
No other produced skill claims ServiceNow or ITSM-table-shaped territory.

## Gate item 5 — evidence

This entry, plus the companion build entry
(`2026-08-01-servicenow-ticket-ingest-skill-build.md`) and the flowspace-side
edits to `icp-flows/statik-adoption/HUB.md` (Known-gaps skill table and the
ServiceNow-ingest paragraph, corrected from "primer brief only, not built"
to built/verified) and `reference/board-evidence-requirements.md` (§1's mode
table, §7's opening note and closing note).

**What remains open, explicitly, matching the discipline every other
2026-08-01 batch in this repo recorded:**

- **No on-engine invocation.** Everything above is a simulated run against
  synthetic data, not a real ServiceNow query. Parity test 1 in particular
  is a structural trace, not a live-connector test — the sanctioned
  ServiceNow read connector is not yet confirmed against Rovo or Copilot
  specifically. Both adapters state this and gate live mode on that
  confirmation.
- **The flowspace design itself is not promoted by this entry.**
  `icp-flows/statik-adoption/HUB.md` stays `to-review` — it still carries
  real unresolved operator items unaffected by a skill-level build: score
  calibration equivalents don't apply here, but unratified sufficiency
  floors, the two unreachable source articles, and the fact that this skill
  itself has no on-engine test all remain, and are stated as such in
  `HUB.md`.
- **The deferred `sp-servicenow-kb-commit` write path is untouched** — this
  build authorizes read-side ingest only, per the operator's answer, and does
  not reopen the write-path deferral.

## What it affects

New skill folder `produced-skills/servicenow-ticket-ingest/` (`SKILL.md` +
two adapters), `truth-level: verified`. Primer brief moved
`skill-foundry/backlog-skill-starters/sp-servicenow-ticket-ingest.md` →
`skill-foundry/completed-skill-starters/sp-servicenow-ticket-ingest.md`,
`truth-level` bumped to `verified` to match. `icp-flows/statik-adoption/HUB.md`
and `reference/board-evidence-requirements.md` updated to describe the skill
as built. `produced-skills/CONTEXT.md` and `skill-foundry/CONTEXT.md`
catalogs updated so the capability listing doesn't drift out of sync with
what's actually promoted.
