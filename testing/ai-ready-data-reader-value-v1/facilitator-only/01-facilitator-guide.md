# Facilitator Guide

**Packet:** DATA-RV-PILOT-001 version 1.2.0
**Status:** Facilitator-only; prepared and unrun

## Purpose

Observe whether the plain-language journey supports a bounded AI-data readiness
decision and whether the artifact transfers to a decision owner.

## Recommended timing

### Stage A — 70 to 90 minutes

- consent and setup: 5 minutes;
- route and exact-start capture: 5 minutes;
- scenario and recognition: 10 minutes;
- readiness journey and assessment: 35 minutes;
- live update and revision: 10 minutes;
- one-screen handoff and feedback: 10 to 20 minutes.

### Stage B — 35 to 50 minutes

- route, one-screen scan, and independent read-back: 15 minutes;
- executive brief and value ledger: 10 minutes;
- bounded decision: 10 minutes;
- debrief: 5 to 15 minutes.

## No-coaching rule

During scored work, repeat written text or resolve file access only. Do not
identify the stale index, recommend excluding work orders, define the correct
readiness outcome, name the missing owners, or suggest the stop condition.
Record every pause, participant question, intervention, file open, and route
deviation. Do not permit terminal, repository or Git status/history commands,
internet searches, omitted links, completed examples, or other out-of-surface
materials.

## Sealed flat delivery and provenance

Before each stage, copy the exact approved immutable files into a separate
sealed flat stage input. Preserve these local filenames exactly when supplied:
`AI-READY-DATA-JOURNEY.md`, `ai-data-readiness-assessment.md`, optional
`data-product-contract.md`, `EXECUTIVE-DECISION-BRIEF.md`, and
`VALUE-AND-EVIDENCE-LEDGER.md`. Hash every supplied file in a run-specific
SHA-256 manifest before the start time. A manifest hashes other files and never
lists or hashes itself. Do not rely on repository-relative paths, and do not
replace a frozen file in place.

## Stage A sequence

1. Complete consent, privacy, authority, storage, access, retention, deletion,
   withdrawal, sealed flat input, and run-specific manifest prerequisites
   before the scored stage.
2. Record the exact Stage A start immediately before the first scored file is
   opened.
3. Enforce and log the exact order in the participant packet route: route;
   scenario; workbook Section 1; journey; assessment; optional contract only
   if independently requested; remaining detailed work.
4. Record every first open and material re-open. Recognition must finish before
   teaching or template assets open.
5. Freeze the initial workbook and detailed artifact with exact filenames,
   IDs, versions, timestamps/timezones, SHA-256 hashes, and manifest before the
   update.
6. Read the update:

> During a dry content check, the proposed assistant retrieved Heat Response
> Policy v2 above v3 and drafted the obsolete escalation timing. The answer
> cited only a document title, not version or effective date. The query came
> from an HG-03 agent, but the retrieved context also included a restricted
> resident note from HG-11 because the service account could search all
> buildings. The source owner corrected v3 later that morning, but no owner can
> say when the correction will reach the index. No resident message or work
> order was sent; the candidate remains offline.

7. Ask only: “What may the team safely conclude or do now, and what changes in
   your artifact?”
8. Treat the live update as the planned revision that creates the first revised
   set, not a correction of already frozen revised bytes. Save exactly
   `DATA-A-REVISED-WORKBOOK-v1.md`,
   `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md`, and, only if used,
   `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md`. Every included detail must
   contain its ID, version, completion timestamp/timezone, and pre-hash state
   `REVISED COMPLETE`; the optional contract is `REVISED COMPLETE` when used or
   `NOT USED` otherwise. No artifact may self-declare `FROZEN`.
9. Remove every `DRAFT`, `PENDING`, `PENDING FREEZE`, `AWAITING FREEZE`, blank,
   or equivalent incomplete state. Create
   `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`; it hashes exactly the included
   revised details and does not hash itself.
10. Complete `DATA-A-REVISED-FREEZE-RECORD-v1.md` with exact freeze
    timestamp/timezone, filenames, IDs/versions, completion
    timestamps/timezones, pre-hash states, hashes, optional-artifact
    disposition, and governing manifest filename/hash. The verified manifest
    and detached record establish `FROZEN` for included artifacts; verify them
    before the blank handoff opens.
11. Supply the blank one-screen handoff. Ensure its exact inventory matches the
    detached record and manifest, complete it as
    `DATA-A-ONE-SCREEN-HANDOFF-v1.md`, and freeze it separately.
12. Collect material feedback only after all freezes verify.

## Stage B sequence

1. Complete the same human consent and run prerequisites and use a reviewer who
   did not create Stage A work.
2. Record the exact Stage B start immediately before the first scored file is
   opened.
3. Supply the route, then `DATA-A-ONE-SCREEN-HANDOFF-v1.md` as the first
   substantive artifact. Supply the decision-owner workbook and freeze
   `DATA-B-SECTION-1-SCAN-v1.md` before the scenario or detailed artifacts
   open.
4. Record the Section 1 exact filename, artifact ID/version, freeze
   timestamp/timezone, SHA-256, and manifest reference. Preserve this freeze.
5. Then supply `02-scenario-and-task.md`, the detached revised freeze record,
   governing revised manifest, and every exact included handoff-linked detail.
   Verify literal filenames, IDs/versions, completion timestamps/timezones,
   pre-hash states, hashes, and detached freeze statuses. A rename,
   regenerated copy, summary, substitution, omission, mismatch, or missing
   record/manifest stops detailed read-back. Complete and checksum-freeze
   `DATA-B-SECTION-2-DETAIL-v1.md`.
6. Only after the Section 2 freeze, supply `EXECUTIVE-DECISION-BRIEF.md`, then
   `VALUE-AND-EVIDENCE-LEDGER.md`. Record their exact first-open times.
7. The reviewer completes Sections 3-5. Export and checksum-freeze
   `DATA-B-SECTIONS-3-5-DECISION-v1.md` and record artifact ID/version,
   timestamp/timezone, hash, and manifest. Keep Section 6 closed.
8. Keep the Stage A participant unavailable until Stage B Sections 1-5 are
   frozen. End scoring before Section 6, explanation, or repair.

If any correction is necessary after a freeze, preserve the previous file and
log exact old/new immutable filenames, IDs/versions, hashes, reason, correction
timestamp/timezone, replacement freeze record, and replacement manifest. A
corrected artifact is a new freeze, not a silent replacement or the planned
live-update revision.

## Intervention levels

- **L0:** silence or think-aloud reminder;
- **L1:** repeat written text;
- **L2:** neutral probe such as “Ready for which use?”;
- **L3:** define a term without applying it;
- **L4:** recommend or supply the decision.

L3 is aided. L4 contaminates the affected gate.

## Stop conditions

Stop and retain partial evidence on consent withdrawal, confidential-data
disclosure, unblinding, changed frozen bytes, distress, material tool failure,
or coaching that makes a central result uninterpretable.
