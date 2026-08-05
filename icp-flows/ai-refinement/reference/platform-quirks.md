---
id: ai-refinement-platform-quirks
title: "Platform Quirks — AI Refinement"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-05
updated: 2026-08-05
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
---

# Platform Quirks — AI Refinement

**Status: observed once, not yet a broad pattern.** Everything below is drawn
from a single live Rovo Chat session (2026-08-04) refining a Feature with a
child Spike and closing a duplicate — not from repeated on-engine runs. Treat
the specific quirks named here as illustrative examples of the *class* of
problem, not an exhaustive or permanent list: platform behavior changes
between runtime versions, and Copilot has not produced any of this file's
observations at all (no Copilot adapter has had a live invocation yet — see
`HUB.md`'s Known gaps). Add to this file as future runs surface new
platform-specific behavior; this is where that kind of finding belongs,
distinct from the flow-design amendments in `ai-refinement-hybrid.md`. The
rules that respond to these observations (reading write-API stubs before the
first call, building content and committing in one execution block) live in
`ai-refinement-hybrid.md`'s `commit_boundary_hardening` house amendment and
Stage 06's Process — this file is the concrete, engine-specific evidence
behind that rule, not the rule itself.

## Session state volatility

Observed on Rovo: Python variables built in one execution block (full ADF
content structures for a Feature's description, acceptance criteria, scope,
dependencies, and risks) were undefined in the next execution block — the
agent had to rebuild all of it from scratch, wasting a turn and roughly
doubling the token cost of constructing that content. The runtime's execution
state is not guaranteed to persist across turns, particularly across time
gaps or when the platform's own tool inventory changes mid-session (see
"Tool inventory churn," below).

**What to do about it:** build all content for a work item and make the
commit call in a single execution block wherever the platform allows it,
rather than constructing content in one block and committing in a later one.
Where a single block genuinely isn't possible, serialize the intermediate
content to disk (Rovo exposes `/tmp`) as a backup before moving to the next
block, and never assume a variable from an earlier block still exists —
check before use rather than letting a reference error be the first signal.

## API parameter discovery

Observed on Rovo: three write calls failed on the first attempt because the
agent guessed a parameter name from common REST-API convention instead of
reading the platform's actual function stub first:

| Function | Guessed | Actual |
|---|---|---|
| `get_create_issue_metadata` | `project_ids` | `project_id_or_key` |
| `create_issue_link` | `type_name` | `type` |
| `transition_issue` | `transition_id` (a bare value) | `transition` (a dict) |

Each cost a full retry cycle: call, error, read the stub, retry. The
underlying rule — read the function signature for every write API before the
first call of the session — is `api_preflight`, part of the
`commit_boundary_hardening` house amendment in `ai-refinement-hybrid.md`,
cited from Stage 06's Process. This table exists to accumulate the concrete
parameter-naming differences observed across engines as they're found, so a
future session doesn't rediscover the same mismatch from scratch even though
the preflight rule would catch it either way — a known quirk found here can
be treated as a hint, not just a thing the preflight step will eventually
surface again.

## Tool inventory churn

Observed on Rovo: the runtime added and removed roughly 50 tool integrations
multiple times over the course of one session, each add/remove cycle
injecting a block listing every available tool name into context — pure
overhead with no task value, and enough of it (an estimated 10,000–15,000
tokens across the session) to be a meaningful fraction of the session's
`session_budget_checkpoint` consumption (`ai-refinement-hybrid.md`).

**What to do about it:** don't cache tool-availability assumptions from
earlier in the session — if a previously-available action fails
unexpectedly, treat a possible inventory change as a plausible cause and
re-check rather than assuming the action itself regressed. There is no
flow-level mitigation for the token cost of the churn itself; it's a runtime
behavior outside this pipeline's control, recorded here so it isn't mistaken
for a flow defect if seen again.

## Changelog

- **1.0** (2026-08-05) — Initial file, drawn from the 2026-08-04 Rovo session
  retrospective. See
  `../decision-log/2026-08-05-rovo-session-friction-fixes.md`.
