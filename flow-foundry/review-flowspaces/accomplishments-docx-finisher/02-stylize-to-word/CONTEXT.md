# Stage 2 — Stylize to Word (`CONTEXT.md`)

## Inputs

Stage 1's enriched content set (`work/01-enriched-content.md`), including its
flagged-additions list, and the handoff's stated style/template preference
(if any).

## Process

Apply the house Word template/branding — headings, theme structure, and
typography consistent with the `accomplishments-document-shape.md` structure
the source flow already used, so the Word version reads as the same document
in a different format, not a re-authored one. If no house template exists yet
at the target instance, apply the concrete fallback defined in
`../reference/docx-minimal-default-style.md` (heading sizes, one neutral
accent color, body type, margins) and flag the missing house template as a
note rather than inventing house branding on the fly. Preserve Stage 1's
flagged-additions markers through to the styled output in a form Stage 3 can
still identify (e.g. a distinct character style or a trailing "Enrichment
notes" appendix) — styling must not erase the traceability Stage 1 built.
`Layer-3: skill built, staged in
skill-foundry/review-skills/accomplishments-docx-stylizer/ —
sp-accomplishments-docx-stylizer` awaiting operator promotion.

## Outputs

A **draft `.docx` file**: the enriched content in house-styled Word format,
with Stage 1's additions still identifiable. Lands as `work/02-draft.docx`.

## Verify

A specific cross-stage trace check: every theme/section present in Stage 1's
enriched content set appears in the styled `.docx` — no section silently
dropped during template application, and no content introduced that wasn't
in Stage 1's output. Result recorded as a one-line entry in the run's
decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `light` — mechanical template application against defined
  source content; no new judgment about what the document says.
- **Evidence:** the draft `.docx` is handed to the engineer for Stage 3's
  review; no separate sign-off at this boundary.

## Data boundary

- **Max data-class this stage handles:** `internal` (inherits Stage 1's
  classification; pure formatting, no new content sourced).
- **Sanctioned engines for this stage:** Copilot, consistent with Stage 1 —
  no engine change mid-flow.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
