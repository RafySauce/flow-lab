---
id: decision-2026-08-01-portfolio-rationalization-skill-hierarchy-update
title: "Decision Log — jira-portfolio-ingest and portfolio-profiler: Connected-Space Discovery and the Hierarchy/Orphan View"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related:
  - "[[jira-portfolio-ingest]]"
  - "[[portfolio-profiler]]"
  - "[[portfolio-rationalization]]"
  - "[[export-and-field-requirements]]"
---

# Decision Log — 2026-08-01 — jira-portfolio-ingest and portfolio-profiler: Connected-Space Discovery and the Hierarchy/Orphan View

**What was decided:** update both promoted skills that implement
`portfolio-rationalization`'s Stage 01 and Stage 02 — `SKILL.md`, both
adapters (`rovo-agent.md`, `copilot-prompt.md`), each — to match the stage
contract changes recorded in the companion flow-foundry entry
(`flow-foundry/decision-log/2026-08-01-portfolio-rationalization-art-hierarchy-and-connected-spaces.md`).
**By whom:** agent, on the same explicit operator instruction that entry
records. **What it affects:** `produced-skills/jira-portfolio-ingest/` and
`produced-skills/portfolio-profiler/` in place — no new folders, no change to
either skill's promotion status. Both skills remain `truth-level: to-review`;
nothing here re-promotes or re-gates them.

## Departure from the 2026-07-29 precedent, stated

The prior dictionary-inference decision explicitly deferred skill edits to "a
separate skill-foundry invocation," on the grounds that flowspace-design
confirmation doesn't carry authority over a skill spec (`AGENTS.md` rules
1–2). That skill (`objective-keyword-mapper`) was, at the time, still staged
in `review-skills/` and unpromoted — its staleness against the new Stage 03
contract was a real but not yet *live* problem.

`jira-portfolio-ingest` and `portfolio-profiler` are different: both already
sit in `produced-skills/`, promoted ahead of this session (commit `50db7b5`).
Leaving them as they were would mean the flowspace's authoritative Stage 01/02
contracts and their own promoted Layer-3 implementations disagree the moment
the flow-foundry entry lands — not a future risk to flag, an immediate one.
The operator's instruction covered the analysis flow's behavior end to end
("the portfolio analysis flow should look for... The analysis should also
output..."), which describes what running the skill actually does, not only
what the design document says it should do. Both were read as in scope and
updated in this same pass.

## Changes made

### `jira-portfolio-ingest`

- `SKILL.md`: description gained the connected-space discovery capability;
  flow diagram gained a discovery decision node and an updated Output node
  listing the connected-space hierarchy context; Method gained step 11
  (renumbering the former step 11 to 12); Inputs-and-grounding, Data
  boundary, and "What this skill is not" each gained one clause on the
  narrow cross-project exception; Review criteria gained item 11 (item 12
  renumbered); Adapters table and Changelog updated. `1.0` → `1.1`.
- `adapters/copilot-prompt.md` and `adapters/rovo-agent.md`: mirrored the
  same step, self-check, refusal/scope, and knowledge-scoping changes at
  each adapter's own register (Copilot's export-primary framing; Rovo's
  native-Jira-action framing, including its "no cross-project queries" scope
  line, narrowed to name the one permitted exception rather than dropped).
  Both headers bumped to "Generated from ... v1.1."

### `portfolio-profiler`

- `SKILL.md`: description gained the hierarchy view and orphan/dangling
  counts; flow diagram gained a field-availability branch into the hierarchy
  step; Method gained step 9 (renumbering the former steps 9–11 to 10–12);
  Inputs-and-grounding and Data boundary each gained the connected-space
  context and `work-item-schemas.md` as inputs; "What this skill is not"
  gained a clause distinguishing this skill (draws the diagram) from
  `jira-portfolio-ingest` (resolves the links); Review criteria gained items
  9–10 (renumbering the rest); Adapters table and Changelog updated.
  `1.0` → `1.1`.
- `adapters/copilot-prompt.md` and `adapters/rovo-agent.md`: mirrored the
  same step, self-check, refusal, and knowledge-scoping changes. Rovo's
  Knowledge scoping gained `work-item-schemas.md` as a read-only source for
  hierarchy-level placement. Both headers bumped to "Generated from ... v1.1."

## Notable calls

- **Neither skill gained new write scope or new unrestricted external
  access.** `jira-portfolio-ingest`'s one new capability (connected-space
  discovery) is explicitly a by-key read, never a second search/JQL query —
  stated identically in the spec and both adapters, including a dedicated
  "Permitted actions" line in the Rovo adapter distinguishing a by-key fetch
  from a search. `portfolio-profiler` gained no external access at all: it
  only ever reads what `jira-portfolio-ingest` already resolved and screened.
- **The orphan/dangling-reference distinction and the "never fabricate a
  hierarchy" degrade rule are stated identically across all four touched
  files (two `SKILL.md`, two adapters) for `portfolio-profiler`**, and
  likewise for connected-space discovery's targeted-lookup constraint across
  `jira-portfolio-ingest`'s three files (`SKILL.md` plus two adapters) — a
  deliberate redundancy, matching how every other cross-cutting rule in this
  skill pair (e.g. the distribution-not-ranking rule) already repeats itself
  at each artifact rather than being stated once and assumed to travel.
- **Boundary/collision check, informal:** neither change moves either skill
  closer to a skill it already declines to overlap with. `jira-portfolio-ingest`
  still does not bind, page, or profile a second project as its own cycle
  (new "Not a multi-project binder" clause states this explicitly, distinct
  from `jira-accomplishments-gatherer`'s unrelated unit of analysis).
  `portfolio-profiler` still does not query Jira or resolve a link itself
  (new "Not a hierarchy resolver" clause). No new collision surface against
  the other eleven produced skills was introduced. A formal collision
  re-check was not run — this is a same-day, same-flowspace revision of two
  already-promoted, already-checked skills, not a new build.

## Flagged, not silently resolved

**Neither skill's promotion status changed.** Both remain `truth-level:
to-review` in `produced-skills/`, which is itself a pre-existing state this
entry does not address (see the companion flow-foundry entry's "Flagged"
section on `HUB.md`'s stale Known-gaps note). Whether these edits should
trigger a re-run of the five-point gate before the next live use is an
operator call, not one this pass makes for them — `AGENTS.md` rule 5, the
verified gate is always human.

**No adapter has been re-tested on-engine** against the new steps. The
connected-space discovery step in particular depends on a targeted by-key
Jira lookup capability that neither adapter's prior version exercised; until
it runs against a real (or synthetic) portfolio with genuine cross-project
parent links, the step's wording is unverified against actual engine
behavior, same as every other part of this skill pair before its own
five-point gate.

## Notes

- Nothing in this pass touches `sp-jira-portfolio-ingest.md` or
  `sp-portfolio-profiler.md` in `skill-foundry/completed-skill-starters/` —
  those are terminal intake records of the original build, not living specs.
- All frontmatter-bumped files (`jira-portfolio-ingest/SKILL.md`,
  `portfolio-profiler/SKILL.md`) moved `artifact-version` `1.0` → `1.1`,
  `updated: 2026-08-01`. Both skills' adapter headers moved their "Generated
  from" version reference `v1.0` → `v1.1` to match.
