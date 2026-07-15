---
id: sp-servicenow-kb-commit
title: "Skill Primer Brief — ServiceNow KB Commit (DEFERRED)"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.4"
data-class: public
related: ["[[documentarian]]", "[[doc-type-registry]]", "[[sp-confluence-page-commit]]"]
---

# Skill Primer Brief — ServiceNow KB Commit (DEFERRED)

> **Deferred at filing (2026-07-15) — do not build yet.** No sanctioned
> ServiceNow integration exists for any engine in the current toolchain, and
> the repo's surface story is Atlassian-only today. Filed now so the
> documentarian flowspace's designed-for ServiceNow gap stays registry-
> visible instead of living only in prose (the `sp-mirror-drift-checker`
> precedent: a brief can hold a place without authorizing a build).
> Prerequisites to lift the deferral, in order: (1) the operator confirms a
> sanctioned ServiceNow integration and records it on this brief; (2) the
> `kb-article` field mapping in `reference/doc-type-registry.md` is ratified
> against the real instance; (3) `confluence-page-commit` is built and
> verified — its commit discipline is this skill's template and its staged
> output (`servicenow-pending` pages) is this skill's input queue.

## Purpose

Commit a validated, `kb-article`-typed document to ServiceNow as a
`kb_knowledge` record — closing the loop for documents that Stage 06
currently stages on Confluence with the `servicenow-pending` label.

## Triggering intent

- **Fires on (once built):** documentarian Stage 06, ServiceNow-destined
  work-order lines; and a backlog-drain mode over existing
  `servicenow-pending` pages once the write path exists.
- **Does not fire on:** Confluence writes (`confluence-page-commit`); KB
  content authoring or validation (upstream stages); any ServiceNow record
  type other than `kb_knowledge`; incident/change/request workflows —
  those are ITSM operations, not documentation custody.

## Method sketch

- Map the document per the registry's `kb-article` mapping: title →
  `short_description`, body → `text` (translated to the KB's expected
  markup), review-by → `valid_to`, category per the instance's taxonomy;
  land in `workflow_state: draft` — ServiceNow's own KB approval workflow
  owns publication, this skill never force-publishes.
- Same commit discipline as `confluence-page-commit`: rendered dry-run
  preview, explicit per-document approval, partial-failure honesty,
  version-safe updates.
- On success, flip the Confluence staged page's label
  `servicenow-pending` → cross-link both surfaces, and update the registry
  row's surface field.
- Failure modes to guard: markup mangling between Confluence storage format
  and KB HTML; duplicate KB records on retry; bypassing the instance's KB
  approval workflow.

## Inputs and data boundary

Receives the validated `kb-article` document and its registry row; writes
one `kb_knowledge` record via the sanctioned integration (to be named on
this brief when it exists). Max data-class: `internal`, and subject to the
sanctioned-tool matrix's ruling on ServiceNow at that time. Engine:
undetermined — depends entirely on which integration is sanctioned
(Rovo-side connector, MCP-style integration, or an intermediate export);
the build decides when the deferral lifts.

## Demand source

Documentarian flowspace, Stage 06 (`06-commit-and-link/CONTEXT.md`), step 6
— the declared ServiceNow designed-for gap, flagged at scaffold triage
(`flow-foundry/review-flowspaces/documentarian/decision-log/2026-07-15-scaffold-triage.md`).

## Definition of done

(Assessed when the deferral lifts.) On a test KB category: a staged
`kb-article` page lands as a draft `kb_knowledge` record whose rendered body
matches the approved preview, `valid_to` matches the registry row's
review-by, the record enters the instance's normal KB approval workflow
(never published directly), the Confluence page and registry row are
cross-updated, and a forced retry does not create a duplicate record.
