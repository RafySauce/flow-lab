---
id: board-evidence-requirements
title: "Board Evidence Requirements — Fields, History, Floors, and Parity"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related: ["[[statik-adoption]]", "[[jira-portfolio-ingest]]"]
---

# Board Evidence Requirements

What this flowspace needs from a Jira board, what each stage loses when it is
absent, and the rule that a run in one source mode produces the same *shape* of
output as a run in another. Layer-3 stable reference for Stages 01, 03, 04, and
05.

## 1. The parity contract

A run is bound in one of three source modes. **The output shape is identical in
all three; only the evidence basis and the sufficiency of the findings differ.**

| Mode | What it is | What changes |
|---|---|---|
| **Live Jira** | Bound to a project, board, or saved filter via the engine's native Jira capability | Findings can be `measured`; history may or may not be retrievable — checked separately |
| **Jira export** | A file supplied by the operator, normalized by `jira-portfolio-ingest` | Same as live, bounded by what the export's columns carry; history usually absent unless deliberately exported |
| **Live ServiceNow** | Bound to an incident, request, or named custom table via `servicenow-ticket-ingest` (§7 — backlog-staged, not yet built) | Same parity guarantee as Jira once built: findings can be `measured`; history is a separate audit-table query, checked separately |
| **ServiceNow export** | A file supplied by the operator, normalized by `servicenow-ticket-ingest` | Same as live ServiceNow, bounded by what the export's columns carry |
| **Conversation-only** | No board/table, or one that does not reflect the work | Every finding is `estimated`; no finding is ever labelled `measured` |

A service tracked in both Jira and ServiceNow binds both sources explicitly
at Stage 01 and records the split — the two bound sets are never silently
merged, since a merged set would double-count or arbitrarily drop items that
exist in both systems.

Three rules make parity real rather than nominal:

1. **Every figure carries its basis tag** — `measured` or `estimated` — in every
   mode, including runs where all figures share the same tag. A tag that only
   appears in mixed runs is a tag nobody reads.
2. **Estimated and measured figures never share a column.** Separate columns, or
   separate tables. A reader scanning a table cannot be relied on to check a tag.
3. **Conversation-only is a declared mode, not a fallback reached by failure.**
   It is chosen at Stage 01 and recorded in the mode declaration. A run that
   fails to bind a board does not silently become conversation-only — it stops
   and asks.

## 2. Fields, by stage

`jira-portfolio-ingest` produces the field-availability report; this table says
what the flow does with each field's absence.

| Field | Needed by | Absence costs |
|---|---|---|
| Issue key, summary | 03, 04, 05 | Hard-required — the run cannot proceed |
| Created | 03, 04 | Hard-required — no arrival rate, no lead time |
| Resolved / completed date | 04 | Hard-required for capability — throughput and lead time both need it |
| Issue type | 03 | Type discovery loses its comparison baseline; clustering still works, disagreement analysis does not |
| Status, status category | 03, 04, 05 | Workflow modelling loses its board-derived candidate states; Stage 05 becomes conversation-only |
| Status transition history | 04, 05 | See §4 — the single most consequential absence in the flow |
| Due date | 04, 06 | No due-date performance; fixed-date class must be derived from conversation alone |
| Priority | 06 | Minor — priority is explicitly *not* a class of service, so this is corroboration only |
| Reporter / requesting group | 03 | Demand cannot be segmented by customer group; expectations must be elicited per group instead |
| Labels, components | 03 | Type discovery loses a clustering signal; not fatal |
| Blocked flag or blocked-time field | 04, 07 | No blocked-time analysis; blocked-item policy at Stage 07 is designed without a baseline |
| Assignee | 03 | Used in aggregate only. Never produces a per-person figure — see §5 |

## 3. Sufficiency floors

A step is marked `evidence-grounded` in Stage 01's mode declaration only if the
data clears the relevant floor — **not merely because a board was bound.** Stage
01's Verify field checks exactly this.

| Step | Floor | Below the floor |
|---|---|---|
| 3 — Demand | At least one full arrival cycle for the service (a cycle being whatever period the demand pattern repeats over — commonly a quarter; longer where demand is annual or seasonal) | Report arrival rate as an observation over the window available, tagged `insufficient window`, and elicit the pattern |
| 3 — per type | At least 10 items of that type in the window | The type is marked `below floor` in the type set — it may still be a valid type; it just cannot carry a measured rate |
| 4 — per type | At least 30 completed items of that type | Report individual observations as a list, explicitly labelled observations. **Never percentiles over a handful of items** |
| 4 — residency | Transition history present (see §4) | Take the §4 degrade path |
| 5 — Workflow | Status history, or a status field with meaningful usage | Candidate states come from conversation only; the board-disagreement analysis is skipped and recorded as skipped |

**These floors are reasoned, not calibrated.** They are defensible defaults from
general practice, not derived from this operator's actual boards, and they are
exactly the kind of number that quietly becomes policy. Operator ratification
before the first live run — this is a named gap in `HUB.md`.

