---
id: decision-2026-10-28-cab-change-manifest-skill-build
title: "Decision Log — cab-change-manifest Skill Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-28
updated: 2026-10-28
owner: operator
source: human+ai
data-class: public
related:
  - "[[cab-change-manifest]]"
  - "[[sp-cab-change-manifest]]"
  - "[[servicenow-ticket-ingest]]"
  - "[[m365-accomplishments-gatherer]]"
---

# Decision Log — 2026-10-28 — cab-change-manifest Skill Build

**What was decided:** build `cab-change-manifest` from the primer brief
`backlog-skill-starters/sp-cab-change-manifest.md` v2.0, and stage it in `review-skills/` at
`truth-level: to-review`. The operator asked for it to be committed here
after the build.
**By whom:** agent, on direct operator instruction ("go for creation"),
after the operator answered the scoping questions and the plans-boundary
decision the same day.
**Triage classification:** skill-primer-brief, clean path. The brief was
written to v2.0 from the operator's answers and transcribed into the spec
without reopening settled exploration.

## Operator decisions carried in (2026-10-28)

- Goal widened from a private problem-first briefing (v1) to a full change
  manifest that can be given to CAB (v2.0).
- Scope is asked at run time: window, assignment group, assignee, keywords.
  The default area is the assignment group.
- Freeze source is ServiceNow blackout schedules. Late means submitted
  after a fixed lead-time cutoff, with the value asked and remembered on
  first run.
- Short descriptions pass through as written.
- Context sources are Jira, Confluence, email, and Teams meeting content.
- Plans stay out: no implementation, backout, or test plan content, and no
  plan-presence flag.

## Build decisions (agent defaults, not yet contested by the operator)

1. **Review gate before the CAB copy.** A manifest that leaves the
   manager's hands carries context from their mail and meetings. So no CAB
   copy exists until the manager has confirmed each line.
2. **Mail and Teams reach CAB as paraphrase only.** These lines carry no
   reference, link, or quote, because CAB cannot open the manager's mailbox
   and should not see its contents. Jira and Confluence keep references.
3. **Mail and Teams are never keyed on service name alone.** Searching them
   by change number and keywords only cuts noise and exposure.
4. **Teams is limited to meetings the manager attended.** Ad-hoc chats and
   channels are out.
5. **Word for the CAB copy.** The audience is at the employer.
6. **Still one skill, not a flowspace.** One person runs and reviews it.
   Revisit if a CAB-wide mode or multiple reviewers arrive.
7. **Review criterion 15 fails a run outright.** Any write to a source
   system fails the run, whatever the output quality.

## Revision 1.1 (2026-10-28, operator-instructed)

8. **The skill validates its own access.** Step 1 makes one minimal
   read-only test call per source (ServiceNow, Jira, Confluence, mail,
   Teams) before reading anything, and reports each as confirmed, denied,
   or no connector next to the scope line. This replaces the open question
   of which connectors exist with a runtime answer. Denied and no connector
   are worded differently, and neither is ever "nothing found." Review
   criterion 2 tests it.

## Open

- [NEEDS INPUT] The lead-time cutoff value. The skill asks for it on the
  first run.
- The five-point review (`foundry-spec.md` §4) and the live test are the
  operator's to run, as is promotion to `produced-skills/`.
