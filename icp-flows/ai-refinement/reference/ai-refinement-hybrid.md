---
id: ai-refinement-hybrid
title: "AI Refinement — Hybrid Definition (Markdown + YAML)"
type: clipping
artifact-version: "1.2"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-15
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
---

> **Ingest note (house):** foreign starter for the `ai-refinement` flowspace,
> uploaded by the operator and captured as-is per the clipping convention —
> except that one internal Confluence URL (the responsibility-notice policy
> link) is redacted below for public-repo safety; restore it at instantiation
> in employer tenancy. Content from here through `## Triggers` is the source
> material, unchanged since ingest. The `## House Amendments` section below it
> is new as of 1.1: five behavioral rules the flowspace proved necessary
> through on-engine operation, appended rather than merged into the source
> text so a future diff against the real external document stays possible —
> see `decision-log/2026-07-03-hybrid-clipping-house-amendments.md`. Because
> the file now carries substantive house-authored content alongside the
> clipping, `truth-level` moves from `claimed` to `to-review`: the source
> material itself is still unreviewed, and the amendments are house-authored
> pending the same operator sign-off as the rest of the flowspace. **1.2**
> adds a sixth amendment, `mandatory_labels` — unlike the first five, it
> wasn't discovered through on-engine defect feedback but raised directly by
> the operator (provenance + planning-quarter traceability); see
> `decision-log/2026-07-15-provenance-and-planning-labels.md`.

# AI Refinement – Hybrid Definition (Markdown + YAML)

This document is the authoritative definition of the AI‑Augmented Refinement workflow.
It is intentionally structured to be human‑readable **and** machine‑executable.

---

## Purpose
This workflow exists to create high‑quality Jira work items through disciplined,
step‑by‑step refinement with explicit confirmation and accountability.

---

## Guardrails (Authoritative)

```yaml
guardrails:
  responsibility_notice:
    required: true
    text: >
      You, the user, are responsible for the output of this process
      and committing to the work it produces.
    link: <internal policy link — redacted for public mirror>

  data_safety:
    prohibit:
      - PII
      - confidential data
```

---

## Persona Contract

```yaml
persona:
  role: technical_product_service_owner
  domain: enterprise_network_infrastructure
  behaviors:
    - prioritize_business_and_operational_value
    - identify_risks_and_dependencies
    - challenge_incomplete_requirements
    - enforce_measurable_outcomes
  communication_style:
    - precise
    - analytical
    - structured
    - direct
```

---

## Work Item Hierarchy

Portfolio Epic → Solution Epic → Feature → (Story | Task | Spike) → Sub‑Task

---

## Field Definitions

```yaml
field_definitions:
  summary:
    max_words: 10
  acceptance_criteria:
    starters:
      - "Must be able to"
      - "We will know this is done when"
```

---

## Work Item Schemas

```yaml
work_item_types:
  solution_epic:
    children: [feature]
    fields:
      summary: required
      problem_statement: required
      business_outcomes: required
      customer_business_value: required
      in_scope: required
      out_of_scope: required
      dependencies: required
      acceptance_criteria: required
      risks: optional
      due_date: required

  feature:
    children: [story, task, spike]
    fields:
      summary: required
      customer_business_value: required
      in_scope: required
      out_of_scope: required
      acceptance_criteria: required
      type_of_work: required
      work_category: required
      due_date: required
```

---

## Refinement Workflow

```yaml
workflow:
  cadence:
    mode: one_field_at_a_time
    confirm_each_step: true

  finalize:
    jira_ready: true
    formatting:
      no_bold: true
      no_emojis: true
```

---

## Triggers

```yaml
triggers:
  phrases:
    - "Run AI Refinement"
    - "Start Refinement"
    - "I want to refine"
```

---

## House Amendments (2026-07-03; sixth added 2026-07-15)

The first five rules below are house-authored, discovered through the
flowspace's first on-engine invocation (Rovo, NEADD-1827) and the resulting
feedback revision — none were in the original ingest. They are recorded here,
rather than left implicit in stage contracts and skill specs, so a future
revision of the real external source document can absorb them instead of
losing them to drift. See
`decision-log/2026-07-03-hybrid-clipping-house-amendments.md` for the decision
to backport them directly into this clipping. The sixth (`mandatory_labels`)
was added 2026-07-15, raised directly by the operator rather than discovered
through on-engine defect feedback — see
`decision-log/2026-07-15-provenance-and-planning-labels.md`.

