# traces/ — Context

## What this room is for

Promoted, signal-bearing usage traces. When an interaction with the Delivery Manager is notable — a good decision, a surprising retrieval, a synthesis that landed well, a pattern worth studying — Cincinnatus flags it and it gets promoted to a trace here. Traces are the raw material the heavyweight scheduled task reads to write synthesis findings.

## What a trace is

A trace captures one interaction: what was asked, what came back, and what would have made it better. It is freeform prose, not a structured form. Its job is to carry enough signal that a synthesis task can cluster it by capability and propose where it belongs in the eventual Hermes stack.

## The capability enum

Every trace carries one `capability` field from this seeded enum:

| Value | When to use |
|---|---|
| `summarize` | Condensing a body of material into a shorter form |
| `synthesize` | Drawing connections across multiple inputs to produce a new insight |
| `retrieve` | Finding or surfacing a specific piece of information |
| `decide` | Working through a decision with tradeoffs |
| `draft` | Producing a new artifact (guide, spec, doc) |
| `monitor` | Scanning for state changes, clusters, or anomalies |

Refine this enum as real usage reveals gaps. When a new value is added, document it here.

## What does NOT live here

- The **usefulness field** — there is no usefulness field on traces, ever. Cincinnatus holds usefulness himself during the proving-out phase. Formal usefulness-scoring is a Hermes-side problem to design after migration. Do not add one.
- Drafts and working notes (→ project rooms or `intake/`)
- Finished work products (→ `corpus/`)
- Synthesis findings (→ `synthesis/`)

## DNA stamping for traces

`usage-trace` is a project-local candidate type — not yet in the DNA spec. Until it is absorbed:
- `type: specification`
- `tags: [usage-trace, capability/[value]]`

Always check the live `dna-spec.md` at stamp time. If `usage-trace` has been absorbed as a first-class type, use it.

## Naming

`trace-YYYY-MM-DD-[capability]-[short-description].md`
Example: `trace-2026-05-27-decide-frigate-camera-strategy.md`

## Frontmatter template

```yaml
---
id: trace-YYYY-MM-DD-[capability]-[short-description]
title: "[Human-readable title]"
type: specification
artifact-version: "1.0"
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: living
truth-level: to-review
domain: [homelab | ai | ...]
phase: "Phase 5 — Knowledge Architecture & AI Integration"
systems:
  - hermes
tags:
  - usage-trace
  - capability/[value]
source: human+ai
capability: [summarize | synthesize | retrieve | decide | draft | monitor]
---
```

## What good work looks like

Traces are honest and specific. The body says what actually happened, not what was hoped. "What would have made it better" is answered even when the interaction went well — there is always something. A trace that says "it was fine" carries no signal.
