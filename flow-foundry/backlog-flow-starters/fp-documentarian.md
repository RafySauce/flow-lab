---
id: fp-documentarian
title: "Flow Primer Brief — Documentarian"
type: flow-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related: ["[[documentarian]]", "[[ai-refinement]]"]
---

# Flow Primer Brief — Documentarian

> Intake path 1 for the flow-foundry: crystallized intent, written down
> *before* scaffolding starts.

## Purpose

Produce, point-in-time update, and maintain over time quality operational
documentation — SOPs, MOPs, runbooks, SADs (system architecture documents and
their diagrams), ServiceNow KB articles, and meeting pages — from evidence
already sitting in Jira, Confluence, meeting transcripts, and delivered work.
Complementary to `ai-refinement`: that flowspace refines work *items*; this one
drives the documentation *practice* end-to-end, and hands candidate work items
back to ai-refinement when documentation work surfaces them. Humans drive it
first; over time, agents run it as standing custodians of the documentation
platforms (Confluence primary; ServiceNow KB as a designed-for future surface).
Recurs continuously — every closed work item, delivered feature, meeting, and
quarterly doc-hygiene pass is a candidate run.

## Trigger and cadence

Event-driven, five job types observed so far:

1. **Close-out** — a work item is closing; generate the documentation for the
   work that was done (investigate the closed items, comments, linked docs;
   recommend docs and build them collaboratively, leaving marked-open sections
   for the user).
2. **Modernize** — bring an existing Confluence space's pages into the house
   templated patterns.
3. **SAD update** — a feature just delivered; update the affected system
   architecture documentation and diagrams.
4. **Tree audit** — crawl a documentation tree; propose structure improvements,
   bring content in line with standards, archive stale content.
5. **Meeting** — turn a transcript/summary into a Confluence meeting page,
   link the Jira items discussed, and identify candidate work items for
   ai-refinement.

Cadence: on demand per event today; the custody stage is designed so a
scheduled (weekly/quarterly) custodial run becomes possible once agents
operate the flow.

## Stage sketch

| # | Stage | What happens | Review intensity (est.) |
|---|---|---|---|
| 1 | Intake & Routing | Trigger, responsibility acknowledgment, data-safety screen, job-type selection (agent-proposed, user confirms), doc-type registry loaded, target surface identified | heavy |
| 2 | Evidence Gathering | Job-type-steered evidence dossier from Jira, Confluence, transcripts, delivered-work artifacts | light |
| 3 | Doc Plan & Template Match | Dossier + registry → confirmed doc work order: per document, create/update/archive, doc type, matched template, open-section plan, Jira-link plan | heavy |
| 4 | Draft & Update | One document drafted/updated against its template, with collaborative open sections marked for the user; updates presented as diffs | light |
| 5 | Standards Validation | Structure, metadata, link, and formatting checks against the doc-type schema and standards baseline; findings report | light |
| 6 | Commit & Link | Rendered dry-run preview → explicit approval → Confluence create/update, labels/properties, Jira remote links; meeting jobs emit the ai-refinement handoff | heavy |
| 7 | Custody & Close | Doc-registry bookkeeping, freshness + review-by stamping, human-confirmed archive moves, next custody review scheduled | heavy |

Stages 4–6 loop per document in the work order (one job can yield several
documents); Stage 7 runs once per job after the loop drains.

## Data profile

`data-class: internal` throughout in instances (this design copy is `public` —
it carries no real content). Transcripts and incident-adjacent runbook content
routinely carry names — Stage 1 screens all source material per the
ai-refinement data-safety pattern, with the strictest screen on the meeting
job type. If confidential material appears in gathered evidence, the run halts
and re-routes per the sanctioned-tool matrix.

## Layer-3 inventory

- Stage 1: inline — guardrails, routing rules, and registry pointers specific
  to this flowspace.
- Stage 2: gap — **doc evidence gatherer** (job-type-steered dossier builder).
- Stage 3: gap — **doc planner** (dossier + registry → confirmed work order).
- Stage 4: gaps — **doc drafter** (template-shaped drafting with the
  collaborative open-section protocol) and **SAD diagram maintainer**
  (text-editable diagram source updates; possible merge into the drafter).
- Stage 5: gap — **doc standards validator**; `provenance-stamper` (verified)
  referenced for mirror-side artifact stamping.
- Stage 6: gap — **Confluence page commit** (no existing skill writes to
  Confluence; `jira-commit` is the shape to model); deferred gap —
  **ServiceNow KB commit** (no sanctioned ServiceNow integration exists yet).
- Stage 7: gap — **doc custodian** (registry, freshness, archive execution).

Deliberate non-reuse: `jira-accomplishments-gatherer` and
`confluence-contribution-gatherer` are scoped to one engineer's accomplishments
evidence; `context-elicitation` is bound to the ai-refinement TPSO persona and
work-item schemas; `jira-commit` commits work items, which this flow never does
directly — candidates go to ai-refinement via the handoff.

## Surfaces

Primary: a Confluence documentation space `<set at instantiation>` (confirm the
Mermaid macro per the setup questionnaire, else "diagram: see mirror").
Designed-for secondary: ServiceNow KB (`kb_knowledge`) — the write path is a
declared gap until a sanctioned integration exists; ServiceNow-destined
documents stage on Confluence in the meantime. Mirror: `<internal repo>` →
`flows/documentarian/`.

## Open questions

- No stakeholder register exists for the documentation domain (doc ownership,
  audience). Ownership questions run in ungrounded mode — ask the user — until
  a documentation-owners register is instantiated from
  `platform-stakeholder-register-template.md`.
- Which ServiceNow integration (if any) will be sanctioned, and what subset of
  `kb_knowledge` fields the house KB template must map to — resolve before the
  deferred `sp-servicenow-kb-commit` brief is built.
- Archive mechanics per tenant: archive space vs. archive label vs. Confluence
  native archiving — the custody model should confirm at instantiation.
- Whether scheduled custodial runs (agent-initiated tree audits) need their own
  trigger discipline beyond the five event-driven job types — revisit once the
  flow has run manually a few times.
