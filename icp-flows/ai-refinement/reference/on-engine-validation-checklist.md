---
id: ai-refinement-on-engine-validation-checklist
title: "On-Engine Validation Checklist — AI Refinement"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[work-item-schemas]]"
---

# On-Engine Validation Checklist — AI Refinement

**Status: prepared, not executed.** The flowspace has exactly one on-engine
run to date (Rovo, NEADD-1827, a `spike`), which surfaced five defects since
fixed in spec. Every fix, and every capability added since (communication
style enforcement, the broadened input taxonomy, the domain-configurable
stakeholder register, and fast-track mode) has only been validated by
simulated invocation — running adapter instructions verbatim against
synthetic scenarios. None of it has been re-confirmed on a live engine. This
checklist is the operator's run sheet for closing that gap once the
Confluence instantiation and Rovo deployment
(`confluence-instantiation-guide.md`) are done.

## How to use this

Run one full pipeline (Stage 01 → Stage 06) per refinable type, in both
modes where the row says "both modes," recording pass/fail and any defect
found. A defect found here becomes a revision pass, the same pattern used for
NEADD-1827 — log it in a new decision-log entry, fix the spec, and re-run
this same row.

## Per-type run matrix

| Type | Full-interactive run | Fast-track run | Notes |
|---|---|---|---|
| `solution_epic` | [ ] | [ ] | No parent in scope (Stage 06 skips linkage) — confirm the skip is clean, not a silent no-op. |
| `feature` | [ ] | [ ] | Parent = solution epic; confirm candidate query returns real epics. |
| `story` | [ ] | [ ] | Schema is `to-review` (REC-04) — confirm `type_of_work`/`work_category` screens exist before committing. |
| `task` | [ ] | [ ] | Same schema caveat as `story`. |
| `spike` | [ ] | [ ] | Schema is `to-review`; confirm `question_to_answer`/`timebox` custom fields exist or get created per the discovery step. This is the type that already failed once (NEADD-1827) — weight this row highest. |

## Per-run check list (apply to every row above)

- [ ] **Trigger detection** — one of the three phrases fires the flow.
- [ ] **Guardrail presentation** — responsibility notice and data-safety
      prohibition both shown and acknowledged; policy link resolves (not the
      public-mirror redaction placeholder).
- [ ] **Schema loading** — Stage 01 loads the correct schema for the type,
      matching the registry field-for-field.
- [ ] **Type auto-detection** (fast-track run only) — agent's proposed type
      and rationale appear before the user's confirm/override.
- [ ] **Fast-track mode proposal** (fast-track run only) — rationale for
      which fields look extractable appears before the user's mode choice;
      full-interactive run confirms the agent defaults there absent
      structured material.
- [ ] **Stakeholder-register grounding check** — Stage 01 correctly reports
      grounded or ungrounded for the domain in use.
- [ ] **Field cadence, full-interactive** — every field walked one at a time
      with individual confirmation.
- [ ] **Field cadence, fast-track** — extracted fields appear at the
      consolidated Stage 03–05 checkpoint with source citations; unextractable
      fields fall back to one-at-a-time.
- [ ] **Hard carve-outs held in fast-track** — stakeholder sweep (Stage 02),
      coalition/conflict-axis annotation (Stage 03), and due-date elicitation
      (Stage 04) all ran interactively, not extracted — check the transcript
      directly for this; it is the one behavior most worth catching a
      regression in.
- [ ] **Communication style** — spot-check drafted text (problem statement,
      AC, dry-run preview, transition offer) reads precise/analytical/
      structured/direct, not narrative or hedged.
- [ ] **ADF format translation** — dry-run preview and the fetched-back
      committed issue both show rendered structure, zero raw Markdown
      syntax (`#`, `*`, code fences) in any field.
- [ ] **Parent mapping** — for every type except `solution_epic`, candidate
      parents were queried and presented; user's confirm/skip/create-new
      choice is explicit in the transcript; no silently-carried-forward
      hierarchy position.
- [ ] **Dependency linkage** — every Stage 03 blocking dependency appears as
      a Jira issue link post-commit.
- [ ] **Stakeholder labeling** — Stage 02/03 tags and annotations appear as
      Jira labels (or the instance's designated fields) on the committed
      issue.
- [ ] **Commit success** — issue key and URL returned; fetched-back issue
      matches the signed-off payload field-for-field aside from format
      translation.
- [ ] **Post-commit transition offer** — offered once, response (accept or
      decline) recorded, correct end state either way.

## After all rows pass

- [ ] Record the outcome of every run in
      `decision-log/` (one entry, or one per defect found and fixed).
- [ ] Update `HUB.md`'s Known gaps section to reflect a clean on-engine
      record — this is the point at which "deployment pending" and
      "on-engine validation pending" can finally be retired from that table.
- [ ] Confirm the schema-ratification gap (REC-04) separately — a clean
      on-engine run for `story`/`task`/`spike` is strong evidence toward
      ratification but the operator's explicit sign-off on
      `work-item-schemas.md`'s `to-review` status is still a distinct step.
