# projects/agentic/ — Context

## What this project is

The AI inference and agent stack. This lane owns everything from raw model serving up through agent frameworks, MCP tooling, and each individual agent. It sits on top of Homelab Infrastructure and provides the runtime that Service Ops and the Delivery Manager itself consume. The Torres-Core AI Council architecture governs the roadmap here.

## Current state

All designed, largely not deployed. Governing docs exist (AI Council roadmap, MCP gateway design doc, DNA v1.1 schema). The substrate services — HermesAgent (VM108), LiteLLM, MCP gateway v1 — are designed but none are live. OpenWebUI is running but at base maturity; Crawl4AI and vLLM/Ollama decisions are pending. The RAG pipeline (Obsidian → pgvector → ChromaDB) is designed. All agent phases (A–D) are gated on substrate. See `review/board.md` (AGENTIC INFRASTRUCTURE lane) for the card picture.

## What this lane owns

**Infrastructure tier**
- Model serving: vLLM vs Ollama decision, runtime deployment
- LiteLLM inference gateway (routing, cost management, model abstraction)
- OpenWebUI (current: base; target: advanced features, RAG wired)
- Crawl4AI (web crawling for agent context)
- RAG pipeline: Obsidian → pgvector, ChromaDB, embedding pipeline
- MCP gateway v1 (folder-as-tool-library, Tailscale-only)
- HermesAgent framework (VM108) — replaces OpenClaw/CrewAI

**Agent tier** (each agent is a subfolder here once active)
- `agentic/life-flow/` — Phase A: morning briefing to Telegram
- `agentic/homelab-manager/` — Phase B: this Delivery Manager prototype graduates here
- `agentic/council-forum/` — Phase C: Topology C, agents deliberate in shared Telegram group
- `agentic/analyst-prepper/` — Phase D: World Monitor ensemble feeds Analyst
- `agentic/meta-agents/` — Anthropologist / Biologist / (third TBD); deferred

Agent subfolders are created when a phase moves to Active. They do not exist until the substrate is live.

## Architecture phases (AI Council roadmap)

- **Phase A** — Life Flow: first live agent, gated on substrate
- **Phase B** — Homelab Manager: this prototype graduates into it
- **Phase C** — Council forum (Topology C)
- **Phase D** — Analyst + Prepper (World Monitor ensemble)
- **Meta-agent class** — deferred to its own design space

## Process

1. **Infrastructure before agents.** No agent subfolder is created until the substrate tier (LiteLLM, MCP gateway, HermesAgent) has a deploy session scheduled.
2. **Design before deploy.** Use `ecosystemic-thinking-partner` for architecture decisions; specs land in `corpus/` before terminal sessions begin.
3. **vLLM vs Ollama decision** needs a dedicated thinking session before any model serving work starts.
4. **Harness material goes to harness/.** Design insights from using the Delivery Manager that affect agent architecture belong in `harness/`, not here.

## What gets promoted

- Architecture decision records, design docs, agent specs, MCP skill manifests → `corpus/`
- Signal-bearing design decisions → `traces/`
- Status changes → `review/board.md` (AGENTIC INFRASTRUCTURE lane)

## Skills

- `ecosystemic-thinking-partner` — primary for design and architecture work
- `mcp-builder` — for MCP skill manifest work
- `homelab-architect` — for infrastructure deploy sessions (LiteLLM, MCP gateway, HermesAgent)
- `torres-rna` — stamping when artifacts go to corpus

## Open threads

- vLLM vs Ollama: decision session needed before model serving work begins
- Substrate deploy session: LiteLLM + MCP gateway v1 + HermesAgent (VM108) — all gated together
- OpenWebUI maturity: advanced features + RAG wiring; gated on RAG pipeline + LiteLLM
- Crawl4AI: deployment and integration design not yet started
- RAG pipeline: pgvector + ChromaDB + embedding pipeline; design exists, deploy pending
- Weekly digest script (~200 lines Python): seed corpus for meta-agents; not yet started
