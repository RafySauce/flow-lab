---
id: decision-2026-07-27-chat-session-degrade-paths
title: "Decision Log — Chat-Session Degrade Paths (START-HERE.md)"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-27
updated: 2026-07-27
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[jira-commit]]"
  - "[[jira-accomplishments-gatherer]]"
  - "[[confluence-contribution-gatherer]]"
  - "[[repo-context-enricher]]"
---

# Decision Log — 2026-07-27 — Chat-Session Degrade Paths

**What was decided:** a new repo-level entry point, `START-HERE.md`, lets a
user reference this repo directly in a chat session (no employer-side
source-repo required) and run a flow or skill against whatever tools that
session actually has. Where a stage or skill assumed a live external system
(Jira, Confluence, a connected repo) with no path for "that system isn't
connected," one is added: ask the user for the material directly, or (for
`jira-commit`) present the already-built dry-run preview as the terminal
output instead of committing. **By whom:** agent, on direct operator
instruction. **What it affects:** `icp-flows/ai-refinement/01-intake-and-
guardrails/CONTEXT.md` (1.9 → 1.10 — degrade branches on the
supporting-context research hunt and the team_code query), and four skills:
`jira-commit` (1.7 → 1.8, `verified` → `to-review`),
`jira-accomplishments-gatherer` (1.0 → 1.1, `verified` → `to-review`),
`confluence-contribution-gatherer` (1.0 → 1.1, `verified` → `to-review`),
`repo-context-enricher` (1.0 → 1.1, `verified` → `to-review`). Nothing is
deployed to a live engine; this is a design-time change, same as prior
revision passes.

## Design decisions

1. **One entry point, not per-flow/per-skill probing logic.** `START-HERE.md`
   runs the capability probe once per session and hands the result down;
   individual stages and skills only need to know their own degrade
   behavior, not how to detect what's available.
2. **Degrade, never fail or fabricate.** Every touchpoint gets a named,
   valid terminal or fallback state — a labeled preview instead of a
   commit, a request to paste material instead of a live query — never a
   silent stall and never a result presented as if a live system produced it
   when it didn't.
3. **Distinct from existing "not found" branches.** Several of these
   touchpoints already had a manual fallback for "queried live, found
   nothing" (e.g., Stage 01's team_code: "None found: ask the user
   directly"). The new branches are for a different case — no query path
   exists at all — and are written as separate, explicitly named branches
   so the two failure modes aren't conflated.
4. **Scope held to the touchpoints actually found.** Only files with a real
   external-system dependency were touched:
   `jira-commit` (writes Jira), `jira-accomplishments-gatherer` and
   `confluence-contribution-gatherer` (read Jira/Confluence),
   `repo-context-enricher` (reads a repo), and Stage 01's own inline
   Confluence/Jira/Jira-label queries. `accomplishments-docx-stylizer` was
   considered and excluded: it only formats content already gathered
   upstream and writes a local `.docx`, with no external-system read/write
   of its own.

## Remaining for the operator (the human gate)

1. Sign off `START-HERE.md` itself (currently `truth-level: draft`, house
   convention for a new specification document pending its own review).
2. Gate re-run for the four `to-review` skills above and Stage 01
   (1.10) — each carries a content change (an added branch) without a
   simulated pre-gate pass, logged rather than assumed clean, consistent
   with how prior revision passes in this flowspace have been handled.
3. `README.md`, `AGENTS.md`, `icp-flows/CONTEXT.md`, and
   `produced-skills/CONTEXT.md` framing updated to describe flows/skills as
   runnable directly in a chat session (via `START-HERE.md`) as well as
   instantiable into a full source-repo — the operator should confirm this
   framing matches intent before treating it as settled.
