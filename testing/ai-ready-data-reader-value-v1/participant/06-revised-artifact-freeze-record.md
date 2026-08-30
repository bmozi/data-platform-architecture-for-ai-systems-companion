# Revised Artifact Freeze Record

**Packet:** DATA-RV-PILOT-001 version 1.2.0
**Status:** Blank detached record; complete and verify before the one-screen
handoff opens

This record governs the first revised artifact set created by the planned live
update. That planned revision is not a correction of already frozen revised
bytes.

- Completed record exact local filename: `DATA-A-REVISED-FREEZE-RECORD-v1.md`
- Freeze timestamp and timezone:
- Governing manifest exact local filename:
  `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt`
- Governing manifest SHA-256:
- Manifest verification timestamp and timezone:
- Planned live-update revision complete: yes / no

The governing manifest hashes only the revised detail files included below. It
does not list or hash itself. A later Stage B delivery manifest may hash this
completed record and the governing manifest as supplied files.

## Exact revised-detail inventory

The first two rows are required. Before hashing, every included artifact must
contain its artifact ID/version, completion timestamp/timezone, and pre-hash
state `REVISED COMPLETE`; it must not self-declare `FROZEN`. The optional
contract is `REVISED COMPLETE` when used or `NOT USED` when not opened; never
invent a file for an unused optional artifact. A blank, `DRAFT`, `PENDING`,
`PENDING FREEZE`, `AWAITING FREEZE`, or equivalent incomplete state fails this
record. Matching hashes in the governing manifest plus this verified detached
record establish the later `FROZEN` condition for included artifacts.

| Exact immutable local filename | Required or optional | Artifact ID/version | Completion timestamp/timezone | Pre-hash state | SHA-256 | Matches governing manifest | Freeze status established by this record |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DATA-A-REVISED-WORKBOOK-v1.md` | required | | | `REVISED COMPLETE` | | yes / no | `FROZEN` / not established |
| `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md` | required | | | `REVISED COMPLETE` | | yes / no | `FROZEN` / not established |
| `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md` | optional | | | `REVISED COMPLETE` / `NOT USED` | | yes / no / not used | `FROZEN` / `NOT USED` / not established |

## Verification before handoff

- All included revised work is complete: yes / no
- Optional contract use is recorded without ambiguity: yes / no
- All included literal filenames match the governing manifest: yes / no
- All included IDs, versions, completion timestamps/timezones, pre-hash states,
  and hashes match: yes / no
- No incomplete-state marker or premature self-declared `FROZEN` remains:
  yes / no
- This record establishes `FROZEN` for every included verified hash: yes / no
- Record completed and verified before `05-one-screen-handoff.md` opened:
  yes / no
- Verified by, relationship, timestamp, and timezone:

Any `no`, blank required field, mismatch, rename, regenerated copy, summary,
substitution, or omission stops the handoff.

## Post-freeze correction, only if required

Do not enter the planned live-update revision here. If any already frozen byte
later changes, preserve the prior artifact and complete a new correction record
and replacement freeze. Never overwrite or reuse the old filename.

| Correction ID | Reason | Correction timestamp/timezone | Exact old filename, ID/version, SHA-256, manifest | Exact new filename, ID/version, SHA-256, manifest | Replacement freeze record |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
