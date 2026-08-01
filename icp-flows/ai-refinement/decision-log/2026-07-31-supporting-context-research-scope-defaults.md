---
id: decision-2026-07-31-supporting-context-research-scope-defaults
title: "Decision Log — Supporting-Context Research Scope Defaults (Recency, OneDrive, Keywords, Time Frame)"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-31
updated: 2026-07-31
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
  - "[[start-here]]"
---

# Decision Log — 2026-07-31 — Supporting-Context Research Scope Defaults

**What was decided:** revise the seventh house amendment,
`supporting_context_research`, in place — no new amendment number. The
agent's default *proposed* research scope now comes from recency (the
requesting user's most recently created/touched Confluence spaces and Jira
projects, expanded to spaces/projects tied to any person or team the user
names or that appears in supplied material) instead of pure inference; a new
engine-conditioned OneDrive/SharePoint surface is proposed when the host
engine is Copilot and a live Microsoft Graph/OneDrive connector is present;
the user may supply search-term filters (technology stack names, app/system
codes, team names, team member names) as an addition to or explicit override
of agent-proposed terms; a default 6-month time-frame now bounds document
recency unless the user states otherwise; and a parent Confluence page or
OneDrive folder entering the session gets a quick one-level relevance pass
over its children rather than being treated as self-contained.
Confirm-then-hunt discipline is unchanged throughout — these are defaults
for the *proposal*, never an unconfirmed auto-search. **By whom:** agent, on
direct operator instruction (like the sixth and eighth amendments, this was
operator-raised, not discovered through on-engine defect feedback — the
flowspace still has no live-engine run to date). **What it affects:**
`reference/ai-refinement-hybrid.md` (1.5 → 1.6, `truth-level` stays
`to-review`), Stage 01 `01-intake-and-guardrails/CONTEXT.md` (1.14 → 1.15),
`HUB.md` (1.18 → 1.19: Supporting-context research section revised,
eleventh Known-gaps entry), `START-HERE.md` (1.0 → 1.1: new
OneDrive/SharePoint capability-probe row and degrade path),
`reference/confluence-instantiation-guide.md` (1.0 → 1.1, `verified` →
`to-review`: REC-02 extended, new §4a for the OneDrive/SharePoint deployment
checklist), and `reference/on-engine-validation-checklist.md` (1.2 → 1.3,
`verified` → `to-review`: new "Supporting-context research checks"
section). `context-elicitation` and `scope-dependency-mapper` are **not**
touched. Nothing is deployed to a live engine.

## Operator direction (verbatim intent)

1. Default the optional research step to probe the user's most recently
   created and touched Confluence, Jira, or OneDrive (if Copilot is running
   the session) spaces for additional context first, rather than a blanket
   approach across all of Confluence.
2. The user can also provide keywords to search for — technology stack, app
   codes, team names, or team members — and a time frame to limit the
   search; if no time frame is given, default to the past 6 months for
   document creation/recent updates.
3. Raised after plan review: think through how the documentation itself is
   searched — if a parent Confluence page is provided, do a quick check on
   its child pages for relevant information too.

Two design questions were resolved with the operator directly during
planning, before any file was touched:

- OneDrive should be built as a real new engine-conditioned surface (not
  skipped or deferred), gated on: host engine is Copilot **and** a live
  Microsoft Graph/OneDrive connector is actually present in the session
  (probed, never assumed).
- The recency-first default applies to **both** Confluence spaces and Jira
  projects — not Confluence alone, since Jira's nearest analog to a
  "space" is a project and the same blanket-sweep problem applies there.

Four further open questions were resolved with the operator before writing
any content:

- Revise the seventh amendment in place rather than add a new (ninth)
  amendment.
- Recency default = a fixed top-N (3), not an open-ended lookback window.
- "Touched" = the requesting user's own activity, plus any spaces/projects
  tied to a specific person or team the user names, or that is surfaced
  from supplied material such as a transcript or meeting summary.
- `context-elicitation` and `scope-dependency-mapper` are left untouched —
  no precautionary version bump.

## Design decisions

1. **Revision-in-place, not a new amendment.** The rule's shape — propose a
   scope, user confirms/trims/redirects, then hunt — is unchanged; every
   requested behavior changes *what gets proposed*, not *whether or how
   confirmation happens*. This mirrors the 1.4 precedent, which revised
   `mandatory_labels` in place when only the label's mechanics changed
   rather than splitting a new amendment off. Introducing a ninth amendment
   here would suggest a new confirmation rule exists where none does.
