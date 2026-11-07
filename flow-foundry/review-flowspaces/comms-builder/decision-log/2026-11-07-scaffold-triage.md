---
id: decision-2026-11-07-comms-builder-scaffold-triage
title: "Decision — Comms Builder: triage, lanes, scope, and design-system calls"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-11-07
updated: 2026-11-07
owner: operator
source: human+ai
data-class: public
related:
  - "[[fp-comms-builder]]"
  - "[[comms-builder]]"
  - "[[executive-slide-digest]]"
---

# Decision — Comms Builder: triage, lanes, scope, and design-system calls

## Context

The operator asked for a flow that takes "we need to get communications out
to <audience> regarding <subject>", decides whether it is a campaign or a
one-off, and produces audience design, templated drafts, linked change
materials, a comms plan with a timeline visual, and implementation meeting
materials — consistent in look with the operator's design system. The
operator brainstormed the shape on 2026-11-06, chose among labeled options,
and gave the go-ahead to scaffold on 2026-11-07.

## Decisions

### 1. Triage: case 4 — bare conversation

No filed starter existed. The setup questionnaire is answered in the
backfilled brief, `backlog-flow-starters/fp-comms-builder.md`. Not case 3: the
work is multi-stage with judgment at several boundaries and recurs per
subject.

### 2. One flow with two lanes (operator: D1 option A)

One flowspace; Stage 1 proposes one-off or campaign and the user decides.
Rejected: a separate one-off skill plus campaign flow (the triage would live
in the user's head), and campaign-only (one-offs are common and benefit from
the same audience and data checks). `comms-drafter` stays standalone-callable
for a quick single message.

### 3. Sibling of `executive-slide-digest`, sharing a generalized stylizer (operator: D2 options A and C)

The digest reports initiative status to executives; this flow prepares
stakeholders for something happening to them. They stay separate flowspaces.
A new brief, `sp-deck-stylizer`, generalizes `executive-slide-pptx-stylizer`
around a design-system binding so both flows can share it. Nothing about
the digest or its stylizer changes in this build; switching the digest over
is a later, separate operator decision.

### 4. Design system implemented inside the stylizer; operator's system stays private (operator: D3, then "Go, Forest stays private")

The binding contract and a brand-neutral default ship here
(`reference/design-system-binding.md`) and move into `deck-stylizer` when it
is built. The operator's own design system is bound only in their instance
and is not committed to this repo. Emails and Teams posts take voice rules
only, never visual styling: recipients' clients strip styling, and internal
messages must read as the employer's own comms.

### 5. Timeline: Mermaid gantt, image plus raw source, meaningful colors (operator: D4 option A)

Colors map to gantt task states (upcoming, sent, awaiting validation, key
window, milestone) and always pair with a word. Jira gets a table fallback;
Jira comments do not render Mermaid.

### 6. Source records via a new narrow skill (operator: D5 option A)

`sp-comms-context-linker` is keyed by record number, borrowing
`cab-change-manifest`'s source probe and cite-not-paste rules. Renamed from
the brainstorm's `change-context-linker` because the operator widened scope
to incidents and CVEs.

### 7. Scope widened beyond changes

Operator: changes are the first use case; the flow also covers shared
services, platform changes, key projects, and CVE or incident response
plans. Primary audiences: application owners, technical owners, business
users — the default segments. CVE and incident response came off the
brainstorm's non-goals list, with a data rule: impact, timing, and actions
only; no exploit details, configs, IPs, or control descriptions.

### 8. Campaign signals

Operator: large-scale changes impacting many stakeholders; changes needing
specific validation from application teams; projects with many different
stakeholders. The validation signal adds a validation tracker to Stage 4
and validator roles to Stage 6.

### 9. Copilot-only execution; Rovo by manual handoff

Operator: everything runs in Copilot; anything that must go into Rovo is a
manual `.md` handoff. Stage 8 emits commit packets per
`methodology/engine-handoff-contract.md`. This removes the need for a new
Jira-comment skill (`jira-commit` is create-only); the Rovo executor posts
the comment natively.

### 10. Templates from an operator folder, else plain defaults

Operator will place templates in a folder the agent can read; the binding
config carries `template-path`. Without it, `reference/default-message-templates.md`
applies.

## Pre-checks run by the foundry (agent-side)

- Stage table matches the eight stage folders and the diagram one-for-one.
- Every `CONTEXT.md` has all six fields populated; Verify fields name two
  stages, an artifact, and a property.
- Every stage's Layer-3 status is declared; five briefs exist in
  `skill-foundry/backlog-skill-starters/`.
- No employer content, names, or design-system values beyond the neutral
  default.
- Not done: GitLab rendering check, human dry-run, on-engine test. Those are
  the operator's gates.
