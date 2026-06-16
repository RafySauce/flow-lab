# Application Pipeline — Apply mode orchestration

The drafter-reviewer workflow, harvested from the source's `/apply` command and
re-grounded on docx/pdf output. Phases run strictly in order; Phase A's gate
(user approval) is never skipped.

## Token-efficiency rules (inherited, they work)

- Never re-read a file already in context from an earlier phase.
- Pass draft content to the reviewer **inline in its prompt** — a fresh-context
  agent should not be sent to re-Read files the orchestrator already holds.
- Run the verification checklist exactly once, at the end (Phase D). The reviewer
  critiques content; it does not duplicate verification.

## Phase A — Evaluate

1. Fetch the posting (URL) or take pasted text. Extract company, role, department,
   location, language.
2. Score against the profile using `evaluation-framework.md`. Check every
   deal-breaker gate first — a hard fail ends the evaluation with a clear "this
   violates X" rather than a softened score.
3. Present: skills match (with named gaps), experience match, culture fit,
   logistics pass/fail, career alignment, overall verdict
   (strong / moderate / weak fit).
4. If experience match scores below 50, warn that drafting would require
   extensive reframing — and that reframing has limits (writing-style.md).
5. **Ask: proceed to documents?** No → stop, offer to log the evaluation to
   seen-state as `evaluated`.

## Phase B — Draft

Read `writing-style.md` and `document-standards.md` if not already in context.
Build via the house docx skill (pdf skill for PDF output):

- **CV** — `applications/<company>/cv-<person>-<company>.docx`. Tailored profile
  statement, reframed bullets (emphasis, never substance), 2 pages.
- **Cover letter** — `applications/<company>/cover-<person>-<company>-<role>.docx`.
  Posting's language, named addressee when the posting provides one, ~1 page,
  forward-looking framing.

Keep both draft texts in working memory for Phase C.

## Phase C — Review (sub-agent)

Spawn one general-purpose reviewer agent. Its prompt carries:

- Role: "hiring-manager proxy — make this application as targeted and compelling
  as possible without letting a single unverifiable or stretched claim through."
- The job posting text, inline.
- Both drafts, inline (instruct: do not Read the files).
- The candidate's profile file path plus `writing-style.md` — the reviewer checks
  voice against the profile's self-assessment register (a collaborative profile
  shouldn't get solo-hero prose; a direct one shouldn't get hedged apologies).
- Tasks: research the company live (site, news, the specific team if named);
  critique targeting, voice, structure; list concrete revisions; flag any claim
  that smells stretched or unverified.

Reviewer output is advice, not authority. Anything company-specific it proposes
gets independently verified by the orchestrator before inclusion (writing-style
rule 5).

## Phase D — Revise, verify, present

1. Apply accepted critique; independently verify company claims kept.
2. Run the full checklist in `document-standards.md` against the **rendered
   documents** (open/inspect the output, not just the source content).
3. Present documents with checklist results and each flagged stretch-bullet as an
   explicit user decision: keep / soften / drop.
4. Offer tracker update (`job-search-tracker.csv`: date, person, company, role,
   url, status=applied, next-action).

## Phase E — Interview prep (on request)

`interview-prep.md`. Triggered by "prep me," an interview invitation, or offered
after an application is logged.
