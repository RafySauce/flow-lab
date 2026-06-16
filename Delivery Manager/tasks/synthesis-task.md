---
id: task-def-heavyweight-synthesis
title: "Delivery Manager — Heavyweight Synthesis Task Definition"
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
  - task-definition
  - ai/agentic-harness
source: human+ai
---

# Heavyweight Synthesis — Task Definition

## Purpose

Read the accumulated traces and corpus, write one synthesis finding, and advance the design intelligence for the eventual Hermes stack. Synthesis findings are the product of this whole apparatus — they are what Cincinnatus carries across the wall into agent specs, LiteLLM routing rules, and MCP skill manifests.

## Trigger / Cadence

**Weekly.** Sunday evening is the suggested default — end of the week, before the next week's work begins. Start time-based; revisit threshold-based if quiet periods produce findings with fewer than 5 traces (a synthesis run over too little signal is noise, not intelligence).

**Minimum trace threshold:** do not write a finding if fewer than 5 traces exist since the last synthesis run. If the threshold is not met, log a skipped-run note to `review/pulse.md` instead: `YYYY-MM-DD: synthesis skipped — [N] traces below threshold`.

## Inputs (read)

1. `traces/` — full set; note capability distribution, dominant life-domains, patterns across interactions
2. `corpus/` — full set; note what work products have been produced, what domains they serve
3. `review/board.md` — project state context; which initiatives are Active/Blocked and why

## Output

One synthesis finding written to `synthesis/synthesis-YYYY-MM-DD-[topic-cluster].md`.

### Finding structure

```markdown
## Capability clusters

[For each cluster: name the capability, count the traces, describe the pattern.]

## Dominant life-domains

[Which domains (homelab, hermes, household, etc.) are generating the most signal this period.]

## Migration-target proposals

[For each capability cluster, assert one migration target:]
- [capability]: → agent | gateway | mcp-skill
  - Rationale: [one sentence]

## Room proposals

[If intake clustering suggests a new project room has been earned, name it and argue for it.]
[If no room proposals: "No new rooms warranted this period."]

## Open threads for Cincinnatus

[Anything that surfaced during synthesis that requires a human decision — not an action item for the task, but a flag for review.]
```

### Frontmatter

```yaml
---
id: synthesis-YYYY-MM-DD-[topic-cluster]
title: "Synthesis Finding — [topic-cluster]"
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

## Done-condition

A new synthesis finding exists in `synthesis/` that:
- Clusters the trace set by capability
- Names the dominant life-domains generating signal
- Proposes at least one migration target with a rationale
- Addresses room proposals (even if the answer is "none warranted")
- Flags any open threads for Cincinnatus

Cincinnatus reviews and approves/rejects proposals. The task is done when the finding is written — not when the proposals are acted on.

## Constraints

- **Does not mint project rooms** — proposes only; Cincinnatus approves
- **Does not stamp migration targets on individual traces** — asserts them in the finding only
- **Does not add a usefulness field** to anything, ever
- **Does not modify existing traces or corpus items**
- **Flags any proposal that would route sensitive data toward a cloud API** explicitly in "Open threads for Cincinnatus" — do not silently pass it
- `source: ai` on every finding — these are the first artifacts in the system with no human in the loop; that must be visible in the frontmatter
