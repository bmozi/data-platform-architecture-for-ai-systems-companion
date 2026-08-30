# Participant Packet Route

**Packet:** DATA-RV-PILOT-001 version 1.2.5
**Status:** Prepared and unrun with people

This file controls the read order. Use `UNKNOWN`, `UNASSIGNED`, or `STOP` when
the supplied facts do not support an answer. Do not guess.

## Choose exactly one entry branch

Before `RUN_STARTED`, the facilitator records `ENTRY_BRANCH_SELECTED` as
exactly `HUMAN` or `SYNTHETIC`. The branches are mutually exclusive. A blank
human form is not synthetic consent, and a run may not switch or mix branches.

- **Human branch:** complete the [consent and privacy
  notice](01-consent-and-privacy.md) with real-person affirmations and every
  required owner, storage, access, retention, deletion, withdrawal, recording,
  participant, and facilitator field before the applicable Stage A or Stage B
  context gate. A blank prerequisite is a stop.
- **Synthetic branch:** do not complete or sign the human notice. The
  facilitator completes [the synthetic-context
  template](07-synthetic-context-record.md) as exact immutable
  `DATA-SYNTHETIC-CONTEXT-v1.md`, creates and verifies
  `DATA-SYNTHETIC-CONTEXT-SHA256SUMS-v1.txt`, and supplies that manifested
  record instead of a completed human consent form. Any fictional human
  affirmation or human-result claim is a stop.

The facilitator logs `RUN_STARTED`, then the applicable context gate, before
the scored stage start. The same selected branch governs the entire attempt.

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

The sealed input contains only files declared by this route and its current
phase release. Do not open or follow an `ORCHESTRATION.md`, run note, hidden
prompt, facilitator file, or other undeclared control file. Its presence is a
stop and deviation. The facilitator keeps instructions and the item-by-item
access history outside this input.

For every detached verification record named below, record the attempt ID,
stage/phase, artifact-producing actor, facilitator, manifest verifier, exact
verification command, complete observed output, exit code, observed
verification timestamp and timezone, record-completing actor, and explicit
later record-completion timestamp and timezone. A blank field, failed command,
or missing chronological separation prevents `FROZEN` and stops release.

Plain labels used here:

- a **freeze** is a locked copy saved so later edits cannot replace the
  evidence;
- a **manifest** is the exact list of supplied files and their digital
  fingerprints; and
- an **artifact** is the participant's saved workbook, assessment, or handoff.

## Stage A exact read order

Pre-session only: complete the selected branch and verify its exact context
evidence. The facilitator logs `RUN_STARTED`, then
`STAGE_A_CONTEXT_GATE_OPENED`. Then:

1. The facilitator records `STAGE_A_STARTED` with exact timestamp/timezone and
   the completed human consent evidence or verified synthetic-context manifest
   before this route is opened for scored work.
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
8. Before receiving the live update, save the exact required
   `DATA-A-INITIAL-WORKBOOK-v1.md` and
   `DATA-A-INITIAL-READINESS-ASSESSMENT-v1.md`, plus
   `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md` only if the optional contract
   was used. Give each included artifact an ID/version, completion
   timestamp/timezone, and `INITIAL COMPLETE` state. Hash only those completed
   artifacts in `DATA-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt`, verify it, and
   then create `DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md`. Create and verify
   `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt`. It must bind the two
   required initial artifacts; `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md`
   exactly when it was used and included in the initial governing manifest;
   `DATA-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt`;
   `DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md`; and exact immutable
   `DATA-A-LIVE-UPDATE-v1.md`. The optional contract must be present in both
   manifests when used and absent from both when not used. Omission, rename,
   regeneration, summary, substitution, mismatch, or an unmanifested update
   stops the revision phase.
9. Only after that revision-phase input manifest verifies, open
   `DATA-A-LIVE-UPDATE-v1.md` and record its contents exactly. Then complete
   workbook Sections 5-6 and revise the detailed
   artifacts. This planned revision creates the first revised set and is not a
   correction of already frozen revised bytes. Save exactly
   `DATA-A-REVISED-WORKBOOK-v1.md`,
   `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md`, and, only if used,
   `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md`.
