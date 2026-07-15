---
id: ai-refinement-stage-05
title: "Stage 05 — Validation & Formatting"
type: stage-context
stage: 5
review-intensity: light
artifact-version: "1.4"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.1"
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[workitem-validation]]"
---

# Stage 05 — Validation & Formatting

## Inputs

| Input | Source | Required |
|---|---|---|
| Complete set of refined field values | Stage 04 | Yes |
| Work item schema (required/optional fields) | Stage 01 | Yes |
| Formatting rules (no bold, no emojis) | `../reference/ai-refinement-hybrid.md` | Yes |
| Active persona contract (communication_style binding) | Stage 01 | Yes |
| Selected mode (fast-track / full-interactive) | Stage 01 | Yes |
| Cross-field conflict report (if any) | Stage 04 | If exists |
| Resolved team_code + session planning quarter | Stage 01 | Yes |

## Process

`Layer-3: workitem-validation` (skill spec in
`produced-skills/workitem-validation/`, `to-review` as of 1.2 — mandatory-label
check added, gate re-run owed)

1. **Completeness scan** — walk the schema's required-field list and confirm every field has a non-empty value.
2. **Mandatory label check** — distinct from schema completeness (labels are
   not schema fields, per `../reference/work-item-schemas.md`'s cross-cutting
   note): `refine-ai-built` must be present for every type; for `feature`,
   `story`, `task`, `spike`, `bug` the `<team_code>-<yyyy>-q<n>` planning
   label resolved at Stage 01 must also be present and well-formed
   (`portfolio_epic`/`solution_epic` are exempt from this second check). This
   check is a warn-and-bypass, not a hard halt (see step 4) — the one check
   in this gate that isn't a stop.
3. **Constraint validation** — check each field against its constraints:
   - Summary ≤ 10 words
   - AC starters match approved patterns
   - Due date is a valid future date
   - Dependencies reference real items (if Jira-linked)
   - Spike only: question_to_answer is a single question; timebox states an
     explicit bound closing on or before the due date
     (`../reference/work-item-schemas.md`, extension field definitions)
   - **Communication style** — drafted field text (problem statement,
     acceptance criteria, value statements, any free-text field) reads as
     precise, analytical, structured, and direct, per the persona's
     `communication_style` house amendment
     (`../reference/ai-refinement-hybrid.md`). Verbose, narrative, hedging, or
     informal phrasing is a constraint violation, not a style preference —
     flag it the same as a missing AC starter.
4. **Formatting pass** — apply the `no_bold`, `no_emojis` rules:
   - Strip `**bold**` markers
   - Remove emoji characters
   - Normalize whitespace and list formatting
5. **Auto-correct vs. halt vs. warn-bypass decision tree**:
   - **Auto-correct**: formatting violations, minor whitespace — fix silently and note in report.
   - **Halt**: missing required fields, constraint violations, unresolved cross-field conflicts — present to user for resolution, no fix attempted.
   - **Warn-and-bypass**: a missing or malformed mandatory label (step 2) — present the specific defect (which label, why it's malformed) and let the user either fix it (an updated Stage 01 resolution or a Stage 06 override) or explicitly accept the bypass and proceed. A bypass is always recorded in the validation report as a named exception — never a silent pass. This tier exists only for the mandatory-label check; nothing else moves into it without a spec amendment. When in doubt between halt and auto-correct, halt.
6. **Validation report** — produce a structured pass/fail report for user review, naming any accepted mandatory-label bypass explicitly.
7. **User sign-off** — user confirms the validated, formatted work item is ready for Jira commit.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Validated + formatted work item payload | Stage 06 | Key-value pairs (clean) |
| Validation report (incl. any named label bypass) | User / run decision log | Structured pass/fail |
| User sign-off confirmation | Stage 06 | Boolean |

## Verify

Cross-stage trace: the validated payload's field set must equal Stage 04's
refined field set (no field added, dropped, or content-changed by the
formatting pass — formatting alters markup only), and every required field in
the Stage 01 schema must appear in the payload — the failure this catches is
the validator silently rewriting content or a required field lost between
stages. Running this check leaves a one-line result in the run's decision log.

- [ ] Every required field passes completeness check
- [ ] All constraints pass (summary length, AC format, date validity,
      communication_style)
- [ ] No bold or emoji characters remain in any field
- [ ] Auto-corrections are logged in the validation report and touch formatting only
- [ ] Any halt-level issues were surfaced and resolved with the user
- [ ] `refine-ai-built` presence was checked for the item; for
      `feature`/`story`/`task`/`spike`/`bug`, the `<team_code>-<yyyy>-q<n>`
      planning label's presence and well-formedness were also checked
- [ ] Any missing/malformed mandatory label produced a warn-and-bypass, never
      a silent pass — and any accepted bypass is named in the report with its
      specific defect
- [ ] User explicitly signed off on the final payload

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — validation is largely mechanical; review confirms the
  report is accurate.
- **Evidence:** the validation report itself plus a one-line entry in the run's
  decision log.

**Fast-track consolidation (canonical definition).** In fast-track mode,
Stages 03, 04, and 05 do not each get their own light-review pass. Instead,
one consolidated draft-and-review checkpoint — presented here, at the end of
Stage 05 — covers all three together: the confirmed scope/dependency package
(Stage 03), the complete field set with source citations for anything
extracted (Stage 04), and this stage's validation report. The user reviews
and confirms (or edits) the combined package once, rather than three times.
This consolidation applies **only** to Stages 03–05. It never reaches into
Stage 02 (heavy, always its own checkpoint — see Stage 02's Review section)
or Stage 06 (heavy, always its own checkpoint — see Stage 06's Review
section), and it never substitutes for the hard carve-outs that stay
interactive regardless of mode: Stage 02's stakeholder sweep, Stage 03's
coalition/conflict-axis annotation, Stage 04's due-date elicitation, and
Stage 06's parent-mapping confirmation. In full-interactive mode, Stages
03–05 keep their own separate light-review passes as described in each
stage's own Review section.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- Validated payload is `internal` — ready for Jira but not for external sharing.
- Validation report may reference field values — same `internal` classification.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
