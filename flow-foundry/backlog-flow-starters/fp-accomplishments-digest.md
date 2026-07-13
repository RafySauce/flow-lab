---
id: fp-accomplishments-digest
title: "Flow Primer Brief — Accomplishments Digest"
type: flow-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-07-08
owner: operator
source: human+ai
data-class: public
related: ["[[accomplishments-digest]]"]
---

# Flow Primer Brief — Accomplishments Digest

> Filed and built in the same session, on direct operator instruction. Build staged at `flow-foundry/review-flowspaces/accomplishments-digest/`, `truth-level: to-review` — awaiting the operator's three-gate review before promotion to `icp-flows/`.

## Purpose

Turn the scattered signal of an engineer's Jira and Confluence activity into a single, readable accomplishments document they can hand to their manager ahead of a performance review — grouped by theme, framed in outcome terms rather than a ticket list, and carrying the engineer's own read on impact rather than only what the tracker shows. Recurs once per formal review cycle (quarterly / annual / promo).

## Trigger and cadence

Review-cycle driven: the engineer (or their manager, on the engineer's behalf) kicks off a run ahead of a scheduled performance review, self-assessment deadline, or promotion packet. Not a rolling background job — one run per cycle, scoped to that cycle's date range.

## Stage sketch

| # | Stage | What happens | Review intensity (est.) |
|---|---|---|---|
| 1 | Frame | Engineer sets the review period, audience, and their own read on top impact; flags anything sensitive to exclude | heavy |
| 2 | Gather — Jira | Pull delivered work (closed tickets/epics) in the period, grouped by theme, outcome-framed rather than counted | light |
| 3 | Gather — Confluence & collaboration signal | Pull initiatives and docs authored/driven (RFCs, design docs, postmortems) plus cross-team collaboration signal (reviews, mentions, comments) where the platform surfaces it | light |
| 4 | Draft | Synthesize stage 1's narrative with stages 2–3's digest into the house accomplishments-document shape | light |
| 5 | Align & publish | Engineer reviews against stage-1 framing, edits, and finalizes the version they actually share with their manager | heavy |

## Data profile

Internal project and performance-adjacent data throughout (`data-class: internal` at instantiation — this exemplar/design copy is `public`, no real content). Performance-review material is people-sensitive by nature even when not formally confidential: stage 1's exclusion list and stage 5's final read are the two points that most need a human, not an agent, holding the pen. No customer PII expected; if gathered material surfaces any, stages 2–3's data boundary escalates and the run is flagged.

## Layer-3 inventory

- Stage 2: candidate skill gap — a **Jira accomplishments gatherer** (query closed work in a date range, group by theme, reframe from ticket titles to outcomes). `sp-jira-accomplishments-gatherer` filed.
- Stage 3: candidate skill gap — a **Confluence contribution gatherer** (authored/co-authored pages, collaboration signal, in a date range). `sp-confluence-contribution-gatherer` filed.
- Stage 4: candidate skill gap — an **accomplishments drafter** (digest + narrative → house document shape). `sp-accomplishments-drafter` filed.
- Stages 1 and 5: human judgment, inline — no skill gap.

## Surfaces

Primary: the engineer's personal or team Confluence space, an `Accomplishments` page tree (one page per review cycle). Mirror: internal repo `flows/accomplishments-digest/`.

## Open questions

- Does the target org's Jira/Confluence instance expose enough activity history (comments, review participation) to make the collaboration-signal slice reliable, or does stage 3 need to fall back to a narrower "authored pages only" scope per instance? (Resolve at instantiation — flagged in stage 3's contract as a per-tenant capability check, not assumed.)
- Should promotion-packet runs (higher stakes, wider audience) get a distinct stricter mode, or is stage 5's heavy review sufficient across all review types? Deferred — no evidence yet that they need to diverge.