2. **Top-3, not an open lookback window.** A fixed, small count gives a
   bounded, predictable proposal size regardless of how active the
   requesting user has been — a window (e.g. "anything touched in the last
   30 days") could return one space or thirty depending on activity level,
   which is a worse default to hand the user for confirmation. Top-3 also
   composes cleanly with the named-person/team expansion below: the base
   proposal stays small, and named parties add to it rather than the whole
   proposal ballooning from an open window.
3. **"Touched" includes named-party expansion, folded into the existing
   keyword mechanism rather than a separate concept.** The operator's ask
   named "team names or team members" as a keyword category in the same
   breath as the recency default, and specifically called out material like
   a meeting transcript naming people. Rather than invent a second,
   parallel "who counts" mechanism, a named person or team — whether stated
   directly or surfaced from supplied material — expands the recency-based
   proposal to include spaces/projects associated with them. One list, two
   ways of arriving at candidates for it.
4. **OneDrive/SharePoint shares the Confluence/Jira defaults instead of its
   own.** Top-3 recency and the 6-month window apply identically across all
   three surfaces, folded into one scope confirmation rather than a
   surface-by-surface set of rules the user has to track separately. This
   also keeps the amendment's rule text from growing a third, divergent
   set of defaults for a surface that, per repo-wide search, has zero
   existing precedent to diverge from.
5. **OneDrive is strictly gated, never assumed.** Two independent
   conditions — host engine is Copilot, and a live Microsoft Graph/OneDrive
   connector is actually present — both have to hold, checked via
   `START-HERE.md`'s capability probe (extended with a new row for this).
   Either condition failing skips the surface and records it as a gap,
   mirroring the existing "no live Confluence/Jira query path" degrade this
   step already had. This is genuinely new ground for the repo — no
   OneDrive/SharePoint/Microsoft Graph reference existed anywhere before
   this change — so the gating stays conservative by design.
6. **Child-page/child-folder sweep stays one level deep by default.** A
   parent Confluence page (or OneDrive folder, once that surface exists)
   entering the session — user-supplied or hunt-surfaced — gets a quick
   relevance pass over its immediate children, with relevant ones folded
   into the same candidate list the user already selects from. Bounded to
   one level for the same reason as the top-3 space/project default:
   predictable, boundable scope. A full recursive tree crawl is available
   only as an explicit user-requested widening, identical to widening the
   hunt to more spaces or projects — never automatic, and never a separate
   approval step from the rest of scope confirmation.
7. **`context-elicitation` and `scope-dependency-mapper` are untouched.**
   Unlike the 2026-07-21 change (the first time either skill received a
   document set and research record at all, which justified a version bump
   as new consumers), this change doesn't alter the *shape* of what Stage
   01 hands downstream — still a typed/screened document list and a
   sought/found/selected/not-found research record, now simply extended
   with surfaces-searched, time-window, and sweep-result fields that both
   skills already consume generically. Neither skill's Method branches on
   how Stage 01 arrived at its proposal, so neither needs a content change
   or a gate re-run.

## Data-boundary reasoning

The OneDrive/SharePoint read surface is bounded identically to the existing
Confluence/Jira research surface: engine-native, read-only, results capped
at data-class `internal`, search scope user-confirmed before any query runs,
and every retrieved document (including child-page/child-folder sweep
results) passes the Stage 01 data-safety screen before entering the
session. The one addition specific to this surface is the capability gate
itself — read access extends to OneDrive/SharePoint only when both the host
engine is Copilot and a live Microsoft Graph/OneDrive connector is
confirmed present via `START-HERE.md`'s probe; absent either condition, no
read access is attempted and the surface is recorded as a gap, not silently
skipped without a trace.

## Remaining for the operator (the human gate)

1. Sign off the seventh amendment's revision (hybrid clipping back at
   `to-review`).
2. Confirm the top-3 count and the 6-month default window are the right
   concrete numbers for this pipeline's actual usage pattern — both were
   fixed based on the operator's stated preference for a bounded, predictable
   default over an open lookback window, but neither has run on-engine yet.
3. Grant the actual Microsoft Graph/OneDrive connector at Copilot
   instantiation if OneDrive/SharePoint support is wanted live — see the new
   §4a in `reference/confluence-instantiation-guide.md`.
4. Execute the extended REC-02 knowledge-scoping checklist (recency default
   can surface spaces/projects outside a fixed pre-approved list — decide
   whether a ceiling is needed) and the new "Supporting-context research
   checks" section of `reference/on-engine-validation-checklist.md` before
   the first live run.
5. No gate re-run is required for `context-elicitation` or
   `scope-dependency-mapper` — their `truth-level` and `artifact-version`
   are unaffected by this change.
