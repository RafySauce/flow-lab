---
id: decision-2026-07-07-portfolio-epic-and-bug-type-extension
title: "Decision Log — Portfolio Epic and Bug Type Extension"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-07
updated: 2026-07-07
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[work-item-schemas]]"
---

# Decision Log — 2026-07-07 — Portfolio Epic and Bug Type Extension

**What was decided:** bring `portfolio_epic` into the refinable set as the new
top of the hierarchy (parent of `solution_epic`), reversing the 2026-07-03
out-of-scope call, and house-author a `bug` schema as a new peer of
`story`/`task`/`spike` under `feature`. **By whom:** agent, on operator
instruction ("add the portfolio epic work item type which sits above solution
epic and the bug item type which is a peer to tasks and stories"); all new
artifacts emitted at `to-review` — nothing promoted. **What it affects:**
`reference/work-item-schemas.md` (1.1 → 1.2), `HUB.md` (1.9 → 1.10), Stages
01/02/03/06 `CONTEXT.md`, `reference/on-engine-validation-checklist.md`, and
the `jira-commit`, `context-elicitation`, `scope-dependency-mapper`, and
`field-refinement-cadence` skill specs and their adapters.

## The change

1. **`portfolio_epic` becomes refinable.** The hierarchy string
   (Portfolio Epic → Solution Epic → Feature → …) always named it, but the
   2026-07-03 schema-extension decision put it out of scope, reasoning it was
   "Portfolio-level investment case, owned by Portfolio & Sourcing processes"
   and outside the TPSO persona's remit. That reasoning is not wrong on its
   own terms, but the operator has now explicitly asked for portfolio-epic
   refinement, which supersedes it. `portfolio_epic`'s schema mirrors
   `solution_epic`'s field-for-field (see `work-item-schemas.md` derivation
   rule 6) — same outcome-level framing, one hierarchy level higher —
   and its only child is `solution_epic`.
2. **`bug` is added as a house-authored peer of `story`/`task`/`spike`.**
   Unlike `portfolio_epic`, `bug` was never named anywhere in the source
   clipping's hierarchy or schemas — it is a pure house addition. Its field
   set follows the same derivation-rule discipline as the original
   `story`/`task`/`spike` extension: pipeline invariants
   (`summary`/`customer_business_value`/`acceptance_criteria`/`due_date`)
   stay required; `type_of_work`/`work_category` are required because every
   refinable type traverses the Jira board workflow (rule 5); and its scope
   contract is a reproduction triad (`steps_to_reproduce`, `expected_result`,
   `actual_result`) plus `severity`, not `in_scope`/`out_of_scope` — the same
   pattern `spike` established for a type whose bounds aren't a scope
   statement (rule 4/7). `environment` is optional: not every bug report
   captures it, and its absence shouldn't block refinement.

## Decisions and alternatives

1. **`feature.children` gains `bug` in the registry, not the clipping.** The
   clipping (`ai-refinement-hybrid.md`) is `claimed` foreign material
   preserved as-is; its own ingest note says content through `## Triggers` is
   "unchanged since ingest." Editing its `feature.children` list to add `bug`
   would violate that preservation rule. Instead, `work-item-schemas.md`
   (already the house extension surface, already transcribing the clipping's
   `feature` schema) carries the divergence explicitly, with a code comment
   and a prose note in its authority-split paragraph flagging that this one
   list item — not the field lists — no longer follows "clipping wins on
   divergence." *Alternative considered:* amend the clipping's House
   Amendments section instead (the mechanism used for the five NEADD-1827
   behavioral rules) — rejected: House Amendments are operational rules
   discovered through on-engine use, not new type/taxonomy additions; folding
   a schema change into that section would blur two different kinds of
   extension the file currently keeps legible as separate.
