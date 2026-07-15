---
id: decision-2026-07-15-documentarian-scaffold-triage
title: "Decision Log — Documentarian Scaffold Triage"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
data-class: public
related:
  - "[[documentarian]]"
  - "[[fp-documentarian]]"
---

# Decision Log — 2026-07-15 — Scaffold Triage

## Classification

**Input**: `fp-documentarian.md` (flow-primer-brief, filed same day from the
operator's crystallized intent — five named use cases, complementarity to
ai-refinement, humans-first / agent-custodians-later mandate)
**Classification**: Flow-primer-brief → clean path
**Rationale**: Purpose, trigger set, stage sketch, data profile, Layer-3
inventory, and surfaces all populated; transcribe decided intent into
structure without re-opening exploration.

## Topology Decision

**Choice**: Four-band topology — Foundation (S1) / Job Framing (S2–S3) /
Per-Document Pipeline (S4–S6, loop) / Custody & Close (S7)
**Alternatives considered**: (a) a family of sibling flowspaces per use case;
(b) a core authoring flow plus a separate custodial companion (the
accomplishments-digest / docx-finisher pairing); (c) ai-refinement's two-band
shape as-is.
**Reason**: One job (a close-out, an audit) yields *many* documents, so the
per-item loop must sit mid-flow, not span it — that forces the extra band
beyond ai-refinement's two. The five use cases share the whole lifecycle
(gather → plan → draft → validate → commit → custody) and differ only in
gathering mode and work-order shape, so one routed flow with job-type
steering beats five near-identical flowspaces or a split companion.
**Affects**: HUB Topology section, the S6→S4 loop edge, Stage 07's
once-per-job position.

## Two calls recorded so the omissions read as decisions

- **No distinct tree-audit band.** The audit use case is a `tree-audit` job
  whose Stage 3 output is simply a large work order (audit-report preamble +
  remediation and archive lines); each line rides the same Band ③ loop and
  Stage 7 executes confirmed archives. Only cardinality differs — the
  work-order artifact already is the routing contract.
- **No fast-track analog.** ai-refinement's fast-track compresses field
  elicitation; here Stage 4's open-section protocol is already the
  collaboration dial (richer evidence → fewer open sections). A mode switch
  would duplicate that mechanism. Stated in HUB Topology.

## Stage Breakdown

| Stage | Name | Intensity | Rationale |
|---|---|---|---|
| 01 | Intake & Routing | Heavy | Session trust boundary — a missed screen or wrong job type cascades into every document |
| 02 | Evidence Gathering | Light | Read-only, mode-constrained sweep; inspected for coverage and citation |
| 03 | Doc Plan & Template Match | Heavy | U-curve deviation, stated: decides what gets built/updated/archived — framing errors cascade (the ai-refinement Stage 02 rationale) |
| 04 | Draft & Update | Light | Constrained execution against confirmed line + template; user inspects each draft inline |
| 05 | Standards Validation | Light | Mechanical checks against written schema/baseline; review confirms report accuracy |
| 06 | Commit & Link | Heavy | Commit boundary, unconditionally — writes to shared platforms colleagues rely on |
| 07 | Custody & Close | Heavy | Last stage (U-curve default) + independent reason: archive/lifecycle calls are judgment; also the precedent boundary for future agent-custodians |

Four heavy of seven — each deviation carries its stated reason per the
validation checklist.

## Layer-3 Triage

| Capability | Classification | Action |
|---|---|---|
| Guardrails, routing rules, registry pointers | Inline | Stage 01 Process |
| Job-type-steered evidence gathering | Gap | → `sp-doc-evidence-gatherer` |
| Work-order planning & template match | Gap | → `sp-doc-planner` |
| Template drafting with open-section protocol | Gap | → `sp-doc-drafter` |
| Diagram-source maintenance (sad-update) | Gap (merge candidate) | → `sp-sad-diagram-maintainer` — the skill-foundry decides fold-vs-standalone at build |
| Schema/standards validation | Gap | → `sp-doc-standards-validator` |
| Confluence write path | Gap | → `sp-confluence-page-commit` — verified: no existing skill writes to Confluence (`confluence-contribution-gatherer` is read-only); `jira-commit` is the discipline mold |
| ai-refinement handoff packaging | Inline | Stage 06 step 7, per `reference/ai-refinement-handoff-contract.md` |
| Registry/freshness/archive bookkeeping | Gap | → `sp-doc-custodian` |
| Archive-confirmation dialogue | Inline | Stage 07 step 3 — judgment protocol owned by the flowspace |
| ServiceNow KB write path | Gap, **deferred** | → `sp-servicenow-kb-commit`, filed not-to-build (prerequisites on the brief) |
| Mirror-side frontmatter stamping | Existing skill | `provenance-stamper` (verified) referenced at Stages 05/07 |
| Scaffold contract pre-check (build-time) | Existing skill | `contract-reviewer` (verified) — agent-side pre-check before staging |

**Deliberate non-reuse** (near-misses, rationale also in each brief):
`jira-accomplishments-gatherer` / `confluence-contribution-gatherer` are
scoped to one engineer's accomplishments evidence with different quality
bars; `context-elicitation` is bound to the TPSO persona and work-item
schemas; `jira-commit` commits work items, which this flow never does —
candidates route to ai-refinement via the handoff contract.

## Skill Demand Generated

Eight skill-primer-briefs filed into `skill-foundry/backlog-skill-starters/`
per the demand loop: `sp-doc-evidence-gatherer`, `sp-doc-planner`,
`sp-doc-drafter`, `sp-sad-diagram-maintainer`, `sp-doc-standards-validator`,
`sp-confluence-page-commit`, `sp-doc-custodian`, and `sp-servicenow-kb-commit`
(deferred).

## Deferred questionnaire item

Question 9 (stakeholder register): none exists for the documentation domain.
Ownership/audience questions run in ungrounded mode until a
documentation-owners register is instantiated from
`platform-stakeholder-register-template.md`. Noted in HUB Known gaps and the
primer brief's open questions.

## Spec/template divergences flagged for operator ratification

Per provenance-spec ("when a template and this spec disagree, the spec
wins") and its rule that foundries flag rather than extend:

1. **`stage-context` is absent from the provenance-spec Type enum** yet is
   the established practice in every ai-refinement stage contract; this
   scaffold follows the practice. Operator to add the enum row (or rule
   otherwise).
2. **`skill-primer-brief-template.md` omits `generated-by-version`**;
   conditional rule 3 says the pair travels together. The eight briefs carry
   both. Template touch-up for the operator.
3. **`flowspace-scaffold.md` shows per-stage `work/` and `handoffs/`**; both
   promoted flowspaces omit them from design copies as instantiation-time
   additions. This scaffold follows the promoted precedent, stated in HUB
   Surfaces.
4. **`flow-diagram-guide.md` names GitLab as the mirror render surface**;
   this repo hosts on GitHub (also native Mermaid). Gate-1 "rendering
   confirmed" is read as the GitHub rendered view for this public copy.
5. **Decision-log default truth-level**: the spec's type table says
   `verified (records an event)`, but rule 5 requires review evidence for
   `verified`, and the ai-refinement scaffold-triage precedent stages at
   `to-review`. This entry follows the precedent.
