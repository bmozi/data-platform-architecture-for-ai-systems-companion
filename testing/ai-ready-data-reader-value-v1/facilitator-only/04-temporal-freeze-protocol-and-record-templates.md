# Temporal Freeze Protocol and Record Templates

**Packet:** DATA-RV-PILOT-001 version 1.2.8
**Status:** Facilitator-only static protocol and blank run-record schema;
prepared and unrun

Version 1.2.8 binds each synthetic helper config to the exact verified
phase-input manifest identity/path/hash and enforces full membership/hash
equality on every invocation. It preserves v1.2.6's pre-run checksum-bound
synthetic access boundary and v1.2.5's entry-branch, full-route,
immutable-results, external-closeout, and literal-layout controls and v1.2.4's
exact immutable `DATA-A-LIVE-UPDATE-v1.md` and optional-contract semantics.
Every detached record requires attempt, phase, actor, facilitator,
exact verification command/output/exit/time/timezone, and a later
record-completion timestamp/timezone. The facilitator separately maintains the
[`execution and access log`](05-execution-and-access-log.md). Passing static
checks is non-human evidence only.

## Valid causal order

`COMPLETE ARTIFACT BYTES -> GOVERNING MANIFEST -> MANIFEST VERIFICATION ->`
`DETACHED VERIFICATION RECORD -> NEXT-PHASE SEALED INPUT MANIFEST`

1. Complete every governed artifact's bytes, ID/version, completion
   timestamp/timezone, and complete pre-hash state.
2. Create a manifest over only those completed artifacts. It excludes itself
   and the later detached record.
3. Run the exact verification command and retain its complete output, exit
   code, observed timestamp, timezone, actor, and facilitator.
4. Only after successful verification, complete the detached record. Give the
   record its own later completion timestamp and timezone; never claim its own
   hash.
5. Create and verify the next phase's sealed manifest over the governed
   artifacts, their manifest, their detached record, and newly released files.
6. Keep all facilitation and orchestration outside participant input. An
   `ORCHESTRATION.md`, run note, hidden prompt, facilitator file, or other
   undeclared file in participant input is a stop.

## Exact freeze inventory

| Freeze | Governed artifact(s) and required state | Governing manifest | Later detached verification record | Next-phase input manifest |
| --- | --- | --- | --- | --- |
| Stage A initial | `DATA-A-INITIAL-WORKBOOK-v1.md`; `DATA-A-INITIAL-READINESS-ASSESSMENT-v1.md`; optional `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md`; `INITIAL COMPLETE` | `DATA-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt` | `DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md` | `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt`, also binding exact new input `DATA-A-LIVE-UPDATE-v1.md` and the optional initial contract iff used and included in the governing manifest |
| Stage A revised | required `DATA-A-REVISED-WORKBOOK-v1.md`; required `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md`; optional `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md`; `REVISED COMPLETE` | `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` | `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md` | `DATA-A-HANDOFF-PHASE-INPUT-SHA256SUMS-v1.txt` |
| Stage A handoff | `DATA-A-ONE-SCREEN-HANDOFF-v1.md`; `HANDOFF COMPLETE` | `DATA-A-HANDOFF-SHA256SUMS-v1.txt` | `DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md` | `DATA-B-PHASE-1-INPUT-SHA256SUMS-v1.txt` |
| Stage B Section 1 | `DATA-B-SECTION-1-SCAN-v1.md`; `SECTION 1 COMPLETE` | `DATA-B-SECTION-1-SHA256SUMS-v1.txt` | `DATA-B-SECTION-1-FREEZE-VERIFICATION-v1.md` | `DATA-B-PHASE-2-INPUT-SHA256SUMS-v1.txt` |
| Stage B Section 2 | `DATA-B-SECTION-2-DETAIL-v1.md`; `SECTION 2 COMPLETE` | `DATA-B-SECTION-2-SHA256SUMS-v1.txt` | `DATA-B-SECTION-2-FREEZE-VERIFICATION-v1.md` | `DATA-B-PHASE-3-INPUT-SHA256SUMS-v1.txt` |
| Stage B Sections 3-5 | `DATA-B-SECTIONS-3-5-DECISION-v1.md`; `SECTIONS 3-5 COMPLETE` | `DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt` | `DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md` | `DATA-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt` |

## Exact Stage A revision-phase input inventory

Create `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` over:

1. required `DATA-A-INITIAL-WORKBOOK-v1.md`;
2. required `DATA-A-INITIAL-READINESS-ASSESSMENT-v1.md`;
3. conditional `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md` exactly when it
   was used and appears in the initial governing manifest, and otherwise not;
4. `DATA-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt`;
5. `DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md`; and
6. exact immutable `DATA-A-LIVE-UPDATE-v1.md`.

No other member is allowed. Verify this manifest before opening the live
update. Record the exact manifest/update filenames and hashes and the optional
contract disposition. Omission, rename, regeneration, summary, substitution,
mismatch, or an unmanifested update is a stop and deviation.

## Mutually exclusive run entry

Select exactly `HUMAN` or `SYNTHETIC` once before `RUN_STARTED`.

- `HUMAN` requires completed real-person consent and every required
  privacy/authority prerequisite before each applicable stage opens.
- `SYNTHETIC` forbids fictional human affirmations and human-result claims.
  Complete `07-synthetic-context-record.md` as exact
  `DATA-SYNTHETIC-CONTEXT-v1.md`, create
  `DATA-SYNTHETIC-CONTEXT-SHA256SUMS-v1.txt` over that record alone, and verify
  it before scored input opens.

Branch omission, switching, mixing, or treating a blank human notice as
synthetic consent is a stop.