2. **`portfolio_epic.children: [solution_epic]` reshapes Stage 06 hierarchy
   linkage.** Previously `solution_epic` was "top of the refinable set — no
   parent within scope" and `portfolio_epic` was excluded entirely. Now
   `portfolio_epic` takes the no-parent position and `solution_epic` gains a
   parent to resolve (query candidate portfolio epics, confirm/skip/create-new
   — same mechanism already used for feature→solution-epic and
   story/task/spike/bug→feature). *Alternative considered:* leave
   `solution_epic` parent-less and treat `portfolio_epic` as a label-only
   grouping outside the linkage mechanism — rejected: it would make
   `portfolio_epic` refinable in name only, since nothing would ever link a
   committed solution epic back up to it, defeating the purpose of adding the
   type.
3. **Downstream skill specs (`jira-commit`, `context-elicitation`,
   `scope-dependency-mapper`, `field-refinement-cadence`) are edited, not left
   generic.** Unlike the 2026-07-03 extension (where all five skills read "the
   schema from Stage 01" generically and needed no edits), three of these four
   specs hardcode type names in prose: `jira-commit`'s parent-mapping
   exception list and custom-field enumeration, `context-elicitation`'s
   business-outcomes conditional, and `scope-dependency-mapper`'s
   risks-optional conditional. Each was updated to match the new type set;
   `field-refinement-cadence`'s cross-field conflict check (the
   `type_of_work`/`work_category` type list) was extended to include `bug`.
   These four move from `truth-level: verified` to `to-review` as a result —
   consistent with how `ai-refinement-hybrid.md` moved from `claimed` to
   `to-review` when it gained substantive new content beyond its original
   gate. **Follow-up owed:** a five-point gate re-run (spec review, simulated
   live test per adapter, trigger check, collision check) before these four
   return to `verified`; not performed as part of this change — this is an
   honest gap, not a simulated pass, unlike the precedent set by
   `jira-commit` 1.2–1.4's "pre-gate evidence re-run" changelog entries, which
   this decision deliberately does not fabricate.
4. **`bug`'s severity field is a closed set** (`blocker | critical | major |
   minor`), matching common Jira defect-triage conventions, rather than a free
   text field — consistent with `work_category`/`type_of_work` already being
   board-configuration-driven closed-ish vocabularies for other types.
   Amendment path: confirm against the real Jira project's actual severity
   scheme at instantiation (per `jira-commit`'s per-instance field-discovery
   step) and adjust the enum, not the field's required-ness.

## Assumptions (operator to confirm or amend)

- **C1 — `portfolio_epic` reuses `solution_epic`'s field set exactly**,
  including `dependencies` as a required text field. Amendment path: if the
  real portfolio-management process tracks dependencies differently (e.g., a
  separate investment-planning tool), drop the field and route dependency
  awareness through Stage 03's classification only, mirroring rule 3's
  treatment of every non-`solution_epic`/`portfolio_epic` type.
- **C2 — `bug` carries `customer_business_value`** despite defects often being
  framed as "fix this," not "here's the value." Kept for pipeline-invariant
  consistency (derivation rule 1) and because the persona's
  `enforce_measurable_outcomes` behavior applies to every refinable type; if
  this proves to be friction in practice (bugs are usually self-evidently
  worth fixing), the amendment path is a lighter elicitation prompt for this
  one field on this one type, not dropping the field.
- **C3 — `severity`'s four-value enum** (B1 in the earlier extension's
  numbering scheme continues as C3 here) is a best-guess default; confirm
  against the target Jira project's actual severity field values (some
  instances use five levels, some use P0–P4) at instantiation.
- **C4 — Downstream skill spec truth-level demotion (decision 3)** is itself
  an assumption the operator should ratify or override: an alternative is to
  keep those four specs at `verified` and treat this as a documentation-only
  update on the theory that the type-conditional prose changes are additive,
  not behavior-altering, for the already-verified types. This log takes the
  more conservative position (demote, log the gate re-run as owed) but flags
  it as reversible if the operator judges the risk differently.
