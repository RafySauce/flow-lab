---
id: docx-minimal-default-style
title: "Docx Minimal Default Style — Accomplishments Word Output"
type: template
artifact-version: "1.1"
status: living
truth-level: to-review
created: 2026-07-14
updated: 2026-10-27
owner: operator
source: human+ai
data-class: public
related: ["[[accomplishments-digest]]", "[[accomplishments-document-shape]]"]
---

# Docx Minimal Default Style — Accomplishments Word Output

> 1.1 (2026-10-27): moved here from the retired `accomplishments-docx-finisher`
> flow. It is now the "build from the default style" option that Stage 9
> offers the engineer, alongside "use your own template."

The style `accomplishments-docx-stylizer` applies at Stage 9 when the
engineer chooses "build from the default style" rather than supplying a
template. It is deliberately generic, with no employer branding and no color
beyond one neutral accent, so it stays public-safe in this repo. It maps
directly onto `accomplishments-document-shape.md`'s structure: one style rule
per element that shape defines.

## Style rules

| Element | Rule |
|---|---|
| Document title (`# <Engineer> — Accomplishments, <Period>`) | 20pt, bold, single accent color (see below), one blank line after. |
| Prepared-for line (`_Prepared for: …_`) | 10pt, italic, neutral gray (`#595959`), directly under the title. |
| Theme/section headings (`## <Theme>`, `## Summary`, `## Operational load`, `## Notes`) | 14pt, bold, same accent color as the title, 12pt space-before / 6pt space-after. |
| Body text | 11pt, a single legible serif or sans-serif body font (e.g., Calibri, Georgia — pick one, don't mix), 1.15 line spacing. |
| Bullets | Standard round bullet, one level deep — this document shape doesn't nest bullets; a nested bullet appearing in the styled output signals content that should have been split into its own theme instead. |
| Ticket/doc citations | Not shown inline in the Word version's reading text (per `accomplishments-document-shape.md`'s own rule: "ticket/doc reference kept out of the reader-facing line") — citations stay in the run's Stage 6 correlation map, not in the styled document. |
| Accent color | Exactly one, used only for the title and section headings — a neutral slate blue (`#2C5282`) as the placeholder value. This is the one value an operator should swap first when house branding is sourced; everything else in this default is intentionally plain enough to not need a swap. |
| Margins | 1 inch on all sides; no headers/footers beyond an optional page number, bottom center. |

## Style note appendix (required)

A short trailing section, styled distinctly from body text (10pt, with a plain
"Style note" heading), stating which style was applied ("minimal default" or
"engineer-supplied template: <file name>") and, for a template, any style
mappings made where the template lacked a style this shape needs. This is
the traceability Stage 9's Verify relies on, so a reader can tell which
format they are looking at. It replaces 1.0's top-of-document
missing-template note and Enrichment notes appendix, both of which belonged
to the retired finisher flow's enrichment step.

## When a house template is sourced

The engineer supplies it at Stage 9 as "use your own template." This default
stays available as the other option. Keep the style note appendix in both
cases, because it is a structural requirement of the flow, not an artifact
of this being the fallback.
