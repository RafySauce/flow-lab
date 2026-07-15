---
id: documentarian-stage-02
title: "Stage 02 — Evidence Gathering"
type: stage-context
stage: 2
review-intensity: light
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
  - "[[sp-doc-evidence-gatherer]]"
---

# Stage 02 — Evidence Gathering

## Inputs

| Input | Source | Required |
|---|---|---|
| Selected job type + rationale | Stage 01 | Yes |
| Screened source material references (item keys, space/tree links, feature reference, transcript) | Stage 01 | Yes |
| Acknowledged responsibility flag | Stage 01 | Yes |
| Jira project(s) and Confluence space(s) to read | User (confirmed against Stage 01 source references) | Yes |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-doc-evidence-gatherer)`

Build the **evidence dossier** in the mode the job type selects. One skill,
mode-steered — the gathering discipline is shared (read-only, cite
everything, flag confidence), only the sweep differs:

1. **`closeout` mode** — walk the closed work item(s): all fields, the full
   comment thread, linked Confluence pages, linked issues (blocks/relates),
   and attachments' names (not contents, unless the user opens them). Record
   what was actually done and decided, distinguishing outcome statements from
   plan statements — a comment saying "we will" is not evidence that "we
   did."
2. **`modernize` / `tree-audit` mode** — inventory the target page tree: per
   page, title, parent, labels, last-updated date, contributors count, and a
   structure sketch (headings). Collect staleness signals per
   `../reference/documentation-standards.md` (age past the doc type's
   threshold, dead links, orphaned position). `tree-audit` sweeps the full
   tree; `modernize` sweeps the pages the user scoped.
3. **`sad-update` mode** — gather the delivered feature's evidence: the
   feature's Jira items, linked design docs or ADRs, and (where a repo is in
   scope and Copilot is the engine) the delivering change's repo context.
   Identify which existing SAD pages and diagram sources reference the
   touched components.
4. **`meeting` mode** — distill the screened transcript/summary into:
   decisions made, actions agreed, topics discussed, and Jira items
   explicitly mentioned (resolve mentioned keys against Jira to confirm they
   exist). Separate decisions from discussion; carry no attributions the
   Stage 01 screen did not approve.
5. **Dossier assembly** — every entry carries its source link (Jira key,
   page URL, transcript line reference) and a confidence note where the
   evidence is indirect. Gaps the evidence cannot answer are listed
   explicitly as **open evidence questions** — Stage 3 turns these into open
   sections rather than letting them be silently guessed.

This stage is read-only on every platform it touches.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Evidence dossier (header: job type, sources swept; body: cited entries in the job type's mode shape) | Stage 03 | structured markdown |
| Open evidence questions list | Stage 03 | list, each with what's missing and why |
| Mentioned-Jira-items list with existence confirmed (meeting mode) | Stages 03, 06 | list of keys + summaries |

## Verify

Cross-stage trace: the dossier Stage 02 hands forward answers to the job type
Stage 01 confirmed. Check that the dossier header's job type equals Stage
01's confirmed selection, and that every dossier entry carries a resolvable
source link — an uncited entry is treated as an open evidence question, not
evidence. The failure this catches is Stage 03 planning documents from
unsourced or wrong-mode material. Running this check leaves a one-line result
in the run's decision log.

- [ ] Dossier header names Stage 01's job type
- [ ] Every dossier entry has a source link that resolves (spot-check at
      minimum the entries Stage 03 builds work-order lines from)
- [ ] Outcome vs. plan statements distinguished (closeout mode)
- [ ] Staleness signals collected per the standards baseline (modernize /
      tree-audit modes)
- [ ] Mentioned Jira keys resolved against Jira (meeting mode)
- [ ] Open evidence questions listed explicitly — none silently absorbed
- [ ] No write occurred on any platform touched

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** light — constrained execution against a confirmed job type;
  the dossier is inspected for coverage and citation, not re-derived.
- **Evidence:** the dossier itself (cited) and a one-line entry in the run's
  decision log.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo — the sweep reads Jira and
  Confluence natively and the gathered content stays in Atlassian. For
  `sad-update` repo context, Copilot reads the repo side and contributes via
  a handoff (mirroring-protocol §5); the Confluence/Jira sweep stays on Rovo.
- If gathered evidence surfaces `confidential` content (customer detail in an
  incident record, credentials in a comment), stop the sweep, flag it, and
  re-scope with the user before continuing.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
