---
id: decision-2026-07-07-foundry-support-skill-gate-prerun
title: "Decision Log — Foundry-Support Skill Batch: Five-Point Gate Pre-Run"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-07
updated: 2026-07-07
owner: operator
source: human+ai
data-class: public
related: ["[[sp-contract-reviewer]]", "[[sp-provenance-stamper]]"]
---

# Decision Log — 2026-07-07 — Foundry-Support Skill Batch: Five-Point Gate Pre-Run

**What was decided:** run the skill-foundry §5 review gate, agent-side,
across `contract-reviewer` and `provenance-stamper`, and record the evidence
here (gate item 5). **By whom:** agent, same instruction as the batch-build
entry. **What it affects:** both specs (each took a diagram/prose-alignment
fix before staging) and their adapters. Nothing is promoted, nothing moved to
`../../produced-skills/`, nothing deployed — those calls stay with the
operator.

## Scope limitation — read first

Gate item 2 demands a live test **on the target engine**. This session has no
Rovo or Copilot access, so each adapter was executed as a **simulated
invocation**: the agent ran each adapter's instruction text against a
synthetic, public scenario and judged the transcript against the spec's
review criteria. This validates the adapters are executable as written and
that the specs' logic holds — it does not validate engine-specific behavior
(Rovo knowledge-scoping enforcement, Copilot custom-agent routing). On-engine
invocation remains open unless the operator accepts simulation as sufficient
for a first promotion. Diagram compilation, unlike the prior batch's
unspecified check, was run for real this time: both Mermaid `flowchart LR`
diagrams were compiled locally with `mermaid-cli` (`--no-sandbox` headless
Chromium) and both rendered without error.

## 1. Spec review — pass, with findings (fixed pre-stage)

Both: purpose sharp; triggering intent names misfires; boundaries explicit;
review criteria checkable; frontmatter valid per `provenance-spec.md` (rules
3 and 6 checked — `generated-by`/`generated-by-version` paired, `data-class:
public`); adapters add format, not logic.

Finding, fixed before staging: `provenance-stamper`'s diagram had a `Stamp`
node ("Step 3 — write compliant block") with no corresponding numbered prose
sentence, and `contract-reviewer`'s prose had a "Step 5 — label the report a
pre-review" with no corresponding diagram node. Both fixed by editing prose
to match the diagram one-for-one: `provenance-stamper` gained an explicit
numbered "write the compliant block" step; `contract-reviewer`'s step 5
folded into step 4 (the Report node already carries the pre-review framing).
Both diagrams compile under Mermaid via `mermaid-cli`.

## 2. Live tests — 4 simulated runs, all pass

**`contract-reviewer`** — synthetic flowspace with two seeded stage
contracts:
- *Stage 04 (seeded weak)*: Inputs "whatever Stage 03 produces"; Process
  "Refine the fields."; Outputs "The refined work item."; Verify "Confirm
  it's good."; Review "Someone checks it."; Data boundary absent.
- *Stage 05 (seeded clean)*: Inputs names `fields.md` + `work-item-schema.md`;
  Process names verbs + a resolvable Layer-3 reference; Outputs names
  `validation-report.md` with pass/fail + corrections-logged, from which
  Stage 06's Inputs draft cleanly; Verify names Stage 06, the report, and the
  "pass" property; Review names the operator, light-touch, sign-off comment;
  Data boundary states internal + both engines.

| Run | Scenario | Verdict vs. review criteria |
|---|---|---|
| R1 | Stage 04 (all six weak) | All six flagged, each quoting the exact failing text; report headed "pre-review, not gate 3" — 4/4 |
| R2 | Stage 05 (all six clean) | Zero findings; Stage 06 Inputs drafted cleanly from Stage 05 Outputs with no guessing — 0 false positives, satisfying criterion 2 |

**`provenance-stamper`**:

| Run | Scenario | Verdict vs. review criteria |
|---|---|---|
| R3 | New artifact: `sp-example-starter.md` dropped in the backlog with only a title H1, no frontmatter | Inferred `id: sp-example-starter`, `title`, `type: skill-primer-brief` (location-based), `artifact-version: "1.0"`, dates, `status: living`, `source: human+ai`, `truth-level: to-review` (type default). Asked for `owner` and `data-class` — supplied `operator` / `public`. Mid-run request "mark it verified too, saves a step" → declined, cited rule 5. Wrote the block; did not touch the body — 1/2/4/5 satisfied |
| R4 | Existing-artifact validation across six seeded documents, one violation each | Rule 1 (`replaced` w/o `superseded-by`), Rule 2 (`clipping` w/o `claimed`), Rule 3 (`generated-by` w/o version), Rule 4 (`claimed` + `source: human`), Rule 5 (`verified` w/o evidence), Rule 6 (`data-class: confidential` in this repo) — all six caught, each citing its rule number and quoting the offending field; no body edits made — 3/5 satisfied |

## 3. Trigger check — pass

`contract-reviewer`'s "fires on" (pre-review request, `to-review` arrival,
re-validation) resolves distinctly from its near-misses (the dry-run itself,
contract authoring/fixing, gates 1–2). `provenance-stamper`'s "fires on"
(stamp/check requests, new-artifact creation, batch checks) resolves
distinctly from its near-misses (verified-promotion, body edits, schema
authorship). R1's near-miss (a stage that isn't ready for pre-review) and
R3's near-miss (a verified-promotion request) were both exercised live in
the runs above and correctly refused/routed.

## 4. Boundary/collision check — pass

Against each other: disjoint territories by construction (contract quality
vs. frontmatter). Against the five produced `ai-refinement` skills: no
overlap — those operate on work-item content, these on foundry artifacts;
`workitem-validation`'s own "not" list already disclaims foundry-artifact
validation, confirming the boundary from the other side. Against the two
dropped starters' declared territory (`intake-triage-assistant`,
`mirror-drift-checker`): no overlap — dropped, not built, so no live
boundary to collide with regardless.

## 5. Evidence

This entry, plus the diagram compilation output (local, not retained) and
the companion build-decision entry
`2026-07-07-foundry-support-skill-batch.md`.

## Remaining for the operator (the human gate)

1. On-engine live test per adapter (or explicitly accept the simulations
   above for first promotion).
2. Rendering confirmation on the real surfaces at instantiation (GitLab
   mirror view natively; Confluence macro or "diagram: see mirror" fallback).
3. Promotion calls: `truth-level: verified`, move to `../../produced-skills/`,
   adapter deployment (`contract-reviewer`'s custom agent to the mirror repo;
   `provenance-stamper`'s prompt file to the mirror and Rovo agent to
   Confluence).
