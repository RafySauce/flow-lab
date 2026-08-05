---
id: decision-2026-08-05-rovo-session-friction-fixes
title: "Decision Log — Rovo Session Friction Fixes"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-05
updated: 2026-08-05
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

# Decision Log — 2026-08-05 — Rovo Session Friction Fixes

**What was decided:** incorporate all eight friction points and two
resource-consumption findings from an operator-supplied retrospective on a
live Rovo Chat session (2026-08-04: one Feature created, one Task converted
to a child Spike, one duplicate cancelled) into the `ai-refinement`
flowspace, in one bundled revision pass. **By whom:** agent, on direct
operator instruction to think through the retrospective's recommendations
and apply them. **What it affects:** three new house amendments in
`reference/ai-refinement-hybrid.md` (1.6 → 1.7); `HUB.md` (1.21 → 1.22); Stage
01 (1.15 → 1.16), Stage 05 (1.6 → 1.7), and Stage 06 (1.10 → 1.11);
`reference/work-item-schemas.md` (1.6 → 1.7); a new reference file,
`reference/platform-quirks.md` (1.0); and two promoted skills, `jira-commit`
(1.10 → 1.11) and `workitem-validation` (1.3 → 1.4), both `verified` →
`to-review`, both adapters regenerated.

## The gap this closes

The retrospective's own framing is accurate: none of the eight friction
points were platform bugs the flow was powerless against — each one is a
place where the flow either had no mechanism to catch a class of error, or
had the mechanism in one file but not in the file an operator would actually
read for a summary. Grouped by root cause rather than by the retrospective's
numbering:

1. **Two Confluence access problems (retrospective §1.1, §1.2) were really
   one gap: the flow trusted metadata-level search as if it were content
   access.** CQL and title search can find a page the agent cannot read —
   different permission gates — and the flow had no annotation distinguishing
   the two, so degraded research shipped indistinguishable from verified
   research. Space-key guessing was the same class of problem one step
   earlier: assuming a human-friendly name resolves without checking.
