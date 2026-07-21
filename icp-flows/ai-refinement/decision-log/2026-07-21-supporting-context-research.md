---
id: decision-2026-07-21-supporting-context-research
title: "Decision Log — Supporting-Context Research (SAD + Relevant Documents)"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-21
updated: 2026-07-21
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
  - "[[context-elicitation]]"
  - "[[scope-dependency-mapper]]"
---

# Decision Log — 2026-07-21 — Supporting-Context Research

**What was decided:** add a seventh house amendment,
`supporting_context_research`, making intake active instead of passive — the
pipeline now looks for the SAD (systems architecture diagram) and other
relevant grounding documents rather than only classifying whatever the user
pastes in. **By whom:** agent, on direct operator instruction (like
`mandatory_labels`, this was operator-raised, not discovered through
on-engine defect feedback). **What it affects:**
`reference/ai-refinement-hybrid.md` (1.2 → 1.3, back to `to-review`),
`HUB.md` (1.12 → 1.13: taxonomy row 7 expanded, new row 9, new
"Supporting-context research" section, sixth Known-gaps entry), Stage 01
(1.8 → 1.9: new research step), Stage 02 (1.5 → 1.6), Stage 03 (1.4 → 1.5),
and the `context-elicitation` (1.4 → 1.5) and `scope-dependency-mapper`
(1.2 → 1.3) skills with all four adapters regenerated — both skills move to
`truth-level: to-review`. Nothing is deployed to a live engine.

## Operator direction (verbatim intent)

1. Prompt the user for context they already hold — Confluence documents,
   exported Miro content, PDF files, email content, etc.
2. The user confirms the scope of the initial research in Confluence and
   Jira, or asks the agent to hunt across more Confluence documents —
   propose → confirm → hunt, with user-confirmed widening.
3. Use the user's initial prompt to read the focus of the work being
   refined: heavier on new engineering or enhancements → look for more
   architecture, data, and topology documentation; OS upgrades, hardware
   refreshes, and other operations efforts → look for those related
   documents, especially prior completed processes of the same type in the
   same areas.

## Design decisions

1. **Placement — Stage 01, after type selection, before the fast-track
   assessment.** The gathered document set is exactly the material the
   fast-track confidence call weighs, so research must precede it; and the
   research scope proposal benefits from knowing the selected type.
2. **Work-focus profiles, not a fixed document list.** Engineering/
   enhancement → SAD first, then HLD/LLD, ADRs, data models,
   network/topology diagrams. Operations → runbooks, MOPs/SOPs,
   upgrade/refresh guides, prior completed same-type/same-area processes.
   Mixed/unclear → both sets proposed, user trims. The classification and
   its rationale go in the transcript — it is a proposal, never a silent
   filter.
3. **Confirm-then-hunt.** The agent names spaces, projects, terms, and
   document types before any search runs; the user confirms, trims, or
   redirects. Every widening is explicitly user-confirmed. This mirrors the
   query-then-confirm discipline of `parent_mapping_confirmation` and the
   team_code query, applied to a search scope.
4. **Taxonomy row 9 — prior completed work item or process record.** The
   operator's "prior completed processes of the same type in the same
   areas" emphasis did not fit any existing row: row 6 (incident/problem
   record) is problem-shaped, row 9 is precedent-shaped — mined for scope,
   risks, and duration reference after a type-and-area match check, never
   copied forward unexamined. Row 7 now names the SAD and its common
   carriers (Confluence page, Miro export, PDF) explicitly.
5. **Not-found is a recorded gap, not a blocker.** A missing SAD on an
   engineering item is named to the user and worked around by elicitation —
   never silently substituted with invented content.
6. **Downstream consumption stays propose-not-decide.** SAD integration
   points seed the Stage 02 stakeholder sweep and Stage 03 dependency sweep
   as *cited candidates*; prior-process records seed "tried before" and
   risks. The hard carve-outs (interactive stakeholder sweep,
   coalition/conflict-axis annotation, due-date elicitation) are untouched.

## Data-boundary reasoning

The Confluence read surface is new. It is bounded the same way as the
existing Jira label and parent-candidate queries: engine-native, read-only,
max data-class `internal`, no write action. Two additional controls apply
because search returns *content*, not just labels: the search scope is
user-confirmed before any query runs, and every retrieved document passes
the Stage 01 data-safety screen (PII/confidential check, taxonomy typing)
before entering the session — the same screen user-supplied material gets.

## Remaining for the operator (the human gate)

1. Sign off the seventh amendment (hybrid clipping back at `to-review`).
2. Gate re-run for `context-elicitation` 1.5 and `scope-dependency-mapper`
   1.3 — agent pre-run recorded in
   `../../skill-foundry/decision-log/2026-07-21-supporting-context-skill-revision-pass.md`.
3. Extend `reference/confluence-instantiation-guide.md` (REC-02 knowledge
   scoping — the Rovo agents' Confluence scope must now include the spaces
   the research step may search, or the step must be constrained to
   user-pasted links) and `reference/on-engine-validation-checklist.md`
   (REC-09 — add research-step checks: scope confirmed before search,
   widening confirmed, screen applied to retrieved content) before the
   first live run. Neither file is modified by this change.