10. Give every included revised artifact an ID, version, completion
    timestamp/timezone, and pre-hash state `REVISED COMPLETE`. Record the
    optional contract as `REVISED COMPLETE` when used or `NOT USED` otherwise.
    Remove any incomplete state. Do not put a future verification time, the
    artifact's own hash, or `FROZEN` inside a governed artifact.
11. After those bytes are complete, create
    `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`. It hashes exactly the
    included revised artifacts, never itself or the later verification record.
    Verify the manifest and capture that observed timestamp and timezone. Only
    then complete `06-revised-artifact-freeze-record.md` as
    `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md`, recording the literal artifact
    filenames, IDs/versions/hashes, completion metadata, manifest filename/hash,
    and observed verification event. The verified manifest plus detached record
    establish `FROZEN` for those exact bytes.
12. Only after that detached record verifies, complete the blank
    [One-Screen Handoff](05-one-screen-handoff.md) as
    `DATA-A-ONE-SCREEN-HANDOFF-v1.md`. Record its ID/version, completion
    timestamp/timezone, and pre-hash state `HANDOFF COMPLETE`; point forward to
    `DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md` without embedding its own hash or
    a future freeze time. Then create and verify
    `DATA-A-HANDOFF-SHA256SUMS-v1.txt` over the completed handoff only, capture
    the observed verification time, and create the detached verification
    record. Do not edit the handoff after hashing.
13. The next sealed phase input manifest hashes each supplied governed
    artifact, its governing manifest, and its detached verification record.
    Render the exact frozen handoff to `DATA-A-ONE-SCREEN-HANDOFF-v1.pdf` and
    complete `DATA-A-HANDOFF-LAYOUT-PROOF-v1.md` from the declared layout-proof
    template. A failed local layout gate is retained as `HOLD`; it does not
    rewrite the frozen handoff or become human-comprehension evidence.
14. Collect all material feedback in the external
    run-specific results record; do not reopen or append to the governed
    practitioner workbook or handoff. The facilitator records
    `STAGE_A_MATERIAL_FEEDBACK_COMPLETED` and then `STAGE_A_ENDED`, each with an
    exact timestamp/timezone and prior-event binding.

If a revised frozen byte changes after step 11, preserve the old file and use a
new immutable filename and a new artifact ID/version. Record exact old/new
filenames, IDs/versions, hashes, reason, correction timestamp/timezone,
replacement governing manifest, and replacement detached record before the
corrected set may continue.

## Stage B exact read order

Pre-session only: continue the same selected branch. For a human reviewer,
complete and close that reviewer's real consent record. For a synthetic
reviewer, verify the unchanged exact synthetic context and manifest. The
facilitator records `STAGE_B_CONTEXT_GATE_OPENED`. Then:

1. The facilitator records `STAGE_B_STARTED` with exact timestamp/timezone and
   the completed human consent evidence or verified synthetic-context manifest
   before this route is opened for scored work.
2. Read this route.
3. Verify the handoff artifact, `DATA-A-HANDOFF-SHA256SUMS-v1.txt`, and
   `DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md`, then read the frozen
   `DATA-A-ONE-SCREEN-HANDOFF-v1.md` first. Do not open the scenario or
   detailed Stage A work yet.
4. Open the [Decision-Owner Workbook](04-decision-owner-workbook.md), complete
   Section 1 from the handoff alone, export it as
   `DATA-B-SECTION-1-SCAN-v1.md`. Give it an ID/version, completion
   timestamp/timezone, pre-hash state `SECTION 1 COMPLETE`, and a forward
   pointer to `DATA-B-SECTION-1-FREEZE-VERIFICATION-v1.md`. Then create and
   verify `DATA-B-SECTION-1-SHA256SUMS-v1.txt` over the completed export only
   and create that detached record. Do not open another substantive file first.
5. Read `02-scenario-and-task.md`,
   `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md`, and
   `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`. Verify every included detail
   named by the handoff under that same literal filename with matching
   ID/version, completion timestamp/timezone, pre-hash `REVISED COMPLETE`
   state, hash, and detached-record `FROZEN` condition. The optional contract
   must be consistently `NOT USED` or included and frozen. A rename,
   regenerated copy, summary, substitution, omission, mismatch, or missing
   record/manifest is a stop.
