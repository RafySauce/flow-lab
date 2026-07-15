---
id: documentarian-stage-03
title: "Stage 03 — Doc Plan & Template Match"
type: stage-context
stage: 3
review-intensity: heavy
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
  - "[[collaborative-sections-protocol]]"
  - "[[ai-refinement-handoff-contract]]"
  - "[[sp-doc-planner]]"
---

# Stage 03 — Doc Plan & Template Match

## Inputs

| Input | Source | Required |
|---|---|---|
| Evidence dossier | Stage 02 | Yes |
| Open evidence questions list | Stage 02 | Yes |
| Doc-type registry (loaded, version recorded) | Stage 01 → `../reference/doc-type-registry.md` | Yes |
| Grounding status (grounded / ungrounded) | Stage 01 | Yes |
| Target surface + ServiceNow staged-path acceptance (if applicable) | Stage 01 | Yes |
| Mentioned-Jira-items list (meeting jobs) | Stage 02 | If applicable |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-doc-planner)`

Turn the dossier into a confirmed **doc work order** — the artifact that
drives Bands ③ and ④. The agent proposes with rationale; the human confirms,
edits, or strikes every line. Nothing enters the work order unconfirmed.

1. **Document identification** — from the dossier, propose the set of
   documents this job should produce, update, or archive. Per proposed
   document, state the evidence entries that justify it. A document with no
   citing evidence doesn't get proposed.
2. **Doc-type and template match** — match each document to one of the six
   registry types (`sop`, `mop`, `runbook`, `sad`, `kb-article`,
   `meeting-notes`) with a stated rationale (which evidence reads as
   procedure vs. maintenance operation vs. incident response vs.
   architecture vs. knowledge answer vs. meeting record). Intents matching
   the registry's out-of-scope table are redirected, not planned. For
   `update` lines, identify the existing page and which of its sections the
   evidence touches.
3. **Open-section plan** — map Stage 02's open evidence questions onto each
   document as planned open sections per
   `../reference/collaborative-sections-protocol.md`: which sections the
   evidence can fill, which the human must, and who owns each open section
   (ungrounded mode: ask the user who owns what — no register to walk yet).
4. **Jira-link plan** — per document, which Jira items it should carry remote
   links to (closeout: the closed items; sad-update: the delivering feature;
   meeting: the discussed items confirmed by Stage 02).
5. **Job-type specifics** —
   - `tree-audit`: assemble the **audit report** (structure findings,
     standards deviations, archive candidates with staleness evidence) as
     the work order's preamble; every remediation and archive candidate
     becomes a work-order line. Archive lines are proposals only — execution
     is Stage 7's, behind per-item human confirmation.
   - `meeting`: from dossier decisions/actions, propose **candidate work
     items** for ai-refinement, shaped per
     `../reference/ai-refinement-handoff-contract.md`. Candidates ride the
     work order for Stage 6 to package; they are never created in Jira by
     this flow.
6. **Work-order confirmation** — present the full work order (documents,
   types, templates, open-section plans, link plans, audit preamble and
   candidates where applicable) with per-line rationale. The user confirms,
   edits, or strikes lines; record each decision. The confirmed work order
   fixes Band ③'s scope — adding a document later means re-entering this
   stage.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Confirmed doc work order (per line: action create/update/archive, doc type, template ref, target page/space, open-section plan, Jira-link plan, user decision) | Stages 04–07 | structured markdown table + per-line detail |
| Audit report preamble (tree-audit jobs) | Stage 07, user | structured markdown |
| Candidate work items for ai-refinement (meeting jobs) | Stage 06 | per `../reference/ai-refinement-handoff-contract.md` |

## Verify

Cross-stage trace: every work-order line traces to dossier evidence, and
every open evidence question from Stage 02 appears in some line's
open-section plan (or is explicitly struck by the user). Check line-by-line:
work-order line → cited dossier entries → resolvable sources; open evidence
questions → open-section plan entries, one-for-one or user-struck. The
failures this catches are planned documents without evidence and evidence
gaps silently dropped instead of surfaced as open sections. Running this
check leaves a one-line result in the run's decision log.

- [ ] Every work-order line cites dossier evidence
- [ ] Every line's doc type is one of the six registry types, with rationale;
      out-of-scope intents redirected
- [ ] Registry version cited equals the version Stage 01 loaded
- [ ] Every Stage 02 open evidence question is in an open-section plan or
      explicitly struck by the user
- [ ] Archive lines marked as proposals (execution deferred to Stage 7)
- [ ] Candidate work items (meeting jobs) shaped per the handoff contract,
      none targeted at direct Jira creation
- [ ] Every line carries the user's recorded confirm/edit/strike decision

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy — deviation from the U-curve middle, with reason: this
  stage decides what documentation gets built, updated, or archived; a
  framing error here cascades into every document the job produces, the same
  rationale as ai-refinement Stage 02's heavy call.
- **Evidence:** the confirmed work order with per-line user decisions, and a
  one-line entry in the run's decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- The work order references evidence by link; it does not duplicate
  confidential content. If a proposed document would require content above
  `internal`, the line is flagged and re-scoped, not planned.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
