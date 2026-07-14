---
name: accomplishments-docx-stylizer
description: >
  Applies a house Word template/branding to Stage 1's enriched
  accomplishments content set and produces a final .docx — preserving
  section/theme structure and Stage 1's flagged-addition markers in a still-
  identifiable form. Falls back to a clean minimal default and flags a
  missing house template rather than inventing branding on the fly. Invoke
  at Stage 2 of accomplishments-docx-finisher with Stage 1's enriched content
  set in hand. Do NOT use to enrich content (repo-context-enricher), for the
  final human review/share (Stage 3 stays inline), or for Word-document
  generation unrelated to this flow's specific content shape.
# --- provenance (house layer) ---
id: accomplishments-docx-stylizer
type: skill
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-14
updated: 2026-07-14
owner: operator
source: human+ai
generated-by: skill-foundry
generated-by-version: "1.4"
data-class: public
related: ["[[sp-accomplishments-docx-stylizer]]", "[[accomplishments-docx-finisher]]"]
---

# Accomplishments Docx Stylizer

Stage 2 of `accomplishments-docx-finisher` — the last automated step before
the flow's own heavy human review. It is pure formatting: it applies house
branding to Stage 1's enriched content and produces a `.docx`, introducing no
new content and never erasing the traceability Stage 1 built into its
flagged additions.

## Flow Diagram

```mermaid
flowchart LR
    Start(["Trigger: Stage 1 enriched content set,<br/>with flagged-additions list"]):::start --> R["Step 1 — Read enriched content<br/>Preserve section/theme structure<br/>from the house document shape"]:::process
    R --> T{"House Word template<br/>configured for this instance?"}:::decision
    T -->|Yes| A["Apply house template/branding"]:::process
    T -->|No| D["Apply clean minimal default;<br/>flag missing house template as a note"]:::halt
    A --> P["Step 2 — Preserve flagged additions<br/>Distinct character style or<br/>trailing 'Enrichment notes' appendix"]:::process
    D --> P
    P --> Output(["Output: draft .docx<br/>(work/02-draft.docx)"]):::output

    classDef start fill:#1e293b,stroke:#94a3b8,color:#f1f5f9
    classDef process fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef decision fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef output fill:#14532d,stroke:#4ade80,color:#dcfce7
    classDef halt fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

## Triggering intent

- **Fires on:** Stage 2 of `accomplishments-docx-finisher`, given Stage 1's
  enriched content set.
- **Does not fire on (near-misses):** enriching content (that's
  `repo-context-enricher`); the final human review/share (Stage 3 stays
  inline, human); any Word-document generation unrelated to this flow's
  specific content shape.

## Method

1. **Read the enriched content set,** preserving the section/theme structure
   from `accomplishments-digest`'s house document shape
   (`flow-foundry/review-flowspaces/accomplishments-digest/reference/accomplishments-document-shape.md`)
   — the Word version must read as the same document in a different format,
   never a re-authored one. Every section present in the input must appear
   in the output; dropping one to fit a template layout is a defect.
2. **Apply the house template if one exists** for the target instance:
   headings, theme structure, and typography consistent with the source
   shape. **If no house template has been sourced yet** — an
   instantiation-time asset this design does not assume exists — apply the
   concrete fallback defined in
   `flow-foundry/review-flowspaces/accomplishments-docx-finisher/reference/docx-minimal-default-style.md`
   (heading sizes, one neutral accent color, body type, margins) rather than
   inventing a look. Flag the missing house template as the explicit note
   that reference defines, above the document title — a stylizer that
   guesses at "what the company's branding probably looks like" has failed
   this step.
3. **Preserve Stage 1's flagged-addition markers** through to the styled
   output in a form Stage 3 can still identify — a distinct character style
   (e.g., a consistent highlight or footnote marker) or a trailing
   "Enrichment notes" appendix listing each addition and what it supports.
   Styling must never erase the traceability Stage 1 built; an addition that
   reads as indistinguishable original prose after stylizing is the known
   failure mode this step guards against, alongside silently dropping a
   section or introducing content absent from Stage 1's output.

## Inputs and grounding

Reads: Stage 1's enriched content set (`work/01-enriched-content.md`),
including its flagged-additions list, and the handoff's stated style/template
preference if any. Grounding rules: no content beyond what Stage 1 produced
enters the `.docx` — this skill formats, it does not draft, enrich, or
summarize; a missing house template is reported, never fabricated from
assumption.

## Data boundary

- Max data-class: internal (inherits Stage 1's classification; pure
  formatting, no new content sourced).
- Sanctioned engine: Copilot only, consistent with Stage 1 — no engine
  change mid-flow. No Rovo adapter is built for this skill.

## What this skill is not

- **Not an enrichment tool** — it formats what Stage 1 already produced; it
  never searches a repo or adds supporting evidence itself.
- **Not the final review** — Stage 3's human review determines whether the
  styled result is fit to share.
- **Not a branding-inventor** — a missing house template is a flagged gap,
  never an invitation to design new house branding unilaterally.
- **Not a general Word-generation tool** — it only formats content already
  shaped by this flow's specific structure.

## Review criteria

A single output of this skill is acceptable when:

1. Every theme/section present in Stage 1's enriched content set appears in
   the styled `.docx` — none silently dropped.
2. No content appears in the `.docx` beyond what Stage 1's output contained.
3. If no house template was configured, the output uses the clean minimal
   default and carries an explicit note flagging the missing template.
4. Every one of Stage 1's flagged additions remains identifiable as such in
   the styled output (distinct character style or an Enrichment notes
   appendix) — none blended into indistinguishable body text.
5. Heading hierarchy and structure mirror the house accomplishments-document
   shape's theme organization.

## Adapters

| Engine | Artifact | Generated from spec version |
|---|---|---|
| Copilot | adapters/copilot-prompt.md | 1.0 |

No Rovo adapter is built: Stage 2 stays Copilot-side to match Stage 1, and
`.docx` generation from repo-context-enriched content has no Confluence-
native point of use in this pairing — see
`../../decision-log/2026-07-14-accomplishments-digest-skill-batch.md`.

## Changelog

- **1.0** (2026-07-14) — Initial build from `sp-accomplishments-docx-stylizer`.
