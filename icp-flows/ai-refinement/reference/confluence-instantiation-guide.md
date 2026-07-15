---
id: ai-refinement-confluence-instantiation-guide
title: "Confluence Instantiation Guide — AI Refinement"
type: specification
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-03
updated: 2026-07-15
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
---

# Confluence Instantiation Guide — AI Refinement

**Status: prepared, not executed.** This guide exists because the flowspace's
own dual-surface design (`methodology/mirroring-protocol.md`) names Confluence
as the primary surface and this git tree as the Copilot mirror, but the
primary surface has never been instantiated — only the mirror exists. This
document is the operator's checklist for doing that instantiation and for
deploying the produced skills as live Rovo agents. No step in this guide has
been executed by any agent session; publishing to Confluence, creating Rovo
agent definitions, and granting them Jira actions are all actions this repo
cannot take on its own.

## 1. Why this is the operator's act, not an agent's

Per `AGENTS.md` rule 5 and `flow-foundry/foundry-spec.md` §5, promotion and
deployment are human-only gates. Beyond governance, the mechanics require
access this repo-editing environment does not have: a Confluence space to
write to, a Rovo agent-authoring surface, and a target Jira project to grant
actions against. Treat every checkbox below as a manual action log, not
something to script here.

## 2. Page-tree structure (target shape)

Mirrors `methodology/mirroring-protocol.md` §2's structure-mapping table,
applied to this flowspace:

```
AI Refinement (parent page — maps to HUB.md)
  ├── Stage 01 — Intake and Guardrails (01-intake-and-guardrails/CONTEXT.md)
  ├── Stage 02 — Context and Problem Framing (02-context-and-problem-framing/CONTEXT.md)
  ├── Stage 03 — Scope and Dependencies (03-scope-and-dependencies/CONTEXT.md)
  ├── Stage 04 — Field-by-Field Refinement (04-field-by-field-refinement/CONTEXT.md)
  ├── Stage 05 — Validation and Formatting (05-validation-and-formatting/CONTEXT.md)
  ├── Stage 06 — Jira Commit and Close (06-jira-commit-and-close/CONTEXT.md)
  ├── Reference
  │   ├── AI Refinement — Hybrid Definition (reference/ai-refinement-hybrid.md)
  │   ├── Work Item Schemas — Refinable Set (reference/work-item-schemas.md)
  │   ├── Platform Stakeholder Register (reference/platform-stakeholder-register.md)
  │   ├── Platform Stakeholder Register — Template (reference/platform-stakeholder-register-template.md)
  │   ├── Confluence Instantiation Guide (this page)
  │   └── On-Engine Validation Checklist (reference/on-engine-validation-checklist.md)
  └── Decision Log
      └── (one child page per icp-flows/ai-refinement/decision-log/ entry)
```

Naming rule (per the mirroring protocol): page title and git path both derive
from the artifact `id` in each file's frontmatter. Restore the redacted
internal policy link (`reference/ai-refinement-hybrid.md`'s responsibility
notice) at this step — it is safe only in employer tenancy.

## 3. Migration checklist (REC-01)

- [ ] Confluence space chosen and access confirmed.
- [ ] Mermaid-rendering macro installed in the target space, or the
      `HUB.md` diagram gets a "diagram: see mirror" fallback note (per
      `flow-foundry/foundry-spec.md` §2 question 4 and
      `methodology/mirroring-protocol.md` §2).
- [ ] `HUB.md` → parent page, with provenance frontmatter mapped to page
      properties + labels + Status macro (mirroring-protocol §2, §7).
- [ ] Each stage `CONTEXT.md` → numbered child page, section headings
      preserved (Inputs / Process / Outputs / Verify / Review / Data
      boundary).
- [ ] `reference/` files → Reference child page tree, including the two new
      prep artifacts and the stakeholder-register template.
- [ ] `decision-log/` entries → Decision Log child pages, one per entry.
- [ ] `MIRROR-STATE.md` established in the mirror per mirroring-protocol §3,
      stamped with this instantiation as the first sync.
- [ ] Drift check (mirroring-protocol §4) run once immediately after initial
      sync to confirm the two surfaces agree before any live use.

## 4. Rovo agent deployment checklist (REC-02)

- [ ] Decide: five separate per-stage agents (one per produced skill, per
      each skill's existing `adapters/rovo-agent.md`), or a single
      orchestrating agent embedding all six stages' logic and reading stage
      contracts from the Confluence pages as its instructions. The
      drift-analysis recommendation is the orchestrating agent, for the
      "hand a document to Rovo" goal — five separate agents require the user
      to invoke each in sequence.
- [ ] If orchestrating: instructions include the trigger phrases, guardrails,
      persona contract (with `communication_style` binding), the full schema
      registry, the fast-track mode-selection logic, and stage-transition
      logic that proceeds only on user confirmation at each boundary
      (respecting the hard carve-outs: Stage 02 stakeholder sweep, Stage 03
      coalition/conflict-axis annotation, Stage 04 due-date elicitation,
      Stage 06 parent-mapping confirmation — none of these compress under any
      agent design).
- [ ] `jira-commit`'s agent (whichever deployment shape) is granted exactly
      its stated permitted-action set: create/update Jira issue, create Jira
      issue link, search/query Jira issues, transition Jira issue — in the
      target project only. No other skill's agent gets write actions.
- [ ] Knowledge scoping for each agent matches its `SKILL.md`'s "Knowledge
      scoping" section — the instantiated Confluence page tree only, not the
      whole space.
- [ ] Confirm the target Jira project's board configuration actually
      supports what `jira-commit` assumes: a parent-candidate query action,
      a native (or connector) transition-issue action, and the custom fields
      the schema registry names (`type_of_work`, `work_category`,
      `question_to_answer`, `timebox` — see REC-04 / the schema-ratification
      gap in `HUB.md`'s Known gaps).

## 5. Sequencing note

Do §3 before §4 — the Rovo agents' instructions reference Confluence page
IDs, so the page tree needs to exist first. Do the on-engine validation
checklist (`on-engine-validation-checklist.md`) after both, using the newly
deployed agents.
