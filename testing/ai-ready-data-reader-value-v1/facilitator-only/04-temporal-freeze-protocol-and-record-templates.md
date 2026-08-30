# Temporal Freeze Protocol and Record Templates

**Packet:** DATA-RV-PILOT-001 version 1.2.3
**Status:** Facilitator-only static protocol and blank run-record schema;
prepared and unrun

Version 1.2.3 makes the execution history auditable, not merely the final
files. Every detached record requires attempt, phase, actor, facilitator,
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
| Stage A initial | `DATA-A-INITIAL-WORKBOOK-v1.md`; `DATA-A-INITIAL-READINESS-ASSESSMENT-v1.md`; optional `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md`; `INITIAL COMPLETE` | `DATA-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt` | `DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md` | `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` |
| Stage A revised | required `DATA-A-REVISED-WORKBOOK-v1.md`; required `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md`; optional `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md`; `REVISED COMPLETE` | `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` | `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md` | `DATA-A-HANDOFF-PHASE-INPUT-SHA256SUMS-v1.txt` |
| Stage A handoff | `DATA-A-ONE-SCREEN-HANDOFF-v1.md`; `HANDOFF COMPLETE` | `DATA-A-HANDOFF-SHA256SUMS-v1.txt` | `DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md` | `DATA-B-PHASE-1-INPUT-SHA256SUMS-v1.txt` |
| Stage B Section 1 | `DATA-B-SECTION-1-SCAN-v1.md`; `SECTION 1 COMPLETE` | `DATA-B-SECTION-1-SHA256SUMS-v1.txt` | `DATA-B-SECTION-1-FREEZE-VERIFICATION-v1.md` | `DATA-B-PHASE-2-INPUT-SHA256SUMS-v1.txt` |
| Stage B Section 2 | `DATA-B-SECTION-2-DETAIL-v1.md`; `SECTION 2 COMPLETE` | `DATA-B-SECTION-2-SHA256SUMS-v1.txt` | `DATA-B-SECTION-2-FREEZE-VERIFICATION-v1.md` | `DATA-B-PHASE-3-INPUT-SHA256SUMS-v1.txt` |
| Stage B Sections 3-5 | `DATA-B-SECTIONS-3-5-DECISION-v1.md`; `SECTIONS 3-5 COMPLETE` | `DATA-B-SECTIONS-3-5-SHA256SUMS-v1.txt` | `DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md` | `DATA-B-PHASE-4-DEBRIEF-INPUT-SHA256SUMS-v1.txt` |

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
