---
id: ai-refinement-on-engine-validation-checklist
title: "On-Engine Validation Checklist — AI Refinement"
type: specification
artifact-version: "1.3"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-07-31
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
| `portfolio_epic` | [ ] | [ ] | No parent in scope (Stage 06 skips linkage) — confirm the skip is clean, not a silent no-op. New type (added 2026-07-07); schema is `to-review` — weight this row and `bug` highest alongside `spike`. |
| `solution_epic` | [ ] | [ ] | Parent = portfolio epic (as of 2026-07-07 — previously no parent); confirm candidate query returns real portfolio epics, and that skip (no parent yet) still works cleanly for the operator's transition period before portfolio epics exist in the target project. |
| `feature` | [ ] | [ ] | Parent = solution epic; confirm candidate query returns real epics. |
| `story` | [ ] | [ ] | Schema is `to-review` (REC-04) — confirm `type_of_work`/`work_category` screens exist before committing. |
| `task` | [ ] | [ ] | Same schema caveat as `story`. |
| `spike` | [ ] | [ ] | Schema is `to-review`; confirm `question_to_answer`/`timebox` custom fields exist or get created per the discovery step. This is the type that already failed once (NEADD-1827) — weight this row highest. |
| `bug` | [ ] | [ ] | New type (added 2026-07-07, simplified same day); schema is `to-review` — confirm the `description` field (standard Jira field, no custom-field discovery needed) actually carries reproduction steps, expected result, and a contradicting actual result per the registry's `description` content rule, not a vague summary restated. |

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
- [ ] **Parent mapping** — for every type except `portfolio_epic`, candidate
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

## Supporting-context research checks (Stage 01 step 8)

Run once per engine (Rovo; Copilot, if the OneDrive/SharePoint surface is
deployed there per §4a of `confluence-instantiation-guide.md`), not once per
type — this step's behavior doesn't vary by work-item type.

- [ ] **Scope confirmed before search** — the proposed research scope
      (spaces, projects, terms, document types, time window) was presented
      and explicitly confirmed, trimmed, or redirected by the user before
      any search ran, on both Confluence and Jira.
- [ ] **Recency default, not a blanket sweep** — the initial proposal named
      specific spaces/projects (top 3 most recently created/touched for the
      requesting user), not a generic "search all of Confluence" framing;
      if a person or team was named or appeared in supplied material, the
      proposal expanded to their associated spaces/projects.
- [ ] **OneDrive/SharePoint gate** — where the host engine was Copilot and a
      live Microsoft Graph/OneDrive connector was present, the surface was
      proposed with the same recency default, folded into the single scope
      confirmation; where either condition was absent, the surface was
      skipped and recorded as a gap, not silently proposed or silently
      omitted.
- [ ] **Keyword filter merge** — a user-supplied search term (tested with at
      least one of: tech stack name, app/system code, team name, team
      member name) appeared in the proposal alongside agent-proposed terms;
      a stated override replaced the named term explicitly, never silently.
- [ ] **Time-frame default and override** — with no user-stated window, the
      proposal named the past-6-months default; with a user-stated window,
      that window replaced the default and was named in the proposal and
      the research record.
- [ ] **Child-page/child-folder sweep** — a parent Confluence page (and, if
      OneDrive is deployed, a parent OneDrive folder) entering the session
      triggered a one-level relevance pass over its children, with relevant
      children surfaced as additional candidates rather than the parent
      treated as self-contained; confirm the sweep stayed one level deep
      absent an explicit user request to go deeper.
- [ ] **Widening confirmed** — a user request to widen the hunt (more
      spaces, more projects, more OneDrive folders, a deeper child sweep)
      was treated as its own explicit confirmation, never silently folded
      into the original scope.
- [ ] **Screen applied to retrieved content** — every document entering the
      session via search (including child-page/child-folder sweep results)
      passed the Stage 01 data-safety screen and received a taxonomy type
      tag, identical to user-supplied material.
- [ ] **Research record completeness** — sought/found/selected/not-found is
      recorded alongside the surfaces actually searched, the confirmed time
      window, and any child-page/child-folder sweep results.

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
