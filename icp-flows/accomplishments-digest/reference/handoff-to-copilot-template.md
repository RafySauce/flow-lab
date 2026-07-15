---
id: accomplishments-digest-handoff-template
title: "Handoff Template — Accomplishments Digest to Docx Finisher"
type: template
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-07-08
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related: ["[[accomplishments-digest]]", "[[accomplishments-docx-finisher]]"]
---

# Handoff Template — Accomplishments Digest → Docx Finisher

The flow-specific instantiation of the generic handoff shape in
`methodology/mirroring-protocol.md` §5, filled with the fields Stage 6
(Handoff to Copilot) needs to populate and Stage 1 of
`accomplishments-docx-finisher` needs to receive. File a completed copy per
run at `handoffs/YYYY-MM-DD-accomplishments-digest-to-docx-finisher.md`.

```markdown
---
id: accomplishments-digest-handoff-<date>
type: clipping
truth-level: claimed
source: human+ai
owner: <engineer driving the flow>
data-class: internal
---

# Handoff: accomplishments-digest → accomplishments-docx-finisher

**From:** Rovo, Confluence (accomplishments-digest, Stage 5 complete)
**To:** Copilot, <repo/workspace> (accomplishments-docx-finisher, Stage 1)

## State

- Stage 5 (Align & Publish) complete: <date>. Published document:
  <Confluence page URL> / <mirror path>.
- Review period: <start date> – <end date>. Audience: <stated audience>.
- Document status: human-approved, published — this is not a draft.

## Inputs for the receiving stage

- **Published document content/link:** <URL or attached content>
- **Exclusion list (carried forward from Stage 1 of the source flow):**
  <items that must never appear, including in any enrichment>
- **Repo/file-access scope authorized for enrichment:** <e.g. "may reference
  PRs and commits in repo X for the stated period; may not pull from other
  repos or private channels">
- **Style/template preference (if known):** <house Word template name, or
  "engineer's choice at Stage 2">

## Open questions / operator decisions pending

- Enrichment is presentation and supporting-evidence only — the receiving
  flowspace's Stage 1 must not add new accomplishments or claims beyond what
  this published document already states. This is a hard constraint, not a
  default the receiving engine may relax.
- <any other unresolved items specific to this run>
```

## Rules (inherited from mirroring-protocol §5, restated for this pair)

- The handoff names its human owner — never anonymous or agent-owned.
- The receiving flowspace's Stage 1 `CONTEXT.md` is the contract; this
  handoff carries state and scope, never instructions that override it.
- A handoff whose authorized enrichment scope is left blank should be
  treated as **no repo/file access authorized** — the receiving flowspace
  must ask before assuming a broader scope, not infer one from the document
  content.
