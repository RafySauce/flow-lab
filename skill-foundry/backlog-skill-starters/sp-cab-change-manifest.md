---
id: sp-cab-change-manifest
title: "Skill Primer Brief — CAB Change Manifest"
type: skill-primer-brief
artifact-version: "2.0"
status: living
truth-level: to-review
created: 2026-10-28
updated: 2026-10-28
owner: operator
source: human+ai
generated-by: ecosystemic-thinking-partner
generated-by-version: "0.7"
data-class: public
related: ["[[servicenow-ticket-ingest]]", "[[m365-accomplishments-gatherer]]"]
---

# Skill Primer Brief — CAB Change Manifest

> Intake path 1 for the skill-foundry: crystallized intent, written before authoring starts. Built as `../review-skills/cab-change-manifest/`. This brief contains no employer content.

## Purpose

Build a **fully fleshed-out change manifest** for an upcoming CAB: the changes in scope, the problems they carry, and the story behind each one, assembled from ServiceNow plus related context in Jira, Confluence, email, and Teams meetings. The manager uses it to prepare, and can hand a **CAB-ready copy** to CAB itself. Replaces the manual pre-CAB walk through the ServiceNow change list and the hunt for "what was this one about, who agreed to it, and what's still open."

## Triggering intent

Invoke on:
- "Build the CAB manifest," "prep me for CAB," "what's on CAB for my group," "pull together the changes for Thursday's CAB with context."
- "Manifest of changes for [assignee / group] between [dates]," "CAB manifest for anything about [keyword]."
- A manager opening the agent on CAB-prep day with no further phrasing.

Do **not** invoke on (near-misses):
- Drafting, reviewing, or improving an individual change request's content (that was the change-readiness idea, deliberately not pursued).
- Post-incident review or incident analysis.
- Running or minuting the CAB meeting itself.
- Flow or throughput analysis of a service's change history; that is `statik-adoption` / `flow-capability-analyzer`.
- Normalizing a ServiceNow table for flow evidence; that is `servicenow-ticket-ingest`.
- A general search of Jira, Confluence, mail, or Teams not tied to change requests ("find everything about service X").
- Evaluating a person's or team's change record (performance, reliability scoring).

## Method sketch

1. **Ask for scope, then confirm it.** At the start of every run, ask for:
   - **Time window:** defaults to the next CAB date's agenda; can be any date range of planned windows.
   - **Assignment group:** defaults to the manager's remembered group(s); can be any group.
   - **Assignee:** optional, narrows to one person's changes.
   - **Keywords:** optional, narrow the change list (matched in short description, service, or CI name) and are added to the context search keys.

   Filters combine (AND). At least a window plus a group or assignee is required. On first run also ask for the **CAB lead-time cutoff** (check D) and remember it with the default group. State the resolved scope back in one line before pulling anything. If the engine cannot persist defaults, ask each run and say so.
2. **Pull the changes, read-only.** Pull the in-scope change requests, limited to the permitted fields below. For check A, also pull every other change with a planned window overlapping the in-scope ones, since collisions can come from outside the scope. Borrow the confirm-the-field-map mechanics from `servicenow-ticket-ingest` (present the map, never auto-accept it) rather than calling that skill.
3. **Screen** each in-scope change:
   - **A. Overlap:** another change touches the same CI or business service with an overlapping planned window. The other change is shown only as number, window, service, and owning group.
   - **B. Freeze conflict:** the planned window intersects a **ServiceNow blackout schedule** that applies to the change's CI or service, or a global one. Maintenance schedules are not a freeze.
   - **D. Emergency or late:** the change type is emergency or expedited, or it was **submitted after the fixed lead-time cutoff** before its CAB date. [NEEDS INPUT: the cutoff value; asked and remembered on first run]
4. **Gather related context, read-only, per source.**
   - **Probe first.** For each of Jira, Confluence, Outlook mail, and Teams meetings, check whether the engine can reach it. An unreachable source gets a declared skip, never guesswork, and never reads as "no context."
   - **Keys:** every source is searched by **change number** and the user's **keywords**. Jira and Confluence are also searched by **business service name**. Mail and Teams are never searched by service name alone, because they are the noisiest and most sensitive sources.
   - **Window:** from the earliest submitted date in scope to the CAB date.
   - **Surfaces:**
     - **Jira:** issues and epics that name the change number or keywords, or are linked to it.
     - **Confluence:** pages that name the change number, keywords, or service (designs, release notes, comms plans).
     - **Mail:** the running manager's own mailbox only.
     - **Teams meetings:** recaps, transcripts, and meeting chat only for meetings the running manager attended. Ad-hoc chats and channels are out.
   - **Filters before reading.** Mail and Teams apply the mandatory exclusions (HR, medical, personal, compensation) plus anything the manager names. Threads and meetings that match are excluded before their content is read; only their count is kept. Never a whole-mailbox, all-meetings, whole-space, or whole-project sweep. Widening (another mailbox, a longer window) is proposed and confirmed first.
