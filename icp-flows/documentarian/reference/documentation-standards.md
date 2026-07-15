---
id: documentation-standards
title: "Documentation Standards — Stage 05 Baseline"
type: specification
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[documentarian]]"
  - "[[doc-type-registry]]"
  - "[[custody-model]]"
---

# Documentation Standards — Stage 05 Baseline

The house baseline every governed document is validated against at Stage 05,
and the staleness/archive criteria Stages 02 and 07 apply. House-drafted at
`to-review`; where an employer style guide exists, that guide wins and this
baseline records the delta at instantiation.

## Naming

- Page title pattern: `<System/Area> — <Doc Type Label> — <Specific subject>`
  (e.g., "Edge Network — Runbook — BGP session flap"). Title derives from the
  registry row's id where one exists; if you can't compute one from the
  other, the mapping is broken (same rule as mirroring-protocol §2).
- No dates in titles except `meeting-notes` (which lead with `YYYY-MM-DD`).
- One document, one subject — a title needing "and" is usually two documents.

## Structure

- The matched registry template's required sections, in the registry's order.
  Extra sections are allowed after required ones; missing required sections
  are findings.
- Headings nest without skips (no H2 → H4).
- Procedures are numbered steps with one action per step; expected results
  stated where a step's success isn't self-evident (MOPs: mandatory per
  step).
- The common metadata block present and complete: `doc-type`, `owner`,
  `source-evidence`, `last-verified`, `review-by`, `status`.

## Labels and page properties (Confluence primary)

- Doc-type label per the registry (`doc-sop`, `doc-mop`, `doc-runbook`,
  `doc-sad`, `doc-kb-article`, `doc-meeting-notes`).
- Lifecycle labels: `servicenow-pending` (Stage 06 staged path),
  `archive-candidate` (audit finding, pre-confirmation), `archived`
  (post-Stage-07 execution).
- Provenance labels per mirroring-protocol §2 (`src-human-ai`,
  `dc-internal`, truth-level label) on instantiated instances.

## Link hygiene

- Every internal link resolves (no dead page links; Jira keys well-formed and
  existing — Stage 02 confirms, Stage 05 re-checks).
- Jira linkage goes through remote links per the Stage 03 plan, not bare-text
  keys in prose (bare keys are findings; linked keys in context are fine).
- Related documents section links govern documents by title, not raw URL
  text.

## Voice and formatting

- Instructional voice, second person, present tense for procedures ("Restart
  the service", not "The service should be restarted").
- No bold-as-structure, no emojis in governed documents (same rule as
  ai-refinement Stage 05's formatting pass).
- Open sections appear only as protocol-conformant markers
  (`collaborative-sections-protocol.md`) — a TODO, TBD, or empty heading
  outside the marker syntax is a finding.
- No names, attributions, or PII beyond what the Stage 01 screen approved.

## Staleness thresholds (Stage 02 signals, Stage 07 cadences)

| Doc type | Review cadence (review-by) | Staleness signal past review-by |
|---|---|---|
| `sop` | 12 months | archive-candidate after 6 months past due with no owner response |
| `mop` | change-window close | archive-candidate by default once the window closes |
| `runbook` | 6 months | escalate to owner at due; archive-candidate at 6 months past due |
| `sad` | 12 months (and every sad-update touch) | flag for tree-audit; SADs archive only on system retirement |
| `kb-article` | 6 months | archive-candidate at 6 months past due |
| `meeting-notes` | none (point-in-time record) | space retention policy applies |

Additional staleness signals regardless of age: dead links past threshold
(>20% of a page's links), orphaned position (no parent, no inbound links),
owner departed with no reassignment.

## Archive criteria

- **Archive, never delete** — content moves to the tenant's confirmed archive
  mechanism (custody model fixes which: archive space, archive label, or
  Confluence native archiving) with its registry row updated to `archived`.
- Archiving requires: a staleness/supersession rationale recorded, the
  per-item human confirmation (Stage 07, no exception), and inbound links
  checked — a page other active documents link to gets its links re-pointed
  or the archive is declined.
- A superseded document's registry row records what replaced it.
