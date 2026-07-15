---
id: docx-minimal-default-style
title: "Docx Minimal Default Style — Accomplishments Docx Finisher"
type: template
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-14
updated: 2026-07-15
owner: operator
source: human+ai
data-class: public
related: ["[[accomplishments-docx-finisher]]", "[[accomplishments-document-shape]]"]
---

# Docx Minimal Default Style — Accomplishments Docx Finisher

The concrete fallback `accomplishments-docx-stylizer` (Stage 2) applies when
no house Word template/branding asset has been sourced for the target
instance — resolving the open question in
`../../../backlog-flow-starters/fp-accomplishments-docx-finisher.md` ("where
does the house Word template live?") from "undefined until someone sources
one" to "a usable, brand-neutral default exists now; swap it for house
branding whenever one is sourced." This is deliberately generic — no
employer branding, no color beyond one neutral accent — so it stays public-
safe in this repo. It maps directly onto `accomplishments-document-shape.md`'s
structure: one style rule per element that shape defines.

## Style rules

| Element | Rule |
|---|---|
| Document title (`# <Engineer> — Accomplishments, <Period>`) | 20pt, bold, single accent color (see below), one blank line after. |
| Prepared-for line (`_Prepared for: …_`) | 10pt, italic, neutral gray (`#595959`), directly under the title. |
| Theme/section headings (`## <Theme>`, `## Summary`, `## Notes`) | 14pt, bold, same accent color as the title, 12pt space-before / 6pt space-after. |
| Body text | 11pt, a single legible serif or sans-serif body font (e.g., Calibri, Georgia — pick one, don't mix), 1.15 line spacing. |
| Bullets | Standard round bullet, one level deep — this document shape doesn't nest bullets; a nested bullet appearing in the styled output signals content that should have been split into its own theme instead. |
| Ticket/doc citations | Not shown inline in the Word version's reading text (per `accomplishments-document-shape.md`'s own rule: "ticket/doc reference kept out of the reader-facing line") — carried instead in the Enrichment notes appendix (see below) where a citation is itself the flagged content. |
| Accent color | Exactly one, used only for the title and section headings — a neutral slate blue (`#2C5282`) as the placeholder value. This is the one value an operator should swap first when house branding is sourced; everything else in this default is intentionally plain enough to not need a swap. |
| Margins | 1 inch on all sides; no headers/footers beyond an optional page number, bottom center. |

## Missing-house-template note (required)

Whenever this default is used instead of a sourced house template, the
stylizer appends a single-line note at the top of the document, above the
title: *"No house template configured for this instance — formatted with
the accomplishments-digest minimal default."* This is not optional styling
polish; it's the traceability the skill's spec requires (Review criterion
3) so a reader — and Stage 3's reviewer — knows this is a placeholder
format, not the org's intended final look.

## Enrichment notes appendix

A trailing section, styled distinctly from body text (10pt, boxed or
shaded background if the target format supports it; a plain "Enrichment
notes" heading plus a bulleted list otherwise), listing each of Stage 1's
flagged additions with the theme it supports and its source citation
(commit/PR/doc link). This is where every enrichment-stage citation actually
lives in the Word version — never inline in the reading text.

## When a house template is sourced

Replace the accent color, title/heading fonts, and margins with the
sourced template's values; keep the Enrichment-notes-appendix and missing-
template-note *mechanisms* (the appendix's existence, the flag format) even
after a house template exists — those are structural requirements of the
flow, not artifacts of this being the fallback.
