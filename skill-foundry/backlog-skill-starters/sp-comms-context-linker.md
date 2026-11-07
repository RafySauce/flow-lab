---
id: sp-comms-context-linker
title: "Skill Primer Brief — Comms Context Linker"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-11-07
updated: 2026-11-07
owner: operator
source: human+ai
generated-by: flow-foundry
data-class: public
related: ["[[comms-builder]]", "[[cab-change-manifest]]"]
---

# Skill Primer Brief — Comms Context Linker

> Filed from a Layer-3 gap in the `comms-builder` flowspace
> (`flow-foundry/review-flowspaces/comms-builder/`), Stage 2 (Link Source Records).

## Purpose

Pull the records a communication is about — a change, an incident, a
vulnerability record, a Jira item — into one cited context sheet, so drafts
quote real dates and impacts instead of someone re-typing them from three
tabs. Replaces copying fields by hand from ServiceNow and Jira into an
email.

## Triggering intent

- **Fires on:** `comms-builder` Stage 2 with one or more record numbers;
  standalone on "pull the comms-relevant details for CHG… / INC… / KEY-…".
- **Does not fire on:** a CAB-window sweep (`cab-change-manifest`); a
  portfolio ingest (`jira-portfolio-ingest`, `servicenow-ticket-ingest`);
  writing to any record.

## Method sketch

- Probe each source with one test read; declare live / paste / skip per
  source (pattern from `cab-change-manifest`).
- Pull a fixed field list per record: number and link, short description,
  state, planned window with timezone, affected services, stated impact,
  actions required of others, backout timing (time only), owning group.
- Enforce the response-plan data rule on every field: no exploit details,
  configurations, IPs, hostnames beyond service names, or control
  descriptions — replace with "see <record>".
- Cite every field to its record; never paste record bodies.
- List cross-source conflicts (e.g., differing dates) without resolving
  them.
- Failure modes to guard: inventing a window when the record has none;
  carrying a security detail through a free-text field.

## Inputs and data boundary

Record numbers from the framing brief. Reads up to `confidential` (security
and incident records); outputs at most `internal`. Engine: Copilot,
read-only — the operator runs this flow entirely in Copilot.

## Demand source

`comms-builder` Stage 2 (`02-link-source-records/CONTEXT.md`).

## Definition of done

Given a change and an incident record, the sheet carries every field in the
list or a declared gap, each cited; a seeded configuration string in a
record's notes never appears in the output; a date conflict between Jira and
ServiceNow is listed, not resolved; an unreachable source produces a paste
prompt, not a guess.
