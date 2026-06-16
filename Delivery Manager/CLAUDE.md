# Delivery Manager — The Map

**Read this first on every task.** This file is the routing table. It tells you where things go, what to load, and which skills to reach for. The project's rooms do the actual work — this file tells you which room you're in.

---

## What this project is

A delivery cockpit for Cincinnatus's concurrent initiatives: Torres-Core homelab, the Hermes agent projects, and whatever else emerges. It is also an instrumented Hermes prototype — usage here is design intelligence for the eventual self-hosted Homelab Manager agent. Everything built in this project is designed to eventually port to the Hermes stack.

---

## Routing table

| Task type | Room | Read first | Skills |
|---|---|---|---|
| New capture / raw thought / unsorted idea | `intake/` | `intake/CONTEXT.md` | — |
| Delivery Manager / harness improvement | `projects/delivery-manager/` | `projects/CONTEXT.md` + `projects/delivery-manager/CONTEXT.md` | `ecosystemic-thinking-partner`; `schedule` for task cadence |
| Homelab infrastructure work | `projects/homelab-infra/` | `projects/CONTEXT.md` + `projects/homelab-infra/CONTEXT.md` | `homelab-architect` for design → deployment; `ecosystemic-thinking-partner` for dependencies |
| Agentic infrastructure & services (AI stack, agents) | `projects/agentic/` | `projects/CONTEXT.md` + `projects/agentic/CONTEXT.md` | `ecosystemic-thinking-partner`; `mcp-builder` for MCP manifests; `homelab-architect` for deploy sessions |
| Service operations, lifecycle & enhancements | `projects/service-ops/` | `projects/CONTEXT.md` + `projects/service-ops/CONTEXT.md` | `homelab-architect` for service deploy; `ecosystemic-thinking-partner` for complex integrations |
| New project room (not yet minted) | `intake/` first; room created only after heavyweight task proposes it and Cincinnatus approves | — | — |
| Status check / next actions / board update | `review/` | `review/CONTEXT.md` + `review/board.md` | — |
| Storing a work product | `corpus/` | `corpus/CONTEXT.md` | `torres-rna` for connection-wiring |
| Promoting an interaction to a trace | `traces/` | `traces/CONTEXT.md` | `torres-rna` for connection-wiring |
| Reading synthesis output | `synthesis/` | `synthesis/CONTEXT.md` | — |
| Scheduled task definitions / cadence changes | `tasks/` | `tasks/CONTEXT.md` | `schedule` |
| Hermes design / architecture material | `harness/` | `harness/CONTEXT.md` | `ecosystemic-thinking-partner` |

---

## Naming conventions

### Document IDs
Format: `[type-prefix]-[YYYY-MM-DD]-[short-kebab-description]`

Type prefixes:
- `trace-` — usage traces in `traces/`
- `synthesis-` — synthesis findings in `synthesis/`
- `corpus-` — work products in `corpus/`
- `dp-` — designed prompts
- `ml-` — mission logs
- `runbook-` — runbooks

Example: `trace-2026-05-25-synthesize-frigate-stack`

### Trace naming
`trace-YYYY-MM-DD-[capability]-[short-description].md`
Capability enum: `summarize | synthesize | retrieve | decide | draft | monitor`
Example: `trace-2026-05-25-decide-dns-session-followup.md`

### Synthesis finding naming
`synthesis-YYYY-MM-DD-[topic-cluster].md`
Example: `synthesis-2026-06-01-homelab-deploy-capability-cluster.md`

### Corpus work product naming
`corpus-YYYY-MM-DD-[short-description].md`
Example: `corpus-2026-05-25-frigate-deployment-guide.md`

---

## Room creation policy

Only `homelab/` and `hermes/` are pre-built. Everything else lands in `intake/` unsorted. The heavyweight scheduled task **proposes** new rooms when it sees a cluster — it never mints them. Cincinnatus approves, then the room gets a folder and a `CONTEXT.md`. Do not pre-build rooms for initiatives that have not yet earned one.

---

## DNA frontmatter

All DNA-stamped artifacts use DNA v1.1 schema. Always read the live `dna-spec.md` at stamp time — it wins over any frontmatter example in this project. Connection-wiring is done by `torres-rna`; this project's authoring emits `## Connection Notes`, never formal `## Connections`.

`usage-trace` is a project-local candidate type (not yet in the DNA spec). Until absorbed: stamp traces with `type: specification` + `tags: [usage-trace]`. No usefulness field — ever. Usefulness is held by Cincinnatus during the proving-out phase.

---

## Privacy / sensitivity boundaries

- Cards referencing Steven's VM109 dev work or partner onboarding/access: keep card titles generic on the board; take substance to local models.
- Paperless receipt-reconciliation thread and anything carrying credentials: board can hold a card title; never hold the receipts or secrets here.
- Synthesis findings that would move sensitive data toward a cloud API: flag before approving any proposed room or migration-target.

---

## The pipeline in one sentence

Captures land in `intake/` → signal-bearing ones get promoted to stamped traces in `traces/` → scheduled tasks read traces + corpus and write synthesis findings to `synthesis/` → findings are carried by Cincinnatus into the Hermes agent spec, LiteLLM routing rules, or MCP skill manifests.
