# synthesis/ — Context

## What this room is for

Scheduled-task output. The heavyweight synthesis task reads traces and corpus items, then writes one synthesis finding here. These are the first artifacts in the Delivery Manager with no human in the loop — `source: ai`. They cluster traces by capability, surface patterns, and propose migration targets. The findings are the product: Cincinnatus carries them across the wall into Hermes agent specs, LiteLLM routing rules, or MCP skill manifests.

## What a synthesis finding contains

A synthesis finding:
1. **Capability cluster summary** — which capabilities are firing most, which life-domains generate the most signal, what patterns are visible across the trace set
2. **Room proposals** — if the trace set suggests an intake cluster has earned a project room, the finding names it and argues for it. Cincinnatus approves; the room is not minted silently.
3. **Migration-target proposals** — for each capability cluster, the finding proposes one of: `agent` / `gateway` / `mcp-skill`

Migration-target vocabulary:
- `agent` → a Hermes agent spec (something that runs, reasons, acts)
- `gateway` → a LiteLLM inference-routing rule (something that directs traffic)
- `mcp-skill` → an MCP gateway tool manifest (something that exposes a capability)

**Migration targets are asserted by the synthesis task, never stamped on the trace at capture time.** The trace holds the signal; the synthesis holds the conclusion.

## What synthesis does NOT do

- Mint new project rooms (proposes only; Cincinnatus approves)
- Move sensitive data toward a cloud API (any proposal that would do this should be caught here before approval)
- Rewrite or retroactively update traces

## DNA stamping for synthesis findings

Reuse an existing DNA type:
- `type: brainstorm-recap` (if the finding is exploratory / pattern-surfacing)
- `type: specification` (if the finding is assertive / proposal-heavy)

Always `source: ai`.

## Naming

`synthesis-YYYY-MM-DD-[topic-cluster].md`
Example: `synthesis-2026-06-01-homelab-deploy-capability-cluster.md`

## Frontmatter template

```yaml
---
id: synthesis-YYYY-MM-DD-[topic-cluster]
title: "[Human-readable title]"
type: brainstorm-recap
artifact-version: "1.0"
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: living
truth-level: to-review
domain: ai
phase: "Phase 5 — Knowledge Architecture & AI Integration"
systems:
  - hermes
tags:
  - synthesis-finding
  - capability/[primary-cluster]
generated-by: heavyweight-synthesis-task
source: ai
---
```

## What good work looks like

A synthesis finding earns its place by saying something Cincinnatus could not have seen by reading the traces individually. It notices a pattern, names it, and proposes an action. A finding that merely restates the traces is not synthesis — it is a summary, and the lightweight tally already does that.
