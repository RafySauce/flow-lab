---
id: delivery-manager-board-seed
title: "Delivery Manager — board.md First-Pass Seed"
aliases:
  - "board seed"
type: specification
artifact-version: "1.0"
created: 2026-05-25
updated: 2026-05-25
status: living
truth-level: draft
domain: ai
phase: "Phase 5 — Knowledge Architecture & AI Integration"
systems:
  - hermes
tags:
  - specification
  - ai/agentic-harness
created-by: "Cincinnatus & Claude Opus 4.7"
source: human+ai
related:
  - "[[dp-delivery-manager-cowork-build]]"
  - "[[delivery-manager-build-checklist]]"
---

# review/board.md — First-Pass Seed

> **Read this before trusting it.** Every card below is Claude's read of your state from project knowledge, not ground truth. Project knowledge reflects *drafted/intended* state — a written deployment guide does not mean a service is live. Verify each card against reality before this becomes canonical. Once verified, this content moves into `review/board.md` and this seed doc can be retired.
>
> Cards are tagged `[verify]` until you confirm them. Drop the tag as you confirm each one.

---

## HOMELAB

### Done
- [verify] **Vaultwarden (CT109, .15)** — deployed; LastPass migration complete. -> next: nothing; steady state.
- [verify] **SearXNG (CT110, .40)** — deployed; wired as Open WebUI + Hermes search backend. -> next: nothing; steady state.
- [verify] **Obsidian LiveSync (VM105)** — knowledge spine live; replaced Affine. -> next: nothing; steady state.
- [verify] **Karakeep (VM105)** — bookmark/reading staging live. -> next: nothing; steady state.
- [verify] **Health-check v3** — symlinked across hosts; CoreGaming WSL baseline passing. -> next: nothing; steady state.
- [verify] **DNS spine** — AdGuard active/active (.14 / .22), Unbound dual (.17 / .24). -> next: confirm DoH-direct test outcome.

### Active
- [verify] **Frigate stack** — three-part deploy written and ready (MQTT CT211, NFS from datapool/surveillance, Frigate CT205 on proxmox-mf w/ RTX 4060 TensorRT). -> next: start with 2-3 RTSP-native cameras; Neolink/E1 deferred.
- [verify] **DNS session follow-up** — test DoH-direct in AdGuard now UDR7 is live; confirm full Unbound chain. -> next: schedule the dedicated DNS session.

### Blocked
- [verify] **Immich** — guides written (vfio-preflight + deployment, VM206 on proxmox-mf). -> blocked on: GPU-passthrough preflight via throwaway VM299 not yet run.
- [verify] **Paperless-NGX + Paperless-GPT** — guide written for VM105; four downstream workflows scoped. -> blocked on: Brother MFC-J1205W lacks scan-to-SMB; printer replacement deferred. (NOTE: receipt-reconciliation workflow = financial data -> local models.)
- [verify] **proxmox-cortana conversion** — pending Frigate first (surveillance storage dependency). -> blocked on: Frigate live + physical drive verification in Cortana.

### Backlog
- [verify] **Gitea** — LXC via community helper script (not Docker).
- [verify] **VLAN + network hardening** — guide v2 written; EdgeSwitch config remaining; rolled back the Apr 26 attempt. -> dedicated session; build/test services first.
- [verify] **Fail2Ban** — guide written; proxmox-n3 + VM104 first targets.
- [verify] **RAG pipeline** — embed Obsidian into pgvector; wire Open WebUI + ChromaDB; pilot Life Flow context.
- [verify] **MkDocs/Material -> docs.torres-core.us** via Cloudflare Pages.
- [verify] **Media stack revamp (post-Cortana)** — Tautulli -> Kometa -> Tdarr -> ErsatzTV -> Dispatcharr; HDHomeRun capstone.
- [verify] **GrapheneOS migration** — three-phase plan on Pixel; Aegis + DAVx5 + Vaultwarden stack designed.
- [verify] **Dev workstation (VM109)** — provisioned. (NOTE: coworker collaboration context -> keep generic here; verify employer-code sanction.)

---

## HERMES / AI COUNCIL

> Honesty marker: this whole column is **designed, largely not built**. Most cards are specs and roadmaps, not running services. The board should make that obvious so it never implies more exists than does.

### Done
- [verify] **AI Council roadmap** — governing document exists (`torres-core-ai-council-roadmap.md`).
- [verify] **MCP gateway design doc** — pre-session design captured.
- [verify] **DNA v1.1 schema** — verified and canonical (`dna-spec.md`).
- [verify] **This project (Delivery Manager)** — the instrumented Homelab Manager prototype, in build now.

### Active
- [verify] **Delivery Manager harness build** — folder skeleton + CONTEXT files + board + scheduled tasks. -> next: work the build checklist.

### Blocked / Gated
- [verify] **HermesAgent framework deploy (VM108)** — undeployed; replaces OpenClaw/CrewAI. -> gated on: substrate readiness.
- [verify] **LiteLLM inference gateway** — designed, not deployed. -> gated on: deploy session.
- [verify] **MCP gateway v1** — designed (folder-as-tool-library, Tailscale-only). -> gated on: build session.

### Backlog
- [verify] **Life Flow Hermes (Phase A)** — morning briefing to Telegram; the first agent. -> gated on: substrate.
- [verify] **Homelab Manager (Phase B)** — this prototype graduates into it.
- [verify] **Council forum (Phase C)** — Topology C; agents deliberate in shared Telegram group.
- [verify] **Analyst + Prepper (Phase D)** — World Monitor ensemble feeds Analyst.
- [verify] **Meta-agent class** — Anthropologist / Biologist / (third TBD); deferred to its own design space.
- [verify] **Weekly digest script** — ~200-line Python; seed corpus for meta-agents.

---

## INTAKE (unsorted — route or promote)

*Empty at seed time. New raw captures land here before they earn a room or a board card.*

---

*Column semantics: Backlog (not started) · Active (in motion now) · Blocked (waiting on a named dependency) · Done (steady state, no next action). A card in Blocked must name what it is blocked on.*
