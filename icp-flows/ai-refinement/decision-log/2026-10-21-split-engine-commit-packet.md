---
id: decision-2026-10-21-ai-refinement-split-engine-commit-packet
title: "Decision Log — Split-Engine Commit Packet (ai-refinement)"
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
  - "[[ai-refinement]]"
  - "[[ai-refinement-commit-packet]]"
  - "[[engine-handoff-contract]]"
  - "[[2026-10-21-engine-handoff-contract-and-published-copies]]"
---

# Decision Log — 2026-10-21 — Split-Engine Commit Packet

**What was decided:** when the engine running Stages 01–05 cannot write to
Jira, Stage 05 ends by emitting a **commit packet** and Stage 06 runs in a
different engine from that packet alone. **By whom:** agent, on direct
operator instruction. **What it affects:** new `reference/commit-packet.md`
(1.0); Stage 05 `CONTEXT.md` (1.8 → 1.9, step 8, output row, verify item);
Stage 06 `CONTEXT.md` (1.12 → 1.13, packet input row, packet-entry
paragraph, step 6's no-write-path output, outputs, verify items, data
boundary line); `HUB.md` (1.25 → 1.26, topology, run procedure, Sixteenth
gap, reference row, two Band ③ descriptions). Stages 05–06 and the HUB move
`verified` → `to-review`. No skill content changed. Shared rationale for the
packet shape: `flow-foundry/decision-log/2026-10-21-engine-handoff-contract-and-published-copies.md`.

## The feedback

> "The AI refinement and documentation flow need an output to feed directly
> into rovo to go and actually create the jira and confluence documents.
> It's essentially a manual external agent handoff."

## Decisions and alternatives

1. **The packet is emitted at Stage 05's exit, not partway through Stage
   06.** Stage 06's parent confirmation needs a live candidate query, and the
   executor can run it. Keeping all of Stage 06 in one engine keeps its
   heavy review in one place. *Alternative considered:* the producing engine
   runs Stage 06 up to parent confirmation and labels (it has Jira read
   access), and the executor only writes — rejected because it splits one
   heavy-review stage across two engines and two sessions, and because the
   executor must re-validate the parent live anyway.
2. **The parent confirmation is taken in the executor even though the packet
   names an intended parent.** `parent_mapping_confirmation` forbids setting
   a link from an unconfirmed hierarchy position; the packet's parent is
   exactly that. A "create a new parent" answer stops the item, since
   refinement lives in the producing engine.
3. **The commit packet replaces Stage 06's bulk-only "Markdown handoff
   document."** The two had the same purpose and nearly the same contents;
   the packet adds the executor brief and the return slip, and now applies in
   single-item mode too. `bulk-child-creation`'s SKILL.md still names its
   degrade output a "Markdown handoff document"; the packet is a superset of
   it, and aligning the skill's wording is queued rather than done here, to
   keep the skill `verified`.
4. **No Stage 01 change.** Stage 01 could record the commit route up front.
   Not added, to keep Stage 01 `verified`; Stage 05 detects the missing
   write path when it matters.
5. **The provenance label becomes `refine-ai-flow-v1.26`.** The HUB bump
   changes it by design (`mandatory_labels`). The retired adapters held the
   only hard-coded copy; `jira-commit` uses a `<version>` placeholder, so no
   skill edit is needed.

## Assumptions (operator to confirm or amend)

- **G1** — The operator republishes 1.26 to both the SharePoint static copy
  and the Confluence copy. Until the Confluence copy moves past 1.21, the
  executor's version check will flag a mismatch on every packet, which is
  the intended behavior.
- **G2** — Return of the slip to the producing session is optional for a
  single item and required only when a later item uses a just-created item
  as its parent.
