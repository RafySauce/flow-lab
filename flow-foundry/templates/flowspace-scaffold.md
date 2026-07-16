# Flowspace Scaffold — the output shape

What the flow-foundry produces for one flowspace. This folder tree, as markdown with YAML frontmatter, *is* the instance form — an instantiated flowspace lives in the internal GitLab repository, the sole source of truth (`methodology/mirroring-protocol.md`).

```
<flowspace-slug>/
├── HUB.md                  # the flowspace card — the hub the stage folders hang off
├── 01-<stage-slug>/
│   ├── CONTEXT.md          # six-field stage contract (see stage-context-template.md)
│   └── work/               # Layer-4 working artifacts for runs (transient; may be gitignored)
├── 02-<stage-slug>/
│   └── CONTEXT.md
├── …
├── reference/              # Layer-3 material: stable rules, style guides, skill pointers
├── decision-log/           # this instance's logged calls, YYYY-MM-DD-<slug>.md
└── handoffs/               # Rovo⇄Copilot handoff records (mirroring-protocol §4)
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

## Stage Flow Diagram

Mermaid `flowchart LR`, one node per stage, colored by review intensity — see
`references/flow-diagram-guide.md` for syntax, palette, and the rendering
check (GitLab renders Mermaid natively).

```mermaid
flowchart LR
    S1["1. <Stage Name><br/>review: <intensity>"]:::heavy --> S2["2. <Stage Name><br/>review: <intensity>"]:::light

    classDef heavy fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef light fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef gap fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

## Stage table

| # | Stage | Review intensity | Max data-class | Sanctioned engines | Layer-3 |
|---|---|---|---|---|---|
| 1 | <name> | heavy | internal | Rovo | <skill-id> |
| 2 | <name> | light | internal | Copilot | inline |
| … | | | | | |

## Source of truth

- **Instance:** <internal GitLab repo / path> — the sole source of truth for this flowspace
- **External systems touched:** <the Confluence/Jira/ServiceNow (or other) targets this flow reads from or writes to, if any — with the stage(s) that touch them>

## Run procedure

One paragraph: how a run starts, how it moves stage to stage (human inspects at each
boundary — that's the method, not an inconvenience), and where a finished run's
outputs land.

## Known gaps

Skill-primer-briefs filed from this flowspace's Layer-3 triage, with ids and status.
```

Rules: the stage table matches the stage folders one-for-one (checked at validation gate 1); the Stage Flow Diagram matches the stage table one-for-one (same gate); `work/` contents are per-run and never block promotion; nothing in the scaffold self-declares `verified`.
