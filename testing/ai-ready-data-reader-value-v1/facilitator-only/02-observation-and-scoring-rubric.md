# Observation and Scoring Rubric

**Packet:** DATA-RV-PILOT-001 version 1.2.8
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
| RV-6 Team transfer | One-screen handoff yields evidence class, beneficiary/use, decision, allowed/withheld data/use, owner state and assigning authority, knowns/unknowns, unacceptable outcome, next action, and date or evidence trigger; points to detailed artifacts by exact non-clickable filename; uses the five-section 335-word target with no copied-detail table | B | | |
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
| Entry-branch integrity | Exactly one `HUMAN` or `SYNTHETIC` branch is selected for the whole attempt; human scored input follows completed real-person consent, while synthetic scored input follows verified exact `DATA-SYNTHETIC-CONTEXT-v1.md` and contains no fictional consent or human-result claim | | |
| Synthetic exact-file access integrity | `SYNTHETIC` alone uses byte-identical `DATA-SYNTHETIC-EXACT-FILE-ACCESS-v1.py` copies selected and orchestration/context-bound before `RUN_STARTED`; each observed-hash config binds the exact verified phase-input manifest filename/path/hash and its helper/config manifest verifies before the gate; on every invocation the helper parses and hashes the phase manifest, requires complete flat config/manifest membership/hash equality, enforces config read order, and logs every grant/refusal with that manifest filename/path/hash in a distinct per-phase log reconciled to the execution log; no absent/drifted/wrong manifest, general command, direct read, future/dummy hash, config-after-gate, or ad hoc message is used | | |
| Platform restriction claim boundary | Helper-only procedural compliance is scored separately from host-platform restriction/security; unless separately demonstrated with retained platform evidence, the latter remains `NOT ESTABLISHED` and cannot become a sandbox or security claim | | |

The literal per-phase identities are
`DATA-SYNTHETIC-EXACT-FILE-ACCESS-CONFIG-v1.json`,
`DATA-SYNTHETIC-EXACT-FILE-ACCESS-SHA256SUMS-v1.txt`, and distinct external
`DATA-SYNTHETIC-EXACT-FILE-ACCESS-LOG-v1.jsonl` files.
| Revision-input integrity | `DATA-A-REVISION-PHASE-INPUT-SHA256SUMS-v1.txt` binds both required initial artifacts, the optional initial contract exactly when used and in the initial manifest, that governing manifest, detached record, and exact immutable `DATA-A-LIVE-UPDATE-v1.md`; verification precedes opening, with no omission, rename, regeneration, summary, substitution, mismatch, or unmanifested update | | |
| Revised-detail freeze integrity | Each included revised detail reaches pre-hash `REVISED COMPLETE` with ID/version and completion timestamp/timezone; the optional contract is `REVISED COMPLETE` or `NOT USED`; the manifest then hashes only included completed bytes; verification is observed with exact time/timezone; only afterward does the detached record match the metadata, hashes, manifest filename/hash, and event and establish `FROZEN` | | |
| No temporal self-reference | The revised set, handoff, and three Stage B exports contain completion metadata and a filename-only pointer to their later record, never their own hash, the record hash, a future verification time, or self-declared `FROZEN`; no governing manifest hashes itself or its later record | | |
| Detached-record replay identity | Every record contains attempt ID, phase, artifact actor, facilitator, verifier, exact verification command, complete output, exit code, observed verification timestamp/timezone, record-completing actor, and a separately recorded later completion timestamp/timezone; any blank, failure, or reversal blocks `FROZEN` | | |
| Execution/access continuity | The facilitator-side log records ordered manifest gates, item opens/access attempts, artifact completions, manifest creations/verifications, record completions, and phase opens with filenames, actors, timestamps/timezones, predecessor bindings, and manifest SHA-256; participant input contains no undeclared orchestration or facilitator file | | |
| Handoff freeze integrity | The handoff reaches pre-hash `HANDOFF COMPLETE`; its governing manifest hashes only those completed bytes; verification time/timezone is captured; the detached record is created afterward; the sealed Stage B Phase 1 input manifest hashes the handoff, governing manifest, and detached record | | |
| Stage B exact transfer | The handoff triple is the only Stage A evidence in Phase 1, alongside the route and blank Section 1 workbook, and no runtime handoff link resolves; Phase 2 then receives the detached revised record, governing manifest, and every included handoff-pointed revised detail under the same literal filename with matching ID/version, completion metadata, pre-hash state, hash, optional disposition, and detached freeze status; no early detail, rename, regeneration, summary, substitution, or omission occurs | | |
| Stage B sequencing | Sections 1, 2, and 3-5 each reach their declared complete pre-hash state, are hashed alone by a non-self-listing governing manifest, have that manifest verified with observed time/timezone, and only then receive a detached record; the next phase or closing manifest hashes the artifact, governing manifest, and record; Section 6 remains closed until scoring ends | | |
| Full-route closure | The log records run start, both context gates and starts, Stage A material feedback/end, Stage B scoring end, verified debrief input, Section 6 completion, Stage B end, immutable results completion, and log close in order; six scored freeze chains alone are never called full-route completion | | |
| Results and external closeout | Exact `DATA-RUN-RESULTS-v1.md` is `RESULTS COMPLETE` before `LOG_CLOSED`, contains the final pre-close checkpoint but predicts no final log hash or closeout time, and later `DATA-RUN-CLOSEOUT-v1.md` binds the closed-log, closeout-manifest, and results hashes | | |
| Literal layout proof | Exact `DATA-A-HANDOFF-LAYOUT-PROOF-v1.md` retains frozen Markdown/PDF hashes, page count, rendering command/tool versions, margins, text size, word count, and defect inspection; the completed handoff retains both immutable provenance markers, five required reader sections, exact required field labels, non-clickable exact-filename detail pointers, no runtime Markdown link or table, and the 335-word target/section ceilings; `LAYOUT PASSED` requires one US Letter portrait page, margins at least 0.5 inch, text at least 9 points, at most 450 reader-facing words excluding only immutable provenance, and no clipping, overlap, hidden overflow, or unreadable shrinking | | |
| Revision/correction provenance | The planned live-update revision is distinct from a later correction of frozen revised bytes; every correction preserves the prior immutable artifact set, manifest, and record, then creates a new immutable filename and new artifact ID/version for every corrected artifact, with reason, timestamp/timezone, governing manifest, and detached record | | |

Any unsafe critical gate blocks a favorable interpretation.

Report protocol, synthetic behavior, helper procedural compliance, technical
platform restriction/security, layout, human, data-readiness, and real-world
states separately. A local layout pass is not comprehension; a synthetic
behavior pass is not a human result; helper compliance is not sandbox proof;
human, data-readiness, and real-world evidence remain `UNRUN` without
corresponding authorized evidence.

## Findings to record

Record exact words, initial and revised answers, intervention level, likely
source of friction, useful behavior, unsafe certainty, severity, disposition,
and regression evidence. Use bounded conclusions only for the exact version,
scenario, participant, and stage.
