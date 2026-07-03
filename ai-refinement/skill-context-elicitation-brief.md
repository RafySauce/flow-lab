---
id: skill-context-elicitation-brief
title: "Skill Primer Brief — Context Elicitation"
type: skill-primer-brief
status: to-review
truth-level: to-review
created: 2026-07-03
updated: 2026-07-03
source: human+ai
data-class: internal
owner: rafael.torres
demanded-by: ai-refinement-stage-02
target-adapters: [rovo, copilot]
---

# Skill Primer Brief — Context Elicitation

## What This Skill Does

Extracts structured problem context from a user through a guided question sequence,
producing confirmed problem statements, business outcomes, and value statements
suitable for Jira work item fields.

## Why It's Needed

The `AI-Refinement-Hybrid.md` source doc defines *what* fields exist (problem_statement,
business_outcomes, customer_business_value) but provides no protocol for *how* to draw
that information from a user who may not have it articulated yet.

## Consuming Flowspace Stage

- `ai-refinement` → Stage 02 (Context & Problem Framing)

## Core Capabilities Required

1. **Structured question sequence** — ordered prompts that progressively narrow from
   broad context to specific problem/value statements.
2. **Pushback patterns** — detection and reframing of vague, circular, or overly broad
   answers (e.g., "it needs to work better" → ask for specific failure modes).
3. **Confirmation UX** — present drafted fields to user and obtain explicit yes/no
   before marking as confirmed.
4. **Multi-type awareness** — adapt question depth based on work item type
   (solution_epic needs business_outcomes; feature does not).

## Acceptance Criteria

- Must be able to produce a problem statement from a user who starts with only a vague idea.
- Must be able to detect when an answer is too abstract and apply a specific pushback pattern.
- We will know this is done when the skill can produce confirmed problem_statement,
  business_outcomes (solution_epic), and customer_business_value fields that pass
  Stage 05 validation without rework.

## Constraints

- Must respect the `technical_product_service_owner` persona's communication style
  (precise, analytical, structured, direct).
- Must not introduce PII or confidential data.
- Must work on both Rovo and Copilot surfaces.
