---
id: dp-delivery-manager-cowork-build
title: "Delivery Manager Cowork Project — Launch Prompt"
aliases:
  - "delivery manager build prompt"
  - "delivery manager launch prompt"
  - "UC1 designed prompt"
type: designed-prompt
artifact-version: "1.1"
created: 2026-05-23
updated: 2026-05-25
status: living
truth-level: draft
domain: ai
phase: "Phase 5 — Knowledge Architecture & AI Integration"
systems:
  - hermes
  - litellm
  - obsidian
tags:
  - designed-prompt
  - ai/hermes
  - ai/agentic-harness
created-by: "Cincinnatus & Claude Opus 4.7"
generated-by: ecosystemic-thinking-partner
skill-version: "0.3"
source: human+ai
related:
  - "[[dna-spec]]"
  - "[[mission-log-2026-05-23-cowork-project-harness-design]]"
---

# Delivery Manager Cowork Project — Launch Prompt

Paste this into a fresh Cowork chat pointed at the new `delivery-manager/` project folder. It carries everything decided in the harness-design session so the build chat starts from settled ground, not a blank page.

> **Schema currency note (patched 2026-05-25).** This prompt was authored 2026-05-23 and patched two days later for DNA schema drift: `cssclasses` was removed from the DNA spec entirely on 2026-05-24 (gone, not reserved), and `torres-rna` now supersedes the deprecated `torres-spore-migration` skill for all connection-wiring. Both are corrected below. When stamping DNA frontmatter, always read the live `dna-spec.md` at build time — it wins over any frontmatter example in this prompt.

---

## Prime

You are helping Cincinnatus build out a Cowork project called **Delivery Manager**. Its job is to keep his many concurrent initiatives — the Torres-Core homelab, the Hermes agent projects, and whatever else he builds or dreams up — in one coherent, trackable place. He has a lot of chats and a lot of ongoing thoughts, and they currently live nowhere durable.

This project is special: it is an **instrumented Hermes prototype**. It is the early, folder-form version of the Homelab Manager agent from the Torres-Core AI Council architecture. Everything built here is designed to eventually port to the self-hosted Hermes stack. So the project does double duty — it is useful *now* as a delivery cockpit, and it is *instrumented* so its own usage becomes design intelligence for the eventual agent.

Read the project's `CLAUDE.md` first on every task. It is the map.

## Architecture this project is built on

