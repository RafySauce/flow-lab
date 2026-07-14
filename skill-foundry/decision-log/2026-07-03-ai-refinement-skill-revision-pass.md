---
id: decision-2026-07-03-ai-refinement-skill-revision-pass
title: "Decision Log — AI Refinement Skill Revision Pass: jira-commit 1.2 + context-elicitation 1.2"
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
  - "[[context-elicitation]]"
  - "[[work-item-schemas]]"
  - "[[decision-2026-07-03-ai-refinement-skill-gate-prerun]]"
---

# Decision Log — 2026-07-03 — AI Refinement Skill Revision Pass

**What was decided:** apply the two logged-but-deferred content revisions to
the `ai-refinement` skill batch — `jira-commit` 1.1 → 1.2 and
`context-elicitation` 1.1 → 1.2 — regenerate their four adapters, and re-run
the affected gate items, agent-side, recording the evidence here. **By whom:**
agent, on operator instruction ("process and integrate the skills into the
flowspace; the jira-commit skill should lean on what's built into Rovo first
and use the guiding documentation originally provided for required field
mappings"). **What it affects:** the two skill specs, their adapters, the
flowspace HUB (1.5) and Stage 06 contract (1.3). Nothing is promoted, nothing
moved to `completed-skills/`, nothing deployed — those calls stay with the
operator. Like the gate pre-run, this entry stretches the ~10-line shape
because gate evidence *is* the entry.

## The two revisions and why

1. **`jira-commit` 1.2 — registry-grounded, Rovo-native-first.** The 1.1 spec
   hardcoded a flat custom-field list that omitted the spike fields
   (`question_to_answer`, `timebox`) and never referenced the flowspace's
   `reference/work-item-schemas.md` — the guiding documentation that is the
   authoritative required-field registry per work-item type. 1.2 reads the
   field set from the registry per selected type (per-instance custom-field-ID
   *discovery* retained as the mechanism, seeded by registry field names), and
   makes the engine's native Jira capabilities the primary commit path —
   Rovo's built-in create issue / update issue / create issue link actions —
   with the sanctioned connector (Copilot + Atlassian MCP) as the explicit
   fallback. The Rovo adapter's permitted-actions set is unchanged (it was
   already the native minimum set); what changed is that the spec now
   *instructs* the native path instead of describing a generic API call.
   Timing note: the work-item-schema-extension log deferred the spike-field
   addition to "after ratification"; the operator's instruction supersedes
   the deferral. Because 1.2 reads the registry rather than freezing its
   contents, the `story`/`task`/`spike` schemas remain the single surface
   still awaiting operator ratification.
