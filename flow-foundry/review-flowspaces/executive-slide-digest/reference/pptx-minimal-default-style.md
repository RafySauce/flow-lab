---
id: pptx-minimal-default-style
title: "Pptx Minimal Default Style — Executive Slide Digest"
type: template
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-06
updated: 2026-08-06
owner: operator
source: human+ai
data-class: public
related: ["[[executive-slide-digest]]", "[[executive-slide-shape]]"]
---

# Pptx Minimal Default Style — Executive Slide Digest

The concrete fallback `executive-slide-pptx-stylizer` (Stage 5) applies when
no house PowerPoint template/branding asset has been sourced for the target
instance — resolving the primer brief's open question 2 ("whether a house
PPT template exists yet") from "undefined until someone sources one" to "a
usable, brand-neutral default exists now; swap it for house branding
whenever one is sourced." Deliberately generic — no employer branding, no
color beyond one neutral accent per RAG state — so it stays public-safe in
this repo. Maps directly onto `executive-slide-shape.md`'s structure: one
style rule per element that shape defines.

## Style rules

| Element | Rule |
|---|---|
| Title/agenda slide (portfolio scope) or lightweight title slide (single-initiative scope) | 28pt title, bold, one neutral accent color (see below); subtitle line naming the period, 14pt, italic, neutral gray (`#595959`). |
| Initiative title (`## <Initiative Name>`) | 24pt, bold, same accent color as the title slide, top of its slide. |
| Status line | 14pt, bold, prefixed with a RAG color chip — see RAG colors below — followed by the one-line why in regular weight. |
| Headline | 16pt, italic, directly under the status line, one sentence. |
| Section headings (`Key accomplishments`, `Risks / Blockers`, `Upcoming milestones`, `Ask`) | 14pt, bold, same accent color as the title, 8pt space-before / 4pt space-after. |
| Body bullets | 12pt, a single legible sans-serif body font (e.g., Calibri, Arial — pick one, don't mix), one level deep — this shape doesn't nest bullets; a nested bullet signals content that should have been split into its own initiative slide. |
| Accent color | Exactly one, used only for titles and section headings — a neutral slate blue (`#2C5282`) as the placeholder value. This is the one value an operator should swap first when house branding is sourced. |
| RAG colors | Red `#B91C1C`, Amber `#B45309`, Green `#15803D` — used only for the status chip, never as a slide background or heading color; this keeps the status signal legible without turning the deck into a traffic light. |
| Margins / layout | Standard 16:9 widescreen, 0.5 inch content margins, no footers beyond an optional slide number, bottom right. |

## Missing-house-template note (required)

Whenever this default is used instead of a sourced house template, the
stylizer adds a single text box at the bottom of the title/agenda slide (or
the lightweight title slide, for single-initiative scope): *"No house
template configured for this instance — formatted with the
executive-slide-digest minimal default."* This is not optional polish; it's
the traceability the skill's spec requires (Review criterion 3) so a
reader — and Stage 6's reviewer — knows this is a placeholder format, not
the org's intended final look.

## When a house template is sourced

Replace the accent color, RAG chip colors (if house branding defines its
own status-color convention), title/heading fonts, and margins with the
sourced template's values; keep the missing-template-note *mechanism* (the
flag format) available for any future instance that hasn't sourced a
template yet — that is a structural requirement of the flow, not an
artifact of this being the fallback.