Van Clief three-layer routing (map -> rooms -> tools), which is mechanically identical to Hermes agent containment: a `CLAUDE.md` map that routes, per-workspace `CONTEXT.md` files that scope what gets loaded (an agent's mode-specific memory), and skills that plug in per room. When this ports to Hermes, the workspaces become the agent's operating modes almost without translation.

On top of the three layers, this project carries a **sealed-laboratory pipeline** that the self-contained projects do not: work products accumulate, signal-bearing ones get promoted to stamped usage traces, and scheduled tasks read the traces and corpus to write synthesis findings. The findings are the product — carried by Cincinnatus across the wall into a Hermes agent spec, an inference-gateway routing rule, or an MCP-skill collection.

## Folder skeleton to build

```
delivery-manager/
├── CLAUDE.md                  # the map + routing table + naming conventions
├── intake/                    # chats, raw thoughts, unsorted captures land here
│   └── CONTEXT.md
├── projects/                  # one room per active initiative
│   ├── CONTEXT.md             # how a project room works; the room template
│   ├── homelab/               # predefined
│   │   └── CONTEXT.md
│   └── hermes/                # predefined
│       └── CONTEXT.md
├── review/                    # status board, next actions — the cockpit surface
│   ├── CONTEXT.md
│   └── board.md               # the canonical markdown Kanban (source of truth)
├── corpus/                    # work products produced while using the project
│   └── CONTEXT.md
├── traces/                    # promoted, signal-bearing usage traces
│   └── CONTEXT.md
├── synthesis/                 # scheduled-task output — design intelligence
│   └── CONTEXT.md
├── tasks/                     # scheduled-task definitions
│   └── CONTEXT.md
└── harness/                   # emergent Hermes design material
    └── CONTEXT.md
```

## Room creation — hybrid model

Predefine only the two obvious project rooms (`homelab`, `hermes`). Everything else lands in `intake/` unsorted. The heavyweight scheduled task **proposes** new project rooms when it sees a cluster of related intake items — it does not mint them silently. Cincinnatus approves a proposed room, and only then does it get a folder and a `CONTEXT.md`. Do not pre-build rooms for initiatives that have not yet earned one.

## The cockpit surface — folder-native now, Planka later

The canonical source of truth for status is `review/board.md` — a markdown Kanban (columns: Backlog, Active, Blocked, Done; cards reference project rooms and carry next-action lines). This stays canonical permanently.

The eventual visual surface is **Planka** (self-hosted, Trello-style, visual-first), wired via MCP once Cincinnatus stands up his own instance. Planka is a presentation skin that markdown is pushed into and status read back from — it is never the system of record. This matters: Planka's API is thin, but because `board.md` is canonical, the thin API never bites. Do not wire any commercial cloud PM connector — it would recreate the Google-entanglement problem the lab exists to escape.

## The usage-trace apparatus

**Work products** accumulate in `corpus/` with standard DNA v1.1 frontmatter as they are produced.

**Usage traces** live in `traces/`. When an interaction is signal-bearing, Cincinnatus flags it and you promote it to a trace. A trace carries DNA v1.1 standard fields plus one project-local field:

```yaml
capability: summarize | synthesize | retrieve | decide | draft | monitor
```

`capability` is a seeded enum — refine the value list as real usage reveals gaps. The trace body is freeform prose: what was asked, what came back, what would have made it better. Note: there is deliberately **no usefulness field**. Cincinnatus holds usefulness himself during this proving-out phase; formal usefulness-scoring is a Hermes-side problem to design after migration. Do not add a usefulness field.

`usage-trace` is a **project-local candidate type** — it is not yet in the DNA spec. (As of the 2026-05-25 patch, DNA v1.1 added `designed-prompt` and `template` as first-class types but did **not** absorb `usage-trace` — so the fallback stamping below still holds.) Log it as an open thread for future promotion (the way `claimed` earned its way into the truth-level enum). Stamp traces with `type: specification` plus a `tags: [usage-trace]` marker for now, or whatever the DNA spec says at build time if it has since absorbed the type.

**Synthesis findings** live in `synthesis/`, written by the scheduled tasks. They reuse an existing DNA type (`brainstorm-recap` or `specification`) with `source: ai` — the first artifacts in the system with no human in the loop. A synthesis finding clusters traces by `capability`, reports which capabilities fire most and which life-domains generate the most signal, and *proposes* a migration-target (`agent` / `gateway` / `mcp-skill`) for each cluster. The migration-target is the synthesis task's conclusion to assert — never stamped on the trace at capture time.

> Migration-target vocabulary maps onto the real substrate: `agent` -> a Hermes agent spec, `gateway` -> a LiteLLM inference-routing rule, `mcp-skill` -> an MCP-gateway tool manifest. See `mcp-gateway-design-document.md` and the AI Council roadmap for the destinations.

## Scheduled tasks — two tiers

Mirror the two-tier memory pattern from the AI Council architecture:

1. **Lightweight tally** (frequent) — reads what is accumulating in `intake/`, `corpus/`, and `traces/`; surfaces a short count and flags clusters that might warrant a new project room. Writes nothing durable; just keeps Cincinnatus oriented.
2. **Heavyweight synthesis** (less frequent) — reads traces + corpus, writes one synthesis finding to `synthesis/`, proposes new project rooms, and proposes migration-targets per capability cluster.

Build both as task definitions in `tasks/` with clear trigger cadence. Start time-based; revisit threshold-based if quiet periods produce empty syntheses.

## Skills to wire per room

- `intake/`, `projects/`, `review/` -> the delivery-management working skills (capture, route, status). Wire `ecosystemic-thinking-partner` into `projects/` for genuine think-through work.
- `synthesis/`, `tasks/` -> the analysis skills the scheduled tasks use.
- All DNA-stamped artifacts defer to the `torres-rna` tooling for connection-wiring; this project's authoring emits `## Connection Notes`, never formal `## Connections`. (`torres-rna` supersedes the deprecated `torres-spore-migration` skill.)

## What to do first in the build chat

1. Confirm the folder skeleton with Cincinnatus, adjust names if anything feels off in practice.
2. Write `CLAUDE.md` — the map, the routing table (task -> room -> read -> skills), and naming conventions.
3. Write the eight `CONTEXT.md` files, each short (under a page): what the room is for, its process, what lives there, what good work looks like.
4. Seed `review/board.md` with the current real state of homelab + hermes work (pull from intake of his actual ongoing threads). A first-pass seed is provided alongside this prompt — verify every card against real state before trusting it.
5. Draft the two scheduled-task definitions in `tasks/`.
6. Start using it. Adjust CONTEXT.md files based on what works.

The context files are living documents. Treat them as working notes, not finished specs.

## Open question to resolve in the build chat

- Should the lightweight tally task also write a dated one-line log so trends in *what Cincinnatus is capturing* are themselves visible over time — or does that pollute the signal? (Lean: a single rolling `review/pulse.md`, appended not proliferated.)

---

## Connection Notes

*Un-verified hints for the vault-side connection skill (torres-rna) to action once filed.*

- Worth linking to: the DNA Spec (`dna-spec.md`) — all frontmatter is stamped against it
- Worth linking to: the Torres-Core AI Council roadmap — this is the Homelab Manager agent, prototyped early
- Worth linking to: the harness-design mission log (this session) — the reasoning behind this prompt
- Worth linking to: the LiteLLM inference gateway design and the HermesAgent framework notes — the migration targets
- Worth linking to: `mcp-gateway-design-document.md` — defines the `mcp-skill` migration target
- Entities likely in play: hermes, litellm, obsidian, planka (new, no entity-doc yet)
