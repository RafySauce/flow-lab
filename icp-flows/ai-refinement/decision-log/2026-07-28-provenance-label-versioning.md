---
id: decision-2026-07-28-provenance-label-versioning
title: "Decision Log — Provenance Label Versioning; Stage 01 Session-Start Additions"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-07-28
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
  - "[[work-item-schemas]]"
  - "[[jira-commit]]"
  - "[[workitem-validation]]"
---

# Decision Log — 2026-07-28 — Provenance Label Versioning; Stage 01 Session-Start Additions

**What was decided:** replace the static `refine-ai-built` provenance label
with `refine-ai-flow-v<version>`, where `<version>` is the `ai-refinement`
flowspace's own `artifact-version` (currently `1.14`, so
`refine-ai-flow-v1.14`), and state the label's purpose in the amendment text
itself rather than leaving it implicit: it flags an item as AI-produced and
pending team review, and the team removes it once their review is complete.
Separately, Stage 01 gains two session-start additions: the flowspace's
purpose statement, shown immediately under the session-start header before
anything else, and a provenance-label notice grouped with the existing
guardrails. **By whom:** agent, on direct operator instruction, following a
clarifying question on which artifact's version the label should carry
(flowspace vs. `jira-commit` skill vs. both) — the operator chose the
flowspace version and confirmed the new label replaces `refine-ai-built`
outright ("stick to only that"), not alongside it. **What it affects:**
`reference/ai-refinement-hybrid.md` (1.3 → 1.4), `reference/work-item-schemas.md`
(1.4 → 1.5), Stage 01 `CONTEXT.md` (1.10 → 1.11), Stage 05 `CONTEXT.md`
(1.4 → 1.5, `verified` → `to-review`), Stage 06 `CONTEXT.md` (1.8 → 1.9,
`verified` → `to-review`), `HUB.md` (1.14 → 1.15), the `jira-commit` skill
(1.8 → 1.9, stays `to-review`) and its adapters, the `workitem-validation`
skill (1.2 → 1.3, frontmatter `truth-level` corrected to `to-review`) and its
adapters.

## The change

1. **The provenance label carries the flowspace's own version, not the
   committing skill's.** `<version>` resolves to `ai-refinement`'s `HUB.md`
   `artifact-version` — the number a user or reviewer already associates with
   "which revision of this flow produced this item" — not `jira-commit`'s own
   `artifact-version`, which tracks the commit logic specifically and would
   under-represent upstream-stage changes (e.g. a Stage 02 elicitation
   revision that never touches `jira-commit`).
2. **Replacement, not addition.** `refine-ai-flow-v<version>` fully replaces
   `refine-ai-built` — one mandatory provenance label, not two. The planning
   label (`<team_code>-<yyyy>-q<n>`) is untouched by this change.
3. **No live query for the provenance label.** Unlike `team_code`, the
   flowspace's own version needs no Jira lookup and no per-run candidate
   confirmation — it's known the moment the session starts, so Stage 01
   states the concrete label value immediately rather than deferring
   resolution to later in intake.
4. **The label's purpose is now canonical spec text.** The `mandatory_labels`
   rule previously said only *that* the label gets applied; it now says
   *why*: a pending-review flag, removed by the team once their review of the
   item is complete. This purpose is surfaced to the user twice — once at
   Stage 01 session start (the heads-up) and again at Stage 06's dry-run
   preview (the last point before commit) — not just stated once and assumed
   retained.
5. **Stage 01 gains a purpose statement, ahead of every other guardrail.**
   Placed immediately under the session-start header, before the
   responsibility notice: what the flow produces and its one-run-one-item,
   confirm-every-field-boundary contract. This orients the user to what they
   triggered before any setup question follows.
6. **Enforcement tier is unchanged.** The renamed label stays inside Stage
   05's existing warn-and-bypass mandatory-label check, exactly as
   `refine-ai-built` was — this decision touches the label's name and stated
   purpose, not how strictly it's gated.

## Decisions and alternatives

1. **Flowspace version over skill version.** *Alternative considered:* key
   the label to `jira-commit`'s own `artifact-version`, since that's the
   skill actually executing the commit and the one whose behavior a defect
   would trace back to. *Rejected* by direct operator instruction: the
   flowspace version is what a reviewing team member already thinks of as
   "which version of this flow." **Trade-off accepted, not hidden:** a
   version bump to `HUB.md` alone (no `jira-commit` spec change) now still
   requires regenerating `jira-commit`'s adapters for the label to stay
   accurate — see the Owed item below.
2. **Replace, don't add a second label.** *Alternative considered:* keep
   `refine-ai-built` as a static "this was AI-built" flag and add
   `refine-ai-flow-v<version>` alongside it as a separate, more granular
   marker. *Rejected* by direct operator instruction ("stick to only that")
   — one label carries both signals (AI-produced *and* which flow version),
   keeping the mandatory-label surface at two labels total (provenance +
   planning), not three.
3. **State the purpose in the spec, not just in a UI message.** *Alternative
   considered:* add the heads-up only to Stage 01's session-start prose,
   leaving the `mandatory_labels` amendment's `rule:` text purpose-silent as
   before. *Rejected*: the amendment is the canonical definition other stages
   and skills read from (Stage 05's check, Stage 06's preview, the
   cross-cutting note in `work-item-schemas.md`) — stating the purpose only
   in one stage's prose would leave every other consumer of the amendment
   without it.
4. **Owed — new adapter-regeneration coupling.** Recorded here rather than
   left implicit: because the label now carries the *flowspace's* version,
   any future `HUB.md`-only version bump (one that doesn't touch
   `jira-commit`'s own spec content) still requires regenerating
   `jira-commit`'s adapters purely to keep the baked-in label value accurate.
   Previously, adapter regeneration was triggered only by a change to that
   skill's own spec. This is a new maintenance dependency between `HUB.md`
   and `jira-commit`'s deployment artifacts, not present before this change.

## Assumptions (operator to confirm or amend)

- **D1 — Dot separator in the label value.** The label is written with a
  literal period (`refine-ai-flow-v1.14`), matching how `artifact-version` is
  already written elsewhere in this repo's frontmatter. Jira Cloud's label
  validation rules for this character are not verified here (no live
  instance to check against). Amendment path: if the target Jira instance's
  label validation rejects periods, substitute an underscore
  (`refine-ai-flow-v1_14`) in the `mandatory_labels` rule at instantiation —
  a separator swap only, no other logic change.
- **D2 — "Version" means the flowspace's `artifact-version`, resolved at the
  time the executing adapter was generated.** The deployed Rovo agent or
  Copilot prompt bakes in whatever `HUB.md` version was current when that
  adapter was last regenerated (mirroring how adapters already carry a
  "generated from spec version" stamp) — it is not a live lookup at commit
  time. Amendment path: if drift between a deployed adapter's baked-in
  version and `HUB.md`'s latest version becomes a practical problem, a live
  resolution mechanism would need designing — not built here.
- **D3 — This replaces `refine-ai-built` in every artifact, with no
  transition period.** No item previously committed under the old label gets
  retroactively relabeled by this change — this decision governs new
  commits going forward only, consistent with how prior label amendments in
  this flowspace were scoped.

## Files intentionally not touched

`decision-log/2026-07-15-provenance-and-planning-labels.md` — append-only
historical record of the original `mandatory_labels` introduction; it
correctly describes the label as it was defined at that time and is left as
literal history, not edited to match the current rule.
