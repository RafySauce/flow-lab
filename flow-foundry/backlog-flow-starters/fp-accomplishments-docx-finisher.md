---
id: fp-accomplishments-docx-finisher
title: "Flow Primer Brief — Accomplishments Docx Finisher"
type: flow-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-07-08
owner: operator
source: human+ai
data-class: public
related: ["[[accomplishments-digest]]", "[[accomplishments-docx-finisher]]"]
---

# Flow Primer Brief — Accomplishments Docx Finisher

> Companion to `accomplishments-digest`, filed and built in the same session
> on direct operator instruction. Build staged at
> `flow-foundry/review-flowspaces/accomplishments-docx-finisher/`,
> `truth-level: to-review`.

## Purpose

Take the human-approved document `accomplishments-digest` publishes, and use
Copilot's repository/file context and access to produce a final, stylized
Word document — the version an engineer actually attaches to an email or a
promo packet, rather than a bare Confluence export. Recurs whenever an
`accomplishments-digest` run's Stage 6 hands off (same cadence as the source
flow: review-cycle driven).

## Trigger and cadence

A handoff file landing in `handoffs/` from `accomplishments-digest` Stage 6.
Never triggers on its own — it has no independent entry point, by design:
it only ever enriches and stylizes content another flow already got
human-approved.

## Stage sketch

| # | Stage | What happens | Review intensity (est.) |
|---|---|---|---|
| 1 | Receive & Enrich | Copilot ingests the handoff, pulls authorized repo/file context to add supporting evidence — presentation only, no new claims | light (deviation from U-curve default — see below) |
| 2 | Stylize to Word | Apply the house Word template/branding to the enriched content, produce a `.docx` | light |
| 3 | Align & Publish | Engineer reviews the styled Word doc against the handoff's exclusion list and the original Stage-5 approval, then shares it | heavy |

Stage 1 deviates from the U-curve's "first stage heavy" default: the
direction-setting judgment already happened upstream, at the source flow's
Stage 5. Stage 1 here is enrichment against an explicit, narrow, pre-
authorized scope — not open framing. The heavy check moves to Stage 3
instead, which re-verifies nothing Stage 1 added violates the carried-forward
exclusion list.

## Data profile

Internal document content (inherited from the handoff) plus whatever
repo/file content Stage 1 is authorized to pull — code references, commit
links, project docs. `data-class: internal` at instantiation; `public` here
since this is the sanitized design copy. No new PII expected, but Stage 1's
authorized-scope constraint is the guardrail if repo content unexpectedly
carries any.

## Layer-3 inventory

- Stage 1: candidate skill gap — a **repo-context enricher** (Copilot: pull
  scoped, authorized supporting evidence from repo/file access; flag every
  addition distinctly for Stage 3's review). `sp-repo-context-enricher` filed.
- Stage 2: candidate skill gap — an **accomplishments docx stylizer**
  (Copilot: merge enriched content into a house Word template, produce a
  `.docx`). `sp-accomplishments-docx-stylizer` filed.
- Stage 3: human judgment, inline — no skill gap.

## Surfaces

Primary: Copilot-side, grounded in the internal git mirror (this flowspace
has no independent Confluence page tree — it's a Copilot-native companion to
a Rovo-primary flow). Mirror: internal repo `flows/accomplishments-docx-finisher/`.
Output: a `.docx` file, not a Confluence page — the terminal artifact leaves
the ICP structure entirely once Stage 3 shares it.

## Open questions

- Where does the house Word template/branding live, and who owns keeping it
  current? Not resolved here — Stage 2's contract flags it as an
  instantiation-time asset to source, not assumed to already exist.
- Does every target org sanction Copilot with the repo access Stage 1 needs,
  or does this flowspace need a narrower "no repo access, text-only
  restyling" fallback mode? Deferred — no evidence yet that it's needed;
  revisit if instantiation hits a sanctioned-tool-matrix wall.