2. **A hierarchy violation reached the Jira API instead of being caught
   before it (retrospective §1.3).** The registry already models the
   hierarchy (`work-item-schemas.md`'s `children:` lists) and Stage 06
   already queries "candidates of the appropriate parent type," but nothing
   validated the *target project's own* configured hierarchy levels before
   attempting the write — a project-configuration mismatch reached the API
   as a 500 instead of being caught as a precondition.
3. **Commit-time assumptions instead of commit-time checks, three ways
   (retrospective §1.5, §1.6, and part of §1.3).** Guessed API parameter
   names, a custom-field fallback chosen by assumption ("string type, so
   probably can't take ADF, so fold it into description") instead of by
   test, and no verification step after commit to catch either kind of
   mistake before the operator found out independently. These are one
   pattern — write first, verify never — not three unrelated defects.
4. **A structural-confirmation gap that was mostly already closed
   (retrospective §1.7).** Stage 06 already treats hierarchy linkage as a
   hard carve-out never skipped by fast-track. What was actually missing was
   narrower: `HUB.md`'s own summary of the hard carve-outs (Run procedure
   step 3) didn't list it, so an operator reading only the hub's summary
   would not know the carve-out existed. A drift-fix, not a new mechanism.
5. **No budget signal for a resource the flow already consumes heavily
   (retrospective §2.3, §2.4).** The flow has no shortage of heavy,
   multi-turn stages; it had no point anywhere that surfaced consumption
   against the platform's actual limit or offered a way to hand off before
   hitting it.
6. **Platform-specific execution quirks with nowhere to live (retrospective
   §1.4, §1.5's illustrative examples, and part of §5).** State volatility
   and tool-inventory churn aren't flow-design problems — they're engine
   behavior the flow should route around — but the flow had no reference
   file distinct from its behavioral amendments where that kind of
   platform-specific, likely-to-recur evidence could accumulate.

## Design decisions

1. **Three house amendments, not six or ten.** The retrospective's ten
   recommendations map to three coherent behavioral rules, not ten
   mechanisms: `content_access_verification` bundles space-key resolution
   and the access-confidence tag because both are Stage 01 supporting-context
   research problems; `commit_boundary_hardening` bundles API preflight,
   hierarchy validation, field-capability testing, and the post-commit audit
   because all four are "verify before/after the Stage 06 write, don't
   assume" instances of the same discipline; `session_budget_checkpoint`
   stands alone because it's the only one that isn't a per-item correctness
   check. This follows the existing amendment granularity —
   `bulk_creation_acknowledgment` and `supporting_context_research` each
   already bundle several sub-behaviors under one named rule — rather than
   fragmenting into many single-purpose amendments that would be harder to
   cite consistently across six stage contracts and two skill specs.
2. **`research_confidence` is a disclosure at Stage 05, not a gate.** An
   `excerpt-only` or `inaccessible` document backing a required field does
   not halt validation — it's named in the report. The alternative (halting)
   would make degraded-but-real research access strictly worse than no
   access at all (which the flow already handles via the context prompt and
   pasted content), which is backwards: the operator asked for the gap to be
   *visible*, not for the run to be blocked by something the agent has no
   control over.
3. **Hierarchy validation is a new precondition on an existing carve-out, not
   a new carve-out.** `parent_mapping_confirmation` already required
   explicit user confirmation before any parent-link write; this pass adds a
   check the agent runs *before* presenting that confirmation, so the
   candidates and alternatives the user sees are already known-valid rather
   than something the API might reject after approval.
4. **Field-capability testing replaces an assumption with a tested fallback
   order, not a new field type.** The registry's required-field list is
   unchanged; what changes is that "fold it into description" becomes the
   last-resort outcome of testing ADF and plain text first, rather than the
   first thing tried because a field's metadata looked ambiguous. This is
   the direct fix for the retrospective's most severe finding (§1.6): a
   Feature committed with structured content silently absorbed into
   `description`, undetected until manual review.
5. **The post-commit field audit is universal, not bulk-mode-only.** Bulk
   mode already had post-creation parent validation (existing step 7a,
   2026-07-31); the new field audit (7b) applies the same "verify what
   actually landed" discipline to every commit, single-item included, since
   the retrospective's defect happened in a single-item run.
6. **A dedicated platform-quirks file, kept separate from the behavioral
   amendment it evidences.** `commit_boundary_hardening`'s `api_preflight`
   rule doesn't change based on which specific parameter names a platform
   uses — the rule is "read the stub first," full stop. The concrete
   misfires (`project_ids` vs. `project_id_or_key`, and so on) are evidence
   for why the rule exists and a running log for future sessions, not part
   of the rule itself, so they live in the new `reference/platform-quirks.md`
   rather than growing the amendment's own text indefinitely as more quirks
   are found.
7. **The session-budget checkpoint is advisory, matching every other mode
   choice in this flow.** No hard stop at 70% — a warn-and-offer, because
   the flow's whole method is "the operator decides at every boundary," and
   a token-budget estimate is exactly the kind of imprecise signal that
   should inform a human choice rather than force one.
8. **`context-elicitation`, `scope-dependency-mapper`, `field-refinement-cadence`,
   `value-decomposition`, and `bulk-child-creation` are untouched.**
   `research_confidence` rides forward on Stage 01's existing document-set
   output; none of these five skills' own methods needed to change to carry
   it. Keeping the touched surface to exactly the two skills whose Method
   steps actually changed (`jira-commit`, `workitem-validation`) avoids
   demoting artifacts that didn't change.

## Truth-level movements

- `HUB.md`, Stage 01, Stage 05, Stage 06, `jira-commit`, and
  `workitem-validation` drop `verified` → `to-review` — each had a real
  content change in this pass, logged rather than assumed clean, matching
  every prior gap-closure cycle.
- `reference/ai-refinement-hybrid.md` and `reference/work-item-schemas.md`
  were already `to-review` (pending the standing schema-ratification gap);
  they stay there with this pass's content folded in.
- `reference/platform-quirks.md` is a new file, emitted at `to-review` per
  `AGENTS.md` rule 4 — never `verified` on creation.
- Stages 02, 03, 04 and their skills (`context-elicitation`,
  `scope-dependency-mapper`, `field-refinement-cadence`), plus
  `value-decomposition` and `bulk-child-creation`, are unaffected and keep
  their 2026-08-01 gate status.

## Remaining for the operator (the human gate)

1. **Run the Rovo re-gate this pass reopens.** The 2026-08-01 gate closure
   covered the flow as it stood then; `jira-commit` and `workitem-validation`
   in particular need a fresh confirmed live run before returning to
   `verified` — none of this pass's changes have run on-engine.
2. **Confirm the `session_budget_checkpoint` threshold (70%) and handoff
   shape are acceptable**, or adjust — the figure is a starting point drawn
   from the retrospective's own consumption estimate (110,000–140,000 of
   200,000 tokens for a single-Feature session), not a derived value.
3. **Decide whether `reference/platform-quirks.md` should grow a Copilot
   section** once a Copilot adapter has its own live invocation — it
   currently documents Rovo-only observations.
4. **Ratify `commit_boundary_hardening`'s hierarchy-validation and
   field-capability-testing disciplines against a real target project**, the
   same way the schema-ratification gap already asks for the `story`/`task`/
   `spike` field sets — this pass specifies the mechanism but has not
   confirmed it against an actual Jira project's hierarchy configuration or
   custom-field behavior.
