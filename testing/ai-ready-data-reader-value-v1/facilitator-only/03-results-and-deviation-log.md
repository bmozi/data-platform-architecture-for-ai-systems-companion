# Results and Deviation Log

**Packet:** DATA-RV-PILOT-001 version 1.2.7
**Status:** Blank controlled record; no result exists

This checked-in file is a source template, not a completed result. For each
attempt, complete a new immutable instance as exactly
`DATA-RUN-RESULTS-v1.md`, give it a results-record ID/version, completion
timestamp/timezone, and state `RESULTS COMPLETE`, then record
`RUN_RESULTS_COMPLETED` before `LOG_CLOSED`. Do not put the future final
closed-log hash or a future closeout timestamp in the result.

## Run identity

- Packet ID/version: `DATA-RV-PILOT-001` / `1.2.7`
- Results-record exact filename: `DATA-RUN-RESULTS-v1.md`
- Results-record ID/version:
- Attempt ID:
- Entry branch selected once: `HUMAN` / `SYNTHETIC`
- Branch-selection event/checkpoint:
- Execution owner and authorization:
- Stage A participant code:
- Stage B reviewer code:
- Facilitator:
- Evaluator and independence disclosure:
- Date, mode, and time:
- Exact prepared-source manifest filename/hash:
- Exact orchestration manifest filename/hash, or `NOT APPLICABLE`:
- Synthetic helper source/run-copy identities and hashes, or `NOT APPLICABLE —
  HUMAN`:
- Run helper exact filename: `DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py`
- Synthetic access plan/schema and predeclared phase directories, or `NOT
  APPLICABLE — HUMAN`:
- Synthetic per-phase config, binding-manifest, and distinct helper-log
  identities/hashes, or `NOT APPLICABLE — HUMAN`:
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json` /
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt` /
  `DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl`
- Exact verified phase-input manifest filename/absolute path/SHA-256 bound by
  each config, plus config/manifest membership/hash equality result:
- Exact helper-only actor instruction and compliance state, or `NOT APPLICABLE
  — HUMAN`:
- Technical platform restriction/security state: `NOT ESTABLISHED` unless
  separately demonstrated / `NOT APPLICABLE — HUMAN`
- Run start event/timestamp/timezone:
- Exact Stage A start before first scored file opened, with timezone:
- Exact Stage B start before first scored file opened, with timezone:
- Facilitator execution/access log exact filename and SHA-256:

## Consent, privacy, and freeze

- Human branch consent records, or `NOT APPLICABLE — SYNTHETIC`:
- Synthetic context exact filename/hash, or `NOT APPLICABLE — HUMAN`:
  `DATA-SYNTHETIC-CONTEXT-v1.md` /
- Synthetic context manifest exact filename/hash, or `NOT APPLICABLE — HUMAN`:
  `DATA-SYNTHETIC-CONTEXT-SHA256SUMS-v1.txt` /
- Human and synthetic branches remained mutually exclusive: yes / no /
  deviation
- Storage/access/retention authority:
- Run-specific SHA-256 manifest:
- Sealed flat Stage A input location and manifest:
- Sealed flat Stage B input location and manifest:
- Prepared-source manifest match:
- Supplied and withheld materials correct: yes / no / deviation
- Declared participant-input inventory matches item by item: yes / no /
  deviation
- Undeclared orchestration, run note, hidden prompt, facilitator file, or other
  control file in participant input: none / deviation ID
- Confidentiality or privacy concern:
- Out-of-surface command, repository/status/history inspection, omitted link,
  internet search, or extra file: none observed / deviation ID
- Absent, after-start, changed, or overbroad synthetic helper: none / deviation
  ID / `NOT APPLICABLE — HUMAN`
- Future/dummy config hashes or config created after its phase gate: none /
  deviation ID / `NOT APPLICABLE — HUMAN`
- Absent, drifted, wrong, outside-root, malformed, duplicate/path/self-listing,
  or config-membership/hash-mismatched phase-input manifest: none / deviation
  ID / `NOT APPLICABLE — HUMAN`
- Direct read, undeclared/pasted message content, or ad hoc facilitator file
  delivery: none / deviation ID / `NOT APPLICABLE — HUMAN`

## Exact file-open order

Record every first open and material re-open, including optional or attempted
opens. The route file is first scored in each stage; the Stage B handoff is the
first substantive artifact.

