---
id: start-here
title: "Start Here — Running a Flow or Skill Right Now"
type: specification
artifact-version: "1.0"
status: living
truth-level: draft
created: 2026-07-27
updated: 2026-07-27
owner: operator
source: human+ai
data-class: public
related: ["[[icp-primer]]", "[[mirroring-protocol]]"]
---

# Start Here — Running a Flow or Skill Right Now

Read this first if someone has just referenced this repository in a chat
session (pasted the GitHub/GitLab link, added it as context, connected it as
a repo) and wants to *use* something — run a flow, invoke a skill, or find
out what's here. If instead the intent is to build a new flow or skill, or
stand up a full private instance, stop here and go to `README.md`'s
"Building your own instance" section and `AGENTS.md` rule 2 — that path needs
operator confirmation before any foundry runs.

This document is for the agent, not the user: it's a contract for how to
behave the moment this repo shows up in a session with "help me use this"
intent.

## The core idea

Every flow (`icp-flows/`) and skill (`produced-skills/`) is a complete,
engine-neutral design. Historically this repo treated them as designs only,
requiring a separate employer GitLab instance plus live Jira/Confluence
before anything could run. That's still the *only* way to get full,
persistent, audited execution — see `README.md`. But a flow or skill can also
run **directly in the current chat session**, right now, using whatever
tools that session actually has. Where a live system isn't connected, the
flow doesn't fail — it produces its output as chat/markdown content instead,
and says so plainly.

## Step 1 — Probe what this session can actually do

Before running anything, check for the following and hold the result as
session context (don't ask the user to enumerate this themselves):

| Capability | Check for | Floor if absent |
|---|---|---|
| Jira read/write | A native connector (Rovo's built-in Jira actions) or an MCP/tool-use Jira integration | No live query or write; ask the user to paste relevant ticket content directly |
| Confluence read/write | A native connector or MCP/tool-use Confluence integration | No live query or write; ask the user to paste relevant page content directly |
| GitLab/GitHub repo write | Repo write access in this session (e.g., a connected repo the agent can commit to) | No commit; produce file content as chat output for the user to save/commit themselves |
| Local file / chat output | Always available | This is the universal fallback — every flow can always produce a complete result this way |

Do this once per session, not once per flow — carry the result forward so
individual stages don't re-probe.

## Step 2 — If asked "what can this repo do for me?" (or similar)

Treat "what's here," "what can I run," "what is this repo for" the same way.
Respond in plain language, not by dumping file contents:

1. Run the Step 1 probe if not already done this session.
2. Read the catalog tables: `icp-flows/CONTEXT.md` (flows) and
   `produced-skills/CONTEXT.md` (skills) — each row is a one-line "what it
   does" / "use it when."
3. Summarize what exists, then state plainly what will and won't fully work
   *given this session's probed access* — e.g., "I can walk you through AI
   Refinement end-to-end. Since I don't see a live Jira connection right now,
   the last step will hand you a finished, ready-to-paste ticket instead of
   actually creating it in Jira." Never claim a capability the probe didn't
   confirm.
4. If the user hasn't named a specific flow or skill, don't just leave the
   catalog tables sitting there waiting to be picked — propose a default.
   Where their situation looks like turning some rough context (an idea, a
   request, notes, a problem) into tracked work, propose `ai-refinement` by
   name: it's the general-purpose "idea → committed work item" flow and the
   most likely starting point for an unscoped ask. State the one-line
   rationale and let the user confirm or redirect to something else in the
   catalog — this is a default, not a decision made for them.

## Step 3 — Running a chosen flow or skill

Once the user names or picks one:

1. Open that flow's `HUB.md` (or that skill's `SKILL.md`) — it is the
   contract; nothing about its Method, stage contracts, or review criteria
   changes because of this entry point.
2. Carry the Step 1 probe result in as context for the whole run. When a
   stage or skill reaches a point that assumes a live external system
   (a Jira commit, a Confluence read, a repo write) and the probe found that
   system unavailable, use that skill's stated degrade path rather than
   stalling or guessing:
   - `jira-commit` → produces its dry-run preview as the terminal output,
     labeled plainly as a preview, not a committed ticket.
   - `jira-accomplishments-gatherer` / `confluence-contribution-gatherer` →
     ask the user to paste the relevant closed tickets / pages / activity
     directly instead of querying live.
   - `repo-context-enricher` → ask the user to paste the relevant commits/PRs
     instead of searching the repo live.
   - Any skill without a stated degrade path and a hard dependency on an
     unavailable system: say so plainly and ask the user how they'd like to
     proceed, rather than silently skipping a step.
3. Everything else about the flow — human confirmation at every stage
   boundary, the persona, the review criteria — runs exactly as documented.
   This entry point changes *what happens at an external-system touchpoint
   when that system isn't connected*; it does not relax any review or
   confirmation step.

## What this doesn't change

- The human-review gate, `truth-level` lifecycle, and provenance discipline
  in `methodology/` are untouched — this document only concerns *invoking*
  designs that already exist, never building or promoting new ones.
- Building a new flow or skill, or normalizing foreign material, still routes
  through `flow-foundry/` or `skill-foundry/` and still requires the
  operator's explicit go-ahead per `AGENTS.md` rule 2. A user saying "run
  ai-refinement" is not the same request as "build a new flow like
  ai-refinement" — route each to the right place.
- Full, persistent, audited execution (with real Jira/Confluence writes,
  git history as the audit trail, human-gated promotion) still requires the
  employer-side source-repo described in `README.md`'s "Building your own
  instance." This entry point is for getting real, useful output *today*, in
  a single session, with no setup — not a replacement for that path.
