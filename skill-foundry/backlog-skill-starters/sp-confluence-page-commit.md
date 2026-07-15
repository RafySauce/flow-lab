---
id: sp-confluence-page-commit
title: "Skill Primer Brief — Confluence Page Commit"
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
related: ["[[documentarian]]", "[[jira-commit]]"]
---

# Skill Primer Brief — Confluence Page Commit

## Purpose

The write side the skill portfolio doesn't have: create or update a
Confluence page — content, labels, page properties, parent position — plus
the planned Jira remote links, always behind a rendered dry-run preview and
explicit human approval. Modeled step-for-step on `jira-commit`'s commit
discipline (format translation, dry-run, confirm, report). Every existing
Confluence skill (`confluence-contribution-gatherer`) is read-only; this
brief closes that gap for the documentarian Stage 06 boundary.

## Triggering intent

- **Fires on:** documentarian Stage 06, once per work-order line, after a
  clean (or user-accepted) Stage 05 report and the open-section waiver gate.
- **Does not fire on:** Jira work-item creation (`jira-commit` — different
  platform, different payload family); ServiceNow writes (deferred —
  `sp-servicenow-kb-commit`); drafting or fixing content (upstream stages);
  registry/page-property custody stamping after commit (that's
  `doc-custodian`'s bookkeeping, though this skill sets the initial
  properties at creation); any commit without an explicit, this-document,
  rendered-preview approval — batch approvals fail the contract.

## Method sketch

- **Format translation gate** (the `jira-commit` precedent): validated
  Markdown → Confluence storage format before any write; raw Markdown
  syntax landing on a page is a defect.
- Dry-run preview in rendered form: content with open-section markers
  visible, title, space + parent position, labels, page properties, and the
  Jira remote links to be created. Explicit approval per document.
- Commit via native Rovo Confluence actions first; the sanctioned Atlassian
  integration is the fallback for engines without them.
- Create the remote links exactly per the Stage 03 plan — discovered links
  are proposed, never silently added.
- Update semantics: version-safe (fetch current version, apply, report the
  new version); a mid-flight edit by someone else is a stop-and-show, not a
  force-write.
- Report page URL, version, links created. Failure modes to guard: content
  drift between approval and write; partial commits (page written, links
  failed) reported as success; clobbering a concurrent human edit.

## Inputs and data boundary

Receives the validated document, waiver record, and the work-order line's
placement/link plan. Writes to the target Confluence space and Jira remote
links. Max data-class: `internal`. Engine: **Rovo** (native Atlassian
actions; content stays in Atlassian); Copilot-driven runs hand off at this
boundary per mirroring-protocol §5.

## Demand source

Documentarian flowspace, Stage 06 (`06-commit-and-link/CONTEXT.md`) —
Layer-3 gap flagged at scaffold triage
(`flow-foundry/review-flowspaces/documentarian/decision-log/2026-07-15-scaffold-triage.md`).

## Definition of done

On a test space: a `create` line lands a page whose rendered content matches
the approved preview exactly (no raw Markdown artifacts), with correct
parent, labels, properties, and both planned remote links; an `update` line
against a page edited mid-flight by another account stops and surfaces the
conflict instead of writing; a simulated link-creation failure after page
write is reported as a partial commit, not success. Nothing writes without
its recorded per-document approval.