| Stage | Sequence | Exact time | File or attempted surface | Expected / optional / prohibited | Outcome or deviation |
| --- | ---: | --- | --- | --- | --- |
| | | | | | |

## Full-route boundary and count reconciliation

| Required boundary | Event ID | Timestamp/timezone | Prior-event or manifest binding | Result/deviation |
| --- | --- | --- | --- | --- |
| `ENTRY_BRANCH_SELECTED` | | | | |
| `RUN_STARTED` | | | | |
| `STAGE_A_CONTEXT_GATE_OPENED` | | | | |
| `STAGE_A_STARTED` | | | | |
| `HANDOFF_LAYOUT_PROOF_COMPLETED` | | | | |
| `STAGE_A_MATERIAL_FEEDBACK_COMPLETED` | | | | |
| `STAGE_A_ENDED` | | | | |
| `STAGE_B_CONTEXT_GATE_OPENED` | | | | |
| `STAGE_B_STARTED` | | | | |
| `STAGE_B_SCORING_ENDED` | | | | |
| `DEBRIEF_INPUT_MANIFEST_CREATED` | | | | |
| `DEBRIEF_INPUT_MANIFEST_VERIFIED` | | | | |
| `STAGE_B_SECTION_6_DEBRIEF_OPENED` | | | | |
| `STAGE_B_SECTION_6_DEBRIEF_COMPLETED` | | | | |
| `STAGE_B_ENDED` | | | | |

- Debrief input manifest exact filename/hash:
  `DATA-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt` /
- Section 6/debrief exact output filename/hash/state:
  `DATA-B-SECTION-6-DEBRIEF-v1.md` / / `DEBRIEF COMPLETE`
- Stage A explanation or repair withheld through scoring end: yes / no /
  deviation
- Scored bytes unchanged by debrief: yes / no / deviation

| Reconciled count | Declared | Observed | Match or deviation |
| --- | ---: | ---: | --- |
| Participant/run input files | | | |
| Files opened/read | | | |
| Synthetic helper access/refusal rows across distinct per-phase logs | | | |
| Execution-log events bound to helper rows | | | |
| Helper rows bound to exact phase-input manifest filename/path/hash | | | |
| Governed scored artifacts | | | |
| Governing-manifest verifications | | | |
| Detached verification records | | | |
| Required stage-boundary events | | | |
| Debrief completions | 1 | | |

- Six scored freeze chains complete: yes / no / deviation
- Full selected-branch route complete before results: yes / no / deviation
- Synthetic helper access rows and execution events reconcile one-to-one: yes /
  no / `NOT APPLICABLE — HUMAN`
- Every config and helper invocation matched the exact verified phase-input
  manifest membership/hashes: yes / no / `NOT APPLICABLE — HUMAN`
- Synthetic helper-only procedural compliance: passed / failed / `NOT
  APPLICABLE — HUMAN`
- Technical platform restriction/security result: `NOT ESTABLISHED` unless
  separately demonstrated / `NOT APPLICABLE — HUMAN`

## Revised-detail and Stage B transfer verification

- Revision-phase input manifest exact filename/hash:
  `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` /
- Immutable live-update participant input exact filename/hash:
  `DATA-A-LIVE-UPDATE-v1.md` /
- Revision-phase manifest binds both required initial artifacts, their
  governing manifest, detached record, and exact live-update input: yes / no /
  deviation
- Optional `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md` included in both the
  initial and revision-phase manifests when used, and absent from both when not
  used: yes / no / deviation
- Live-update filename and bytes matched before opening; no omission, rename,
  regeneration, summary, substitution, mismatch, or unmanifested delivery:
  yes / no / deviation
- Revised manifest verified before detached record was created: yes / no /
  deviation
- Detached record completed before handoff opened: yes / no / deviation
- Detached record exact filename/hash:
  `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md` /
- Revised governing manifest exact filename/hash:
  `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` /
- Manifest verified and does not list/hash itself: yes / no / deviation
- Optional contract pre-hash state: `REVISED COMPLETE` and included / `NOT USED`
- Any incomplete state or premature artifact self-declaration of `FROZEN`:
  none / deviation

