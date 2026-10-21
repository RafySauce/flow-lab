---
id: decision-2026-10-21-documentarian-split-engine-commit-packet
title: "Decision Log — Split-Engine Commit Packet (documentarian)"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-21
updated: 2026-10-21
owner: operator
source: human+ai
data-class: public
related:
  - "[[documentarian]]"
  - "[[documentarian-commit-packet]]"
  - "[[engine-handoff-contract]]"
  - "[[2026-10-21-engine-handoff-contract-and-published-copies]]"
---

# Decision Log — 2026-10-21 — Split-Engine Commit Packet

**What was decided:** a Copilot-driven run reaches the Rovo-only Stages
06–07 through a **commit packet** emitted at Stage 05's exit. **By whom:**
agent, on direct operator instruction. **What it affects:** new
`reference/commit-packet.md` (1.0); Stage 05 (step 6, output row, verify
item), Stage 06 (packet input row, packet-entry paragraph, output row,
verify item, data-boundary wording), and Stage 07 (input row, split-run
paragraph, verify item) `CONTEXT.md`, each 1.0 → 1.1; `HUB.md` (1.2 → 1.3,
topology, run procedure, Fourth gap, reference rows). All four move
`verified` → `to-review`. No skill content changed. Shared rationale:
`flow-foundry/decision-log/2026-10-21-engine-handoff-contract-and-published-copies.md`.

## Decisions and alternatives

1. **This fills a boundary the flow already declared.** Stage 06's data
   boundary already said a Copilot-driven run "hands off to Rovo at this
   boundary," citing a protocol section that never defined the shape. The
   packet is that shape.
2. **In a split run, Stages 04→05 loop across all lines first; one packet per
   job.** One packet per page would mean a paste per page. Stage 06 still
   previews and approves each page separately in Rovo — only the order of
   the loop changes. *Alternative considered:* one packet per page, keeping
   the direct-run loop order — rejected for the paste cost.
3. **At the waiver gate, the executor never drafts an open section.** A
   "fill" means the user supplies the text and the executor inserts it
   verbatim. Drafting returns the page to the producing session, where Stage
   04's open-section protocol governs.
4. **Meeting-job candidates do not ride the commit packet.** The producing
   engine packages them per `ai-refinement-handoff-contract.md` once the
   return slip brings back the committed meeting page URL. This keeps the
   flow's rule that it never creates Jira work items, and keeps candidates in
   the engine that will run ai-refinement on them.
5. **Stage 07 runs in the same Rovo session as Stage 06.** It needs Stage
   06's results and is Rovo-only; the packet carries the rest of its inputs,
   including the doc-registry index location.

## Open — operator decision needed

- **Stage 02 is Rovo-only.** Evidence Gathering's data boundary sanctions
  only Rovo. A run that starts in the Agent Builder agent cannot gather
  evidence under the current boundary, even though that agent has read-only
  Confluence and Jira access. Options: (a) widen Stage 02's sanctioned
  engines to include Copilot for read-only sweeps; (b) run Stage 02 in Rovo
  and hand the dossier into Stage 03 on the producing engine. Not decided
  here; no boundary was widened. Recorded as part of the HUB's Fourth gap.
