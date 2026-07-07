---
id: sp-intake-triage-assistant
title: "Skill Primer Brief — Intake Triage Assistant"
type: skill-primer-brief
artifact-version: "1.0"
status: dead
truth-level: to-review
created: 2026-07-02
updated: 2026-07-07
owner: operator
source: human+ai
data-class: public
related: ["[[flow-foundry-spec]]", "[[skill-foundry-spec]]"]
---

# Skill Primer Brief — Intake Triage Assistant

> **Dropped 2026-07-07 — not skill-worthy at current volume.** Kept for
> record per `governance-and-audit.md` §7; not built. Reason and
> re-file condition: `decision-log/2026-07-07-skill-starter-triage-drop.md`.

## Purpose

Assist the triage front door shared by both foundries: classify an incoming starter (primer-brief / foreign material / not-worthy / wrong foundry), and for foreign material, pre-populate the intake vetting checklist with findings for the human vetter to confirm.

## Triggering intent

- **Fires on:** a new item landing in either backlog; "triage this," "classify this starter."
- **Does not fire on:** building the artifact (that's the foundry method), passing/failing the vetting checklist (human verdict — the assistant gathers evidence, it does not decide), or exploring whether an idea is worth pursuing.

## Method sketch

1. Read the starter; classify against the four triage categories of the relevant foundry spec, with a stated reason.
2. Foreign material: fetch/read the source, then draft checklist evidence — provenance findings, maintenance signals, license identification, a first-pass prompt-injection read with quoted suspicious passages.
3. Recommend a routing (including "drop" or "this is a flowspace, not a skill") and draft the decision-log entry for the human to confirm or amend.

## Inputs and data boundary

Reads backlog folders and, for foreign material, external sources. Max data-class: internal. Engine: **Rovo agent** when backlogs live in Confluence (native), Copilot adapter for the mirror side.

## Demand source

Step 1 of both foundry specs — triage recurs on every starter, and the vetting-evidence gathering is the most mechanical, most skippable-under-pressure part of the gate. Assisting it makes the gate cheaper, which makes it actually run.

## Definition of done

Against a seeded set of six starters (2 clean briefs, 2 foreign — one with an embedded prompt-injection attempt — 1 not-worthy, 1 wrong-foundry), classifications match the operator's, and the injection attempt is quoted and flagged, not just labeled.
