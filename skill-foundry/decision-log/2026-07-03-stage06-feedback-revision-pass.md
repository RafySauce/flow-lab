---
id: decision-2026-07-03-stage06-feedback-revision-pass
title: "Decision Log — Stage 06 Feedback Revision Pass: jira-commit 1.3 + field-refinement-cadence 1.2"
type: decision-log
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
  - "[[jira-commit]]"
  - "[[field-refinement-cadence]]"
  - "[[work-item-schemas]]"
  - "[[decision-2026-07-03-ai-refinement-skill-revision-pass]]"
---

# Decision Log — 2026-07-03 — Stage 06 Feedback Revision Pass

**What was decided:** apply the five defects in the operator's Stage 06
feedback package (first on-engine invocation, Rovo adapter, produced
NEADD-1827 on the Perimeter Security Services board) as revisions to their
named contract surfaces — `jira-commit` 1.2 → 1.3, `field-refinement-cadence`
1.1 → 1.2 — regenerate all four affected adapters, and re-run the affected
gate items, agent-side, recording the evidence here. **By whom:** agent, on
operator instruction ratifying the feedback package and directing
implementation of all five proposed fixes. **What it affects:** the two
skill specs and their four adapters; the flowspace HUB (1.8), Stage 01 (1.4),
Stage 04 (1.3), and Stage 06 (1.4) contract pages. The registry-only fix
(Defect 5) is logged separately in the flowspace-side entry,
`../../icp-flows/ai-refinement/decision-log/2026-07-03-stage06-feedback-revision.md`,
since it touches no skill spec directly. Nothing is deployed to a live
engine — that stays the operator's act.

## The five defects and their fixes

1. **Formatting artifacts reaching Jira (jira-commit 1.3).** NEADD-1827's
   description/AC fields contained literal `### Summary` etc. Stage 05's
   "no bold, no emojis" pass never translated structural Markdown; 1.2's
   field mapping passed it through unchanged. 1.3 adds a format-translation
   gate to Method step 1: Markdown → ADF (or a translated plain layout where
   only plain text is available) before any rich-text field is mapped, and
   step 3's dry-run preview now renders the translated form instead of
   echoing source text.
2. **Silent parent assignment (jira-commit 1.3).** NEADD-1827 committed with
   a parent link the user never confirmed. 1.2's linkage step validated that
   an assigned parent existed but never prompted a choice. 1.3 makes parent
   mapping a confirmed default for every type except `portfolio_epic`/
   `solution_epic`: query candidates, present them (key/summary/status), and
   require confirm/skip/create-new before setting the link.
3. **Fabricated due date (field-refinement-cadence 1.2).** NEADD-1827's due
   date was invented, not elicited. 1.2 adds an explicit due-date-elicitation
   Method step: acceptance criteria are presented as an effort reference
   first (ordering rule changed — AC moved from "last" to "next-to-last" so
   due date can always follow it), the user is asked directly to commit, and
   a spike's timebox is validated against the confirmed date. A source
   deadline (e.g., a vendor advisory expiration) is surfaced as a reference
   point only, never accepted as the answer.
