# Copilot Adapter — Export Log

Surface choice: **prompt file**
(`.github/prompts/export-log.prompt.md` in the internal mirror repo) —
command-shaped triggering intent ("export log," "export learnings"). Emit the
block below verbatim; a human merges it through normal PR review.

---

```markdown
<!-- Generated from export-log/SKILL.md v1.0 — do not edit here; edit the spec. -->
# Export Log (repo-wide — not scoped to any one flow)

Data boundary: max data-class `public` for the produced document; the source
session may be `internal` or higher.

You produce a sanitized feedback export of the current session, for a human
to place wherever it fits.

1. Recognize the trigger and confirm scope: the whole session, or a named
   portion. State back exactly what you're exporting before drafting.
2. Identify what ran by reading the session's own context — which
   flow(s)/skill(s)/stage(s) were actually invoked. Never guess from the
   user's stated intent if the transcript doesn't show it.
3. Capture friction and decisions, cited to the specific stage or skill each
   traces to. Invent nothing; an uneventful session gets a short, honest
   export.
4. Capture outcomes by reference (e.g., "created 12 Jira items via
   bulk-child-creation," keys/URLs where available) — never re-drafting the
   items' own content.
5. Run the data-safety screen before drafting further: strip personal names,
   customer references, hostnames, credentials, employer-identifying
   detail — same pattern as bulk-child-creation step 4 / Stage 01's
   data-safety guardrail. Target ceiling: public. Anything you cannot
   confidently scrub is named as withheld, never guessed and included.
6. Present the draft for review before finalizing — approve, edit, drop a
   section, or decline entirely. Never produce or share anything silently.
7. Output as a standalone Markdown document with valid provenance-spec
   frontmatter, data-class public, handed to the user directly. State near
   the top that placement is a human decision (decision-log entry, new skill
   primer brief, or flowspace gap-log entry) — you write this document to no
   repo path yourself.

Not this prompt's job: replacing a flow's own in-flow session summary (this
is additional, never a substitute); pasting the raw conversation as output
(summarize and screen instead); filing the export into a decision log, gap
log, or backlog starter yourself (hand off the document; placement is a
human decision).

Before presenting output, self-check against: fired only on explicit
request; flows/skills named are read from context, not assumed; every point
traces to something that happened, cited; screen ran before the draft was
shown, unscrubbable content named as withheld; user reviewed and could edit
or decline; output states placement is a human decision and was written to
no repo location.
```
