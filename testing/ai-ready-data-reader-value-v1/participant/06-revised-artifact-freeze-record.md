# Detached Freeze-Verification Record Template

**Packet:** DATA-RV-PILOT-001 version 1.2.5
**Status:** Blank detached template; create an instance only after its governing
manifest has been verified

Use this template for the revised Stage A set, the handoff, Stage B Section 1,
Stage B Section 2, and Stage B Sections 3-5. A completed instance records an
observed verification event. It never predicts a future event and is never
listed in the governing manifest whose verification it records.

## Revision-input lineage for revised Stage A

Complete this section only for the revised Stage A record. For every other
scope, record `NOT APPLICABLE — different release` rather than leaving it
ambiguous.

- Revision-phase input manifest exact filename and SHA-256:
  `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` /
- Live-update participant input exact filename: `DATA-A-LIVE-UPDATE-v1.md`
- Live-update SHA-256 from the verified revision-phase input manifest:
- Both required initial artifacts, their governing manifest, detached record,
  and exact live update were included: yes / no
- Optional `DATA-A-INITIAL-DATA-PRODUCT-CONTRACT-v1.md` was included exactly
  when it appeared in the initial governing manifest and otherwise absent:
  yes / no
- Live-update filename and bytes matched before opening: yes / no
- Any omission, rename, regenerated copy, summary, substitution, mismatch, or
  unmanifested update: none / stop and deviation

## Select one exact record identity

- Initial Stage A: `DATA-A-INITIAL-FREEZE-VERIFICATION-v1.md`
- Revised Stage A: `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md`
- Stage A handoff: `DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md`
- Stage B Section 1: `DATA-B-SECTION-1-FREEZE-VERIFICATION-v1.md`
- Stage B Section 2: `DATA-B-SECTION-2-FREEZE-VERIFICATION-v1.md`
- Stage B Sections 3-5:
  `DATA-B-SECTIONS-3-5-FREEZE-VERIFICATION-v1.md`

## Observed verification event

- Attempt ID:
- Freeze scope and phase:
- Completed record exact local filename:
- Record ID/version:
- Artifact-producing actor code:
- Facilitator name/code:
- Manifest verifier name/code and relationship:
- Governing manifest exact local filename:
- Governing manifest SHA-256:
- Exact manifest verification command:
- Complete observed command output:
- Observed command exit code:
- Manifest verification result: pass / fail / deviation
- Observed manifest verification timestamp:
- Observed manifest verification timezone:
- Record-completing actor name/code:
- Record completion timestamp, explicitly later than manifest verification:
- Record completion timezone:

The governing manifest hashes only the completed governed artifacts listed
below. It never lists or hashes itself or this later record. The artifact bytes
already contain their IDs/versions, completion timestamps/timezones, complete
pre-hash states, and a filename-only pointer to this record. They contain no
self-hash, record hash, future verification time, or self-declared `FROZEN`
state.

## Exact governed-artifact inventory

| Exact immutable local filename | Artifact ID/version | Completion timestamp/timezone | Complete pre-hash state | SHA-256 | Matches governing manifest |
| --- | --- | --- | --- | --- | --- |
| | | | | | yes / no |

For revised Stage A, include every required artifact and the optional contract
only when used. Its expected complete pre-hash state is `REVISED COMPLETE`.
Expected states for the later scopes are `HANDOFF COMPLETE`, `SECTION 1
COMPLETE`, `SECTION 2 COMPLETE`, and `SECTIONS 3-5 COMPLETE`.

## Temporal and integrity determination

- Every governed artifact was complete before the manifest was created:
  yes / no
- Every artifact completion timestamp precedes or equals observed manifest
  verification: yes / no
- Literal filenames, IDs/versions, completion metadata, states, and hashes
  match: yes / no
- The governing manifest excludes itself and this record: yes / no
- No governed artifact contains its own hash or a future verification time:
  yes / no
- No incomplete-state marker or premature self-declared `FROZEN` remains:
  yes / no
- This record was created only after successful manifest verification: yes / no
- Attempt ID, phase, actors, facilitator, verification command, complete
  observed output, exit code, verification timestamp/timezone, and later record
  completion timestamp/timezone are all present: yes / no
- Determination for the exact governed bytes: `FROZEN` / not established
- Stop or deviation ID when any required answer is `no`, blank, or failed:

Any failed or blank required check means `FROZEN` is not established. Preserve
the attempted bytes and record the deviation; do not repair them in place.

## Next sealed phase

After this record is complete, the facilitator creates the next sealed
phase-input manifest—or the closing evidence manifest for the final scope—over
every governed artifact, its governing manifest, and this detached record.
Record that later manifest and its observed verification event in the external
run log. Do not add its future filename, hash, or verification timestamp to
this record, and do not reopen this record afterward. The next manifest is
separate provenance for delivery; it does not alter the earlier governing
manifest or this observed verification event.

## Immutable correction rule

After this record is complete, do not edit it or any governed file. A
correction preserves the old artifact set, manifest, and record, then creates a
new immutable replacement set with a new immutable filename and a new artifact
ID/version for every corrected artifact, a new governing manifest, and a new
detached record. Record the reason and correction timestamp/timezone in the run
log, not by modifying the old record.
