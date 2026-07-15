---
id: ai-refinement-stage-01
title: "Stage 01 — Intake & Guardrails"
type: stage-context
stage: 1
review-intensity: heavy
artifact-version: "1.8"
status: living
truth-level: verified
created: 2026-07-03
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.1"
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
  - "[[work-item-schemas]]"
  - "[[platform-stakeholder-register]]"
---

# Stage 01 — Intake & Guardrails

## Inputs

| Input | Source | Required |
|---|---|---|
| Trigger phrase ("Run AI Refinement", "Start Refinement", "I want to refine") | User | Yes |
| Work item type (agent-proposed from source material when available, otherwise user-selected) | User + agent | Yes |
| Guardrails, persona contract, field definitions, house amendments | `../reference/ai-refinement-hybrid.md` | Yes |
| Work-item schema registry (refinable set + out-of-scope types) | `../reference/work-item-schemas.md` | Yes |
| Source material (see HUB "Common source inputs" — email request, vendor action notice, meeting minutes/notes, chat-stated requirement, structured requirements document, incident/problem record, architecture/design artifact, or unclassified) | User | No |
| Stakeholder register, if one is loaded for this domain | `../reference/platform-stakeholder-register.md` or a domain instance of `platform-stakeholder-register-template.md` | No |
| Existing Jira labels for the target project/space (live query, for team_code inference) | Jira (via native lookup) | Yes |

## Process

`Layer-3: inline (one-off — the guardrail and persona content below is
transcribed from ../reference/ai-refinement-hybrid.md; the schema bullets
transcribe ../reference/work-item-schemas.md, the registry that completes the
refinable set. All of it is specific to this flowspace)`

1. **Trigger detection** — recognize one of the defined trigger phrases.
2. **Responsibility acknowledgment** — present the responsibility notice and obtain explicit user confirmation:
   > "You, the user, are responsible for the output of this process and committing to the work it produces."
   > Policy reference: `<internal policy link — set at instantiation; redacted from this public design copy>`
3. **Data safety reminder** — state the PII / confidential-data prohibition.
   If the user brings source material, identify which common input type it is
   (HUB "Common source inputs" — now eight types, including structured
   requirements documents, incident/problem records, architecture/design
   artifacts, and a catch-all "unclassified document" row) and screen it
   before it enters the session: emails and meeting minutes routinely carry
   names and addresses — have the user strip them; vendor material and
   third-party SOWs are external — confirm safe to ingest at data-class
   `internal`; an unclassified document gets the strictest screen of the set
   (assume it may carry names, credentials, or confidential terms until
   checked) before it is typed further.
4. **Persona activation** — load the `technical_product_service_owner` persona with its four behaviors:
   - Prioritize business and operational value
   - Identify risks and dependencies
   - Challenge incomplete requirements
   - Enforce measurable outcomes

   Also load the persona's `communication_style` — precise, analytical,
   structured, direct — and state plainly that it is binding, not
   descriptive, on every user-facing output this session produces at every
   stage (questions, pushback, drafts, previews, reports), per
   `../reference/ai-refinement-hybrid.md`'s House Amendment
   `communication_style_enforcement`.