2. **`context-elicitation` 1.2 — source-input-type steering.** Applies the
   revision flagged (not applied) in the flowspace's
   `decision-log/2026-07-03-input-taxonomy.md`: when Stage 01 hands over
   screened source material with an input-type tag, the question sequence
   steers by type — requester-named input starts the stakeholder sweep at the
   requester; solution-shaped vendor/task input gets the underlying problem
   elicited before actions are accepted as scope; multi-item minutes are split
   and framed one per run. New review criterion 7: elicited, not transcribed
   (mirrors Stage 02's Verify item).

Both are content changes, so the 2026-07-03 gate pre-run's evidence no longer
covers them — the affected gate items were re-run below. The three untouched
skills (`scope-dependency-mapper`, `field-refinement-cadence`,
`workitem-validation`) keep their existing pre-run evidence.

## Scope limitation — read first

Same as the original pre-run: this session has no Rovo or Copilot access, so
each regenerated adapter was executed as a **simulated invocation** — the
agent ran the adapter's instruction text verbatim against a synthetic, public
scenario and judged the transcript against the spec's review criteria. This
validates executability as written, not engine-specific behavior (Rovo action
wiring, knowledge-scoping enforcement, real Jira field discovery). On-engine
invocation remains open unless the operator accepts simulation for first
promotion.

## 1. Spec re-review — pass

Both revised diagrams stay one-for-one with their Method prose:
`jira-commit`'s Step 1 node now names the registry-driven mapping and Step 4
the native-actions-first commit, matching Method steps 1 and 4;
`context-elicitation`'s Step 1 node carries the steering clause matching the
Method step 1 extension. Frontmatter valid per the provenance spec (rules 3
and 6 re-checked); `jira-commit` gains `[[work-item-schemas]]` in `related:`;
adapter tables and headers stamped 1.2 on all four regenerated adapters —
no version skew. Both diagrams compile under Mermaid 11.16 via mermaid-cli
(local; GitLab/Confluence surface confirmation remains an instantiation-time
item).

## 2. Live tests — 4 simulated runs, all pass

Scenario family continues the pre-run's synthetic DC east-west fabric
expansion; run numbering continues from R10.

| Run | Skill / adapter | Shape | Verdict vs. review criteria |
|---|---|---|---|
| R11 | context-elicitation / Rovo | email-request input, type-steered | 7/7 |
| R12 | context-elicitation / Copilot | vendor notice + minutes probes | 7/7 |
| R13 | jira-commit / Rovo | spike commit, registry-driven (synthetic) | 6/6 |
| R14 | jira-commit / Copilot | connector path, unmapped-field halt | 6/6 |

- **R11** — Stage 01 handed a screened email (type: email request) from a
  storage engineer asking for "more uplink capacity for the new array."
  Steering fired: sweep started at the requester's register entry
  (Systems/Server, 9) rather than the generic opener; the solution-shaped ask
  ("more capacity") was walked back to the problem (replication window
  breaches); Facilities (13) surfaced via "what they value most." Drafts
  confirmed field-by-field; problem statement named the failure, not the
  request — criterion 7 checked against the source email: elicited, not
  transcribed.
- **R12** — vendor advisory (type: vendor action notice) prescribing a fabric
  firmware upgrade: adapter elicited the internal problem (exposure window on
  east-west segmentation) before accepting the prescribed action as scope,
  and tagged the internal owning stakeholder, not the vendor. Second probe:
  meeting minutes carrying three candidate items → split; exactly one framed
  this run, the other two named for their own Band ② runs.
- **R13** — spike "determine east-west telemetry sampling floor": registry
  schema for `spike` loaded — summary, question_to_answer, timebox,
  customer_business_value, acceptance_criteria, due_date; synthetic field-ID
  discovery seeded by registry names resolved question_to_answer and timebox;
  no in_scope/out_of_scope mapped (registry says spikes carry none — the 1.1
  flat list would have looked for them); parent NETDC-301 validated via
  native lookup; commit executed through built-in create-issue +
  create-issue-link actions; dry-run preview → approval after preview →
  synthetic key NETDC-317 + URL; fetch-back matched field-for-field.
- **R14** — same spike payload on the connector path: target instance
  (synthetic) lacked a `timebox` custom field → halt naming `timebox` with
  the registry cited as the source of the requirement, no partial commit, no
  silent drop; after the synthetic instance gained the field, run completed
  6/6 with explicit post-preview approval.

## 3. Trigger check — pass

Neither revision adds a fire condition. `context-elicitation`'s steering is
input-shaped, not trigger-shaped — it still fires only at Stage 02 /
"frame this problem," and typed source material without a framing request
does not fire it (Stage 01 owns screening and tagging). `jira-commit`'s
near-misses are unchanged; "just create a quick ticket" still refuses
(re-probed in R14's preamble).

## 4. Boundary/collision check — pass

The pair inspected hardest: `jira-commit` (writer) vs `workitem-validation`
(gate). Registry grounding does **not** move validation into the writer —
Stage 05 still owns the completeness verdict against the registry;
`jira-commit` reads the registry only to know *which fields to map*, and its
failure mode stays halt-and-name, never fix-and-proceed. `context-elicitation`
steering vs Stage 01 intake: the skill consumes the screened material and its
type tag; screening, stripping, and vetting stay in Stage 01 — no overlap.
No change to the family's disjoint territories or to the non-collision with
the four foundry-support briefs.

## 5. Evidence

This entry. Flowspace-side sync recorded in `ai-refinement` HUB 1.5 (Known
gaps) and Stage 06 contract 1.3.

## Remaining for the operator (the human gate)

1. On-engine live test per adapter — now including the Rovo-native commit
   path and the steering behavior (or explicitly accept the simulations
   above for first promotion).
2. Ratify the `story`/`task`/`spike` schemas and the two spike fields in
   `reference/work-item-schemas.md`, and confirm them against the real Jira
   project configuration at instantiation.
3. Rendering confirmation on the real surfaces at instantiation.
4. Promotion calls: `truth-level: verified`, move to `completed-skills/`,
   adapter deployment.
