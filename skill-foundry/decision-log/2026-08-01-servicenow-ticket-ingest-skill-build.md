---
id: decision-2026-08-01-servicenow-ticket-ingest-skill-build
title: "Decision Log — servicenow-ticket-ingest Skill Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related:
  - "[[servicenow-ticket-ingest]]"
  - "[[sp-servicenow-ticket-ingest]]"
  - "[[statik-adoption]]"
  - "[[board-evidence-requirements]]"
  - "[[jira-portfolio-ingest]]"
---

# Decision Log — 2026-08-01 — servicenow-ticket-ingest Skill Build

**What was decided:** build `servicenow-ticket-ingest` from the primer brief
filed the same day the ServiceNow gap was designed into `statik-adoption`
(`sp-servicenow-ticket-ingest.md`), and stage it in `review-skills/` at
`truth-level: to-review`. **By whom:** agent, on direct operator instruction
— asked whether a ServiceNow-tracked service was coming up soon enough to
warrant building now, the operator said yes, build it. **Triage
classification:** skill-primer-brief — clean path. The brief was
crystallized at flowspace design time (Method sketch, field mapping, known
failure modes, definition of done all already written); this pass transcribed
it into the spec rather than re-opening the design questions the brief had
already settled.

## Build decisions

1. **Structural mirror of `jira-portfolio-ingest`, not a divergent design.**
   The primer brief said so explicitly ("mirrors jira-portfolio-ingest's
   method, substituting ServiceNow's shape"), and the flowspace's own
   `board-evidence-requirements.md` §1 parity contract requires it: Stage 01
   must be able to bind either ticketing system without Stages 03–05 ever
   branching on which. The spec's Method steps (scope → framing → bind →
   screen → count → field map → hard requirements → availability report →
   denominator → normalize → history inventory → confirm) track
   `jira-portfolio-ingest`'s numbering one-for-one, substituting ServiceNow's
   binding mechanics at each step.

2. **No connected-space/ART-board discovery carried over.**
   `jira-portfolio-ingest` v1.1 added ART-board connected-space discovery
   (grouping `Parent key` by project prefix, resolving off-project parents).
   Neither the primer brief nor `board-evidence-requirements.md` establishes
   a ServiceNow analog to a Jira ART-board portfolio/solution-epic hierarchy,
   and inventing one would be minting structure the brief never asked for
   (`AGENTS.md` rule 7). Left out; noted in the spec's Changelog as a
   deliberate omission, not an oversight, so a future reviewer doesn't read
   the absence as a gap.

3. **`Updated` field mapping gap, filled during build.** The flow's shared
   hard-requirement set (Issue key, Summary, Status, Created, Updated) —
   inherited verbatim from `jira-portfolio-ingest`'s own five, per the
   primer brief's step 6 — has no representative ServiceNow column in
   `board-evidence-requirements.md` §7's mapping table as filed. ServiceNow's
   `sys_updated_on` (a standard audit field present on every table, the
   direct analog of Jira's `Updated`) fills it. This is a small, well-
   grounded addition to complete a mapping table the brief's own step 6
   already depended on being complete — flagged here and in
   `board-evidence-requirements.md` §7 itself, not silently patched.
   `board-evidence-requirements.md` bumped 1.1 → 1.2.

4. **Completion denominator carried forward for shape parity, not because
   statik-adoption scores on it.** The primer brief's step 8 says to emit
   the denominator "in the identical shape jira-portfolio-ingest produces."
   Taken literally: the spec computes it exactly as
   `jira-portfolio-ingest` v1.2 now does (count of resolved canonical
   fields, not raw column count — see
   `2026-08-01-portfolio-rationalization-gap-ratifications.md`), and states
   plainly that no statik-adoption stage currently reads it as a scoring
   input the way `portfolio-rationalization`'s close-score model does. An
   unused-but-correctly-shaped output is preferable to a shape mismatch that
   would force Stage 01 to branch on source system later.

5. **History inventory as its own step, not folded into the
   field-availability report.** The primer brief and
   `board-evidence-requirements.md` §4 both insist a complete
   field-availability report says nothing about whether transition history
   exists — the two are checked and reported separately in Jira too. Step 11
   keeps that separation and records one of three named states (full
   transition history / created and resolved only / not checked), plus the
   reopened-incident limitation the primer brief calls out as a known
   failure mode.

6. **Adapters add format, not logic.** Both are mechanical translations of
   the twelve Method steps, matching `jira-portfolio-ingest`'s adapter
   pattern: Rovo carries native ServiceNow search/read actions where
   sanctioned; Copilot's primary path is export mode with live mode gated
   on a confirmed sanctioned integration, exactly as `jira-portfolio-ingest`'s
   Copilot adapter gates Jira live mode.

7. **Collision check, run at authoring time.** One close neighbor:
   `jira-portfolio-ingest` — disjoint by source system, identical by output
   shape and trust-boundary discipline, cross-referenced in both specs'
   boundary sections ("Not the Jira/ServiceNow path"). One inherited,
   deliberately unresolved boundary: the deferred `sp-servicenow-kb-commit`
   write path is named explicitly in the triggering intent's near-miss list
   so a write-shaped request routes to a decline, not to this skill and not
   silently onward — that brief remains deferred, untouched by this build.

## Five-point gate — status

Run in full this session as part of the same pass — see the companion
promotion entry, `2026-08-01-servicenow-ticket-ingest-skill-promotion.md`.

## Notes

- This is a design-time build on public design copy — no real ServiceNow
  data entered this repo.
- No on-engine invocation exists for this skill. The sanctioned ServiceNow
  read connector is not yet confirmed against any specific engine — the spec
  and both adapters state this plainly and gate the live-mode path on that
  confirmation, matching the discipline `sp-servicenow-ticket-ingest.md`
  itself specified.
