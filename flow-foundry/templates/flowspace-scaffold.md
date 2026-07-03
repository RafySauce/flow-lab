# Flowspace Scaffold — the output shape

What the flow-foundry produces for one flowspace. Git-mirror form shown; the Confluence primary is the same tree as pages per `methodology/mirroring-protocol.md` §2.

```
<flowspace-slug>/
├── HUB.md                  # the flowspace card — Confluence parent page equivalent
├── 01-<stage-slug>/
│   ├── CONTEXT.md          # six-field stage contract (see stage-context-template.md)
│   └── work/               # Layer-4 working artifacts for runs (transient; may be gitignored)
├── 02-<stage-slug>/
│   └── CONTEXT.md
├── …
├── reference/              # Layer-3 material: stable rules, style guides, skill pointers
├── decision-log/           # this instance's logged calls, YYYY-MM-DD-<slug>.md
└── handoffs/               # Rovo⇄Copilot handoff records (mirroring-protocol §5)
```

## HUB.md skeleton

```markdown
---
id: <flowspace-slug>
title: "<Flowspace Name>"
type: flowspace
artifact-version: "1.0"
status: living
truth-level: to-review          # verified only via the three gates, human-promoted
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: <accountable human>
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.0"
data-class: <class of the most sensitive content the instance will hold>
related: []
---

# <Flowspace Name>

<Purpose paragraph — from the primer brief.>

## Stage table

| # | Stage | Review intensity | Max data-class | Sanctioned engines | Layer-3 |
|---|---|---|---|---|---|
| 1 | <name> | heavy | internal | Rovo | <skill-id> |
| 2 | <name> | light | internal | Copilot | inline |
| … | | | | | |

## Surfaces

- **Primary:** <Confluence space / parent page>
- **Mirror:** <internal repo / path>

## Run procedure

One paragraph: how a run starts, how it moves stage to stage (human inspects at each
boundary — that's the method, not an inconvenience), and where a finished run's
outputs land.

## Known gaps

Skill-primer-briefs filed from this flowspace's Layer-3 triage, with ids and status.
```

Rules: the stage table matches the stage folders one-for-one (checked at validation gate 1); `work/` contents are per-run and never block promotion; nothing in the scaffold self-declares `verified`.
