---
id: fp-portfolio-rationalization
title: "Flow Primer Brief — Jira Portfolio Rationalization"
type: flow-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-07-28
owner: operator
source: human+ai
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[decision-2026-07-28-portfolio-rationalization-triage-and-scaffold]]"
---

# Flow Primer Brief — Jira Portfolio Rationalization

> Intake path 4 for the flow-foundry, backfilled: this arrived as a bare
> conversation (an operator description of a working four-tab analysis
> workbook), not as a formal starter. Per `foundry-spec.md` §1 case 4 that is
> workable — the setup questionnaire is answered here rather than skipped, so
> the scaffold has a real intake record behind it. Triage rationale:
> `../decision-log/2026-07-28-portfolio-rationalization-triage-and-scaffold.md`.

## Purpose

Turn a whole Jira project or space — not one work item — into a prioritized,
evidence-carrying portfolio review pack: which items deserve human scrutiny for
closure, merge, rewrite, or re-scope, and why. It replaces a hand-built
spreadsheet whose logic lived in whoever made it, and it runs on a recurring
governance cadence rather than once.

The flow's governing principle, stated by the operator and encoded in the
scoring model: **do not close work simply because it is old.** Closure pressure
comes only when multiple weak signals line up — old age, stale updates, weak
objective alignment, low field completion, non-delivery status, overdue dates.

## Trigger and cadence

**Trigger:** the operator opens a portfolio review cycle for a named Jira
project or space — either by pointing the flow at live Jira, or by supplying an
export of the same data.

**Cadence:** per governance cycle. Quarterly is the assumed default (it aligns
with the `<team_code>-<yyyy>-q<n>` planning-label convention already in house
use), but the flow is cadence-neutral — nothing in it assumes a specific
interval. A run covers the whole portfolio, not a subset.

## Stage sketch

| # | Stage | What happens | Review intensity (est.) |
|---|---|---|---|
| 1 | Intake & Source Binding | Bind the run to live Jira or an export; screen data-class; inventory which required fields are actually present; emit the normalized item set | heavy |
| 2 | Portfolio Profiling | Profile the portfolio — counts by status/assignee/priority/due-date category, age ranking, field completion, the oldest-and-sparsest cross-cut — and offer exploration lenses before any judgment | light |
| 3 | Objective Mapping | Match each item's text fields against the instance's objective dictionary; emit mapped area, confidence, score, matched keywords, secondary match; bucket the unalignable as `Needs objective review` | heavy |
| 4 | Rationalization Scoring | Apply the close-score model; every score carries its per-dimension breakdown as evidence | light |
| 5 | Recommendation & Disposition Packet | Band scores into the recommendation taxonomy; build per-item packets and the assignee-routed outreach list | light |
| 6 | Review & Disposition Capture | Owners validate; each reviewed item gets a captured disposition with rationale; dictionary feedback is recorded for the next cycle | heavy |

Stage 3 breaks the U-curve default (a middle stage carrying heavy review) with
stated cause: objective mapping is the highest-judgment content in the flow and
feeds 40 of the model's ~100 points. A mis-mapping propagates straight into a
closure recommendation, and no downstream stage can catch it.

## Data profile

Every stage after intake handles real portfolio content — issue summaries,
descriptions, business outcomes, assignee names — so the whole flow runs at
`data-class: internal` in an instance. This public design copy is `public` by
construction: it carries the method and the molds, never portfolio data.

Stage-specific boundaries:

- **Stage 1** is the classification gate. Exports are the higher-risk carrier:
  a raw Jira export pulls every column including comments and custom fields,
  which routinely carry names, customer references, and occasionally credentials
  pasted into a ticket. The stage screens before the data is typed further, and
  halts on anything above `internal`.
- **Stages 2 and 6** handle assignee names (workload profiling, outreach
  routing) — the flow's only sustained personal-data surface, and the reason
  Stage 2's output is a distribution, not a named performance ranking.
- **No stage writes anything to Jira.** Read-only for the whole flow.

## Layer-3 inventory

**Existing skills to reference:**

- `provenance-stamper` (verified) — stamps and validates the frontmatter on
  every artifact a run produces.
- `contract-reviewer` (verified) — pre-reviews this flowspace's own stage
  contracts before staging for the gate.

**Existing skills deliberately *not* reused:**

- `jira-commit` — creates and updates single work items from a signed-off
  refinement payload. This flow neither creates nor writes. Named here so the
  collision question is settled in the record rather than re-asked.
- `jira-accomplishments-gatherer` — queries one engineer's own closed work for
  a review period. Different unit of analysis (person, not portfolio) and
  different intent (evidence, not triage). Its live-query-with-paste-degrade
  *pattern* is the model for the ingest skill; its scope is not.

**Suspected gaps — five candidate skill-primer-briefs:**

| Candidate | Capability |
|---|---|
| `sp-jira-portfolio-ingest` | Bind live Jira or normalize an export into the canonical item set + field-availability report |
| `sp-portfolio-profiler` | Distribution counts, age ranking, field-completion, oldest-and-sparsest cross-cut |
| `sp-objective-keyword-mapper` | Dictionary-driven objective mapping with confidence, score, matched keywords, secondary match |
| `sp-closure-scorer` | Composite close score with per-dimension evidence and the corroboration rule |
| `sp-disposition-packet-builder` | Per-item disposition packets + assignee-routed outreach list |

**Reference material this flowspace must carry** (Layer-3 stable rules, not
skills): an objective-dictionary template (domain-neutral mold, instantiated
employer-side), the close-score model and recommendation taxonomy, and the
export/field requirements with the live-vs-export parity contract.

## Source-repo

- **Source-repo:** the operator's internal GitLab instance repo,
  `flowspaces/portfolio-rationalization/` — set at instantiation, sole source
  of truth for the instance.
- **External systems read:** Jira — one project or space per cycle, read-only,
  via the engine's native Jira capability. No Confluence dependency. No writes
  to any external system at any stage.

## Open questions

Surfaced for the operator rather than silently decided during setup:

1. **Score calibration is unratified.** The model's ramps were inferred from
   five observed data points in the operator's existing workbook, not derived
   from its formulas. They reproduce the described top-ranked item closely
   (101 against an observed 102) but have never been run against a full real
   cycle. Calibration is an operator gate before the first live run.
2. **Recommendation label rename.** The source taxonomy's top band is `Closed`,
   which reads as a Jira status and invites the reading that the flow already
   closed something. Proposed as `Close (recommended)`; the operator ratifies
   or rejects.
3. **Field-completion denominator.** The source workbook used 216 columns as a
   fixed denominator. Column count varies by Jira configuration and export
   settings, so the design captures it per cycle instead. Whether to also
   exclude always-empty system columns from the denominator — which would make
   completion percentages comparable across cycles but not across
   configurations — is unresolved.
4. **Objective dictionary ownership.** Who authors and ratifies the objective
   areas and their keyword sets each cycle, and whether a mid-cycle dictionary
   revision invalidates that cycle's scores or is applied forward only.
5. **Whether write-back is wanted later.** This build is read-only by decision.
   If a future cycle wants labels or comments applied to reviewed items, that
   is a new skill and a Stage 6 branch, not a tweak.
