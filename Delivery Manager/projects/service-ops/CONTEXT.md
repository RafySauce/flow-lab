# projects/service-ops/ — Context

## What this project is

Service operations, lifecycle, and enhancements. This lane owns the running services on Torres-Core — their deployment, maintenance, upgrades, and feature growth. Services here depend on the substrate (Homelab Infrastructure) and increasingly on the AI stack (Agentic) as integrations mature. This is the most user-visible layer: it is what Cincinnatus and his household actually use day to day.

## Current state

Core services are live: Vaultwarden, SearXNG, Obsidian LiveSync, Karakeep. Active work is Frigate (three-part deploy written and ready). Immich and Paperless are written and blocked on physical prerequisites. Gitea, Fail2Ban, MkDocs, media stack revamp, and GrapheneOS are in backlog. See `review/board.md` (SERVICE OPERATIONS lane) for the authoritative card picture.

## What this lane owns

- Self-hosted service deployments and their running state
- Service upgrades, feature configuration, and integrations
- Client/endpoint work (GrapheneOS) that connects into services
- Services that will eventually gain AI integrations (Paperless-GPT, RAG-wired services)

## What does NOT live here

- The AI inference infrastructure itself (LiteLLM, MCP gateway, model serving) → Agentic
- Network and storage substrate → Homelab Infrastructure
- Agent-native features that belong to a Hermes agent spec → Agentic

## Privacy / sensitivity reminder

- Paperless receipt-reconciliation and any financial document workflow: take to local models. The board holds the card title; it never holds receipts or credentials.
- Anything touching credentials (Vaultwarden tokens, API keys): not here.

## Process

1. Sessions start from the board. Find the Active Service Ops card and its stated next action.
2. Design before deploy for non-trivial services (`homelab-architect` for a build design, then a corpus guide).
3. Physical prerequisites (printer, drive verification, GPU passthrough preflight) are named blockers — name them on the card; do not leave a card in Blocked without a named dependency.
4. Service enhancements that require AI integration (e.g. Paperless-GPT, RAG pipeline for Obsidian) are coordinated with the Agentic lane — neither lane owns the integration alone.

## What gets promoted

- Deployment guides and runbooks → `corpus/`
- Signal-bearing interactions → `traces/`
- Status changes → `review/board.md` (SERVICE OPERATIONS lane)

## Skills

- `homelab-architect` — for service design and deployment guide production
- `ecosystemic-thinking-partner` — for services with complex integration dependencies
- `torres-rna` — stamping when artifacts go to corpus

## Open threads

- Frigate: MQTT CT211 + NFS from datapool/surveillance + Frigate CT205 on proxmox-mf w/ RTX 4060 TensorRT — three-part deploy ready; awaiting execution session
- Immich: GPU-passthrough preflight (VM299) not yet run; gates Immich VM206 deploy
- Paperless-NGX + Paperless-GPT: blocked on printer replacement (Brother MFC-J1205W lacks scan-to-SMB)
- GrapheneOS: three-phase plan on Pixel designed; Aegis + DAVx5 + Vaultwarden stack ready
- Media stack revamp: Tautulli → Kometa → Tdarr → ErsatzTV → Dispatcharr; deferred post-Cortana
