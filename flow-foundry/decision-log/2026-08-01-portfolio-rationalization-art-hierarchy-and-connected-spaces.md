---
id: decision-2026-08-01-portfolio-rationalization-art-hierarchy-and-connected-spaces
title: "Decision Log — Portfolio Rationalization: ART-Board Connected-Space Discovery and the Hierarchy/Orphan View"
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
  - "[[portfolio-rationalization]]"
  - "[[portfolio-rationalization-stage-01]]"
  - "[[portfolio-rationalization-stage-02]]"
  - "[[export-and-field-requirements]]"
  - "[[work-item-schemas]]"
---

# Decision Log — 2026-08-01 — Portfolio Rationalization: ART-Board Connected-Space Discovery and the Hierarchy/Orphan View

**What was decided:** Stage 01 gains a connected-space discovery step, and
Stage 02 gains a Portfolio Epic → Solution Epic → Feature → child Mermaid
hierarchy view with orphan and dangling-reference counts. **By whom:** agent,
on explicit operator instruction this session ("the portfolio analysis flow
should look for projects/spaces that connect to the current backlog... The
analysis should also output a simple mermaid hierarchy of the work item
summaries from portfolio to solution to feature level work and call out how
many items are orphans without parents") — `AGENTS.md` rule 2 / `foundry-spec.md`
§1 Step 0. This is foundry revision work on a `to-review` design; nothing is
promoted, and nothing has run on-engine.

## The problem this addresses

A single Jira project or space rarely holds a backlog's whole hierarchy. The
common shape (SAFe's own): one overarching ART (Agile Release Train) board
carries the portfolio and solution epics that drive strategic goals across
several feature-delivery team projects, each with its own board. A cycle
bound to one such team project, as every prior version of Stage 01 assumed,
would see every Feature's `Parent key` point at a Solution Epic the cycle
never queried — and Stage 02 had no way to show that shape at all, let alone
distinguish "this item genuinely has no parent" from "this item's parent
just isn't in scope."

## Design choices, and why

1. **Discovery is additive to the primary scope, never a silent expansion of
   it.** The flow's one-project-per-cycle discipline
   (`export-and-field-requirements.md` §5) exists so cycle-over-cycle
   comparisons stay valid — widening it quietly would break every downstream
   count and the Verify checks built on them. Connected-space resolution is
   instead a **targeted, by-key lookup** of only the parent keys the primary
   set already references (never a second whole-project or JQL query), and
   the resolved items are kept in a **separate connected-space hierarchy
   context** that never joins the primary item set or its count. Stage 02's
   existing distributions, Stage 03's mapping, Stage 04's scoring, and every
   existing cross-stage trace are untouched by this change — the hierarchy
   view is the only consumer of connected-space context.
2. **The operator is offered the choice, never defaulted.** Discovery
   presents candidate connected spaces (prefix, reference count, level) and
   asks resolve-or-decline, mirroring Stage 02's own exploration-lens offer
   discipline. Declining, or finding nothing to discover, are both complete,
   valid outcomes — not degraded ones.
3. **Orphans and dangling references are reported as two counts, never
   folded into one.** An item with no `Parent key` at all is a different
   finding, calling for different operator action, than an item whose
   `Parent key` points somewhere unresolved this cycle (declined discovery, a
   failed lookup, or a genuinely broken link). This mirrors the flow's
   existing pattern of keeping "absent" and "present but different" apart
   (e.g. the due-date category's "unavailable" vs. "none" distinction,
   `export-and-field-requirements.md` §3).
4. **`Issue Type` and `Parent key` are "strongly preferred," not hard
   requirements.** Neither field existed in the canonical set before this
   change. Making either a hard requirement would halt cycles that don't
   need the hierarchy view; instead, its absence degrades only the hierarchy
   view and connected-space discovery, named explicitly, while every other
   section of both stages runs unaffected — the same degrade-don't-fail
   discipline the rest of `export-and-field-requirements.md` §3 already
   applies.
5. **`Parent key` is documented as one canonical name for whichever
   hierarchy-linking field the instance actually populates at a given
   level** (Epic Link, Parent Link, or Parent, per `ai-refinement`'s
   `parent_mapping_confirmation` convention,
   `icp-flows/ai-refinement/06-jira-commit-and-close/CONTEXT.md`), resolved
   through Stage 01's existing field-mapping step rather than inventing a
   second field-mapping mechanism.

## Changes made

1. **`icp-flows/portfolio-rationalization/01-intake-and-source-binding/CONTEXT.md`**
   — new process step 11 (connected-space discovery), old step 11 renumbered
   to 12; new Outputs rows (discovery outcome, connected-space hierarchy
   context); Verify checklist and cross-stage-trace note; Data boundary's one
   named exception to single-project scope; Review's evidence line. `1.0` →
   `1.1`.
2. **`icp-flows/portfolio-rationalization/02-portfolio-profiling/CONTEXT.md`**
   — new Inputs rows; new process step 9 (hierarchy view), old steps 9–11
   renumbered to 10–12 (including the "step 9" self-reference in Review,
   corrected to "step 10"); new Outputs row; Verify checklist and
   cross-stage-trace note; Data boundary note. `1.0` → `1.1`.
3. **`icp-flows/portfolio-rationalization/reference/export-and-field-requirements.md`**
   — added `Issue Type` to the canonical field table; upgraded `Parent key`
   from "Optional"/Stage-05-only to "Strongly preferred" and multi-stage;
   two new degraded-signal rows; new §8, "Hierarchy linkage and
   connected-space discovery," stating the field conventions and the
   orphan/dangling-reference distinction. `1.0` → `1.1`.
4. **`icp-flows/portfolio-rationalization/HUB.md`** — intro paragraph and Run
   procedure steps 2–3 updated to describe discovery and the hierarchy view.
   `1.1` → `1.2`.
5. **`produced-skills/jira-portfolio-ingest/`** and
   **`produced-skills/portfolio-profiler/`** — see the companion
   skill-foundry entry
   (`skill-foundry/decision-log/2026-08-01-portfolio-rationalization-skill-hierarchy-update.md`);
   recorded here only because both skills are this flowspace's promoted
   Stage 01/02 implementations and would otherwise disagree with the stage
   contracts above the moment this entry lands.

## Flagged, not silently resolved

**Skill edits normally route through a separate skill-foundry invocation**
(the 2026-07-29 dictionary-inference decision deferred `SKILL.md` edits for
exactly this reason, flagging `objective-keyword-mapper`'s staleness rather
than fixing it in the same pass). This entry departs from that precedent
deliberately: `jira-portfolio-ingest` and `portfolio-profiler` are already
promoted to `produced-skills/` (unlike the still-unpromoted skill that 2026-07-29
flagged), so leaving them stale against their own stage contracts would be an
immediate, live inconsistency rather than a future risk. Both were updated in
this pass — method steps, flow diagrams, review criteria, changelogs, and
both adapters each — logged separately in the skill-foundry decision log per
house convention (build-time decisions about a flowspace's *design* live in
the flow-foundry log; decisions about a skill's *spec and adapters* live in
the skill-foundry log). The operator should treat this as the norm going
forward for already-promoted skills whose owning stage contract changes, not
assume every future flowspace revision will also touch its skills in the same
pass.

**Stage 05 and Stage 06 were not extended to consume the hierarchy view or
orphan counts.** The operator's instruction scoped this change to discovery
(Stage 01) and the hierarchy/orphan output (Stage 02); feeding orphan counts
into the disposition packet or the close-score model would be a scoring-model
change, which — per the 2026-07-29 precedent on dictionary-provenance caveats
— is deliberately out of scope for a pass that isn't also running the
model's own calibration gate (`close-score-model.md` §7). If the operator
wants orphan/dangling counts to inform Stage 05's packet context, that is a
follow-up decision, not an implicit consequence of this one.

**HUB.md's "Known gaps" section, describing the five Layer-3 skills as
"staged in `review-skills/`, not promoted," is stale independent of this
change** — `jira-portfolio-ingest` and `portfolio-profiler` already sit in
`produced-skills/` (moved by commit `50db7b5`, prior to this session). Left
untouched here: correcting it is unrelated to the hierarchy/discovery work
this entry covers, and conflating the two in one pass risks getting the
promotion nuance wrong (the note also claims "nothing has run on-engine,"
which is a separate, possibly still-true claim from the folder move).

## Notes

- This build has not been through the three validation gates
  (`foundry-spec.md` §5) as a fresh pass. Existing Known-gaps entries from
  2026-07-28/29 (unratified calibration, pending label rename, unresolved
  completion denominator) are unchanged by this decision.
- Nothing has run on-engine against real Jira data; the connected-space
  discovery step and the hierarchy view are untested against a live or
  exported portfolio.
- All frontmatter-bumped files
  (`01-intake-and-source-binding/CONTEXT.md`,
  `02-portfolio-profiling/CONTEXT.md`,
  `reference/export-and-field-requirements.md`, `HUB.md`) moved
  `artifact-version` as stated above, `updated: 2026-08-01`.
