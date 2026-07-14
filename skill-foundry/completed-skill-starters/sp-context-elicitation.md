---
id: sp-context-elicitation
title: "Skill Primer Brief — Context Elicitation"
type: skill-primer-brief
artifact-version: "1.1"
status: living
truth-level: verified
created: 2026-07-03
updated: 2026-07-07
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.1"
data-class: public
related: ["[[ai-refinement]]", "[[platform-stakeholder-register]]"]
---

# Skill Primer Brief — Context Elicitation

## Purpose

Extract structured problem context from a user through a guided question
sequence — producing confirmed problem statements, business outcomes, value
statements, and a stakeholder tag list suitable for Jira work item fields.
Replaces ad-hoc "tell me about the problem" conversations that yield vague,
unrefinable inputs.

## Triggering intent

- **Fires on:** Stage 02 of the `ai-refinement` flowspace; "frame this problem,"
  "help me articulate what this work item is for."
- **Does not fire on (near-misses):** scope or dependency definition (that's
  `scope-dependency-mapper`), refining individual schema fields (that's
  `field-refinement-cadence`), or open-ended discovery interviews with no target
  work-item schema — this skill always elicits *toward* a selected schema.

## Method sketch

1. Structured question sequence — ordered prompts progressively narrowing from
   broad context to specific problem/value statements.
2. Stakeholder sweep — walk `platform-stakeholder-register.md`, tag the entries
   whose needs or limits define the item, and use each tagged entry's "what they
   value most" to prompt for unvolunteered requirements.
3. Pushback patterns — detect and reframe vague, circular, or overly broad
   answers (e.g., "it needs to work better" → ask for specific failure modes);
   driven by the persona's `challenge_incomplete_requirements` behavior.
4. Confirmation UX — present drafted fields, obtain explicit yes/no per field.
5. Multi-type awareness — adapt depth to the work item type (`solution_epic`
   needs `business_outcomes`; `feature` does not).

Known failure mode to guard: accepting the user's first framing without the
stakeholder sweep — items framed by one voice are how conflict axes detonate
mid-build.

## Inputs and data boundary

Reads the selected work-item schema (from `ai-refinement` Stage 01), the
platform stakeholder register, and the user's conversational input. Max
data-class: internal. Engines: both Rovo and Copilot (the flowspace runs on
either surface).

## Demand source

`ai-refinement` flowspace, Stage 02 (Context & Problem Framing) — the source doc
defines *what* fields exist but no protocol for *how* to draw them from a user
who hasn't articulated them yet. The stage's `CONTEXT.md` carries this brief's id.

## Definition of done

- Produces a problem statement from a user who starts with only a vague idea.
- Detects an over-abstract answer and applies a specific pushback pattern.
- Confirmed `problem_statement`, `business_outcomes` (solution_epic), and
  `customer_business_value` fields pass Stage 05 validation without rework, and
  every stakeholder tag resolves to a register entry.
