---
id: decision-2026-07-07-skill-starter-triage-drop
title: "Decision Log — Skill Starter Backlog Rationalization: Two Drops"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-07
updated: 2026-07-07
owner: operator
source: human+ai
data-class: public
related: ["[[sp-intake-triage-assistant]]", "[[sp-mirror-drift-checker]]"]
---

# Decision Log — 2026-07-07 — Skill Starter Backlog Rationalization: Two Drops

**What was decided:** triage-drop `sp-intake-triage-assistant` and
`sp-mirror-drift-checker` — not skill-worthy *now* — rather than build them.
Both stamped `status: dead`, kept in `backlog-skill-starters/` as the record
per `governance-and-audit.md` §7 (nothing silently deleted). **By whom:**
operator, on the agent's triage recommendation; confirmed before any build
work started.

**Alternatives considered:** build all four remaining starters (rejected —
building ahead of demonstrated demand); delete the files outright (rejected —
retention rule requires `status: dead`, not deletion).

**Reason:**
- `intake-triage-assistant` automates triaging a backlog that has produced 9
  items over months — no evidence the triage step is actually a bottleneck
  worth tooling yet.
- `mirror-drift-checker` solves drift between a Confluence primary and a git
  mirror that isn't live yet in this instance; building it now is speculative.

**Re-file condition:** `intake-triage-assistant` — once backlog volume or
triage cadence makes manual classification a real bottleneck.
`mirror-drift-checker` — once the dual-surface deployment (`mirroring-protocol.md`)
is actually running with real flowspace content to drift-check.

**What it affects:** `backlog-skill-starters/` (both briefs now `status: dead`,
unbuilt); no skill-foundry queue moves, nothing staged, nothing promoted.