5. **Distill into manifest entries.** For each change, sort its context hits into the fields of the manifest entry (see Output). Each hit becomes a one-line paraphrase plus a resolvable reference, labeled **explicit** (names the change number) or **inferred** (matched by keyword or service). Source text is never pasted. Rules that are easy to get wrong:
   - **The excluded-field list follows the content.** If a Jira issue, page, mail, or transcript carries implementation, backout, or test steps, work notes, IPs, hostnames, or configurations, the paraphrase names what the item is, never what it says. A runbook page is cited as "runbook page for the service."
   - **A decision needs a decider.** "Approved" or "agreed" is recorded only where a recap or mail shows who agreed (by role). Attendance or a CC is not approval.
   - **Colleagues appear by role or team only**, as owners, requesters, or approvers. Never characterize or evaluate anyone.
   - **Screen strictest on mail and Teams; halt on high-class content.** If an item surfaces `confidential` or `restricted` content (customer data, credentials, security architecture detail), drop it, flag it without repeating it, and tell the manager. A pulled-in HR or personal item is a filter failure: drop it and say the filter missed.
   - **Context informs, it never decides.** Context never adds, removes, or changes a check result.
6. **Manager review (the gate before anything leaves).** Present the **working manifest** in Copilot chat. The manager confirms, edits, or drops each context line. Inferred items are unconfirmed by default.
7. **Produce the CAB-ready copy** only after review. It carries ServiceNow fields, check results, and confirmed context lines. Mail- and Teams-derived lines appear as the manager-confirmed paraphrase with the source named only by kind ("per change-owner email, 10/24"), with no references, because CAB cannot open a manager's mailbox or meetings and should not see their contents. Jira and Confluence lines keep their references. Unconfirmed and inferred-but-unreviewed lines never appear. Output as a Word document the manager saves and shares. [Default taken: Word, since the audience is at the employer]
8. **Report gaps honestly.** Every manifest ends with a source-status line ("Jira: searched, 6 items. Confluence: not searched, no connector. Mail: searched, 3 items, 2 threads excluded by filter. Teams: searched, 1 recap."). Never present a skipped check as "no issues" or a skipped source as "no context." "Searched, nothing found" and "not searched" are always worded differently.

## Output: the manifest

**Top: problems.** Every A/B/D flag, citing change numbers and the check tripped.

**Then: summary table.** Number, short description as written, window, service, assignment group, risk, impact, state, flags.

**Then: one entry per change,** flagged changes first:
- **Header:** the ServiceNow permitted fields.
- **Why:** the purpose and driver, paraphrased from linked Jira work or Confluence pages.
- **Linked work:** Jira issues/epics and their status.
- **Documentation:** Confluence pages by kind (design, release note, comms plan, runbook), cited, never summarized beyond their kind.
- **Decisions and approvals:** who agreed, by role, from where (recap, mail).
- **Open items and concerns raised:** unresolved questions or risks raised in Jira, mail, or meetings, paraphrased.
- **Stakeholder comms:** whether a notice went out, per the context found.
- **Checks:** A/B/D results for this change.
- **Context gaps:** fields with nothing found, worded as "nothing found in [sources searched]."

**End:** the count of out-of-scope changes screened for overlap, and the source-status line.

Quality bar: every flag traces to change numbers and every context line to a reference (working copy) or a confirmed paraphrase (CAB copy). No silent skips. Problems and table read in two minutes; each change entry in under one.

Known failure modes: false "all clear" when a source is missing; overlap noise from broad CIs (a CI-class exclusion list may be needed); quoting fields outside the boundary; correlation noise from common keywords and service names (hence the inferred label and review); context leaking excluded content through a summary of a runbook, mail, or transcript; reading attendance as approval; **mail or meeting content reaching CAB without the manager confirming it**; and a skipped source read as "nothing related."

## Inputs and data boundary

- **Sources:**
  - ServiceNow change requests (required) and blackout schedules (required for B; declared skip otherwise).
  - Jira, Confluence, the running manager's Outlook mailbox, and Teams meetings they attended (each optional; used only where the tenancy connects it to the engine; declared skip otherwise). The skill validates its own read access to every source at the start of each run and reports confirmed, denied, or no connector (decided 2026-10-28).
- **ServiceNow permitted fields:** number, short description, type, state, planned start/end, CI and business service, assignment group, assignee, risk, impact, CAB date, submitted date. Blackout schedules: name, window, and scope.
- **ServiceNow excluded, never read or quoted:** implementation plan, backout plan, test plan, work notes, justification text, attachments, and CI attributes (hostnames beyond the CI name, IPs, configurations). Decided 2026-10-28: plans stay out of the manifest, including the CAB copy.
- **Context sources, what may be shown:** title or subject, type, status, owner by role or team, date, a one-line paraphrase, and (working copy, plus Jira/Confluence in the CAB copy) a reference. Never shown: pasted body text, transcript quotes, mail quotes, attachments, content of the excluded kinds above, and anything screened out as confidential or restricted.
- **Short descriptions** pass through as written.
- **Max data-class handled:** internal, after screening. Raw mail, Teams, Jira, and Confluence content may hold confidential material; it is screened out before anything is shown, and never stored by the skill.
- **Engine:** Microsoft Copilot (agent). Copilot can reach ServiceNow at the employer (operator, 2026-10-28). Mail and Teams through Microsoft 365; Jira and Confluence only through sanctioned connectors. Runs only in employer tenancy.
- **Writes:** none to any source system. Nothing is commented, linked, flagged, moved, or sent. The only file is the CAB-ready Word copy, which the manager saves and shares themselves.

