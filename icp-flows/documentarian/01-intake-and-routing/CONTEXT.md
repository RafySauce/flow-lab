---
id: documentarian-stage-01
title: "Stage 01 — Intake & Routing"
type: stage-context
stage: 1
review-intensity: heavy
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related:
  - "[[documentarian]]"
  - "[[doc-type-registry]]"
  - "[[documentation-standards]]"
---

# Stage 01 — Intake & Routing

## Inputs

| Input | Source | Required |
|---|---|---|
| Trigger phrase ("Run Documentarian", "Document this work", "Start a doc run") | User | Yes |
| Job type (agent-proposed from source material when available, otherwise user-selected): `closeout`, `modernize`, `sad-update`, `tree-audit`, `meeting` | User + agent | Yes |
| Doc-type registry (the six governed doc types and their templates) | `../reference/doc-type-registry.md` | Yes |
| Documentation standards baseline | `../reference/documentation-standards.md` | Yes |
| Source material — a closing Jira item or key, a Confluence space/tree link, a delivered feature reference, or a meeting transcript/summary | User | No |
| Target surface preference (Confluence space; ServiceNow KB if the document is KB-destined) | User | No |

## Process

`Layer-3: inline (one-off — the guardrail, routing, and registry-pointer
content below is specific to this flowspace; the registry itself lives at
../reference/doc-type-registry.md)`

1. **Trigger detection** — recognize one of the defined trigger phrases.
2. **Responsibility acknowledgment** — present the responsibility notice and
   obtain explicit user confirmation:
   > "You, the user, are responsible for the documentation this process
   > produces and for what it publishes to shared platforms."
   > Policy reference: `<internal policy link — set at instantiation; redacted from this public design copy>`
3. **Data-safety screen** — state the PII / confidential-data prohibition,
   then screen any source material before it enters the session. Meeting
   transcripts get the strictest screen of the set: they routinely carry
   names, attributions, and verbatim quotes — have the user strip or approve
   them explicitly (decisions may be attributed only where the user confirms
   attribution belongs in the record). Incident-adjacent runbook material is
   screened for customer detail. Anything `confidential` or above halts the
   run per the sanctioned-tool matrix.
4. **Job-type selection** — if source material is available, propose one of
   the five job types with a stated rationale (a closed item key reads as
   `closeout`; a space link plus "bring this up to standard" reads as
   `modernize` or `tree-audit` — page-shaped vs. tree-shaped; a delivered
   feature reference reads as `sad-update`; a transcript reads as `meeting`);
   the user confirms or overrides. Without source material, ask directly.
   Exactly one job type per run.
5. **Registry load** — load `../reference/doc-type-registry.md` and confirm
   the six governed doc types are available to Stage 3's template matching.
   If the user's intent names a doc type outside the registry, consult the
   registry's out-of-scope table and redirect (e.g., requirements documents
   route to ai-refinement as source material, not to this flow).
6. **Target-surface identification** — default Confluence. If the intended
   output is a ServiceNow KB article, state the designed-for gap plainly: no
   sanctioned ServiceNow write path exists, so the document will be produced
   against the `kb-article` registry schema and staged on Confluence with a
   `servicenow-pending` label at Stage 6. The user accepts the staged path or
   re-scopes.
7. **Grounding check** — no documentation-owners register exists for this
   domain yet. Flag **ungrounded mode**: Stage 3's ownership and audience
   fields are asked of the user directly rather than walked from a register —
   a degraded but functional path, not a blocked one.
8. **Confirm setup** — echo back: job type (+ rationale, if agent-proposed),
   screened source material, target surface (+ staged-path acceptance, if
   ServiceNow-destined), grounding status, guardrails in effect. Obtain user
   "proceed" before advancing.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Acknowledged responsibility flag | Stage 02 | boolean |
| Selected job type + rationale (if agent-proposed) | Stages 02–07 | text + type tag |
| Screened source material references | Stage 02 | links / text |
| Loaded doc-type registry reference | Stages 03–06 | path reference |
| Target surface + ServiceNow staged-path acceptance (if applicable) | Stages 03, 06 | text |
| Grounding status (grounded / ungrounded) | Stage 03 | boolean |

## Verify

Cross-stage trace: the job type Stage 01 hands forward is the mode Stage 02
actually gathers in. Check that Stage 02's dossier header names the same job
type Stage 01 confirmed, and that the registry version Stage 03 matches
templates against is the one Stage 01 loaded (`artifact-version` of
`../reference/doc-type-registry.md` recorded at load equals the version Stage
03 cites). The failure this catches is a downstream stage gathering or
planning against a different job shape than the user confirmed. Running this
check leaves a one-line result in the run's decision log.

- [ ] Trigger phrase was matched
- [ ] Responsibility notice was displayed and explicitly acknowledged
- [ ] Data-safety prohibition was stated; any source material screened at the
      level its type demands (transcripts strictest), with the user's
      strip/approve decisions recorded
- [ ] Exactly one job type selected; if agent-proposed, the rationale is in
      the transcript and the user's confirm/override is recorded
- [ ] Registry loaded and its version recorded; out-of-scope intents
      redirected, not documented
- [ ] Target surface identified; if ServiceNow-destined, the staged-path
      acceptance is explicit
- [ ] Grounding status (ungrounded, until a documentation-owners register
      exists) recorded for Stage 03
- [ ] User confirmed "proceed"

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy — this is the session's trust boundary; a missed
  screen or a wrong job type propagates into every document the job
  produces.
- **Evidence:** setup confirmation echoed in the session and a one-line entry
  in the run's decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- No PII or confidential data enters the session at this stage; if it appears
  in source material, halt per the data-safety screen — transcripts do not
  advance with names and attributions the user has not explicitly approved.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
