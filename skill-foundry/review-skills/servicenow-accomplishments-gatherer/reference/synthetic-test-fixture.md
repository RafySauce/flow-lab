---
id: servicenow-accomplishments-gatherer-synthetic-fixture
title: "Synthetic Test Fixture — ServiceNow Accomplishments Gatherer"
type: reference
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
generated-by: skill-foundry
generated-by-version: "1.6"
data-class: public
related: ["[[servicenow-accomplishments-gatherer]]"]
---

# Synthetic Test Fixture

An invented export for the live-test gate. Every value is fictional: the
engineer is `ENGINEER-A`, the colleague is `ENGINEER-B`, and no real
person, tenant, or host appears. Feed it to the skill as an export for the
period 2026-03-01 to 2026-03-31, with the attribution fields below, and
compare the result to **Expected results**.

Attribution fields for this tenant: `incident` → `resolved_by`;
`change_task` → `closed_by`; `sc_task` → `assigned_to` at closure;
`problem_task` → `closed_by`. Reopens are inferred from `reopen_count`
only (no state-history table). Times are `YYYY-MM-DD HH:MM`.

| number | table | priority | state | opened_at | resolved/closed_at | attribution value | assigned_to | reopen_count | parent problem | linked change | short_description |
|---|---|---|---|---|---|---|---|---|---|---|---|
| INC9000001 | incident | P2 | Closed | 2026-03-02 08:00 | 2026-03-02 12:00 | ENGINEER-A | ENGINEER-A | 0 | | | Mail relay queue stuck |
| INC9000002 | incident | P3 | Closed | 2026-03-03 09:00 | 2026-03-04 09:00 | ENGINEER-A | ENGINEER-A | 0 | | | Print server rejects jobs |
| INC9000003 | incident | P3 | Closed | 2026-03-05 09:00 | 2026-03-05 21:00 | ENGINEER-A | ENGINEER-A | 0 | | | Share permissions missing |
| INC9000004 | incident | P1 | Closed | 2026-03-06 02:00 | 2026-03-06 03:30 | ENGINEER-A | ENGINEER-A | 0 | | | Directory sync halted |
| INC9000005 | incident | P2 | Closed | 2026-03-07 10:00 | 2026-03-07 16:00 | ENGINEER-B | ENGINEER-A | 0 | | | Backup job failing (reassigned) |
| INC9000006 | incident | P3 | Closed | 2026-03-09 08:00 | 2026-03-10 10:00 | ENGINEER-A | ENGINEER-A | 1 | | | Certificate warning on portal (reopened) |
| INC9000007 | incident | P3 | Closed | 2026-03-10 08:00 | 2026-03-12 08:00 | ENGINEER-B | ENGINEER-A | 1 | | | VPN profile not applied (reopened, finished by B) |
| INC9000008 | incident | P2 | Closed | 2026-03-11 09:00 | 2026-03-11 15:00 | ENGINEER-A | ENGINEER-A | 0 | | | Customer Acme Test reports slowness on db-prod-01.example.test |
| INC9000009 | incident | P3 | In Progress | 2026-03-28 09:00 | | | ENGINEER-A | 0 | | | Patch window question |
| CTASK9000001 | change_task | (not carried) | Closed Complete | 2026-03-13 09:00 | 2026-03-13 11:00 | ENGINEER-A | ENGINEER-A | 0 | | CHG9000001 | Apply firmware update |
| SCTASK9000001 | sc_task | (not carried) | Closed Complete | 2026-03-16 09:00 | 2026-03-16 13:00 | ENGINEER-A | ENGINEER-A | 0 | | | Provision shared mailbox |
| PTASK9000001 | problem_task | (not carried) | Closed Complete | 2026-03-17 09:00 | 2026-03-20 09:00 | ENGINEER-A | ENGINEER-A | 0 | PRB9000001 (Closed) | CHG9000002 (Closed) | Replace failing relay config |
| PTASK9000002 | problem_task | (not carried) | Closed Complete | 2026-03-18 09:00 | 2026-03-19 09:00 | ENGINEER-A | ENGINEER-A | 0 | PRB9000002 (Open) | | Gather evidence for recurring fault |

## Expected results

**Counting set (10 records):** INC9000001, 002, 003, 004, 006, 008;
CTASK9000001; SCTASK9000001; PTASK9000001, 002.

**Assigned-but-not-resolved set (3 records):** INC9000005 (reassigned,
resolved by ENGINEER-B), INC9000007 (reopened, finally resolved by
ENGINEER-B; flagged reopen), INC9000009 (still open).

**Counts by type:** incident 6, change_task 1, sc_task 1, problem_task 2;
total 10.

**Priority mix (incidents only; task tables report "priority unavailable"):**
P1 1, P2 2, P3 3.

**Median time to resolve (calendar hours, per priority, n):**
P1 1.5 (n=1, thin sample), P2 5.0 (n=2, thin sample; INC9000001 is 4.0 and
INC9000008 is 6.0), P3 24.0 (n=3, thin sample; values 24.0, 12.0, 26.0).
INC9000006 uses its final resolution timestamp. No overall pooled median.

**Problem-led fixes:** 1 (PTASK9000001: parent problem closed and linked
change closed). PTASK9000002 is not counted: its parent problem is open and
it has no linked change.

**Reopens:** 1 in the counting set (INC9000006, re-resolved by the
engineer, counted once and flagged). 1 in the assigned set (INC9000007).

**Attribution labels:** SCTASK9000001 appears as "assigned at closure" in
the digest. CTASK9000001 notes that the closer may differ from the fixer.

**Sensitive record:** INC9000008 is cited by number, type, and priority
only. Its description, which carries a customer name and a hostname, does
not appear in any form.

**Halts and skips to also test:** (a) a stated expected count of 12 against
this export's 13 rows halts; (b) removing the export and the live
connection yields a declared skip, not an empty digest; (c) adding a row
whose content is marked `confidential` halts the run.