5. **Work item type selection** — if source material is available, propose a
   work-item type with a stated rationale (which content in the document
   reads as a portfolio epic's enterprise-wide strategic goal — potentially
   spanning organizations and years, containing solution epics rather than
   features directly — a solution epic's narrower outcome-level framing, a
   feature's scoped capability, a story/task's execution-shaped ask, a
   spike's open question, or a bug's reported defect); the user confirms or
   overrides. Without source material, ask the user directly. Load the
   corresponding schema from the registry at `../reference/work-item-schemas.md`
   (for `solution_epic` and `feature` the registry transcribes
   `../reference/ai-refinement-hybrid.md`, which stays authoritative on any
   divergence):
   - `portfolio_epic` → children: solution_epic; required fields: summary, problem_statement, business_outcomes, customer_business_value, in_scope, out_of_scope, dependencies, acceptance_criteria, due_date; optional: risks — same required-field set as `solution_epic`, one hierarchy level up
   - `solution_epic` → children: feature; required fields: summary, problem_statement, business_outcomes, customer_business_value, in_scope, out_of_scope, dependencies, acceptance_criteria, due_date; optional: risks
   - `feature` → children: story, task, spike, bug; required fields: summary, customer_business_value, in_scope, out_of_scope, acceptance_criteria, type_of_work, work_category, due_date
   - `story` → children: sub_task; required fields: summary, customer_business_value, in_scope, out_of_scope, acceptance_criteria, type_of_work, work_category, due_date
   - `task` → children: sub_task; required fields: summary, customer_business_value, in_scope, out_of_scope, acceptance_criteria, type_of_work, work_category, due_date
   - `spike` → children: sub_task; required fields: summary, question_to_answer, timebox, customer_business_value, acceptance_criteria, type_of_work, work_category, due_date
   - `bug` → children: sub_task; required fields: summary, description, customer_business_value, acceptance_criteria, type_of_work, work_category, due_date — `description` carries steps to reproduce, expected result, actual result, and (where known) severity and environment as prose, not as separate fields (see the registry's Extension field definitions)

   If the user asks for a `sub_task`, redirect per the registry's out-of-scope
   table (sub-tasks are created directly in Jira under an already-committed
   parent) — that type alone stays out of this pipeline.
6. **Provenance and planning-label resolution** — every committed item
   carries `refine-ai-built`; items at feature level and below (`feature`,
   `story`, `task`, `spike`, `bug`) additionally carry a
   `<team_code>-<yyyy>-q<n>` planning label (`portfolio_epic`/`solution_epic`
   are exempt from this second label's gate — multi-year/multi-quarter
   outcome horizon — though one may still be attached if the user volunteers
   a quarter for them). Resolve both pieces of the planning label here, once
   per session:
   - **team_code** — query the target Jira project/space live for existing
     labels matching (or closely resembling — different separator, casing)
     the `<code>-<yyyy>-q<n>` shape. One distinct code found: propose it,
     citing the matching labels as rationale. Multiple distinct codes found:
     present all as candidates. None found: ask the user directly. In every
     case the user confirms the proposed code or supplies a different one
     explicitly — never silently accepted from the query.
   - **planning quarter** — ask directly: "What quarter do you plan to do
     this work?" Normalize free-text answers ("Q4 2026", "next quarter") to
     the canonical `<yyyy>-q<n>` form. Applies to every gated item in the
     session by default; Stage 06 offers a per-item override at its dry-run
     preview for an item that targets a different quarter.

   This is the flowspace's `mandatory_labels` house amendment
   (`../reference/ai-refinement-hybrid.md`).
7. **Fast-track assessment** — assess whether the available source material is
   detailed and structured enough to populate most of the selected type's
   required fields with reasonable confidence. If so, propose **fast-track
   mode** with a stated rationale: which fields look extractable and from
   where in the document. The user chooses fast-track or full-interactive;
   the user may force full-interactive regardless of the agent's assessment,
   and nothing below ever infers this choice on the user's behalf. Absent
   source material, or when the agent's confidence is low, default to
   full-interactive and say so. Fast-track never changes what gets checked —
   only how many fields are elicited one at a time versus drafted from the
   document and presented together (Stages 02–05 detail the mode's effect
   per step; due-date elicitation and Stage 06 parent-mapping confirmation
   stay interactive in every mode, without exception).
8. **Stakeholder-register grounding check** — confirm whether a stakeholder
   register is loaded for this domain (`../reference/platform-stakeholder-register.md`
   or a domain instance of `platform-stakeholder-register-template.md`). If
   none is loaded, flag **ungrounded mode**: Stage 02's stakeholder sweep and
   Stage 03's coalition/conflict-axis annotation ask the user directly who is
   affected and what tensions apply, instead of walking a register — a
   degraded but functional path, not a blocked one.
9. **Confirm setup** — echo back: persona active (communication_style
   binding), item type selected (+ rationale, if agent-proposed), mode
   selected (fast-track or full-interactive, + rationale), stakeholder-register
   grounding status, guardrails in effect, resolved team_code and planning
   quarter (or the exemption, if the selected type is `portfolio_epic` or
   `solution_epic`). Obtain user "proceed" before advancing.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Acknowledged responsibility flag | Stage 02 | boolean |
| Selected work item type + loaded schema (+ agent rationale, if proposed) | Stages 02–06 | YAML schema reference + text |
| Active persona contract (communication_style binding) | Stages 02–06 | persona object |
| Screened source material + input-type tag (when provided) | Stage 02 | text + type tag |
| Selected mode (fast-track / full-interactive) + rationale | Stages 02–06 | text |
| Stakeholder-register grounding status (grounded / ungrounded) | Stages 02, 03 | boolean + register reference |
| Resolved team_code (+ query rationale) | Stage 06 | text |
| Resolved planning quarter (session default) | Stage 06 | text (`<yyyy>-q<n>`) |

## Verify

Cross-stage trace: the schema Stage 01 hands forward is the schema Stages 02–06
consume. Check that the loaded schema's required-field list matches the selected
work-item type's entry in `../reference/work-item-schemas.md` field-for-field —
and, for `solution_epic` and `feature`, that the registry entry still matches
`../reference/ai-refinement-hybrid.md` (the clipping is authoritative for those
two; a divergence is a registry defect, not a schema change). The failure this
catches is a downstream stage refining against a stale or wrong-type schema.
Running this check leaves a one-line result in the run's decision log.

- [ ] Trigger phrase was matched
- [ ] Responsibility notice was displayed and explicitly acknowledged
- [ ] Data safety prohibition was stated
- [ ] Persona contract is active (all four behaviors loaded) and
      communication_style was stated as binding, not descriptive
- [ ] Work item type is selected and its schema matches the registry (and the
      clipping, for the two source-defined types); out-of-scope types were
      redirected, not refined; if agent-proposed, the rationale is in the
      transcript and the user's confirm/override is recorded
- [ ] Any source material was typed against the HUB input taxonomy (all eight
      types, including the unclassified catch-all) and screened
      (names/addresses stripped; third-party material vetted) before advancing
- [ ] If fast-track was proposed, the rationale (which fields, from where) is
      in the transcript and the user's mode choice (fast-track or
      full-interactive) is explicit — never assumed
- [ ] Stakeholder-register availability was checked and the grounding status
      (grounded / ungrounded) recorded for Stages 02–03
- [ ] team_code was resolved via live query with explicit user confirmation
      (or a direct ask, if the query found no candidates) — never silently
      assumed from the query or carried forward from a prior session
- [ ] Planning quarter was elicited once, normalized to `<yyyy>-q<n>`, and
      recorded for Stage 06 (or the type's exemption was recorded, for
      `portfolio_epic`/`solution_epic`)
- [ ] User confirmed "proceed"

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy — this is the session's trust boundary; a missed
  guardrail propagates to every downstream stage.
- **Evidence:** setup confirmation echoed in the session and a one-line entry in
  the run's decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- No PII or confidential data enters the session at this stage; if it appears,
  halt per the data-safety guardrail.
- Team-code inference queries the target Jira project/space live (read-only
  label search) via the engine's native Jira capabilities — the same access
  class Stage 06 already uses for parent-candidate queries; no write action
  occurs at this stage.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