| Handoff-linked exact local filename | Required or optional | Artifact ID/version | Completion timestamp/timezone | Pre-hash state | SHA-256 | Detached freeze status | Matched record/manifest | Supplied to Stage B under same filename |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `DATA-A-REVISED-WORKBOOK-v1.md` | required | | | `REVISED COMPLETE` | | `FROZEN` | | |
| `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md` | required | | | `REVISED COMPLETE` | | `FROZEN` | | |
| `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md` | optional | | | `REVISED COMPLETE` / `NOT USED` | | `FROZEN` / `NOT USED` | | |

A rename, regenerated copy, summary, substitution, omission, missing record or
manifest, mismatch, wrong pre-hash state, or missing detached `FROZEN` status
for an included artifact stops detailed read-back.

## Temporal freeze evidence

For each scope, confirm this order from retained timestamps and immutable
bytes: artifact completion -> governing manifest creation -> successful
manifest verification -> detached-record creation. The next sealed phase or
closing evidence manifest then hashes the artifact, governing manifest, and
detached record. Record failures as deviations; do not fill missing history
from recollection.

| Scope | Exact artifact filename(s), ID/version, completion time/timezone, state, hash | Governing manifest filename/hash | Observed manifest verification time/timezone and result | Detached record filename/hash and completion time/timezone | Next phase/evidence manifest and preserved location |
| --- | --- | --- | --- | --- | --- |
| Stage A initial | required `DATA-A-INITIAL-WORKBOOK-v1.md`; required `DATA-A-INITIAL-READINESS-ASSESSMENT-v1.md`; optional `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md`; `INITIAL COMPLETE` | `DATA-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt` / | | `DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md` / | `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` /; includes exact `DATA-A-LIVE-UPDATE-v1.md`; optional initial contract iff used and in governing manifest |
| Stage A revised set | required revised files; optional only if used | `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` / | | `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md` / | Stage B Phase 2 input / |
| Stage A handoff | `DATA-A-ONE-SCREEN-HANDOFF-v1.md`; `HANDOFF COMPLETE` | `DATA-A-HANDOFF-SHA256SUMS-v1.txt` / | | `DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md` / | Stage B Phase 1 input / |
| Stage B Section 1 | `DATA-B-SECTION-1-SCAN-v1.md`; `SECTION 1 COMPLETE` | `DATA-B-SECTION-1-SHA256SUMS-v1.txt` / | | `DATA-B-SECTION-1-FREEZE-VERIFICATION-v1.md` / | Stage B Phase 2 input / |
| Stage B Section 2 | `DATA-B-SECTION-2-DETAIL-v1.md`; `SECTION 2 COMPLETE` | `DATA-B-SECTION-2-SHA256SUMS-v1.txt` / | | `DATA-B-SECTION-2-FREEZE-VERIFICATION-v1.md` / | Stage B Phase 3 input / |
| Stage B Sections 3-5 | `DATA-B-SECTIONS-3-5-DECISION-v1.md`; `SECTIONS 3-5 COMPLETE` | `DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt` / | | `DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md` / | Closing evidence / |

## Detached-record required-field audit

Do not infer missing history. Each row must match the detached record and the
facilitator execution/access log. Any blank, failed verification, output
omission, or record completion that is not explicitly later blocks `FROZEN`.

| Scope | Attempt ID | Phase | Artifact actor | Facilitator | Manifest verifier | Exact command | Complete observed output | Exit code | Verification timestamp/timezone | Record-completing actor | Later record-completion timestamp/timezone | Chronology and log match |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| Stage A initial record audit | | | | | | | | | | | | |
| Stage A revised record audit | | | | | | | | | | | | |
| Stage A handoff record audit | | | | | | | | | | | | |
| Stage B Section 1 record audit | | | | | | | | | | | | |
| Stage B Section 2 record audit | | | | | | | | | | | | |
| Stage B Sections 3-5 record audit | | | | | | | | | | | | |

- Every governing manifest excludes itself and its later detached record:
  yes / no / deviation
- Every governed artifact contains no own hash, future verification time, or
  self-declared `FROZEN`: yes / no / deviation
- Every next phase/evidence manifest hashes the artifact(s), governing manifest,
  and detached record under literal filenames: yes / no / deviation

## Post-freeze corrections

Never overwrite a freeze. The planned live-update revision is not a correction
of frozen revised bytes. Preserve both versions and record every later
correction. Every corrected artifact requires both a new immutable filename and
a new artifact ID/version, plus a new governing manifest and detached record.

| Correction ID | Reason | Correction timestamp/timezone | Preserved old artifact set, manifest, record | Exact new filename, ID/version, SHA-256 | Replacement governing manifest and detached record | Action/effect |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Timing and interventions

