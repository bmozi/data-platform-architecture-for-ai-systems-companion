# Participant Packet Route

**Packet:** DATA-RV-PILOT-001 version 1.2.0
**Status:** Prepared and unrun with people

This file controls the read order. Use `UNKNOWN`, `UNASSIGNED`, or `STOP` when
the supplied facts do not support an answer. Do not guess.

## Before a real human session

Do not begin a scored stage until the consent and privacy notice has been
completed, the participant has consented, and an accountable execution owner
has approved storage, access, retention, deletion, withdrawal, facilitator,
and evaluator arrangements. The facilitator must freeze the supplied files and
record the exact Stage A or Stage B start time immediately before the first
scored file is opened. Blank prerequisites mean do not start.

## Allowed surface

Use only files the facilitator supplies in the order below. Do not use a
terminal, repository or Git status/history commands, internet search, omitted
links, linked full examples, the failure lab, Northbridge completed examples,
facilitator files, or private organizational information. Do not inspect other
repository files. Ask a question or mark an unknown instead. The facilitator
records every pause, question, intervention, extra file, command, or route
deviation.

The miniature example already embedded inside a supplied template remains part
of that file. Do not follow its link to the comprehensive example.

Plain labels used here:

- a **freeze** is a locked copy saved so later edits cannot replace the
  evidence;
- a **manifest** is the exact list of supplied files and their digital
  fingerprints; and
- an **artifact** is the participant's saved workbook, assessment, or handoff.

## Stage A exact read order

Pre-session only: complete and close
[the consent and privacy notice](01-consent-and-privacy.md). Then:

1. The facilitator records the exact Stage A start time and timezone before
   this route is opened for scored work.
2. Read this route.
3. Read the [scenario and task](02-scenario-and-task.md).
4. Open the [practitioner workbook](03-practitioner-workbook.md) and complete
   Section 1, recognition before terminology.
5. Read the supplied local file `AI-READY-DATA-JOURNEY.md`.
6. Open the supplied local file `ai-data-readiness-assessment.md`, then
   complete the relevant detailed work and workbook Sections 2-4.
7. Open the supplied local file `data-product-contract.md` only if you
   independently decide it answers a separate question. Otherwise do not open
   it.
8. Freeze the initial detailed artifact (saved work product) and workbook
   before receiving the live update.
9. Receive the live update, complete workbook Sections 5-6, revise the detailed
   artifacts. This planned revision creates the first revised set and is not a
   correction of already frozen revised bytes. Save exactly
   `DATA-A-REVISED-WORKBOOK-v1.md`,
   `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md`, and, only if used,
   `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md`.
10. Give every included revised artifact an ID, version, completion
    timestamp/timezone, and pre-hash state `REVISED COMPLETE`. Record the
    optional contract as `REVISED COMPLETE` when used or `NOT USED` otherwise.
    Remove any `DRAFT`, `PENDING`, `PENDING FREEZE`, `AWAITING FREEZE`, blank,
    or equivalent incomplete state. Do not make an artifact self-declare
    `FROZEN`.
11. Create `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`, hashing exactly the
    included revised details and not the manifest itself. Open
    `06-revised-artifact-freeze-record.md` and complete it as
    `DATA-A-REVISED-FREEZE-RECORD-v1.md` with exact freeze
    timestamp/timezone, filenames, IDs/versions, completion
    timestamps/timezones, pre-hash states, hashes, optional disposition, and
    governing manifest filename/hash. Only the verified manifest and detached
    record establish `FROZEN` for included artifacts.
12. Only after that detached record verifies, complete the blank
    [One-Screen Handoff](05-one-screen-handoff.md) as
    `DATA-A-ONE-SCREEN-HANDOFF-v1.md`. List the same literal included details
    and freeze the handoff separately.
13. Complete the material-feedback section of the practitioner workbook.

If a revised frozen byte changes after step 11, preserve the old file and use a
new immutable filename. Record exact old/new filenames, IDs/versions, hashes,
reason, correction timestamp/timezone, replacement freeze record, and
replacement manifest before the corrected set may continue.

## Stage B exact read order

Pre-session only: complete and close
[the consent and privacy notice](01-consent-and-privacy.md). Then:

1. The facilitator records the exact Stage B start time and timezone before
   this route is opened for scored work.
2. Read this route.
3. Read frozen `DATA-A-ONE-SCREEN-HANDOFF-v1.md` first. Do not
   open the scenario or detailed Stage A work yet.
4. Open the [Decision-Owner Workbook](04-decision-owner-workbook.md), complete
   Section 1 from the handoff alone, export it as
   `DATA-B-SECTION-1-SCAN-v1.md`, and checksum-freeze it before any other
   substantive file opens.
5. Read `02-scenario-and-task.md`,
   `DATA-A-REVISED-FREEZE-RECORD-v1.md`, and
   `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`. Verify every included detail
   named by the handoff under that same literal filename with matching
   ID/version, completion timestamp/timezone, pre-hash `REVISED COMPLETE`
   state, hash, and detached-record `FROZEN` condition. The optional contract
   must be consistently `NOT USED` or included and frozen. A rename,
   regenerated copy, summary, substitution, omission, mismatch, or missing
   record/manifest is a stop.
6. Complete Section 2, export it as `DATA-B-SECTION-2-DETAIL-v1.md`, and
   checksum-freeze it before opening either decision aid.
7. Only after the Section 2 freeze, read the supplied local file
   `EXECUTIVE-DECISION-BRIEF.md`.
8. Then read the supplied local file `VALUE-AND-EVIDENCE-LEDGER.md`.
9. Complete Sections 3-5, export them as
   `DATA-B-SECTIONS-3-5-DECISION-v1.md`, and checksum-freeze them. Keep Section
   6 closed until the facilitator ends scoring.

Keep the Stage A participant unavailable until Stage B Sections 1-5 are frozen.
Never silently replace a frozen artifact. A correction after any freeze must
preserve the previous file and record exact old/new immutable filenames,
IDs/versions, hashes, reason, correction timestamp/timezone, replacement freeze
record, and replacement manifest. A manifest hashes governed files, never its
own bytes.
