---
id: delivery-manager-build-checklist
title: "Delivery Manager — Build Chat Checklist"
aliases:
  - "delivery manager build steps"
type: runbook
artifact-version: "1.0"
created: 2026-05-25
updated: 2026-05-25
status: living
truth-level: to-review
domain: ai
phase: "Phase 5 — Knowledge Architecture & AI Integration"
systems:
  - hermes
  - obsidian
tags:
  - runbook
  - ai/agentic-harness
created-by: "Cincinnatus & Claude Opus 4.7"
source: human+ai
related:
  - "[[dp-delivery-manager-cowork-build]]"
---

# Delivery Manager — Build Chat Checklist

A trackable companion to the launch prompt. Work top to bottom in the first Cowork build chat. Each step has a done-condition so the chat (and you) can tell when it is actually complete versus merely attempted. This is operator scaffolding, not a spec — the launch prompt remains authoritative on intent.

## Pre-flight

- [ ] **Project folder exists.** A `delivery-manager/` Cowork project is created and the build chat is pointed at it.
- [ ] **Launch prompt pasted.** `delivery-manager-launch-prompt.md` is the first message in the build chat.
- [ ] **Live DNA spec on hand.** Confirm the build chat can read the current `dna-spec.md` — it wins over any frontmatter example in the prompt.

## Step 1 — Confirm the skeleton

- [ ] The ten-folder skeleton from the prompt is reviewed out loud before any file is written.
- [ ] Any name that feels wrong in practice is renamed *now*, before CONTEXT.md files reference it.
- **Done when:** Cincinnatus has explicitly signed off on the folder names.

## Step 2 — Write CLAUDE.md (the map)

- [ ] Routing table written: for each room, `task type -> room -> what to read -> which skills`.
- [ ] Naming conventions written (id format, trace naming, synthesis-finding naming).
- [ ] The "read CLAUDE.md first on every task" instruction is at the top.
- **Done when:** a cold-start chat could route a new capture to the right room using only CLAUDE.md.

## Step 3 — Write the eight CONTEXT.md files

One per room. Each under a page. Each answers: what is this room for, what is its process, what lives here, what does good work look like.

- [ ] `intake/CONTEXT.md`
- [ ] `projects/CONTEXT.md` (this one doubles as the room template for future rooms)
- [ ] `projects/homelab/CONTEXT.md`
- [ ] `projects/hermes/CONTEXT.md`
- [ ] `review/CONTEXT.md`
- [ ] `corpus/CONTEXT.md`
- [ ] `traces/CONTEXT.md` (encode the no-usefulness-field rule and the capability enum here)
- [ ] `synthesis/CONTEXT.md`
- [ ] `tasks/CONTEXT.md`
- [ ] `harness/CONTEXT.md`
- **Done when:** each room can be operated from its own CONTEXT.md without re-reading the launch prompt.

> That is ten files for eight named rooms — `projects/` carries both its own template CONTEXT and the two predefined sub-room CONTEXTs. Count them as one logical step.

## Step 4 — Seed review/board.md

- [ ] Drop in the provided first-pass seed (`board-seed.md`) as a starting point.
- [ ] **Verify every card against real state.** The seed is Claude's read from project knowledge, not ground truth. Correct statuses, kill stale cards, add anything missing.
- [ ] Confirm column semantics: Backlog / Active / Blocked / Done.
- **Done when:** the board reflects what is *actually* true today, in your judgment — not what a guide implies.

## Step 5 — Draft the two scheduled tasks

- [ ] `tasks/` has a **lightweight tally** definition (frequent; reads intake/corpus/traces; writes nothing durable; flags clusters).
- [ ] `tasks/` has a **heavyweight synthesis** definition (less frequent; reads traces+corpus; writes one synthesis finding; proposes rooms + migration-targets).
- [ ] Both start time-based with a stated cadence.
- **Decision point — resolve before finishing this step:** does the lightweight tally also append a dated one-line entry to a single rolling `review/pulse.md` (lean: yes, appended not proliferated), or does that pollute the signal? Pick one and write it into `tasks/CONTEXT.md`.
- **Done when:** both task definitions exist and the pulse.md question is answered in writing.

## Step 6 — Start using it

- [ ] Route one real capture end-to-end (intake -> room -> board card).
- [ ] Promote one real interaction to a trace, to exercise the apparatus once.
- [ ] Note anything that felt awkward; adjust the relevant CONTEXT.md.
- **Done when:** the system has processed real input at least once and you have made at least one CONTEXT.md edit from lived friction.

## Boundaries to hold (surface at these exact points)

These are not blockers — they are where to route detail to your local models rather than working it through in a cloud chat:

- **Step 4, homelab/hermes seeding:** the moment a card touches **Steven's VM109 dev work** or **your partner's onboarding/access**, that is named-individual context. Keep the card title generic on the board; take the substance local.
- **Step 6, first real captures:** the **Paperless receipt-reconciliation** thread and anything carrying credentials (Vaultwarden tokens, API keys) is financial / secret material. The board can hold a card that *says* "receipt reconciliation"; it should never hold the receipts.
- **General:** synthesis findings are `source: ai` with no human in the loop. They can cluster and propose, but a proposal that would move sensitive data toward a cloud API is exactly the kind of thing to catch before approving a room or a migration-target.

## Close-out

- [ ] `git add -A && git commit -m "Session notes: delivery-manager harness build" && git push` (per standing doc discipline).
- [ ] File this checklist and the launch prompt; let torres-rna wire `## Connections` from the Connection Notes.

---

## Connection Notes

- Derived from [[dp-delivery-manager-cowork-build]] (the launch prompt).
- Worth linking to: the harness-design mission log and the AI Council roadmap.
