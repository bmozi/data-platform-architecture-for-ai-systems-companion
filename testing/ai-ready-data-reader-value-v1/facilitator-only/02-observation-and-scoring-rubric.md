# Observation and Scoring Rubric

**Packet:** DATA-RV-PILOT-001 version 1.2.4
**Status:** Predetermined, blank, and unrun

Score retained behavior, not agreement with preferred wording.

## Scale

- **2 — unaided and defensible:** explicit, coherent, and reached with L0–L1.
- **1 — partial or prompted:** material issue appears but is incomplete or
  requires L2–L3.
- **0 — absent, contradicted, unsafe, or coached:** missed, invented, unsafe,
  or supplied by L4.
- **NA — not interpretable:** missing or materially contaminated evidence.

Do not treat the total as a validated psychometric score.

## Seven reader-value gates

| Gate | Observable evidence | Stage | Score | Evidence location |
| --- | --- | --- | ---: | --- |
| RV-1 Recognition | Explains why “we have data” does not answer the use question | A | | |
| RV-2 Plain understanding | Explains use-specific readiness and abstention outside data jargon | A and B | | |
| RV-3 First useful artifact | Produces a bounded assessment with explicit unknowns and separate gates | A | | |
| RV-4 Outside read-back | Stage B reconstructs use, scope, stop, owner state, authority, evidence, and next trigger without repair | B | | |
| RV-5 Failure discovery | Detects obsolete source, missing version, entitlement leak, and correction gap | A | | |
| RV-6 Team transfer | One-screen handoff yields evidence class, beneficiary/use, decision, allowed/withheld data/use, owner state and assigning authority, knowns/unknowns, unacceptable outcome, next action, and date or evidence trigger; links detailed artifacts | B | | |
| RV-7 Decision-owner legibility | Selects a bounded state without universal readiness or invented ROI | B | | |

For RV-6, an assigned owner is not required when none exists. Credit explicit
`UNASSIGNED` only when the handoff also names the authority or trigger that will
assign or act; credit `UNKNOWN` when the supplied facts cannot establish that
authority. A calendar date is not required when a concrete evidence-based
review trigger is given. Never reward an invented owner, authority, or date.

Score the one-screen transfer separately from the detailed read-back: `2`
requires the core decision to be scannable from the handoff alone, `1` means
the detailed artifacts were needed to recover a material core item, and `0`
means the transfer is absent, misleading, unsafe, or invented.

## Critical data-readiness gates

Mark `clear`, `unclear`, `unsafe`, or `contaminated`:

| Gate | Clear behavior | Result | Evidence |
| --- | --- | --- | --- |
| Named use | Readiness remains limited to the HG-03/HG-04 agent-reviewed draft | | |
| Meaning | Policy authority is visible; disputed `resolved` meaning is not smuggled into use | | |
| Fitness | Coverage and unknown evaluation are treated separately from availability | | |
| Provenance | Source, version, effective date, chunk/index, citation, and correction are required | | |
| Purpose and entitlement | Allowed policy use does not authorize resident notes or all-building access | | |
| Restricted-data near miss | Preserves minimum evidence without copying restricted content; checks context, output, logs, viewers, containment, ownership, retention/deletion authority, and separate legal/privacy classification | | |
| Operability | Abstention, stop trust, correction propagation, incident owner or explicit unassigned state, and reassessment exist or remain blockers | | |
| Separate gates | Data fitness does not approve model, tool, action, or release | | |
| Revision-input integrity | `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` binds both required initial artifacts, the optional initial contract exactly when used and in the initial manifest, that governing manifest, detached record, and exact immutable `DATA-A-LIVE-UPDATE-v1.md`; verification precedes opening, with no omission, rename, regeneration, summary, substitution, mismatch, or unmanifested update | | |
| Revised-detail freeze integrity | Each included revised detail reaches pre-hash `REVISED COMPLETE` with ID/version and completion timestamp/timezone; the optional contract is `REVISED COMPLETE` or `NOT USED`; the manifest then hashes only included completed bytes; verification is observed with exact time/timezone; only afterward does the detached record match the metadata, hashes, manifest filename/hash, and event and establish `FROZEN` | | |
| No temporal self-reference | The revised set, handoff, and three Stage B exports contain completion metadata and a filename-only pointer to their later record, never their own hash, the record hash, a future verification time, or self-declared `FROZEN`; no governing manifest hashes itself or its later record | | |
| Detached-record replay identity | Every record contains attempt ID, phase, artifact actor, facilitator, verifier, exact verification command, complete output, exit code, observed verification timestamp/timezone, record-completing actor, and a separately recorded later completion timestamp/timezone; any blank, failure, or reversal blocks `FROZEN` | | |
| Execution/access continuity | The facilitator-side log records ordered manifest gates, item opens/access attempts, artifact completions, manifest creations/verifications, record completions, and phase opens with filenames, actors, timestamps/timezones, predecessor bindings, and manifest SHA-256; participant input contains no undeclared orchestration or facilitator file | | |
| Handoff freeze integrity | The handoff reaches pre-hash `HANDOFF COMPLETE`; its governing manifest hashes only those completed bytes; verification time/timezone is captured; the detached record is created afterward; the sealed Stage B Phase 1 input manifest hashes the handoff, governing manifest, and detached record | | |
| Stage B exact transfer | Stage B receives the detached record, governing manifest, and every included handoff-linked revised detail under the same literal filename with matching ID/version, completion metadata, pre-hash state, hash, optional disposition, and detached freeze status; no rename, regeneration, summary, substitution, or omission occurs | | |
| Stage B sequencing | Sections 1, 2, and 3-5 each reach their declared complete pre-hash state, are hashed alone by a non-self-listing governing manifest, have that manifest verified with observed time/timezone, and only then receive a detached record; the next phase or closing manifest hashes the artifact, governing manifest, and record; Section 6 remains closed until scoring ends | | |
| Revision/correction provenance | The planned live-update revision is distinct from a later correction of frozen revised bytes; every correction preserves the prior immutable artifact set, manifest, and record, then creates a new immutable filename and new artifact ID/version for every corrected artifact, with reason, timestamp/timezone, governing manifest, and detached record | | |

Any unsafe critical gate blocks a favorable interpretation.

## Findings to record

Record exact words, initial and revised answers, intervention level, likely
source of friction, useful behavior, unsafe certainty, severity, disposition,
and regression evidence. Use bounded conclusions only for the exact version,
scenario, participant, and stage.
