# review/board.md

> **Verify before trusting.** Cards tagged `[verify]` are Claude's read from project knowledge, not confirmed ground truth. Drop the tag as you confirm each card against reality.

*Column semantics: Backlog (not started) · Active (in motion now) · Blocked (waiting on a named dependency) · Done (steady state, no next action). A Blocked card must name its dependency.*

---

## DELIVERY MANAGER

### Active
- **Harness build** — folder skeleton, CLAUDE.md, CONTEXT files, 4-lane board, task definitions complete. -> next: verify board cards; run first real capture end-to-end; promote one trace; register scheduled tasks.

### Backlog
- **Scheduled tasks** — tally (daily) and synthesis (weekly) definitions written; not yet registered via `schedule` skill.
- **Planka wiring** — self-hosted Trello-style surface; wire via MCP once instance is live. -> gated on: Planka instance deployed.
- **MCP-native board tools** — read/write board.md via MCP gateway. -> gated on: MCP gateway v1 live.

---

## HOMELAB INFRASTRUCTURE

### Done
- [verify] **DNS spine** — AdGuard active/active (.14 / .22), Unbound dual (.17 / .24). -> next: confirm DoH-direct test outcome.
- [verify] **Health-check v3** — symlinked across hosts; CoreGaming WSL baseline passing. -> next: nothing; steady state.

### Active
- [verify] **DNS session follow-up** — test DoH-direct in AdGuard now UDR7 is live; confirm full Unbound chain. -> next: schedule the dedicated DNS session.

### Blocked
- [verify] **proxmox-cortana conversion** — pending Frigate first (surveillance storage dependency). -> blocked on: Frigate live + physical drive verification in Cortana.

### Backlog
- [verify] **VLAN + network hardening** — guide v2 written; EdgeSwitch config remaining; rolled back Apr 26 attempt. -> dedicated session; build/test services first.
- [verify] **Dev workstation (VM109)** — provisioned. (NOTE: keep card generic; verify employer-code sanction before any detail lands here.)

---

## AGENTIC INFRASTRUCTURE & SERVICES

> Honesty marker: this lane is **designed, largely not built**. Cards reflect specs and roadmaps, not running services.

### Done
- [verify] **AI Council roadmap** — governing document exists.
- [verify] **MCP gateway design doc** — pre-session design captured.
- [verify] **DNA v1.1 schema** — verified and canonical (`dna-spec.md`).

### Active
- *(nothing active — substrate not yet deployed)*

### Blocked / Gated
- [verify] **HermesAgent framework (VM108)** — undeployed; replaces OpenClaw/CrewAI. -> gated on: substrate deploy session.
- [verify] **LiteLLM inference gateway** — designed, not deployed. -> gated on: substrate deploy session.
- [verify] **MCP gateway v1** — designed (folder-as-tool-library, Tailscale-only). -> gated on: substrate deploy session.
- [verify] **vLLM vs Ollama decision** — model serving runtime not yet decided. -> blocked on: dedicated decision session.
- [verify] **OpenWebUI maturity** — running at base; advanced features + RAG wiring pending. -> gated on: LiteLLM + RAG pipeline.
- [verify] **Crawl4AI** — deployment and integration design not started. -> gated on: substrate deploy session.
- [verify] **RAG pipeline** — Obsidian → pgvector → ChromaDB; design exists. -> gated on: substrate deploy session.

### Backlog
- [verify] **Life Flow Hermes (Phase A)** — morning briefing to Telegram; the first agent. -> gated on: substrate live.
- [verify] **Homelab Manager (Phase B)** — this Delivery Manager prototype graduates into it.
- [verify] **Council forum (Phase C)** — Topology C; agents deliberate in shared Telegram group.
- [verify] **Analyst + Prepper (Phase D)** — World Monitor ensemble feeds Analyst.
- [verify] **Meta-agent class** — Anthropologist / Biologist / (third TBD); deferred.
- [verify] **Weekly digest script** — ~200-line Python; seed corpus for meta-agents.

---

## SERVICE OPERATIONS

### Done
- [verify] **Vaultwarden (CT109, .15)** — deployed; LastPass migration complete. -> next: nothing; steady state.
- [verify] **SearXNG (CT110, .40)** — deployed; wired as Open WebUI + Hermes search backend. -> next: nothing; steady state.
- [verify] **Obsidian LiveSync (VM105)** — knowledge spine live; replaced Affine. -> next: nothing; steady state.
- [verify] **Karakeep (VM105)** — bookmark/reading staging live. -> next: nothing; steady state.

### Active
- [verify] **Frigate stack** — three-part deploy written and ready (MQTT CT211, NFS from datapool/surveillance, Frigate CT205 on proxmox-mf w/ RTX 4060 TensorRT). -> next: start with 2-3 RTSP-native cameras; Neolink/E1 deferred.

### Blocked
- [verify] **Immich** — guides written (vfio-preflight + deployment, VM206 on proxmox-mf). -> blocked on: GPU-passthrough preflight via throwaway VM299 not yet run.
- [verify] **Paperless-NGX + Paperless-GPT** — guide written for VM105; four downstream workflows scoped. -> blocked on: Brother MFC-J1205W lacks scan-to-SMB; printer replacement deferred. (NOTE: receipt-reconciliation = financial data → local models.)

### Backlog
- [verify] **Gitea** — LXC via community helper script (not Docker).
- [verify] **Fail2Ban** — guide written; proxmox-n3 + VM104 first targets.
- [verify] **MkDocs/Material → docs.torres-core.us** via Cloudflare Pages.
- [verify] **Media stack revamp (post-Cortana)** — Tautulli → Kometa → Tdarr → ErsatzTV → Dispatcharr; HDHomeRun capstone.
- [verify] **GrapheneOS migration** — three-phase plan on Pixel; Aegis + DAVx5 + Vaultwarden stack designed.

---

## INTAKE (unsorted — route or promote)

*Empty. New raw captures land here before they earn a lane card or room.*