4. **No post-creation transition offer (jira-commit 1.3).** NEADD-1827 sat in
   Backlog with no offer to advance it. This was a contract gap, not just an
   implementation gap (Stage 06's session-loop step never mentioned it). 1.3
   adds a new Method step 5 (session loop renumbered to step 6): offer to
   transition to In Progress after a successful commit, execute via native
   Jira capabilities on "yes," leave the default status on "no."
5. **Missing board-interaction fields.** Schema-only — see the flowspace-side
   entry. Ripple into this pass: `field-refinement-cadence`'s cross-field
   conflict check (Method step 3) is broadened from "type-of-work /
   work-category inconsistency (feature only)" to every type that carries
   both fields per the revised registry (feature, task, story, spike) —
   otherwise the newly-required fields on story/spike would go unchecked for
   internal consistency.

## Scope limitation — read first

Same as the prior revision pass: this session has no Rovo or Copilot access,
so each regenerated adapter was executed as a **simulated invocation** — the
agent ran the adapter's instruction text verbatim against a synthetic, public
scenario and judged the transcript against the spec's review criteria. This
validates executability as written, not engine-specific behavior (Rovo's ADF
rendering fidelity, native transition-issue action availability, real Jira
board configuration for candidate-parent queries). On-engine invocation
remains open unless the operator accepts simulation for this revision too —
notably, the *first* on-engine invocation is what surfaced these defects, so
the operator may reasonably want the next on-engine run to double as
verification before accepting simulation alone.

## 1. Spec re-review — pass

`jira-commit`'s Flow Diagram now carries six process nodes plus the new
parent-confirmation and transition-offer decision diamonds, one-for-one with
Method steps 1–6. `field-refinement-cadence`'s diagram carries the new
due-date node (step 5) between AC reframing and summary enforcement,
one-for-one with the revised Method. Frontmatter valid per the provenance
spec; both specs' `related:` lists already carry (or gained)
`[[work-item-schemas]]`. Adapter tables and headers stamped 1.3/1.2 on all
four regenerated adapters — no version skew. Both diagrams compile under
Mermaid 11.16 via mermaid-cli (local; GitLab/Confluence surface confirmation
remains an instantiation-time item, as before).

## 2. Live tests — 4 simulated runs, all pass

Scenario family continues the prior passes' synthetic DC east-west fabric
expansion; run numbering continues from R14.

| Run | Skill / adapter | Shape | Verdict vs. review criteria |
|---|---|---|---|
| R15 | jira-commit / Rovo | spike commit, Markdown description + heading markers | 8/8 |
| R16 | jira-commit / Copilot | story commit, parent skip + transition decline | 8/8 |
| R17 | field-refinement-cadence / Rovo | task fields, due-date elicitation | 7/7 |
| R18 | field-refinement-cadence / Copilot | spike fields, timebox/due-date conflict | 7/7 |

- **R15** — spike "determine east-west telemetry sampling floor" (same
  synthetic item as prior pass's R13), description drafted with `### Context`
  and a bulleted risk list. Format-translation gate fired: headings and the
  list converted to ADF nodes before mapping; dry-run preview rendered the
  translated structure, not the source markers — confirmed by diffing the
  preview text against the pre-translation draft. Parent step queried
  candidate features under synthetic epic NETDC-301, presented three with
  key/summary/status; user confirmed NETDC-305. Commit → synthetic key
  NETDC-318; post-commit offer accepted, synthetic transition to In Progress
  executed; fetch-back matched content field-for-field with only markup
  translated.
- **R16** — story "document east-west segmentation exceptions" on the
  connector path. Parent step presented candidate features; user chose
  "skip" (backlog-level, no parent decided yet) — commit proceeded with no
  parent link, correctly not treated as a halt. Post-commit transition
  offered; user declined — item left in default (Backlog) status, no
  transition action invoked. Both explicit choices appear in the transcript
  as required by review criteria 3 and 6.
- **R17** — task "patch fabric firmware across east-west leaf pairs": fields
  walked through in the revised order (summary → … → AC → due date last).
  After AC confirmed ("We will know this is done when all leaf pairs report
  the patched firmware version via telemetry"), the adapter presented that AC
  back and asked the user directly for a completion date; user committed to
  a date. Type-of-work/work-category consistency check (now scoped to task,
  which already required the fields) ran clean.
- **R18** — spike "determine east-west telemetry sampling floor" variant with
  a tighter constraint: user first proposed a due date, then a timebox that
  would close *after* it. Conflict surfaced immediately per Method step 3
  ("timebox closes on or before due date"), routed back to due-date
  elicitation; user extended the due date to clear the conflict before
  advancing — matching the spec's "surface immediately, don't defer" rule.

## 3. Trigger check — pass

Neither revision adds a fire condition. `jira-commit` still fires only at
Stage 06 with a Stage 05 sign-off in hand; the new parent-confirmation and
transition-offer steps are internal to that same invocation, not new trigger
surfaces. `field-refinement-cadence` still fires only at Stage 04; due-date
elicitation is a step inside the existing per-field cadence, not a new
fire condition. Near-misses for both skills are unchanged from the 1.1/1.2
gate pre-run.

## 4. Boundary/collision check — pass

Re-inspected `jira-commit` (writer) vs. `workitem-validation` (gate): the
format-translation gate operates strictly on markup, after Stage 05's
content/completeness verdict — it does not re-open or duplicate Stage 05's
"no bold, no emojis" check, and Stage 05's own contract is untouched. The
parent-confirmation flow does not encroach on Stage 01's hierarchy-position
selection: Stage 01 still picks the *type* and its position in the
hierarchy; Stage 06 resolves *which specific existing item* fills that
position, which was always this skill's job (Method step 2), just previously
under-specified. `field-refinement-cadence`'s due-date step does not
encroach on Stage 05's due-date *validity* check (future date, parseable) —
elicitation and validation remain disjoint. No change to the family's
disjoint territories.

## 5. Evidence

This entry. Flowspace-side sync recorded in `ai-refinement` HUB (1.8), Stage
01 (1.4), Stage 04 (1.3), and Stage 06 (1.4) contract pages, and in
`../../icp-flows/ai-refinement/decision-log/2026-07-03-stage06-feedback-revision.md`.

## Remaining for the operator (the human gate)

1. On-engine live test per adapter for both revised skills — given these
   defects were only caught on-engine the first time, weight this over
   accepting simulation alone.
2. Ratify the `story`/`task`/`spike` schemas in
   `reference/work-item-schemas.md`, now including the `type_of_work`/
   `work_category` addition to `story` and `spike` bundled into this same
   ratification.
3. Confirm the target Jira project's board configuration actually exposes a
   parent-candidate query the native/connector path can execute, and that a
   native transition-issue action (or connector equivalent) is available for
   the post-commit offer.
4. Redeployment of the four regenerated adapters, superseding whatever was
   published from 1.2/1.1.
