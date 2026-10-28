---
id: decision-2026-10-28-truth-level-sync-sweep
title: "Decision Log — Truth-Level Sync Sweep (Hubs, Catalogs, Paths, Brief Queues)"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-28
updated: 2026-10-28
owner: operator
source: human+ai
data-class: public
related:
  - "[[2026-10-21-source-repo-protocol-rename-and-citation-sweep]]"
  - "[[provenance-spec]]"
  - "[[governance-and-audit]]"
---

# Decision Log — 2026-10-28 — Truth-Level Sync Sweep

**What was decided:** hubs, catalogs, and pointers are brought back in line
with the frontmatter of the files they describe. No skill, stage, or reference
changes content, and no `truth-level` is raised.

**By whom:** agent, on the operator's instruction to "correct the pieces that
don't require testing", after a read-only audit at `4c7ea3d`.

## Decisions and alternatives

1. **The file wins over the hub.** Six skills and six references were listed
   `verified` in their HUBs after their own files had dropped to `to-review`
   by logged decisions (2026-07-27 chat-session degrade paths; 2026-10-21
   citation sweep). The HUB rows now read `to-review` with the version and the
   cause. *Alternative:* re-promote the files to match the HUBs (rejected:
   promotion is the operator's gate, not a sync fix).
2. **Path-only fixes keep `truth-level` and version**, as in the 2026-10-21
   sweep: `flow-foundry/review-flowspaces/<flow>/…` → `icp-flows/<flow>/…` for
   flows that have since moved, one renumbered stage
   (`04-draft` → `07-draft`), the shared intake-vetting checklist path in
   `flow-foundry-architecture.md`, and the `sp-value-decomposition` pointer.
   The deprecated `repo-context-enricher` keeps its dead pointer as record.
3. **Briefs go where their own decision logs put them.**
   `sp-intake-triage-assistant` and `sp-mirror-drift-checker` (`status: dead`)
   return to `backlog-skill-starters/` per
   `skill-foundry/decision-log/2026-07-07-skill-starter-triage-drop.md`;
   `sp-process-decomposition` returns there because its skill is still staged
   in `review-skills/` (`foundry-spec.md` §4).
4. **Catalogs say what they hold.** `produced-skills/CONTEXT.md` marks its
   seven `to-review` rows; `icp-flows/CONTEXT.md` and `AGENTS.md` note that a
   DONE-queue item can sit at `to-review` after a later content change;
   `review-skills/CONTEXT.md` gains a "Staged now" list (first catalog
   mention of `cab-change-manifest`).
5. **Documentarian diagram** stops coloring Stages 2–7 as `gap`: all six
   skills are built.

## Left for the operator

- Re-gating the twelve demoted items (yes/no validation).
- Three completed briefs still `verified` while their skills are `to-review`
  (`sp-jira-accomplishments-gatherer`, `sp-confluence-contribution-gatherer`,
  `sp-provenance-stamper`), and 16 completed briefs still `to-review` whose
  skills are `verified`: brief stamps follow the operator's promotion act.
- The four built flow briefs still in `backlog-flow-starters/` (no
  `completed-flow-starters/` queue exists), and the deferred
  `sp-servicenow-kb-commit` in `completed-skill-starters/`.

**What it affects:** four HUBs, three catalogs, `AGENTS.md`,
`flow-foundry-architecture.md`, 23 path citations in 20 skills and briefs, three
brief moves.
