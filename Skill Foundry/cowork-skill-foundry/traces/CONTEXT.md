# Traces

## What this room is for
The signal layer. Every meaningful foundry decision gets captured here as a trace — not the whole transcript, but the judgment: what was asked, what the foundry decided, and what would have made it better. Traces are what the Hermes skill-foundry agent inherits. An un-traced build teaches the future agent nothing; a well-traced one is a training example.

## Process
Flag a trace whenever a decision carried real judgment: a triage drop, a security flag, a tricky execution-tier call, a foreign skill whose intent had to be inferred, a primer-brief that turned out underspecified. Stamp it with the capability it exercised. Keep it freeform and honest — including where the foundry got it wrong.

## What lives here
Dated trace files (YYYY-MM-DD-short-name-trace.md), each using the scaffold below.

## Trace scaffold

```markdown
---
type: specification
artifact-version: "1.0"
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: living
truth-level: draft
source: human+ai
tags: [usage-trace]
capability: [triage|vet|normalize|author|route|review|decide]
---

# [What was asked]

[Freeform: what came in, what the foundry decided, why, and what would have made it better.]
```

Note: the capability enum here is foundry-specific (triage / vet / normalize / author / route / review / decide) — it refines the template's generic enum to this project's actual modes. usage-trace stays a project-local candidate type until it earns promotion into the DNA spec the way `claimed` did. No usefulness field — usefulness is held by Cincinnatus during proving-out, formalized Hermes-side later.

## What good looks like
Honest, specific, capability-stamped. A trace that says "routed to baseline, but on reflection the voice load was higher than I scored — should have been frontier" is gold for Hermes. A trace that just restates what happened with no judgment is noise.

## Skills
None directly — tracing is a discipline, not a skill invocation.
