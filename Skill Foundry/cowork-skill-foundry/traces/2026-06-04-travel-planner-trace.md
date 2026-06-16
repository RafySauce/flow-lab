---
date: 2026-06-04
skill: travel-planner
foundry-version: "0.2.2"
triage-outcome: built
intake-type: bare-conversation-intent
---

# Trace — travel-planner build

## Triage decision

Intake arrived as bare conversation intent — no formal primer-brief from thinking-partner
or architect, no foreign material. The exploration phase happened inline in the same
conversation session: entry modes, outputs, and standing context were surfaced and resolved
before the build began. Intent was clear enough to build without a dedicated thinking-partner
session. Noted to user; proceeded.

**Why this is worth tracing:** the foundry's normal clean path assumes a primer-brief
pre-exists. Here the foundry absorbed the exploration role for a tightly scoped personal
skill where the user was present and iterating in real time. This is a legitimate shortcut
for personal/household skills where the exploration cost of a full thinking-partner session
would exceed the complexity of the skill itself. Hermes should recognize this pattern and
allow it, rather than requiring a primer-brief for every personal-productivity skill.

## Key design decisions

- **Two-mode structure (Ideation + Plan):** user confirmed both entry points are real. Plan
  mode is the workhorse; Ideation is occasionally needed and worth including.
- **Four outputs:** user confirmed all four (itinerary, packing list, logistics brief, trip
  doc). Heavy enough to push templates into references/output-templates.md rather than inline.
- **Traveler profile as external file:** medications and personal logistics kept out of the
  skill package entirely. Profile lives in workspace; skill reads it at invocation. This is
  the right call for sensitive/changing data and may be worth formalizing as a house pattern
  for personal skills.
- **F1 allergy elevated to top of every output:** EpiPen + peanut/tree nut allergy is
  life-safety. The skill treats it as a non-negotiable standing alert, not an optional item.
- **Frontier execution tier:** judgment-heavy throughout (cultural research, allergy-aware
  restaurant assessment, multi-variable logistics). Not a baseline candidate.

## Capability this skill embodies

**Standing-context personalization:** a skill that reads a maintained external profile and
uses it to make every output genuinely specific to the user — not a generic template with
names swapped in. The profile-read-at-invocation pattern is the mechanism; the skill is
an instance of it.
