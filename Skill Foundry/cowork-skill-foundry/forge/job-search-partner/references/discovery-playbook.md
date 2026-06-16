# Discovery Playbook — Scout mode mechanics

Replaces the source repo's Danish job-portal CLIs (jobindex/jobnet/jobbank/
jobdanmark) with a live-search researcher sub-agent. The portal-CLI pattern is
documented at the bottom in case a dedicated portal tool ever earns its keep.

## State files (workspace, created on first run)

- `job-scout-state/seen-jobs-<M1|F1>.json` — everything ever fetched:
  `{"seen": {"<url-or-company+title>": {"title", "company", "url",
  "first_seen": "YYYY-MM-DD", "fit": "high|medium|low",
  "status": "new|skipped|evaluated|applied"}}}`
- `job-search-tracker.csv` — applications actually made: date, person, company,
  role, url, status, next-action. Shared file, `person` column separates M1/F1.

Dedupe rule: skip presentation of anything already in seen-jobs OR the tracker,
but still record fresh fetches to seen-jobs so the state stays complete.

## Query construction (from the profile, never about the person)

Build from: target roles × core skills × location/remote constraints. Phrase from
the role's side. Include one latent-discovery query per run when the profile
supports it (see career-profile-contract.md). Time-bound: last 14 days.

Example shapes:
- `site:linkedin.com/jobs "<role>" <region|remote> posted past week`
- `site:indeed.com "<role>" "<distinguishing skill>"`
- `"<niche skill>" jobs <region>` — catches niche boards the big two miss

**Never include the candidate's name, employer, or contact details in any query.**

## Sub-agent dispatch

Preferred: a Nimble-backed researcher sub-agent (`nimble:nimble-researcher` where
available, or the nimble-web-expert skill's search modes) — parallel searches,
structured results, fast. Dispatch with: the query list, the geography constraint,
the 14-day window, and the required output shape (title, company, location, date,
URL, 1-line requirements snippet). The sub-agent returns raw findings; fit
judgment stays with the main skill, against the profile.

Fallback (no Nimble): parallel WebSearch calls with the same queries; WebFetch
only the post-filter survivors.

## Filter → fetch → triage

1. Pre-filter on titles/snippets — drop obvious mismatches and dupes before
   fetching anything.
2. Fetch survivors; extract title, company, location, posting date, deadline,
   key requirements.
3. Quick fit per posting — **high** (core skills are the role), **medium**
   (adjacent), **low** (major gaps). Signal only; the full five-dimension
   evaluation happens in Apply mode.
4. Skip closed/expired postings and anything violating a deal-breaker gate
   (e.g. requires relocation) — note the skip reason in seen-state.

## Presentation

```
## New Matches — YYYY-MM-DD (M1)
Found X new (Y high, Z medium, W low).

| # | Fit | Title | Company | Location | Deadline | Link |

### High-match notes
Per high match: why it fits the profile, what to verify, red flags.
```

Close with: "Full evaluation on any of these?" → Apply mode on selection.

## Rules

1. Never fabricate a posting — live results with URLs only.
2. Dedupe is mandatory, both state files, every run.
3. Geography/deal-breaker gates apply at Scout time, not just Apply time.
4. Be frugal with fetches — snippets first, fetch only what survives.

## Appendix — the portal-CLI pattern (not wired, kept for reference)

The source repo wrapped each job portal in a small Bun/TypeScript CLI
(`.agents/skills/<portal>-search/cli`) with its own SKILL.md, credited to
Mikkel Krogholm (github.com/mikkelkrogsholm/skills). If a specific board ever
matters enough (poor search-engine coverage, rich filters), that per-portal-tool
pattern is the proven shape — build it as its own foundry intake, don't bolt it
onto this skill.
