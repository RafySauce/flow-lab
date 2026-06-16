# projects/homelab-infra/ — Context

## What this project is

The foundational substrate layer. Torres-Core runs on Proxmox across three nodes (proxmox-n3, proxmox-mf, proxmox-cortana) with a UniFi network stack. Homelab Infrastructure is everything the other lanes depend on: compute, networking, DNS, storage architecture, and the VM/CT skeleton. Nothing in Agentic or Service Ops runs without this layer being solid.

## Current state

Core substrate is live: DNS spine (AdGuard active/active + Unbound dual), Health-check v3 across hosts. The UDR7 is live — DoH-direct test in AdGuard is the pending follow-up. proxmox-cortana conversion is blocked on Frigate landing first (surveillance storage dependency). VLAN hardening is designed but deferred until service layer stabilises. See `review/board.md` (HOMELAB INFRASTRUCTURE lane) for the authoritative card picture.

## What this lane owns

- Proxmox node management (proxmox-n3, proxmox-mf, proxmox-cortana)
- Network stack: UniFi UDR7, switches, VLAN architecture
- DNS spine: AdGuard + Unbound
- Storage architecture: pools, NFS shares, drive topology
- VM/CT skeleton and provisioning templates
- Health-check framework

## What does NOT live here

Services that run on top of the substrate (Frigate, Immich, Vaultwarden, etc.) belong in Service Ops. AI inference and agent runtime belong in Agentic. This lane is the ground; the other lanes are what grows on it.

## Process

1. Sessions start from the board. Check the HOMELAB INFRASTRUCTURE card for the active next action.
2. Network and DNS changes get a dedicated session — not mixed with service deployments.
3. Preflight before passthrough/conversion work (VM299 throwaway for GPU passthrough preflight before Immich VM206).
4. Sensitive credential and drive topology details go to local models.

## What gets promoted

- Runbooks and configuration guides → `corpus/`
- Signal-bearing decisions → `traces/`
- Status changes → `review/board.md` (HOMELAB INFRASTRUCTURE lane)

## Skills

- `homelab-architect` — design → deployment for infra changes
- `ecosystemic-thinking-partner` — for dependency and sequencing analysis
- `torres-rna` — stamping when artifacts go to corpus

## Open threads

- DNS: DoH-direct test in AdGuard pending (UDR7 now live)
- VLAN + EdgeSwitch: guide v2 written; deferred until services stabilise
- proxmox-cortana: conversion blocked on Frigate + physical drive verification
- GPU passthrough preflight: VM299 throwaway run not yet done (gates Immich)
