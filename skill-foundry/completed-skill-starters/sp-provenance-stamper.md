---
id: sp-provenance-stamper
title: "Skill Primer Brief — Provenance Stamper"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-02
updated: 2026-07-07
owner: operator
source: human+ai
data-class: public
related: ["[[provenance-spec]]"]
---

# Skill Primer Brief — Provenance Stamper

## Purpose

Stamp and validate provenance frontmatter per `methodology/provenance-spec.md`: fill a compliant block for a new artifact (inferring what's inferable, asking for what isn't), and check existing artifacts against the schema including the conditional rules.

## Triggering intent

- **Fires on:** "stamp this," "is this schema-compliant," creating any new ICP artifact, and as a batch check across a folder or page tree.
- **Does not fire on:** promoting `truth-level` (validation says *invalid*, never *verified* — rule 5 makes promotion evidence-bound and human), or editing document content beyond the frontmatter/properties block.

## Method sketch

1. New artifact: infer `id`/`title`/`type` from filename and body per the spec's patterns; require `owner` and `data-class` from the human — never guess data classification.
2. Existing artifact: validate fields, enums, and all six conditional rules; report violations with the rule number.
3. Confluence side: same logic against page properties/labels per the mirroring protocol's mapping.

## Inputs and data boundary

Reads/writes frontmatter only. Max data-class: internal (it reads documents to infer type). Engines: **both** — Copilot adapter (prompt file, ideal for the mirror and this public repo) and Rovo adapter (page-properties side).

## Demand source

Every foundry step stamps artifacts ("stamp and stage" in both specs); provenance rule-checking is exactly the mechanical-but-critical work that erodes first without tooling. The homelab edition had a dedicated schema skill for this; this is its work-edition descendant.

## Definition of done

Correctly stamps a fresh artifact of each type in the enum; catches all six conditional-rule violations in a seeded invalid set; refuses to set `truth-level: verified` even when asked directly.
