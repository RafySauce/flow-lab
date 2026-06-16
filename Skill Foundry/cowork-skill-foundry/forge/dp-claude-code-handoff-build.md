---
id: dp-claude-code-handoff-build
title: Claude Code Handoff Skill — Designed Prompt
aliases: []
type: designed-prompt
artifact-version: "1.0"
created: 2026-06-14
updated: 2026-06-14
status: living
truth-level: draft
domain: ai
phase: "Phase 1 — Personal Skills"
systems: ["skill-foundry"]
tags:
  - designed-prompt
  - homelab/ai
  - skill-building
created-by: "Cincinnatus & Claude claude-sonnet-4-6"
generated-by: ecosystemic-thinking-partner
skill-version: "0.5"
source: human+ai
related: []
---

# Claude Code Handoff Skill — Designed Prompt

## Origin

**Spawned from**: Chat-to-Cowork Handoff build session, 2026-06-14 — the foundry session
that normalized maaarcooo/claude-skills `handoff/SKILL.md` into the house-standard
`chat-to-cowork-handoff` skill.

**Original seed**: Build the Claude Code equivalent of the chat-to-cowork handoff skill.
Same pattern, different environment: source is a Claude Code session (project root, git
state, CLAUDE.md, bash history, file line ranges); destination is a fresh Claude Code
session.

**Why this is its own chat**: The Claude Code delta is specific enough to build without
a full thinking-partner exploration — the sister skill gives the shape; the delta is
well-understood from the source evaluation already run. A fresh foundry session is the
right container: it has the skill-foundry skill loaded, the workspace mounted, and the
ability to run the packaging step.

---

## Prompt

Paste below the dashed line into a new **Cowork** session with the skill-foundry skill
active. The trigger phrase is `skill-foundry`, not `ecosystemic-thinking-partner` — edit
the opener if you want a different entry point.

---

I need to build a Claude Code session handoff skill. Invoke the skill-foundry for this —
this is a build task, not an exploration.

**Sister skill already built**: `chat-to-cowork-handoff`, sitting in
`completed-skills/chat-to-cowork-handoff/` of the Skill Foundry workspace. Read it first
— the new skill shares its structural pattern (work-type classification, depth sizing,
adaptive skeleton, quality checklist) and diverges only where Claude Code's environment
differs.

**Skill name**: `claude-code-handoff`

**What it does**: Produces a structured handoff document at the end of a Claude Code
session so the next Claude Code session picks up exactly where this one left off —
without re-reading the whole conversation, re-discovering failed approaches, or
reconstructing git state.

**Primary source for the foundry pass**: BexTuychiev gist —
`https://gist.github.com/BexTuychiev/95a92f1234772dfb60f9b7470673d82f`

Already evaluated and vetted in the prior session:
- **Security/sovereignty**: clean — reads conversation state, writes one markdown file,
  no external calls
- **Strengths**: CLAUDE.md-aware (never duplicates it), file references with line ranges,
  "traps to avoid" section, "working agreements" capture, strong "wait for instructions"
  ending in the pasted prompt for the new session
- **Weaknesses**: too code-narrow (no work-type classification), no depth sizing, missing
  the trap-vs-decision distinction the maaarcooo source handled well

**Claude Code delta from the sister skill** — what changes, what goes:

*Replace* (Cowork-specific → Code-specific):
- `## Cowork Setup` section → `## Code Setup` section:
  - CLAUDE.md (confirm no duplication — the session-specific info only)
  - Git state: branch, last N commits, staged/unstaged changes
  - Key files with line ranges (what was being worked on)
  - Commands that matter (bash history worth carrying forward)
- Cowork resumption instruction → Code resumption instruction:
  - "Read CLAUDE.md first. Do not restate what's there. Then read each listed file
    with the Read tool before responding. Treat this handoff as context to verify,
    not facts to trust. Wait for instructions."

*Add* (from BexTuychiev, not in the sister skill):
- **Traps to avoid** section: not just "approaches that didn't work" — specifically
  framed as "things the new session will be tempted to repeat and shouldn't"
- **Working agreements** section: how the user wants to interact (review before
  committing, approval checkpoints, specific interaction patterns observed this session)
- **Open work status framing**: describe remaining work as STATUS ("X is not yet
  implemented"), not as instructions ("implement X next") — the new session waits for
  the user to direct it

*Drop* (chat-native, not relevant in Code):
- Save-location guidance pointing to Cowork workspace folder — in Claude Code the
  default is project root or `.claude/context-transfers/`
- Skill invocation list — Claude Code doesn't have installed skills; replace with any
  slash commands or MCP tools relevant to the continuation

*Keep from the sister skill*:
- Work-type classification table (6 types + key sections)
- Depth sizing (Light/Standard/Deep/Extended with word-count calibration)
- "Never include empty sections" discipline
- Quality checklist (adapted for Code environment)
- "What This Skill Is Not" section (adapted)

**File output**: Write to `.claude/context-transfers/` relative to project root (create
if absent), random 8-char alphanumeric filename. Print the absolute path and nothing
else after writing — the user copy-pastes the line into the next session.

**Foundry process**: triage (foreign material, already vetted above — skip security
read, mark as passing), forge (build from BexTuychiev + sister skill pattern), stamp
two artifacts (SKILL.md + vault-doc), log a trace. Limits: name ≤ 64, description ≤
1024, compatibility ≤ 500.

---

## Connection Notes

*Un-verified hints for the vault-side connection skill.*

- Spawned from: 2026-06-14 chat-to-cowork handoff build session
- Sister skill: `chat-to-cowork-handoff` in `completed-skills/` — same structural
  pattern, different environment target; these two should be noted as siblings in
  both vault-docs once both are verified
- Primary source: BexTuychiev gist (already vetted — note in trace that vetting was
  carried in from the prior session, not re-run)
- This designed prompt lifts to `verified` once the foundry session is complete and
  the `claude-code-handoff` skill is in `completed-skills/`