## 4. The history question

`jira-portfolio-ingest` emits a **point-in-time** normalized item set. Stage 04's
per-state residency analysis needs **history**: when each item entered and left
each state. Stage 01 checks and records this separately from field availability,
because a complete field-availability report says nothing about it.

**With full transition history**, Stage 04 reports per-state residency, the
working-versus-waiting split, flow efficiency, and blocked-time analysis. Stage
07's WIP limits are then *derived* from measured concurrency and residency.

**With Created and Resolved only** (the degrade path): end-to-end lead time,
throughput, arrival-versus-throughput comparison, and due-date performance are
all still computable. Lost: per-state residency, flow efficiency, blocked-time
analysis. The consequence lands at Stage 07 — WIP limits become *starting points
to be tuned at the operations review* rather than derived figures, and must be
labelled as such wherever they appear.

Stage 04 states the degrade explicitly in its output rather than omitting the
sections, because a missing section reads as "nothing to report" — a different
and much stronger claim than "not measurable here."

**Open (operator call, recorded in `HUB.md`):** whether to extend
`jira-portfolio-ingest` with an optional history mode (it is promoted and
`portfolio-rationalization` also depends on it), to have
`flow-capability-analyzer` request history itself, or to accept the degrade
permanently.

## 5. Personal data

Assignee data is read **in aggregate only**, at Stages 03 and 04, and the flow
produces no per-person throughput, lead-time, or cycle-time figure at any stage.
Both stages decline that framing explicitly when asked.

This is a data-handling constraint, not a presentation preference. Individual
flow metrics turn a Kanban rollout into an instrument of performance management,
which ends the honest reporting the method depends on — Stage 02's
dissatisfaction elicitation cannot survive it, and Stage 02 is where every
fitness criterion is corrected.

The constraint also propagates into the *designed system*: Stage 07's metric set
excludes per-person reporting by design, so whoever configures the board inherits
the constraint rather than re-deciding it.

## 6. Export-specific cautions

Exports are the higher-risk carrier and Stage 01 screens accordingly. A raw Jira
export pulls every column, including comments and custom fields, which routinely
carry names, customer references, hostnames, and occasionally credentials pasted
into a ticket. Screen before the data is typed further; halt on anything above
`internal`.

Two export-specific failure modes worth naming: **truncation** (an export capped
at a row limit silently produces a biased sample — `jira-portfolio-ingest` halts
on count mismatch, and that halt must not be overridden) and **filtered
history** (an export that appears to carry transitions but only carries the most
recent one, which yields a residency analysis that is wrong rather than absent —
the more dangerous failure).

## 7. ServiceNow as a source

`servicenow-ticket-ingest` (backlog-staged at
`skill-foundry/backlog-skill-starters/sp-servicenow-ticket-ingest.md`, not yet
built) is designed to emit the identical canonical shape
`jira-portfolio-ingest` produces, so §§1–6 above apply unchanged once it
exists — the same parity contract, the same field-to-stage table, the same
sufficiency floors, the same history question, the same personal-data
constraint, the same export cautions. This section carries only what is
ServiceNow-specific: the field mapping and its instance-taxonomy caveats.

**Field mapping — ServiceNow (`incident` table, representative) to canonical:**

| ServiceNow field | Canonical field | Notes |
|---|---|---|
| `number` | Issue key | e.g. `INC0012345` |
| `short_description` | Summary | |
| `state` / `incident_state` | Status | **Numeric in the underlying field, label-mapped per instance** — the raw integer is never the canonical status; resolve through the instance's label map before mapping |
| `opened_at` | Created | |
| `resolved_at` (falls back to `closed_at` if resolution is not tracked separately) | Resolved / completed date | Instance-dependent which field is populated; check both |
| `category` / `subcategory` | Issue type candidate | Administrative artifact exactly as Jira's issue-type field is (see Stage 03 §1) — cluster on request content, not the raw category |
| `assignment_group` | Reporter / requesting-group proxy | A group, not a person — consistent with §5's aggregate-only constraint |
| `priority` | Priority | |

A request/catalog table (`sc_request`, `sc_req_item`) maps analogously with
`requested_for` in place of `assignment_group` and its own state model — the
skill presents the map for confirmation per table, never auto-accepts, exactly
as `jira-portfolio-ingest` does for Jira's custom fields.

**History is a separate query**, as in Jira: the base table is a point-in-time
record; per-state residency needs the `sys_audit`/state-transition history,
checked and recorded separately per §4's discipline. A closed incident can be
reopened, which the point-in-time set alone will not show — record this as a
known limitation alongside the history-availability finding when ServiceNow is
the bound source.

**Until `servicenow-ticket-ingest` is built**, a ServiceNow-tracked service
either runs Stage 01 in conversation-only mode or uses the operator-paste
degrade path with the field gaps stated — the same reduced path
`jira-portfolio-ingest` offers when no Jira connector is available.
