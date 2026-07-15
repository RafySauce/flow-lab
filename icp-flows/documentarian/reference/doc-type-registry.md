---
id: doc-type-registry
title: "Doc-Type Registry — Governed Documentation Types"
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
  - "[[documentation-standards]]"
  - "[[collaborative-sections-protocol]]"
---

# Doc-Type Registry — Governed Documentation Types

The schema registry for every documentation type the documentarian flowspace
produces and maintains — the analog of ai-refinement's
`work-item-schemas.md`. Stage 01 loads it, Stage 03 matches against it,
Stage 04 instantiates its templates, Stage 05 validates against its schemas,
and the custody model keys cadences off it. House-drafted at `to-review`: the
operator ratifies the section sets and cadences, and confirms the
`kb-article` field mapping against the real ServiceNow instance before the
deferred write path is built.

Every governed document carries the **common metadata block** (as Confluence
page properties in the primary; a frontmatter-style block in the mirror):
`doc-type`, `owner`, `source-evidence` (links), `last-verified`, `review-by`,
`status` (active / archived / servicenow-pending).

## The six governed types

### `sop` — Standard Operating Procedure

- **Purpose:** how the organization performs a recurring operational activity
  — the authoritative "how we do this here."
- **Required sections:** Purpose & scope · Roles & responsibilities ·
  Prerequisites · Procedure (numbered steps) · Verification (how you know it
  worked) · Escalation & exceptions · Related documents.
- **Default open sections:** Roles & responsibilities (ownership is a human
  call in ungrounded mode); Escalation & exceptions (tribal knowledge the
  evidence rarely captures).
- **Review cadence:** review-by 12 months from last-verified.

### `mop` — Method of Procedure

- **Purpose:** the step-by-step execution plan for a specific, usually
  one-time or change-window activity — narrower and more disposable than an
  SOP, with rollback as a first-class concern.
- **Required sections:** Objective & change window · Impact & risk statement
  · Prerequisites & preconditions · Execution steps (numbered, with expected
  results per step) · Validation · Rollback procedure · Approval record.
- **Default open sections:** Impact & risk statement; Approval record
  (always human).
- **Review cadence:** review-by at the change window's close — a MOP past
  its window is an archive candidate by default.

### `runbook` — Operational Runbook

- **Purpose:** what to do when a specific alarm, failure, or operational
  situation occurs — optimized for someone under pressure at 03:00.
- **Required sections:** Trigger conditions (alarms/symptoms) · Severity &
  impact quick-read · Diagnosis steps · Remediation steps · Verification of
  recovery · Escalation path (who, when) · Known failure modes & history.
- **Default open sections:** Escalation path (names/rotations are human
  calls); Known failure modes & history (accretes over incidents).
- **Review cadence:** review-by 6 months from last-verified — runbooks decay
  fastest.

### `sad` — System Architecture Document

- **Purpose:** the current-state architecture of a system: components,
  interfaces, data flows, and the decisions that shaped them. The `sad-update`
  job type maintains these as features deliver.
- **Required sections:** System overview & context · Architecture diagram(s)
  (text-editable source preferred: Mermaid / PlantUML / drawio XML) ·
  Components & responsibilities · Interfaces & integrations · Data flows &
  classifications · Decision record links (ADRs) · Change history.
- **Default open sections:** Decision record links (the "why," which evidence
  often lacks); any diagram flagged for human redraw.
- **Review cadence:** review-by 12 months from last-verified, and touched by
  every `sad-update` job that lands on its system.

### `kb-article` — Knowledge Base Article (ServiceNow-shaped)

- **Purpose:** a self-contained answer to one recurring question or issue,
  written for a support/consumer audience rather than the operating team.
- **Required sections:** Issue / question statement · Environment &
  applicability · Resolution / answer (steps) · Verification · Related
  articles & escalation.
- **ServiceNow field mapping** (`kb_knowledge`, for the deferred write path —
  confirm against the real instance at instantiation): title →
  `short_description`; body sections → `text`; doc metadata → `kb_category`,
  `valid_to` (from review-by), `workflow_state` (staged documents map to
  draft). Until `sp-servicenow-kb-commit` exists, these documents commit to
  Confluence labeled `servicenow-pending` (Stage 06, step 6).
- **Default open sections:** Environment & applicability (support scope is a
  human call).
- **Review cadence:** review-by 6 months from last-verified.

### `meeting-notes` — Meeting Page

- **Purpose:** the durable record of a meeting: what was decided, what was
  agreed to be done, what was discussed — produced by the `meeting` job type
  from a screened transcript/summary.
- **Required sections:** Meeting context (date, purpose — attendees only as
  approved by the Stage 01 screen) · Decisions · Actions (owner, due) ·
  Discussion summary · Discussed Jira items (links) · Candidate work items
  (noted as handed to ai-refinement, with the handoff package reference).
- **Default open sections:** Actions' owners where the transcript doesn't
  name them cleanly (never guessed).
- **Review cadence:** none — meeting pages are point-in-time records; they
  archive on the space's normal retention, not on a review cycle.

## Out of scope

| Intent | Why not here | Route |
|---|---|---|
| Requirements documents (BRD/PRD/SOW) | Requirement-shaped, not documentation-shaped | ai-refinement, as Stage 01 source material (input type 5) |
| Work items of any kind | This flow never writes Jira items | ai-refinement, via the handoff contract |
| Marketing / external-audience content | Different voice, audience, and approval chain | Out of ICP scope — decline |
| Decision logs, flowspace contracts, skills | Method artifacts, not operational docs | The foundries and `methodology/` govern these |
| Ad-hoc personal notes | No custody obligation — a registry row would be noise | Decline politely; offer a governed type if it recurs |

## Extension rule

New doc types are added here by the operator only — the flow flags unmatched
intents (Stage 03 redirects per the table above and notes the miss in the run
decision log); recurring misses are the signal a new row is needed.