6. Complete Section 2 and export it as `DATA-B-SECTION-2-DETAIL-v1.md` with
   ID/version, completion timestamp/timezone, pre-hash state `SECTION 2
   COMPLETE`, and a forward pointer to
   `DATA-B-SECTION-2-FREEZE-VERIFICATION-v1.md`. Then create and verify
   `DATA-B-SECTION-2-SHA256SUMS-v1.txt` over only the completed export and
   create that detached record before opening either decision aid.
7. Only after the Section 2 detached record verifies, read the supplied local file
   `EXECUTIVE-DECISION-BRIEF.md`.
8. Then read the supplied local file `VALUE-AND-EVIDENCE-LEDGER.md`.
9. Complete Sections 3-5 and export them as
   `DATA-B-SECTIONS-3-5-DECISION-v1.md` with ID/version, completion
   timestamp/timezone, pre-hash state `SECTIONS 3-5 COMPLETE`, and a forward
   pointer to `DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md`. Create and
   verify `DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt` over only that completed
   export; then create the detached record. Keep Section 6 closed until the
   facilitator ends scoring.
10. Only after the Sections 3-5 governing manifest verifies and its detached
    record is complete, record `STAGE_B_SCORING_ENDED`. Stage A explanation or
    repair remains forbidden before this event.
11. Create and verify
    `DATA-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt` over exactly
    `DATA-B-SECTIONS-3-5-DECISION-v1.md`, its governing manifest, its detached
    record, and the exact `04-decision-owner-workbook.md` Section 6/debrief
    input. Debrief access before scoring end or manifest verification is a
    stop.
12. Open Section 6 only after that gate and export its completed answers as
    `DATA-B-SECTION-6-DEBRIEF-v1.md` with completion timestamp/timezone and
    state `DEBRIEF COMPLETE`. The debrief may explain a misunderstanding but
    may not modify scored bytes or upgrade a frozen score. Record
    `STAGE_B_SECTION_6_DEBRIEF_COMPLETED`, then `STAGE_B_ENDED`.
13. Complete the immutable run-specific results record as exactly
    `DATA-RUN-RESULTS-v1.md`, state `RESULTS COMPLETE`, including all six freeze
    results, route boundaries, interventions, deviations, rejected attempts,
    semantic inventions, layout findings, scores, separate evidence states,
    final pre-close log checkpoint, counts, decision, and limits. It must not
    predict the final closed-log hash or future closeout time.
14. Record `RUN_RESULTS_COMPLETED` before `LOG_CLOSED`. Validate closed
    `DATA-EXECUTION-ACCESS-LOG-v1.jsonl`, copy it without byte change to the
    dedicated closeout input, and do not reopen it.
15. Create and verify `DATA-RUN-CLOSEOUT-SHA256SUMS-v1.txt` over the closed-log
    copy and `DATA-RUN-RESULTS-v1.md`. Only afterward complete
    `DATA-RUN-CLOSEOUT-v1.md`, binding the closed-log hash, closeout-manifest
    hash, and run-results hash.

At every phase boundary, the next sealed phase-input manifest must hash the
completed artifact, its governing manifest, and its later detached verification
record. The closing evidence manifest does the same for Sections 3-5. A
governing manifest never hashes itself or its later record, and a governed
artifact never embeds its own hash or a future verification timestamp.
Stage B Phase 2 must bind both the frozen Section 1 triple and every included
revised Stage A artifact plus its governing manifest and detached record.

Keep the Stage A participant unavailable until Stage B Sections 1-5 are frozen.
Never silently replace a frozen artifact. A correction after any freeze must
preserve the previous file and use a new immutable filename and a new artifact
ID/version. Record exact old/new immutable filenames, IDs/versions, hashes,
reason, correction timestamp/timezone, replacement governing manifest, and
replacement detached record. A governing manifest hashes completed governed
files, never itself or its later record.

All six scored freeze chains may be complete while the full route remains
incomplete. Claim `Full synthetic route complete` only when synthetic context,
both stage starts and ends, Stage A material feedback, scoring end, debrief,
immutable results, log close, external closeout, and the six chains all verify.
Human evidence, data-readiness evidence, and real-world evidence remain
separate and `UNRUN` until corresponding authorized work occurs.
