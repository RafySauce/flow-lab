---
id: accomplishments-docx-finisher
title: "Accomplishments Docx Finisher — Copilot Word Styling Companion"
type: flowspace
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-07-14
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[fp-accomplishments-docx-finisher]]"
  - "[[accomplishments-digest]]"
  - "[[sp-repo-context-enricher]]"
  - "[[sp-accomplishments-docx-stylizer]]"
---

# Accomplishments Docx Finisher — Copilot Word Styling Companion

A companion flowspace to `accomplishments-digest`: it never starts on its
own, only on a handoff from that flow's Stage 6, and its whole job is to turn
an already human-approved accomplishments document into a final, stylized
Word file — using Copilot's repository and file access to add supporting
evidence (not new claims), then applying house branding, then one more human
review before anything is shared. One run = one `.docx` for one review cycle,
paired one-to-one with an upstream `accomplishments-digest` run.

## Stage Flow Diagram

```mermaid
flowchart LR
    S1["1. Receive &amp; Enrich<br/>review: light"]:::light --> S2["2. Stylize to Word<br/>review: light"]:::light
    S2 --> S3["3. Align &amp; Publish<br/>review: heavy"]:::heavy

    classDef heavy fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef light fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef gap fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

> Stage 1 is `light`, not `heavy`, despite being first — a documented
> deviation from the U-curve default (see Stage 1's `CONTEXT.md` and the
> primer brief): the framing judgment already happened upstream at
> `accomplishments-digest` Stage 5. Stage 3 carries the compensating heavy
> review, re-checking Stage 1's additions against the handoff's exclusion
> list before anything is shared.

## Stage table

| # | Stage | Review intensity | Max data-class | Sanctioned engines | Layer-3 |
|---|---|---|---|---|---|
| 1 | Receive & Enrich | light¹ | internal | Copilot | `sp-repo-context-enricher` (gap — brief filed) |
| 2 | Stylize to Word | light | internal | Copilot | `sp-accomplishments-docx-stylizer` (gap — brief filed) |
| 3 | Align & Publish | heavy | internal | Copilot | inline — human judgment, no skill |

¹ Deviates from the U-curve "first stage heavy" default — see diagram note above.

## Surfaces

- **Primary:** Copilot-side, grounded in the internal git mirror — this
  flowspace has no independent Confluence page tree; it exists to serve the
  Rovo-primary `accomplishments-digest` flow's optional Stage 6 handoff.
- **Mirror:** `<internal repo>` → `flows/accomplishments-docx-finisher/`.
- **Terminal output:** a `.docx` file, not a Confluence page. Once Stage 3
  shares it, the artifact leaves the ICP structure entirely — there is no
  Stage 4 within this flowspace.

This public copy is the sanitized *design*; instantiation happens in employer
tenancy per `methodology/mirroring-protocol.md`. At instantiation, add the
per-stage `work/` folders (Layer-4, transient) and the `handoffs/` folder
that receives `accomplishments-digest`'s Stage 6 output — deliberately absent
here since they only ever hold per-run content.

## Run procedure

A run starts when a handoff file from `accomplishments-digest` Stage 6 lands
in `handoffs/`. Stage 1 parses it, confirms the authorized repo/file-access
scope, and pulls supporting evidence within that scope only — every addition
is flagged distinctly in its output so Stage 3 can scrutinize exactly what
changed versus the handed-off content. Stage 2 applies the house Word
template to produce the `.docx`. Stage 3 is the engineer's own review: does
the styled document still respect the original exclusion list, does Stage 1's
enrichment read as supporting evidence rather than new claims, and does the
result actually look like something worth sending. On approval, the engineer
shares the file directly — there's no publish-to-Confluence step here, since
the source flow already owns that surface.

## Known gaps

Two skills built from this flowspace's Layer-3 triage, both
`truth-level: to-review` and staged in `skill-foundry/review-skills/`,
awaiting the operator's five-point promotion gate (`skill-foundry/foundry-
spec.md` §5) before they land in `produced-skills/`:

| Skill (gap) | Primer brief | Target stage | Status |
|---|---|---|---|
| Repo context enricher | `sp-repo-context-enricher` | 1 | built, staged in `review-skills/repo-context-enricher/` — awaiting promotion |
| Accomplishments docx stylizer | `sp-accomplishments-docx-stylizer` | 2 | built, staged in `review-skills/accomplishments-docx-stylizer/` — awaiting promotion |

Until these are promoted to `produced-skills/`, Stages 1–2 still run as
manual/ungrounded conversation against these contracts in practice — staging
closes the build gap, not the deployment gap. Both skills declare Copilot as
their only sanctioned engine (no Rovo adapter) — see
`skill-foundry/decision-log/2026-07-14-accomplishments-digest-skill-batch.md`
for why. Second gap: the house Word template/branding asset this flowspace
depends on (Stage 2) still doesn't exist in this public repo — that's an
instantiation-time, employer-specific asset no public method repo can hold —
but Stage 2 now has a concrete, brand-neutral fallback to apply until one is
sourced: `reference/docx-minimal-default-style.md`, wired into the
`accomplishments-docx-stylizer` skill's Method as its default behavior, not
left as an unstyled placeholder.

## Reference material (Layer-3)

| Artifact | Location | Covers |
|---|---|---|
| Flow Primer Brief | `../../backlog-flow-starters/fp-accomplishments-docx-finisher.md` | Original crystallized intent this flowspace was built from |
| Source flowspace | `../accomplishments-digest/HUB.md` | The Rovo-primary flow this one is a companion to |
| Handoff Template | `../accomplishments-digest/reference/handoff-to-copilot-template.md` | The exact handoff shape Stage 1 receives |
| Docx Minimal Default Style | `reference/docx-minimal-default-style.md` | Stage 2's brand-neutral fallback until a house Word template is sourced |
| Provenance spec | `methodology/provenance-spec.md` | Frontmatter rules for all artifacts |
| Governance & Audit | `methodology/governance-and-audit.md` | Gate requirements |
| Mirroring Protocol | `methodology/mirroring-protocol.md` | Handoff artifact shape (§5) this flowspace consumes |
