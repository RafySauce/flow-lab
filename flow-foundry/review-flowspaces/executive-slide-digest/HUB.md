---
id: executive-slide-digest
title: "Executive Slide Digest — Jira & Confluence Status to Executive .pptx"
type: flowspace
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-06
updated: 2026-08-06
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[fp-executive-slide-digest]]"
  - "[[sp-executive-slide-drafter]]"
  - "[[sp-executive-slide-pptx-stylizer]]"
  - "[[executive-slide-shape]]"
---

# Executive Slide Digest — Jira & Confluence Status to Executive .pptx

This flowspace turns a manager's request for exec-ready status on one or more
in-flight initiatives into a finished `.pptx` — status, outcome-framed
accomplishments, risks, and next milestones, shaped for an executive reader
from the first draft rather than hand-rewritten from a ticket dump after the
fact. Unlike `accomplishments-digest` (its closest analog: Jira/Confluence
gather, draft, human review), this is a **single pipeline** end to end to the
finished deck, not a digest-plus-styling-companion pair — an explicit
operator call made to keep one thing to maintain rather than two flows that
always run together in practice. One run = one finished deck for one
manager's ask, single-initiative or portfolio-rollup scope.

## Stage Flow Diagram

```mermaid
flowchart LR
    S1["1. Frame<br/>review: heavy"]:::heavy --> S2["2. Gather<br/>review: light"]:::light
    S2 --> S3["3. Draft<br/>review: light"]:::gap
    S3 --> S4["4. Align &amp; Publish<br/>review: heavy"]:::heavy
    S4 --> S5["5. Stylize to .pptx<br/>review: light"]:::gap
    S5 --> S6["6. Final Review &amp; Share<br/>review: heavy"]:::heavy

    classDef heavy fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef light fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef gap fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

> Stages 3 and 5 carry the `gap` color because their Layer-3 skills are built
> but **not promoted** — both are staged at `truth-level: to-review` in
> `skill-foundry/review-skills/`, awaiting the five-point gate
> (`skill-foundry/foundry-spec.md` §5). Per the diagram guide, `gap`
> overrides the review-intensity color while the Stage table below carries
> the real intensity. When the operator promotes both skills, these nodes
> take their true `light` color. See Known gaps.

## Stage table

| # | Stage | Review intensity | Max data-class | Sanctioned engines | Layer-3 |
|---|---|---|---|---|---|
| 1 | Frame | heavy | internal | Rovo, Copilot | inline — human judgment, no skill |
| 2 | Gather | light | internal | Rovo | inline — engine-native Jira/Confluence search (deliberately not a dedicated skill; see Known gaps) |
| 3 | Draft | light | internal | Rovo, Copilot | `executive-slide-drafter` (to-review, `skill-foundry/review-skills/`) |
| 4 | Align & Publish | heavy | internal | Rovo, Copilot | inline — human judgment, no skill |
| 5 | Stylize to .pptx | light | internal | Copilot | `executive-slide-pptx-stylizer` (to-review, `skill-foundry/review-skills/`) |
| 6 | Final Review & Share | heavy | internal | Rovo, Copilot | inline — human judgment, no skill |

## Source-repo

- **Source-repo:** the operator's internal GitLab instance repo,
  `flowspaces/executive-slide-digest/` — set at instantiation, sole source of
  truth for the instance.
- **External systems read:** Jira (primary), Confluence (secondary, where
  relevant) — read-only, via the engine's native search capability, at
  Stage 2 only. No stage writes to Jira or Confluence at any point in the
  flow.

## Run procedure

A run starts when a manager asks for exec-ready status on a named initiative
(single-initiative scope) or a set of initiatives (portfolio-rollup scope),
ahead of a review, steering meeting, or ad hoc executive ask. Stage 1 is the
heaviest-judgment stage: the manager states scope, which initiative(s) or
epics, audience, time period, and any explicit ask or decision needed from
the exec — this framing, not the tool data, is what keeps Stage 3's draft
from reading as an automated ticket export. Stage 2 runs the engine's native
Jira/Confluence search keyed off Stage 1's keywords or epic names — status,
recent activity, open blockers, upcoming due dates. Stage 3 synthesizes
Stage 2's gathered material against Stage 1's framing into the house
`reference/executive-slide-shape.md` content — one slide's content for
single-initiative scope, a deck outline for portfolio scope. Stage 4 is the
manager's own edit/approval pass against Stage 1's framing — the
content-correctness gate, checking the RAG calls, the framing, and any
stated asks, before any file is generated. Stage 5 applies the house
PowerPoint template to the approved content and produces the `.pptx`,
falling back to a clean minimal deck with an explicit missing-template note
if no house template has been sourced for the instance. Stage 6 is the
manager's own check that the generated deck reads correctly before sharing
it — the flow's terminal artifact.

This flow carries **two heavy gates** rather than the strict U-curve's single
first/last pair: Stage 4 checks content correctness, Stage 6 checks that
stylizing didn't distort or drop anything from the approved content.
`accomplishments-digest` gets the same two checks by splitting them across
two flowspaces (its own Stage 5, and its companion finisher's Stage 3); this
flow keeps both checks but folds them into one pipeline instead, per the
primer brief's explicit design call.

## Known gaps

> Per `methodology/governance-and-audit.md` §5a: each entry below is a
> pointer, not an archive — 1–3 sentences plus the decision-log citation
> that carries the full rationale.

Both Layer-3 skills demanded by Stages 3 and 5 are built — engine-neutral
spec plus adapters, staged `truth-level: to-review` in
`skill-foundry/review-skills/`. Evidence: `skill-foundry/decision-log/2026-
08-06-executive-slide-digest-skill-batch.md` (build) and its companion
`2026-08-06-executive-slide-digest-skill-gate-prerun.md` (five-point gate
pre-run — item 2, the on-engine live test, is open; no engine access this
session). Nothing is promoted, moved to `../../produced-skills/`, or
deployed; that is the operator's call per `skill-foundry/foundry-spec.md` §5.

| Skill | Primer brief | Target stage | Status |
|---|---|---|---|
| `executive-slide-drafter` | `sp-executive-slide-drafter` | 3 | built — staged `to-review` in `skill-foundry/review-skills/`; promotion pending |
| `executive-slide-pptx-stylizer` | `sp-executive-slide-pptx-stylizer` | 5 | built — staged `to-review` in `skill-foundry/review-skills/`; promotion pending |

Second gap: **no house PowerPoint template/branding asset exists in this
public repo** — an instantiation-time, employer-specific asset, per the
primer brief's open question 2. `executive-slide-pptx-stylizer`'s Method
falls back to `reference/pptx-minimal-default-style.md` (a concrete,
brand-neutral style: one title slide, one slide per initiative, neutral
accent color, RAG-colored status chips, an explicit missing-template note)
rather than leaving this undefined until someone sources a template — the
same resolution `accomplishments-docx-finisher` used for its own equivalent
gap.

Third gap: the primer brief's remaining open questions (whether Stage 2's
native search needs structure at all; a portfolio-rollup slide-count
ceiling; whether Confluence gather stays first-class) are unresolved by this
build — none of the three has a concrete instance case yet to resolve
against, per the brief's own framing. Deferred, not dropped.

## Reference material (Layer-3)

| Artifact | Location | Covers |
|---|---|---|
| Flow Primer Brief | `flow-foundry/backlog-flow-starters/fp-executive-slide-digest.md` | Original crystallized intent this flowspace was built from |
| Executive Slide Shape | `reference/executive-slide-shape.md` | The house content-shape template Stage 3 drafts into and Stage 4 edits against |
| Pptx Minimal Default Style | `reference/pptx-minimal-default-style.md` | Stage 5's brand-neutral fallback until a house PowerPoint template is sourced |
| Closest analog flowspace | `../../../icp-flows/accomplishments-digest/HUB.md` | The Jira/Confluence-to-document pattern this flow's stage shape and two-heavy-gate design borrow from |
| Provenance spec | `methodology/provenance-spec.md` | Frontmatter rules for all artifacts |
| Governance & Audit | `methodology/governance-and-audit.md` | Gate requirements |
| Mirroring Protocol | `methodology/mirroring-protocol.md` | Source-repo and handoff conventions |
