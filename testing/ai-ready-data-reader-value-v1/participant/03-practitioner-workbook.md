# Stage A Practitioner Workbook

**Packet:** DATA-RV-PILOT-001 version 1.2.3
**Status:** Blank participant record

- Participant code:
- Broad role and experience band, optional:
- Exact Stage A start recorded before first scored file opened:
- End time:
- Locked supplied-file list and digital fingerprints (frozen manifest):
- Exact file-open order is recorded by the facilitator: yes / deviation
- Undeclared orchestration, facilitator, hidden-prompt, or run-note file
  present: none / stop and deviation

## 1. Recognition before terminology

- What does the support agent need to accomplish?
- What problem exists even though Harbor Grove “has the data”?
- Who could be affected by a wrong or stale draft?
- What can become easier if the information is fit for this use?

## 2. Explain AI-ready data plainly

Explain to someone outside the data team what must be true before this
information may influence the named draft. Include one reason to abstain.

## 3. Readiness journey

| Question | Bounded answer | Evidence supplied | Unknown or disputed | Stop/reconsideration trigger |
| --- | --- | --- | --- | --- |
| Ready for what? | | | | |
| What does it mean and who has final say on meaning? | | | | |
| Is it fit for this use? | | | | |
| Can we prove the exact sources, versions, and changes used? | | | | |
| May it be used this way, and who may see what? | | | | |
| Can it remain ready? | | | | |
| Who decides and what remains separate? | | | | |

## 4. Artifact and decision

- Completed assessment file ID/version:
- Exact product/corpus/index version:
- Named use and affected parties:
- Included information:
- Excluded or prohibited information:
- Who has final say on meaning (semantic authority), or missing authority:
- Proof of origin and exact versions (provenance), plus correction path:
- When the system must not answer (abstention/stop-trust rules):
- Who may see what and for which use (purpose and entitlement):
- Separate unresolved gates:
- Outcome: approve / conditionally approve / reject / defer
- Conditions and evidence needed:

## 5. Live update

Record the update exactly as supplied.

This is the planned live-update revision that creates the first revised set.
It is not a correction of already frozen revised bytes.

- Initial answer now challenged:
- Correct behavior now:
- Source, index, entitlement, or citation issue:
- Artifact fields revised:
- Incident/correction owner or missing owner:
- Evidence still missing:

### Offline restricted-data near miss

Use only the supplied fictional update. `UNKNOWN` is valid and is safer than a
guess.

- Minimum evidence to preserve without spreading restricted content:
- Restricted content that must not be copied into this workbook or elsewhere:
- Did restricted content reach search context, draft/output, or logs? For each,
  record yes / no / UNKNOWN:
- Who may have viewed it? Named role(s) / none known / UNKNOWN:
- Immediate containment or quarantine action:
- Incident, privacy, or security owner: assigned role / `UNASSIGNED`:
- Authority or trigger that will assign an owner, or `UNKNOWN`:
- Who may authorize retention or deletion of preserved evidence, or `UNKNOWN`:
- Separate legal/privacy classification status: required / completed by an
  authorized role / not required by an authorized role / `UNKNOWN`:
- Classification or decision record ID and authorized role, or `UNKNOWN` (do
  not self-classify):
- Data-fitness decision after the near miss:
- Separate model, action-authority, and release gates still unresolved:

## 6. Monday-morning action

- Smallest useful readiness change:
- First evaluation case to add:
- Assigned owner, or `UNASSIGNED`:
- Authority or trigger that will assign the owner, or `UNKNOWN`:
- Evidence that would block or reverse the pilot:

## 7. Cross-role handoff

Before opening the handoff, save and freeze exactly:

- `DATA-A-REVISED-WORKBOOK-v1.md`;
- `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md`; and
- `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md` only if the optional contract
  was opened and completed.

Each included file must record an artifact ID, version, completion
timestamp/timezone, and pre-hash state `REVISED COMPLETE`. The optional
contract is `REVISED COMPLETE` when used or `NOT USED` otherwise. A governed
artifact may point to the exact detached verification-record filename that
will be created later, but it must not embed its own hash, the record's hash,
a future verification time, or `FROZEN`. Create
`DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` without listing or hashing the
manifest itself or the later record. Verify it at an observed time and only
then complete `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md` from the detached
record template before opening the blank handoff.

| Exact revised filename | Required or optional | Artifact ID/version | Completion timestamp/timezone | Pre-hash state |
| --- | --- | --- | --- | --- |
| `DATA-A-REVISED-WORKBOOK-v1.md` | required | | | `REVISED COMPLETE` |
| `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md` | required | | | `REVISED COMPLETE` |
| `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md` | optional | | | `REVISED COMPLETE` / `NOT USED` |

- Revised workbook artifact ID/version:
- Revised workbook completion timestamp/timezone:
- Revised workbook pre-hash state: `REVISED COMPLETE`
- Post-hash verification provenance: see
  `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md`, created only after the governing
  manifest verifies
- No incomplete state remains in any included governed artifact: yes / no

Only after those checks, complete the separate [One-Screen
Handoff](05-one-screen-handoff.md) as
`DATA-A-ONE-SCREEN-HANDOFF-v1.md`. Do not invent a person or calendar date to
make the handoff look complete. Because the revised workbook is governed before
the blank handoff opens, do not write handoff completion metadata, hashes, or
verification events back into this workbook. The facilitator records those
later events in the external results log.

If any revised frozen byte later changes, preserve the old file, use a new
immutable filename and a new artifact ID/version, and record the exact old/new
immutable filenames, IDs/versions, hashes, reason, correction
timestamp/timezone, replacement governing manifest, and replacement detached
record. Do not describe that post-freeze correction as the planned live-update
revision.
