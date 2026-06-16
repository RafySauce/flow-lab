# corpus/ — Context

## What this room is for

The work product archive. Finished artifacts produced while using the Delivery Manager live here: deployment guides, runbooks, design docs, architect briefs, agent specs, MCP skill manifests, and any other output that earns a permanent home. Corpus items are stamped with DNA v1.1 frontmatter and are durable — they are not working notes or drafts.

## What lives here

- Deployment guides and runbooks (homelab services)
- Architect briefs and design decision records
- Agent specs and LiteLLM routing design docs (hermes work)
- MCP skill manifests
- Any other finished artifact produced during a Delivery Manager session

## What does NOT live here

- Drafts and working notes (stay in the project room until finished)
- Usage traces (→ `traces/`)
- Synthesis findings (→ `synthesis/`)
- Raw intake captures (→ `intake/`)

## Process

When a work product is ready for corpus:
1. Move or copy it to `corpus/`
2. Stamp it with DNA v1.1 frontmatter — read the live `dna-spec.md` before stamping; it wins over any example here
3. Write `## Connection Notes` at the bottom (not `## Connections` — `torres-rna` handles the formal wiring)
4. Run `torres-rna` to wire connections if filing into the Obsidian vault

## Naming

`corpus-YYYY-MM-DD-[short-description].md`
Example: `corpus-2026-05-25-frigate-three-part-deployment-guide.md`

For artifacts that already have a canonical DNA id (e.g. a runbook or mission log), keep the DNA id as the filename.

## Frontmatter essentials

Every corpus item needs at minimum:
```yaml
---
id: [kebab-case-id]
title: "[Human-readable title]"
type: [DNA type — read dna-spec.md]
artifact-version: "1.0"
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: [draft | living | final]
truth-level: [to-review | reviewed | verified]
domain: [homelab | ai | ...]
source: human | human+ai | ai
---
```

## What good work looks like

Corpus items are findable and self-describing. A cold-start reader can understand what an artifact is and why it exists from frontmatter + first paragraph alone. Connection Notes point toward related documents so `torres-rna` can wire them correctly.
