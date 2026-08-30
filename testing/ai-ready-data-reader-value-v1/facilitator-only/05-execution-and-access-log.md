# Facilitator Execution and Access Log

**Packet:** DATA-RV-PILOT-001 version 1.2.5
**Status:** Blank facilitator-side control record; prepared and unrun

Create the append-only run instance as exactly
`DATA-EXECUTION-ACCESS-LOG-v1.jsonl`. This Markdown file is its field and event
template, not a completed log.

Keep this log outside every sealed participant input. It is not a participant
instruction, artifact, answer key, or substitute for consent. Do not copy an
`ORCHESTRATION.md`, run note, hidden prompt, facilitator file, or any other
undeclared control file into a participant input. A participant input is valid
only when its item-by-item inventory matches the route's declared release and
its verified sealed-input manifest.

## Run identity and continuity

- Attempt ID:
- Entry branch: `HUMAN` / `SYNTHETIC`
- Branch evidence exact filename/manifest/hash:
- Stage and phase:
- Participant or reviewer code:
- Facilitator name/code:
- Execution owner:
- Timezone used for every timestamp:
- Previous phase's terminal event ID, filename, and SHA-256:
- Current sealed-input manifest filename and SHA-256:
- Current phase's first event ID:

Use one immutable attempt directory. Event IDs are monotonically increasing
within that attempt. Every row names its preceding event ID. Every phase-opening
row also binds the verified input manifest and the prior phase's terminal
record or manifest. A missing predecessor, unexplained gap, timestamp reversal,
or changed byte is a deviation, not a detail to reconstruct later.

The branch is selected once before `RUN_STARTED`. `HUMAN` requires completed
real-person consent; `SYNTHETIC` requires exact manifested
`DATA-SYNTHETIC-CONTEXT-v1.md` and forbids fictional consent or human-result
claims. Mixing, switching, or leaving the branch blank stops the run.

## Declared participant-input inventory

Record one row for every expected file and every attempted extra surface before
the phase opens. `Present and manifested` must be `yes` for declared files and
`no` for undeclared files. Any undeclared orchestration or facilitator file
stops the phase.

For the Stage A revision phase, the declared inventory must contain both
required initial artifacts; optional
`DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md` exactly when it appears in the
initial governing manifest; `DATA-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt`;
`DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md`; and exact immutable
`DATA-A-LIVE-UPDATE-v1.md`. All must be bound by verified
`DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` before the update opens. The
optional contract must be absent here when it was not used.

| Stage/phase | Exact local filename or attempted surface | Declared by route/release | Expected SHA-256 | Present and manifested | Participant-accessible | First-open event ID | Disposition/deviation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | yes / no | | yes / no | yes / no | | |

## Required whole-route boundary sequence

Record these boundary event types in this exact chronological order, with any
release-chain events occurring between their applicable boundaries:

1. `ENTRY_BRANCH_SELECTED`
2. `RUN_STARTED`
3. `STAGE_A_CONTEXT_GATE_OPENED`
4. `STAGE_A_STARTED`
5. `HANDOFF_LAYOUT_PROOF_COMPLETED`
6. `STAGE_A_MATERIAL_FEEDBACK_COMPLETED`
7. `STAGE_A_ENDED`
8. `STAGE_B_CONTEXT_GATE_OPENED`
9. `STAGE_B_STARTED`
10. `STAGE_B_SCORING_ENDED`
11. `DEBRIEF_INPUT_MANIFEST_CREATED`
12. `DEBRIEF_INPUT_MANIFEST_VERIFIED`
13. `STAGE_B_SECTION_6_DEBRIEF_OPENED`
14. `STAGE_B_SECTION_6_DEBRIEF_COMPLETED`
15. `STAGE_B_ENDED`
16. `RUN_RESULTS_COMPLETED`
17. `LOG_CLOSED`

Stage A explanation or repair is forbidden until
`STAGE_B_SCORING_ENDED`. `DATA-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt`
must verify over the Sections 3-5 artifact, governing manifest, detached
record, and exact `04-decision-owner-workbook.md` before Section 6 opens.
Section 6 completes as `DATA-B-SECTION-6-DEBRIEF-v1.md` without retroactive
change to scored bytes.

`RUN_RESULTS_COMPLETED` binds completed immutable
`DATA-RUN-RESULTS-v1.md` and its final pre-close checkpoint. `LOG_CLOSED`
cannot precede it. The closed log must not claim its own future external hash
or a future closeout timestamp.

## Item-by-item execution and access ledger

Use these exact event types in this order where applicable:

1. `SEALED_INPUT_MANIFEST_CREATED`
2. `SEALED_INPUT_MANIFEST_VERIFIED`
3. `PHASE_GATE_OPENED`
4. `FILE_OPENED` or `ACCESS_ATTEMPT_RECORDED`, once per item or attempt
5. `ARTIFACT_COMPLETED`, once per governed artifact
6. `GOVERNING_MANIFEST_CREATED`
7. `GOVERNING_MANIFEST_VERIFIED`
8. `DETACHED_RECORD_COMPLETED`
9. `NEXT_RELEASE_MANIFEST_CREATED`
10. `NEXT_RELEASE_MANIFEST_VERIFIED`
11. `NEXT_PHASE_GATE_OPENED`

Repeat events 4-11 for each release chain. A manifest gate or phase may open
only after the immediately required verification succeeded. Record the exact
command, complete observed output, exit code, verification timestamp/timezone,
and actor on every `*_MANIFEST_VERIFIED` row.

| Event ID | Prior event ID | Stage/phase | Event type | Exact filename/surface | Actor | Facilitator | Timestamp | Timezone | Verification command | Complete observed output | Exit code | Continuity binding: manifest or predecessor filename/SHA-256 | Outcome/deviation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| | | | | | | | | | | | | | | |

## Phase close

- Final event ID for this phase:
- Detached record filename, completion timestamp/timezone, and SHA-256:
- Next-release manifest filename, verification event ID, and SHA-256:
- Every participant-visible file declared and manifested: yes / no
- Any undeclared orchestration, hidden prompt, facilitator file, or extra
  surface exposed: no / deviation ID
- Gaps, reversals, failed commands, or access deviations:
- Facilitator signature/code and completion timestamp/timezone:

This log can show what the facilitator recorded for one attempt. It does not
prove participant understanding, data or AI readiness, architecture correctness,
safety, or business value.

## External closeout after `LOG_CLOSED`

After log close, validate `DATA-EXECUTION-ACCESS-LOG-v1.jsonl`, copy it without
byte change under the same filename into a dedicated closeout input, and place
completed `DATA-RUN-RESULTS-v1.md` beside it. Create and verify
`DATA-RUN-CLOSEOUT-SHA256SUMS-v1.txt` over those two files. Only then create
`DATA-RUN-CLOSEOUT-v1.md` with:

- attempt and packet ID/version;
- closed-log exact filename and observed SHA-256;
- closed-log copy byte-identical: yes / no;
- closeout-manifest exact filename, SHA-256, command, complete output, exit
  code, verification timestamp/timezone, and verifier;
- run-results exact filename, ID/version, `RESULTS COMPLETE` state, SHA-256,
  and completion timestamp/timezone;
- closeout-record completion actor and timestamp/timezone; and
- full selected-branch route determination with explicit limits.

The closeout record is later external provenance. It cannot be inserted into
or predicted by the already closed log.
