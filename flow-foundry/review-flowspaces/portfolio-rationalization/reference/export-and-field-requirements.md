---
id: export-and-field-requirements
title: "Export & Field Requirements — Live/Export Parity Contract"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-07-28
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[close-score-model]]"
  - "[[work-item-schemas]]"
---

# Export & Field Requirements — Live/Export Parity Contract

What Stage 01 needs from a source, how live Jira and an export produce the same
normalized shape, and what happens when a field is missing.

---

## 1. The parity contract

**Stages 02–06 never know which source a cycle used.** Stage 01 emits one
canonical item set and one field-availability report, and everything downstream
reads only those. This is the whole reason the flow can take either input.

Two consequences worth stating plainly:

- A field that live Jira exposes but the export omits (or vice versa) is a
  **parity defect**, not a source difference to work around downstream. Fix it
  at Stage 01 or record it as unavailable for the whole cycle.
- Scores from a live-bound cycle and an export-bound cycle over the same
  portfolio must match. If they do not, the normalization is wrong. This is a
  checkable property and worth checking once at instantiation.

## 2. Required field set

The fields the flow's signals are built on. Jira field names vary by
configuration — the left column is this flow's canonical name, and the instance
maps its real fields onto it at Stage 01.

| Canonical field | Used by | Required |
|---|---|---|
| Issue key | All stages — item identity | **Yes** — no key, no run |
| Summary | Stage 03 (mapping), Stage 05 (packet) | **Yes** |
| Status | Stage 02 (counts), Stage 04 (§3.5 adjustment) | **Yes** |
| Status Category | Stage 04 — fallback when a status is unmapped | Strongly preferred |
| Assignee | Stage 02 (workload), Stage 05 (outreach routing) | Strongly preferred |
| Created | Stage 02 (age ranking), Stage 04 (age dimension) | **Yes** |
| Updated | Stage 02, Stage 04 (staleness dimension) | **Yes** |
| Due date | Stage 02 (due-date categories), Stage 04 (overdue) | Preferred |
| Priority | Stage 02 (distribution) | Optional |
| Description | Stage 03 (mapping) | Preferred |
| Business Outcome | Stage 03 — highest-value mapping field | Preferred |
| Scope | Stage 03 | Optional |
| Acceptance Criteria | Stage 03 | Optional |
| Dependencies | Stage 03 (secondary matches) | Optional |
| Risks | Stage 03 (weakest mapping signal) | Optional |
| Parent key | Stage 05 — merge-candidate context | Optional |
| Comments | Stage 04 — human-touch staleness refinement | Optional |
| Labels | Stage 02 (lens) | Optional |

**Hard requirements** — the flow cannot run without Issue key, Summary, Status,
Created, and Updated. Stage 01 halts if any is absent.

Field names, types, and the hierarchy these map onto are in
`icp-flows/ai-refinement/reference/work-item-schemas.md`. This flow **reads**
that registry; it never writes to the fields it describes.

## 3. Degraded-signal handling

A missing optional field degrades the flow; it does not stop it. Stage 01
records every absence in the field-availability report, and the affected stage
states the degradation in its output rather than silently scoring around it.

| Missing | Effect | Handling |
|---|---|---|
| Business Outcome | Weaker objective mapping — the highest-value mapping field is gone | Mapping proceeds on remaining fields; every mapping in the cycle is flagged reduced-confidence |
| Description | Substantially weaker mapping | As above; a Summary-only mapping is explicitly flagged in Stage 03's output |
| Due date | No overdue component | Overdue contributes 0. **Not** treated as "not overdue" in reporting — reported as unknown |
| Assignee | No workload lens, no outreach routing | Stage 02 reports the unassigned count; Stage 05 routes those packets to the operator |
| Comments | Staleness uses raw `Updated` | Staleness scores flagged low-confidence per `close-score-model.md` §3.3 |
| Status Category | Unmapped statuses cannot fall back | Unmapped statuses score 0 and are flagged individually |

**The rule underneath all of these:** a missing signal scores zero, never a
penalty. Absent data is not evidence of neglect — an item is not more closeable
because its export lacked a column.

## 4. Field-completion denominator

Stage 02 computes populated-fields-over-available-columns per item. The
denominator rule:

1. **Capture the denominator per cycle**, from the actual source. Do not
   hardcode it. Column counts vary by Jira configuration, by export settings,
   and over time as fields are added — a fixed denominator silently changes
   meaning between cycles.
2. **Record it in the cycle's decision log** alongside the item count, so a
   cycle-over-cycle comparison can tell whether a completion shift is real or
   an artifact of a changed column set.
3. **Count a field populated** when it holds a non-empty, non-whitespace value.
   Jira's placeholder empties (`None`, `-`, an empty rich-text container that
   serializes as markup with no text) count as empty.
4. **Same denominator for every item in a cycle.** Per-item denominators would
   make completion percentages incomparable within the cycle, which is the one
   comparison Stage 02 actually needs.

> **Open question, carried from the intake brief.** Whether to further exclude
> always-empty system columns from the denominator. Doing so makes percentages
> comparable across cycles but not across Jira configurations; not doing so
> means a portfolio with 216 columns and one with 90 produce percentages that
> look comparable and are not. Unresolved — the operator decides at
> instantiation, and whichever way it goes, the choice is recorded with the
> denominator.

Absolute counts travel with every percentage (`44 of 216 — 20.4%`), because the
denominator matters and a bare percentage hides it.

## 5. Source binding — live Jira

- **Scope:** one project or space per cycle, named by the operator at Stage 01.
  A JQL filter may narrow it; the filter is recorded verbatim in the cycle log,
  because a scope change between cycles invalidates comparison.
- **Access:** read-only, via the engine's native Jira capability — the same
  access class `ai-refinement` Stage 01 uses for its label query. No write
  scope is needed or requested at any point in this flow.
- **Pagination:** portfolios exceed page limits. Stage 01 confirms the returned
  item count matches the query's reported total before proceeding; a silent
  truncation would corrupt every distribution in Stage 02.

## 6. Source binding — export

- **Formats:** CSV or XLSX, as Jira's issue-navigator export produces them.
- **Header row:** the column set is the denominator source (§4) and the field
  map's left-hand side. Capture it before parsing rows.
- **Multi-value columns:** Jira exports repeated fields (labels, comments,
  links) as repeated columns with identical headers. Collapse repeats into one
  canonical field before normalization, and count the collapsed field once in
  the denominator — not once per repeat, which would inflate the denominator
  for portfolios with many comments.
- **Embedded newlines and delimiters** in description and comment fields are
  routine in Jira exports. Parse with a real CSV reader honoring quoting; a
  naive line-split produces phantom rows and a corrupted item count.
- **Item-count confirmation:** the operator states the expected item count at
  Stage 01 and it is checked against the parsed count. A mismatch halts.

## 7. Data-class screening at intake

Exports are the higher-risk carrier, and Stage 01's screen is calibrated for
them. A raw export pulls every column — comments and custom fields routinely
carry personal names, customer references, hostnames, and occasionally
credentials pasted into a ticket by someone in a hurry.

- The screen runs **before the data is typed further** — before profiling,
  before mapping.
- Content above the instance's sanctioned ceiling (`internal` by default) halts
  the run. It is not redacted and carried forward: redaction at this volume is
  not reliably verifiable.
- Assignee names are expected and permitted at `internal`. They are the flow's
  only sustained personal-data surface, and the reason Stage 02 outputs a
  distribution rather than a named ranking.
- **Nothing from a real portfolio ever enters this public repo** — instance
  data lives in employer tenancy, per `methodology/mirroring-protocol.md`.