## Demand source

Operator-raised on 2026-10-27 in a flow brainstorm for the infrastructure group, as a quick win over a fuller change-readiness packet that was set aside as too sensitive. Widened by the operator on 2026-10-28 into a full manifest with run-time scoping, four context sources, and a copy for CAB.

## Decisions (2026-10-28)

- **Goal (v2.0):** a full change manifest for CAB prep that can also be given to CAB. Supersedes the v1 private briefing.
- **Scope asked at run time:** time window, keywords, assignee, assignment group. Area default = assignment group, remembered.
- Freeze source = ServiceNow blackout schedules.
- Late = submitted after a fixed lead-time cutoff before CAB; value pending, asked and remembered on first run.
- Short descriptions pass through as written.
- **Context sources:** Jira, Confluence, the manager's own mail, and Teams meetings the manager attended, searched on change number and keywords (service name too for Jira/Confluence), cited, never pasted.
- Checks: overlap (A), freeze conflict (B), emergency/late (D). Context never changes a check.
- **Defaults taken, pending your view:** the manager reviews every context line before a CAB copy exists; mail and Teams lines reach CAB only as confirmed paraphrase without references; CAB copy is Word; still a single skill with a built-in review step rather than a flowspace.
- **Plans stay out (decided):** "fully fleshed out" means what, when, who, why, risk, checks, and context. No implementation, backout, or test plan content, and no plan-presence flag.
- **Non-goals:** checking whether a test or backout plan exists (C) and risk-versus-impact sanity check (E); cross-service dependency mapping; editing or commenting on any change or context item; general search of Jira, Confluence, mail, or Teams; ad-hoc Teams chats and channels; shared mailboxes; posting to Teams or sending email; evaluating people or teams.

## Definition of done

Scope and checks:
- On every run the skill asks for window, group, assignee, and keywords, applies defaults, and restates the resolved scope before pulling.
- A keyword filter narrows the change list and appears as a context search key; an assignee filter returns only that person's changes.
- Live test against one real upcoming CAB for one manager, run in tenancy: every flag maps to real change numbers, and the manager confirms none of their real concerns were missed.
- A seeded collision (including one from outside the scope), a seeded blackout conflict, a seeded emergency change, and a change submitted one day after the cutoff are each caught.
- On first run the skill asks for the default group and cutoff; on the second it does not (or says it cannot remember).
- With blackout schedules unreachable, check B is reported as not run, not as clear.
- A test change whose backout plan and work notes contain an IP and hostnames produces a manifest where neither appears.

Context:
- Seeded Jira and Confluence items naming the change number appear as explicit, cited lines; one matched only by service name is labeled inferred.
- A seeded mail and a seeded Teams recap naming the change number appear as paraphrase with references in the working copy; an HR-tagged thread and a meeting the manager did not attend, both naming it, do not appear, and the excluded count shows the thread.
- A seeded recap where an attendee says nothing does not produce an approval; one where a role states agreement does.
- A seeded runbook page with a hostname and backout steps is cited by kind only.
- A seeded confidential item is dropped and flagged without repeating it.
- With Confluence absent, the status line says it was not searched, and no entry reads "nothing found" for Confluence.
- A seeded "on hold" Jira epic does not create a problem flag.

CAB copy:
- No CAB copy is produced before review; unconfirmed and inferred-but-unreviewed lines are absent from it.
- The CAB copy contains no mail or Teams references or quotes, only confirmed paraphrase named by kind.
- The CAB copy opens in Word with problems first, then the table, then entries.

---

## Connection Notes

- Sibling to the parked ideas from the same brainstorm: the Team API map (useful) and the monthly ops review (discuss further).
- The excluded-field list is load-bearing for the operator's sensitivity call that ruled out the change-readiness and post-incident flows. With context sources added it governs content in every source, and with a CAB copy it governs what leaves the manager's hands.
- The context step borrows the probe-then-skip, filter-before-read, strictest-mail-and-Teams-screen, and cite-don't-paste mechanics from `m365-accomplishments-gatherer`, without calling it.
- If the manifest grows (CAB-wide mode, more sources, multiple reviewers), revisit splitting it into a flowspace with one gather stage per source and a Correlate gate, the shape `accomplishments-digest` 2.0 took.

## Changelog

- **2.0** (2026-10-28) — Operator widened the goal to a fully fleshed-out change manifest usable by CAB: run-time scope (window, keywords, assignee, group), Teams meetings added as a source, keyword search across sources, a manifest entry structure, a manager review gate, and a CAB-ready Word copy. Boundary, failure modes, decisions, and definition of done rewritten.
- **1.1** (2026-10-28) — Four open items answered; Jira/Confluence/email correlation added as optional enrichment.
- **1.0** (2026-10-28) — First draft from the brainstorm.
