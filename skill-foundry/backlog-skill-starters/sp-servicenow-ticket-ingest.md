---
id: sp-servicenow-ticket-ingest
title: "Skill Primer Brief — ServiceNow Ticket Ingest"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[statik-adoption]]"
  - "[[jira-portfolio-ingest]]"
  - "[[board-evidence-requirements]]"
---

# Skill Primer Brief — ServiceNow Ticket Ingest

## Purpose

Bind a STATIK Adoption run to a service's ServiceNow work — incidents,
requests, or a custom table, one per run — and emit the same canonical
normalized item set and field-availability report that `jira-portfolio-ingest`
produces for Jira, so Stages 03–04 read one shape regardless of which
ticketing system the service actually uses. Replaces the manual ServiceNow
export-and-clean step, and gives services that track work in ServiceNow
rather than Jira (or in both) an evidence-grounded path instead of a forced
drop to conversation-only.

## Triggering intent

- **Fires on:** Stage 01 of `statik-adoption`, when the operator declares the
  service's source mode as live ServiceNow or a ServiceNow export — the same
  point at which `jira-portfolio-ingest` fires for a Jira-tracked service.
  Also standalone on "pull this ServiceNow table into a normalized set,"
  "normalize this ServiceNow export," "bind this incident queue for demand
  analysis."
- **Does not fire on (near-misses):**
  - Publishing or committing content *to* ServiceNow (KB articles, ITSM
    records) — that is the deferred `sp-servicenow-kb-commit` write path, a
    different direction entirely. This skill has no write path and declines
    rather than routing.
  - A Jira-tracked service — that is `jira-portfolio-ingest`. A service that
    genuinely runs both should be recorded at Stage 01 as two bound sets with
    the split stated explicitly, not silently merged by this skill.
  - Any request implying a write — closing, resolving, reassigning,
    commenting. Decline.

## Method sketch

Mirrors `jira-portfolio-ingest`'s method, substituting ServiceNow's shape:

1. Take scope verbatim — table (`incident`, `sc_request`/`sc_req_item`, or a
   named custom table), encoded query or view, source mode (live query /
   export), expected record count.
2. Bind the source: live mode queries read-only through the engine's
   sanctioned ServiceNow capability, paging to completion and halting on a
   count mismatch against the query's own reported total; export mode parses
   the exported CSV/XLSX with a quote-honoring reader; no-connector-and-no-export
   falls to an operator-paste degrade path, stated plainly with what the
   pasted shape lacks.
3. Run the data-class screen before anything else — ServiceNow work notes and
   custom fields carry the same personal-name/hostname/credential risk Jira
   exports do. Halt above `internal`, do not redact and carry forward.
4. Confirm the record count against the operator's stated expectation; a
   mismatch halts.
5. Map ServiceNow's fields onto the same canonical set `jira-portfolio-ingest`
   emits (see the new ServiceNow mapping this brief proposes for
   `reference/board-evidence-requirements.md`): `number` → issue key,
   `short_description` → summary, `state`/`incident_state` → status,
   `opened_at` → created, `resolved_at`/`closed_at` → resolved,
   `category`/`subcategory` → issue type candidate, `assignment_group` →
   requesting-group proxy, `priority` → priority. Present the map for
   confirmation — never auto-accept, since instance taxonomies vary as much
   as Jira's custom fields do.
6. Check the same hard requirements (key, summary, status, created, updated)
   and halt naming any absent.
7. Inventory transition history separately: ServiceNow's `sys_audit` /
   state-transition history is a distinct query from the base record, exactly
   as Jira's changelog is — record whether it was retrievable or only
   opened/resolved timestamps are.
8. Emit the normalized item set, field-availability report, and completion
   denominator in the identical shape `jira-portfolio-ingest` produces, so
   Stage 01's downstream handling (steps 5–8) does not need to branch on
   source system.

**Quality bar, inherited:** a live-bound cycle and an export-bound cycle over
the same ServiceNow table produce identical normalized sets — same parity
test as `jira-portfolio-ingest`.

**Known failure modes to guard:** ServiceNow's `incident_state` is numeric in
the underlying field and label-mapped per instance — do not treat the raw
integer as the canonical status without the instance's label map. Closed
incidents can be reopened, which the point-in-time set will not show — record
as a known limitation alongside the history-availability finding.

## Inputs and data boundary

Reads: the operator's scope declaration; a live ServiceNow table (read-only)
via the engine's sanctioned ServiceNow capability, or an export file, or
pasted content; the session capability-probe result; a ServiceNow field
mapping in `icp-flows/statik-adoption/reference/board-evidence-requirements.md`
(to be added alongside the existing Jira mapping). Max data-class: `internal`,
matching `jira-portfolio-ingest`'s ceiling, and subject to the employer's
sanctioned-tool matrix's ruling on ServiceNow read access at build time —
per `methodology/mirroring-protocol.md` §2, ServiceNow is already sanctioned
as a *read* target in principle (unlike the KB-commit write path, which
remains deferred for lack of a sanctioned write integration). Engine: whichever
of Rovo or Copilot carries the sanctioned ServiceNow read connector at build
time — record on this brief when known, same discipline as the deferred
KB-commit brief.

## Demand source

`icp-flows/statik-adoption/01-service-framing-and-source-binding/CONTEXT.md`
— services whose work lives in ServiceNow (change requests, incidents,
service catalog requests) rather than Jira currently have no evidence-grounded
path and are forced to conversation-only, losing Stages 03–04's measured
demand and capability findings even where the data exists. Flagged at
flowspace design time; not built pending operator confirmation of a sanctioned
ServiceNow read connector.

## Definition of done

On a test ServiceNow table: live-mode and export-mode binding of the same
table produce identical normalized sets; the field map is presented and
requires explicit confirmation; the data-class screen runs before mapping and
halts correctly on injected above-ceiling content; all five hard fields are
checked with a correct halt on a missing one; the field-availability report
and history-availability finding land in the same shape Stage 01 already
expects from `jira-portfolio-ingest`, so Stage 01's process and Stages 03–04
require no branching logic to consume either source.
