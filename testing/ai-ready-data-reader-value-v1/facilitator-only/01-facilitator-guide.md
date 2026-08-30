# Facilitator Guide

**Packet:** DATA-RV-PILOT-001 version 1.2.3
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

Maintain the facilitator-only
[`execution and access log`](05-execution-and-access-log.md) item by item. Log
every manifest gate, file open or attempted access, artifact completion,
manifest creation, manifest verification, detached-record completion, and next
phase open with exact actor, facilitator, timestamp, timezone, filename, and
continuity binding.

## Sealed flat delivery and provenance

Before each stage, copy the exact approved immutable files into a separate
sealed flat stage input. Preserve these local filenames exactly when supplied:
`AI-READY-DATA-JOURNEY.md`, `ai-data-readiness-assessment.md`, optional
`data-product-contract.md`, `EXECUTIVE-DECISION-BRIEF.md`, and
`VALUE-AND-EVIDENCE-LEDGER.md`. Hash every supplied file in a run-specific
SHA-256 manifest before the start time. A manifest hashes other files and never
lists or hashes itself. Do not rely on repository-relative paths, and do not
replace a frozen file in place.

Reject any participant input containing an undeclared `ORCHESTRATION.md`, run
note, hidden prompt, facilitator file, or other extra control file. Keep all
facilitation outside the sealed participant surface and prove the declared
inventory item by item in the external access log.

## Governing freeze sequence

Use this same temporal order for the initial and revised Stage A sets, the
Stage A handoff, and each of the three Stage B exports:

1. Finalize every governed artifact. Its bytes must already contain the literal
   artifact ID/version, completion timestamp/timezone, complete pre-hash state,
   and the exact filename of the detached verification record that will be
   created later.
2. Do not place an artifact's own hash, the detached record's hash, a future
   verification time, or `FROZEN` in the governed artifact.
3. Create the governing manifest over only the completed governed artifact or
   artifacts. The manifest never lists or hashes itself or the later record.
4. Verify that manifest, then capture the exact observed verification timestamp
   and timezone.
5. Only afterward create the detached record from
   `06-revised-artifact-freeze-record.md`. Record literal filenames,
   IDs/versions/hashes, completion metadata, the manifest filename/hash, and
   the observed verification event. A successful detached determination
   establishes `FROZEN` for the exact governed bytes.
6. The next sealed phase-input manifest hashes each governed artifact, its
   governing manifest, and its detached verification record. The closing
   evidence manifest does the same for the final Stage B export.

Every detached record must contain attempt ID, stage/phase,
artifact-producing actor, facilitator, manifest verifier, exact verification
command, complete observed output, exit code, observed verification timestamp
and timezone, record-completing actor, and an explicit later record-completion
timestamp and timezone. Missing evidence prevents `FROZEN`.

Any change after step 3 requires an immutable replacement set with a new
immutable filename and a new artifact ID/version for every corrected artifact,
a new manifest, and a new detached record. Never revise the old set in place.

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
5. Complete `DATA-A-INITIAL-WORKBOOK-v1.md` and
   `DATA-A-INITIAL-READINESS-ASSESSMENT-v1.md`, plus
   `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md` only when the optional contract
   was used. Give every included file its ID/version, completion
   timestamp/timezone, and `INITIAL COMPLETE` state. Create
   `DATA-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt` over only those completed
   artifacts, verify it, and then complete
   `DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md`. Create and verify
   `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` over the initial artifacts,
   their governing manifest, detached record, and live update before opening
   the update.
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
   `NOT USED` otherwise. Point to
   `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md`; do not embed a self-hash, future
   verification time, or `FROZEN`.
9. Remove every `DRAFT`, `PENDING`, `PENDING FREEZE`, `AWAITING FREEZE`, blank,
   or equivalent incomplete state. Create
   `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`; it hashes exactly the included
   revised details and does not hash itself.
10. Verify that governing manifest, capture the exact observed verification
    timestamp/timezone, and only then create
    `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md`. Verify the detached record
    before the blank handoff opens.
11. Supply the blank handoff. Ensure its inventory matches the revised record
    and manifest. Complete it as `DATA-A-ONE-SCREEN-HANDOFF-v1.md` with
    completion metadata, pre-hash `HANDOFF COMPLETE`, and filename-only pointer
    to `DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md`. Create
    `DATA-A-HANDOFF-SHA256SUMS-v1.txt` over the handoff only, verify it and
    capture the exact time/timezone, then create the detached record.
12. Collect material feedback in the separate run record only after all
    freezes verify; do not edit a governed workbook or handoff.

## Stage B sequence

1. Complete the same human consent and run prerequisites and use a reviewer who
   did not create Stage A work.
2. Record the exact Stage B start immediately before the first scored file is
   opened.
3. Verify the handoff, its governing manifest, and detached record. Supply the
   route, then `DATA-A-ONE-SCREEN-HANDOFF-v1.md` as the first substantive
   artifact. Supply the decision-owner workbook. Complete
   `DATA-B-SECTION-1-SCAN-v1.md` with ID/version, completion time/timezone,
   pre-hash `SECTION 1 COMPLETE`, and filename-only pointer to
   `DATA-B-SECTION-1-FREEZE-VERIFICATION-v1.md` before the scenario or details
   open.
4. Create `DATA-B-SECTION-1-SHA256SUMS-v1.txt` over that completed export only,
   verify it and capture the exact observed time/timezone, then create the
   detached record.
5. Before Phase 2 opens, create and verify its sealed input manifest over the
   frozen Section 1 artifact, governing manifest, and detached record; every
   included revised Stage A artifact; the revised Stage A governing manifest;
   the revised Stage A detached record; and the scenario. Then supply
   `02-scenario-and-task.md`, the detached revised freeze record, governing
   revised manifest, and every exact included handoff-linked detail.
   Verify literal filenames, IDs/versions, completion timestamps/timezones,
   pre-hash states, hashes, and detached freeze statuses. A rename,
   regenerated copy, summary, substitution, omission, mismatch, or missing
   record/manifest stops detailed read-back. Complete
   `DATA-B-SECTION-2-DETAIL-v1.md` with ID/version, completion time/timezone,
   pre-hash `SECTION 2 COMPLETE`, and filename-only pointer to its detached
   record. Create and verify `DATA-B-SECTION-2-SHA256SUMS-v1.txt`, capture the
   observed time/timezone, then create
   `DATA-B-SECTION-2-FREEZE-VERIFICATION-v1.md`. Seal all three into the Phase
   3 input manifest.
6. Only after the Section 2 freeze, supply `EXECUTIVE-DECISION-BRIEF.md`, then
   `VALUE-AND-EVIDENCE-LEDGER.md`. Record their exact first-open times.
7. The reviewer completes Sections 3-5. Export
   `DATA-B-SECTIONS-3-5-DECISION-v1.md` with ID/version, completion
   time/timezone, pre-hash `SECTIONS 3-5 COMPLETE`, and filename-only pointer to
   its detached record. Create and verify
   `DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt`, capture the observed
   time/timezone, and only then create
   `DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md`. The closing evidence
   manifest hashes all three. Keep Section 6 closed.
8. Keep the Stage A participant unavailable until Stage B Sections 1-5 are
   frozen. End scoring before Section 6, explanation, or repair.

If any correction is necessary after a freeze, preserve the previous file and
use a new immutable filename and a new artifact ID/version. Log exact old/new
immutable filenames, IDs/versions, hashes, reason, correction
timestamp/timezone, replacement detached record, and replacement manifest. A
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
