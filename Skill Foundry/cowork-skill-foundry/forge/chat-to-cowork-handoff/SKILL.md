---
name: chat-to-cowork-handoff
description: "Creates a structured handoff document when a Claude chat conversation needs to continue in Cowork mode. Captures working state — goals, progress, decisions, context, and next steps — in a format tuned for the Cowork receiving session: recommends skills to invoke, notes workspace files to read, and includes a Cowork-priming resumption block. Adaptive structure matched to work type (Research, Writing, Planning, Building, Learning, Problem-Solving). Depth-sized to complexity. Triggers on: 'handoff to Cowork,' 'continue this in Cowork,' 'take this to Cowork,' 'save this for Cowork,' '/handoff.' Do NOT trigger for general summaries, Claude Code handoffs, or generic session continuations without a Cowork destination."
compatibility: "Chat session is the source; Cowork desktop app is the destination. No connectors required in chat. Writes a markdown handoff file. Frontier execution only."
---

# Chat-to-Cowork Handoff

This skill lives in chat, but it's building something for Cowork. The gap between Claude chat and the Cowork environment is real — chat has no workspace folder, no installed skills, no bash, no MCP connectors. A handoff that ignores that gap delivers the next session to a foreign environment without a map. This skill closes it.

The job is to capture the session's working state — goals, progress, decisions, failed approaches — in a format that a Cowork session can immediately act on: the right skills cued up, the right workspace files identified, the resumption instruction written for the environment that's receiving the work.

---

## When to Use

- The user explicitly asks to hand off to Cowork or continue the work there
- The conversation is approaching context limits with work still in progress
- The work has reached a planning → execution transition (chat explored; Cowork builds)
- The user signals they're stopping and wants to pick this up in Cowork

---

## Process

### Step 1: Classify the Work

Silently assess:

1. **Work type** — which category fits? (see Work Type Classification)
2. **Complexity tier** — how deep is the work? (see Depth Sizing)
3. **Active state** — what is the current task, and where did we stop?
4. **Accumulated context** — what was established that would be costly to rebuild?

### Step 2: Map the Cowork Environment

Before writing, identify what Cowork-specific context the receiving session needs:

- **Skills to invoke** — from what was discussed, which installed Cowork skills are relevant? (homelab-architect, execution-partner, job-search-partner, travel-planner, docx, pptx, ecosystemic-thinking-partner, etc.)
- **Workspace files** — were any files mentioned, created, or referenced? Note paths the receiving session should read first.
- **Connectors** — were any external tools, MCPs, or integrations discussed? Name them so the receiving session knows what to reach for.
- **Shell/bash work** — if the next steps involve running commands, note that the execution-partner skill handles terminal work in Cowork.

If none of these apply (pure writing or research with no tooling), keep the Cowork Setup section minimal.

### Step 3: Check for User Instructions

If the user specified what to include ("make sure to capture X"), incorporate it.

### Step 4: Clarify Ambiguities (Conditional)

**Skip entirely if the session state is clear.** Ask at most 2–3 short questions only when a genuine ambiguity would produce a materially different handoff:

- **Scope** — the session covered multiple topics and it's unclear which the handoff should cover
- **Decision status** — something discussed at length but not clearly resolved
- **Priority / direction** — multiple next steps are plausible and the ordering matters

Do not ask open-ended questions or questions already answered by the conversation.

### Step 5: Generate and Save

Build the document using the adaptive structure below. Save as a markdown file.

**Filename:** `YYYY-MM-DD-handoff-[brief-slug].md`  
**Save to:** the user's Cowork workspace folder if known; otherwise the desktop or working directory. The file should land where Cowork can read it on the next session open.

---

## Work Type Classification

Classify the session to the primary type. Pull in secondary-type sections when a session spans multiple.

| Type | Key sections |
|------|-------------|
| **Research / Investigation** | Objective, Findings So Far, Sources and Evidence, Open Questions, Gaps Remaining |
| **Writing / Drafting** | Objective, Current Draft State, Tone and Style Decisions, Structural Outline, Content Completed vs Remaining |
| **Planning / Strategy** | Objective, Options Considered, Decisions Made, Constraints, Current Plan State, Unresolved Questions |
| **Building / Technical** | Objective, Architecture Decisions, What Has Been Built, Technical Choices, File References, Issues Encountered, Remaining Implementation |
| **Learning / Exploration** | Objective, Concepts Covered, Key Takeaways, Remaining Topics |
| **Problem-Solving / Debugging** | Objective, Problem Description, Hypotheses Tested, What Worked / What Didn't, Remaining Approaches |
| **Mixed / General** | Universal structure + relevant type sections |

---

## Depth Sizing

Size to the complexity of the work. **Complete on decisions, rationale, and failed approaches; ruthless on everything else.**