| Stage/activity | Start | End | Elapsed | Notes |
| --- | --- | --- | ---: | --- |
| A recognition | | | | |
| A readiness artifact | | | | |
| A live update | | | | |
| A handoff | | | | |
| B read-back | | | | |
| B decision | | | | |

| Time | Pause or participant question | Response or non-response | Gate affected | Interpretation effect |
| --- | --- | --- | --- | --- |
| | | | | |

## Handoff layout proof

- Layout-proof exact filename/hash:
  `DATA-A-HANDOFF-LAYOUT-PROOF-v1.md` /
- Frozen handoff Markdown exact filename/hash:
  `DATA-A-ONE-SCREEN-HANDOFF-v1.md` /
- Generated PDF exact filename/hash:
  `DATA-A-ONE-SCREEN-HANDOFF-v1.pdf` /
- Exact rendering command and tool versions retained: yes / no / deviation
- US Letter portrait, exactly one page: yes / no / unverifiable
- Every margin at least 0.5 inch: yes / no / unverifiable
- Body and table text at least 9 points: yes / no / unverifiable
- Reader-facing words, excluding only immutable provenance metadata: / 450 max
- No clipping, overlap, hidden overflow, or unreadable shrinking: yes / no /
  unverifiable
- Literal layout state: `LAYOUT PASSED` / `HOLD — LAYOUT FAILED` / `UNRUN`
- Human scanability/comprehension state: `UNRUN` unless separately consented

A favorable one-page or one-screen claim without the completed proof record,
retained PDF, page count, rendering command, tool versions, and PDF hash is a
deviation and cannot be `LAYOUT PASSED`.

| Time | Exact intervention | Level | Gate affected | Interpretation effect |
| --- | --- | --- | --- | --- |
| | | | | |

## Material feedback after governed artifacts close

Collect this feedback here after the handoff's detached record verifies. Do not
reopen or append it to the governed practitioner workbook or handoff.

- Explanation or prompt that changed the participant's thinking:
- Term or field that was unclear:
- Important decision the materials missed:
- Unsupported confidence the materials encouraged:
- What the participant says this exercise cannot establish:

## Gate results

| Gate | Score/state | Exact evidence | Negative or boundary finding |
| --- | --- | --- | --- |
| RV-1 | | | |
| RV-2 | | | |
| RV-3 | | | |
| RV-4 | | | |
| RV-5 | | | |
| RV-6 | | | |
| RV-7 | | | |

## Deviations and stops

| ID | Condition | What occurred | Action | Evidence retained | Effect |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

- Retained rejected attempts, exact identities/manifests, stops, and non-score
  dispositions:
- Semantic invention or unsupported fact, exact artifact/location, scoring
  effect, and retained correction state:
- Unexplained count, timing, hash, open/read, or artifact variance:

## Findings and disposition

| ID | Finding | Source | Severity | Revise / retest / hold / remove | Owner | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Truthful state statement

- Protocol state: six freeze chains complete / full route complete / partial /
  stopped / unrun
- Synthetic behavior state: passed for exact pair / partial / failed / unrun
- Layout state: passed / hold-failed / unrun
- Human evidence state: `UNRUN` unless a consented human attempt exists
- Data-readiness claim state: `UNRUN`
- Real-world evidence state: `UNRUN`
- What this exact pair establishes:
- What it does not establish:
- Packet state after authorized review:
- Files changed only after raw evidence was preserved:
- Next attempt and version:

## Immutable results completion before log close

- Final pre-close execution-log event ID and entry SHA-256:
- Results-record completion timestamp/timezone:
- Results-record completing actor/facilitator:
- Results-record state: `RESULTS COMPLETE`
- No predicted final closed-log hash or future closeout timestamp appears in
  this record: yes / no

Only after all fields are complete may the facilitator log
`RUN_RESULTS_COMPLETED` for the immutable result and then record `LOG_CLOSED`,
validate `DATA-EXECUTION-ACCESS-LOG-v1.jsonl`, and copy it without byte change to the dedicated
closeout input. The later `DATA-RUN-CLOSEOUT-v1.md` binds the observed
closed-log hash, `DATA-RUN-CLOSEOUT-SHA256SUMS-v1.txt` hash, and this completed
results-record hash. Do not reopen this result after log close.