## Synthetic exact-file access boundary

Human participants use ordinary file surfaces and receive no terminal,
repository, Git, or helper authority. For `SYNTHETIC`, select exact source
`07-synthetic-exact-file-access.py` before `RUN_STARTED`; copy it byte for byte
as `DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py` into every predeclared phase access
directory; and bind the copies, exact invocation, schema, reserved paths, and
`08-synthetic-access-plan-and-config-template.md` in the orchestration manifest
and synthetic context. An absent, after-start, changed, or overbroad helper is
a stop.

Do not invent future artifact hashes. After a phase's exact sealed-input
manifest is created and verified, derive
`DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json` from those observed filenames
and hashes in route order. The config also binds that exact phase-input
manifest's flat filename, absolute path inside the sealed input, and observed
SHA-256. Then create and verify
`DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt` over exactly the pre-run
helper copy and current config before `CURRENT_PHASE_GATE_OPENED`. Each phase
uses a distinct external `DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl`; every
grant, optional skip, or refusal binds one execution-log event. Future/dummy
hashes, an absent, drifted, outside-root, malformed, duplicate, path-bearing,
or self-listing phase-input manifest, config/manifest membership or hash
mismatch, config creation after the gate, shared logs, general commands,
direct reads, concurrent invocation, pasted content, or ad hoc message
delivery are stops.

On every invocation, the helper rehashes and parses the bound phase-input
manifest and requires its complete flat filename/hash set to equal the
config's ordered-file set before reading a target. Read order may be declared
by the config only after that equality succeeds. The helper appends each row
through an explicitly serialized write-all loop and fsync; concurrent
invocation is outside this local durability model. The helper does not prove
the host platform removed other tools or provide cross-process security
isolation. Record helper-only procedural compliance separately, and keep
technical platform restriction/security `NOT ESTABLISHED` unless separately
demonstrated with retained platform evidence.

## Full-route closure after six freeze chains

The six scored freeze chains remain exactly the six rows above. Their
completion does not establish full-route closure. The append-only log must also
record, in order: `RUN_STARTED`; Stage A context gate/start, material feedback,
and end; Stage B context gate/start and scoring end; debrief-manifest creation
and verification; Section 6 open/completion; Stage B end; results completion;
and log close.

`DATA-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt` contains every and only:

1. `DATA-B-SECTIONS-3-5-DECISION-v1.md`;
2. `DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt`;
3. `DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md`; and
4. exact `04-decision-owner-workbook.md` as the Section 6/debrief input.

Verify it only after `STAGE_B_SCORING_ENDED`. Complete Section 6 as exact
`DATA-B-SECTION-6-DEBRIEF-v1.md`, state `DEBRIEF COMPLETE`, without changing
scored bytes. Stage A explanation or repair is forbidden before scoring end.

## Immutable results and external closeout

Complete the blank results template as exact `DATA-RUN-RESULTS-v1.md`, state
`RESULTS COMPLETE`, before `LOG_CLOSED`. It contains the final pre-close log
checkpoint but no predicted final log hash or future closeout timestamp. After
close, validate and copy `DATA-EXECUTION-ACCESS-LOG-v1.jsonl` without byte
change to a dedicated closeout input beside the completed results. Create and
verify `DATA-RUN-CLOSEOUT-SHA256SUMS-v1.txt` over those two files. Only then
complete `DATA-RUN-CLOSEOUT-v1.md`, binding the observed closed-log,
closeout-manifest, and results hashes.
The closeout record is later external provenance.

## Literal one-page layout proof

Complete `DATA-A-HANDOFF-LAYOUT-PROOF-v1.md` from the declared layout-proof
template. The completed handoff retains the exact
`<!-- IMMUTABLE PROVENANCE START -->` and
`<!-- IMMUTABLE PROVENANCE END -->` markers, its eight compact audit lines,
all five required reader sections and labels, non-clickable exact-filename detail pointers, the
five declared section ceilings and 335-word reader target, and no Markdown
table or copied detail. Immutable provenance is excluded only from the
reader-word count, never from page layout. Preserve the frozen Markdown, generated
`DATA-A-ONE-SCREEN-HANDOFF-v1.pdf`, page count, rendering command, tool
versions, and PDF SHA-256. `LAYOUT PASSED` requires one US Letter portrait page,
margins of at least 0.5 inch, body text at least 9 points, no more
than 450 reader-facing words excluding only immutable provenance metadata, and
no clipping, overlap, hidden overflow, or unreadable shrinking. Otherwise
retain `HOLD — LAYOUT FAILED`. Neither state proves human comprehension.

## Required detached-record fields

- Attempt ID
- Stage and phase
- Freeze-verification record ID/version and exact filename
- Artifact-producing actor code
- Facilitator name/code
- Manifest verifier name/code and relationship
- Exact manifest-verification command
- Complete observed command output
- Observed command exit code
- Verification result
- Observed verification timestamp and timezone, as separate fields
- Record-completing actor name/code
- Record completion timestamp and timezone, explicitly later than verification
- Governing manifest exact filename and SHA-256
- Exact artifact inventory, IDs/versions, completion metadata, states, hashes,
  and manifest matches
- Stop/deviation and `FROZEN` determination

Any blank required field, failed verification, or chronology error prevents
`FROZEN`. Do not reconstruct missing command output, actors, or times later.

## Immutable correction rule

A later correction preserves the old artifacts, manifest, detached record, and
execution log. It uses a new immutable filename and artifact ID/version for
every corrected artifact, a new governing manifest, and a new detached record.

This protocol can establish a traceable file history for one attempt. It does
not establish data readiness, AI safety, comprehension, or business value.