| Tier | Word range | When |
|------|-----------|------|
| Light | ~300–600 | Simple, focused tasks near completion. Few decisions, minimal context to rebuild. |
| Standard | ~600–1200 | Moderate tasks with meaningful progress and several decisions. |
| Deep | ~1200–2500 | Complex work: many decisions, built-up domain knowledge, long iterative work. |
| Extended | 2500+ | Sparingly. Large decision chains or multiple interconnected workstreams. |

These are calibration guides, not fill targets.

---

## Handoff Document Structure

Follow this skeleton. Include sections that have content; omit empty ones. **Never include empty sections.**

```markdown
# Handoff: [Descriptive Title]

> **Resumption (Cowork):** Read this document. If workspace files are listed
> in Cowork Setup below, read them with the Read tool before doing anything
> else. Invoke the listed skills as you begin. Then confirm your understanding
> in 2–3 sentences before proceeding.

**Date:** [YYYY-MM-DD]
**Source:** Claude chat
**Destination:** Cowork
**Work type:** [Research / Writing / Planning / Building / Learning / Problem-Solving / Mixed]
**Status:** [In Progress / Paused / Nearing Completion / Blocked]

---

## Cowork Setup

**Skills to invoke:**
- [skill-name] — [why it's relevant to the next steps]

**Workspace files to read first:**
- [filepath or filename] — [what it contains that's relevant]

**Connectors likely needed:**
- [connector/MCP name] — [what for]

*(Omit any row that doesn't apply.)*

---

## Objective

[What we are trying to accomplish and why. The north star — enough context to
understand motivation and scope, not just the task.]

## Current State

[A precise snapshot of where the work stands right now — not a narrative of the
conversation. Not "we discussed the layout" but "the layout is finalised as a
two-column grid; the header is built; the footer is not."]

## Progress

[Concrete outputs and milestones accomplished this session.]

## Decisions Made

[Each decision with its rationale. Rationale prevents the receiving session from
relitigating settled questions or reversing a considered choice.]

- **[Decision]** — [Why this over alternatives]

## Approaches That Did Not Work

[Directions tried and rejected, with reasons. Prevents the most common failure:
the new session re-explores dead ends.]

## Project Context

[Stable background: constraints, preferences, domain knowledge established this
session that doesn't change between sessions. Only include when there is meaningful
context beyond the objective.]

## Open Questions

- [ ] [Specific question needing resolution — not a vague area]

## Next Steps

[Ordered and immediately actionable. The first item is the very next thing to do.]

1. [First action — specific and concrete]
2. [Second action]

## Key References

[Links, file names, or sources relevant to continuing. Only if meaningful.]
```

---

## Content Guidelines

**Include:**
- Tone, style, or voice decisions explicitly established during writing tasks
- Agreed structural outlines that guide remaining work
- Technical specifics (exact values, configurations) that would be hard to rediscover
- Source evaluations for research tasks — which sources proved useful and which didn't

**Exclude:**
- Conversational narrative — capture state, not history
- General knowledge — "we discussed how spaced repetition works" adds nothing; "decided on 2-day initial intervals" does
- Intermediate reasoning — capture conclusions and rationale, not every step
- Verbose tool output — summarise or reference, never reproduce
- Pleasantries and meta-discussion

---

## Quality Checklist

Before saving, verify:

- [ ] Cowork Setup is populated — skills, files, and connectors identified (or explicitly minimal)
- [ ] The resumption instruction primes Cowork behaviors, not generic chat behaviors
- [ ] A fresh Cowork session could continue without asking the user to re-explain anything
- [ ] Current State is a precise snapshot, not a vague summary
- [ ] Every decision includes its rationale; failed approaches are documented
- [ ] Next steps are specific and immediately actionable
- [ ] No empty sections, no narrative filler, no duplicated context
- [ ] Sized to the work: complete on decisions and rationale, lean everywhere else

---

## What This Skill Is Not

- **Not a general session summarizer** — the Cowork Setup section is not optional flavor; a handoff without environment orientation is just a summary
- **Not a Claude Code handoff skill** — Claude Code is a different environment with different file-reading and command patterns; those handoffs live in a different skill
- **Not a backup or archive** — captures working state for continuation, not a permanent record of the conversation
- **Not a substitute for Cowork memory** — if the user has `productivity:memory-management` installed, the handoff complements it; it does not replace persistent memory
- **Not a thinking-partner output** — if the work is still in exploration and no decisions have landed, a handoff is premature; say so and suggest continuing in chat first

---

## Changelog

- **0.1** (2026-06-14) — Initial build. Normalized from maaarcooo/claude-skills `handoff/SKILL.md` (foreign intake). Core structure preserved: work-type classification, depth sizing, adaptive skeleton, quality checklist. Extended for chat→Cowork: Cowork Setup section (skills/files/connectors), Cowork-priming resumption instruction, Process Step 2 (environment mapping), save-location guidance, Cowork-specific "What This Skill Is Not" entries.
