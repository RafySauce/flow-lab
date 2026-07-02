---
id: sp-mirror-drift-checker
title: "Skill Primer Brief — Mirror Drift Checker"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-02
updated: 2026-07-02
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.0"
data-class: public
related: ["[[mirroring-protocol]]"]
---

# Skill Primer Brief — Mirror Drift Checker

## Purpose

Automate the comparison half of the mirroring protocol's drift check (`methodology/mirroring-protocol.md` §4): compare the Confluence primary against the git mirror and produce a findings report. Replaces a manual weekly walk-through.

## Triggering intent

- **Fires on:** "run the drift check," the weekly cadence, pre-audit prep, and after any bulk sync.
- **Does not fire on:** fixing drift (human decides which surface is right), syncing content (that's the sync procedure), or validating a single new flowspace (that's the flow-foundry's gate 1).

## Method sketch

1. Enumerate flowspace hubs on both surfaces; report one-sided entries.
2. Per flowspace: compare stage count/names; compare `truth-level` and `updated` (page properties vs. frontmatter).
3. Check `MIRROR-STATE.md` consistency (no mirror file newer than its last-sync entry implies).
4. Emit a findings report — **report only, never auto-fix, never touch truth-levels.**

## Inputs and data boundary

Reads the Confluence ICP space and the internal mirror repo. Max data-class: whatever the instance holds (internal+). Engine: likely **Copilot agent** on the mirror side with a human-exported Confluence manifest, or a Rovo agent producing the Confluence-side manifest — the build should decide whether this is one skill with two adapters cooperating or a script + one agent.

## Demand source

`methodology/mirroring-protocol.md` §4 names this gap explicitly; every instantiated flowspace inherits it.

## Definition of done

On a test instance with three seeded drift defects (renamed stage, stale truth-level, missing mirror file), the report catches all three with zero false positives, and changes nothing.