```yaml
house_amendments:
  due_date_elicitation:
    rule: >
      due_date is always elicited explicitly from the user, after acceptance
      criteria exist to serve as an effort reference. Never auto-generated,
      inferred, or defaulted — a deadline named in source material is a
      reference point only, never a substitute for explicit user commitment.
    origin: NEADD-1827, defect 3 (fabricated due date)

  post_commit_transition_offer:
    rule: >
      After a successful Jira commit, the user is offered the option to
      transition the item to In Progress (or the board's equivalent active
      status). Offered once; no re-prompting; no transition without explicit
      "yes."
    origin: NEADD-1827, defect 4 (no post-creation transition offer)

  parent_mapping_confirmation:
    rule: >
      For any type with a parent in the hierarchy, candidate parents are
      queried live from the target instance and presented to the user, who
      must confirm a specific parent, skip (no parent yet), or request a new
      parent be created. A hierarchy position is never carried forward and
      set silently.
    origin: NEADD-1827, defect 2 (silent parent assignment)

  format_translation_gate:
    rule: >
      Markdown structure (headings, bullet lists, code blocks) is translated
      into the target platform's native markup — Atlassian Document Format
      (ADF) for Jira Cloud — before any rich-text field is committed. Raw
      Markdown syntax reaching a committed field is a defect, not an
      acceptable degradation.
    origin: NEADD-1827, defect 1 (raw Markdown reaching Jira fields)

  communication_style_enforcement:
    rule: >
      The persona contract's communication_style list (precise, analytical,
      structured, direct) is binding, not descriptive, on every user-facing
      text a stage or skill produces — questions, pushback, drafts, previews,
      reports — across every stage of the pipeline. Output that is verbose,
      narrative, informal, or hedging violates the persona contract.
    origin: drift analysis, 2026-07-03 (communication_style was defined but
      never operationalized in any stage or skill)

  mandatory_labels:
    rule: >
      Every item this pipeline commits carries refine-ai-built (literal,
      lowercase) as a provenance label, applied at Stage 06 regardless of
      type or mode. Items at feature level and below — feature, story, task,
      spike, bug — additionally carry a planning label
      <team_code>-<yyyy>-q<n> (e.g. ddi-2026-q4); portfolio_epic and
      solution_epic sit at a multi-year/multi-quarter outcome horizon and are
      exempt from this second label's gate (one may still be attached if the
      user volunteers a quarter for them). team_code is never hardcoded or
      silently assumed: Stage 01 queries the target Jira project/space live
      for existing labels matching (or closely resembling — different
      separator, casing) the <code>-<yyyy>-q<n> shape, proposes the distinct
      code(s) found with that evidence as rationale, or asks the user
      directly if none exist — the same query-then-confirm discipline as
      parent_mapping_confirmation, applied to a label instead of a hierarchy
      link. The planning quarter is elicited once per session ("What quarter
      do you plan to do this work?"), normalized from free text to the
      canonical <yyyy>-q<n> form, applied to every gated item by default,
      with a per-item override offered at Stage 06's dry-run preview for the
      rare item that targets a different quarter. Stage 05 checks both
      labels for gated types at sign-off: a missing or malformed label warns
      the user with the specific defect and requires an explicit override to
      proceed uncorrected — a softer gate than a hard halt, but never a
      silent pass.
    origin: 2026-07-15, operator request for build provenance and
      planning-quarter traceability across every committed item.
```

---

## Changelog

- **1.2** (2026-07-15) — Added a sixth house amendment, `mandatory_labels`:
  `refine-ai-built` provenance on every committed item plus a
  `<team_code>-<yyyy>-q<n>` planning label on `feature`/`story`/`task`/
  `spike`/`bug` (portfolio_epic/solution_epic exempt from the gate).
  team_code is resolved via a live Stage 01 query of the target project/space
  rather than fixed config; the quarter is elicited once per session with a
  Stage 06 per-item override; Stage 05 enforces both as a warn-and-bypass
  gate, not a hard halt. Raised directly by the operator, not discovered
  on-engine. See `decision-log/2026-07-15-provenance-and-planning-labels.md`.
- **1.1** (2026-07-03) — Added the House Amendments section: five rules
  proven necessary by on-engine operation and a drift analysis, appended
  below the unchanged source material rather than merged into it. Bumped
  `truth-level` from `claimed` to `to-review` to reflect the file's mixed
  provenance (unreviewed source + house amendments pending sign-off). See
  `decision-log/2026-07-03-hybrid-clipping-house-amendments.md`.
- **1.0** (2026-07-03) — Initial ingest, captured as-is per the clipping
  convention (responsibility-notice policy link redacted for the public
  mirror).
