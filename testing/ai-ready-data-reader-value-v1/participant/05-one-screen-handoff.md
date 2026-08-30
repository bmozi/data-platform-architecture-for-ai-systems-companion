# Stage A One-Screen Handoff

**Packet:** DATA-RV-PILOT-001 version 1.2.0
**Status:** Blank Stage A transfer; open only after the revised-detail freeze
record verifies

Use short, plain answers that a person outside the data team can scan without
verbal repair. Link the detailed records instead of copying them. Write
`UNASSIGNED` when no owner has been assigned and `UNKNOWN` when the supplied
evidence cannot answer. Never invent a person, authority, or date.

**Format rule:** keep this to one printed page or one screen and one line per
field. Put depth in the linked artifacts, not in an attachment or verbal note.
Complete it as `DATA-A-ONE-SCREEN-HANDOFF-v1.md` only after
`DATA-A-REVISED-FREEZE-RECORD-v1.md` verifies.

- **Handoff artifact ID and version:**
- **Linked initial artifact IDs, versions, and hashes:**
- **Detached revised freeze record exact local filename/hash:**
  `DATA-A-REVISED-FREEZE-RECORD-v1.md` /
- **Governing revised-artifact manifest exact local filename/hash:**
  `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` /

## Exact revised-detail inventory

Stage B receives each included file under the same literal local filename. The
optional contract must be `NOT USED` when it was not opened. Copy IDs,
versions, completion timestamps/timezones, pre-hash states, hashes, and freeze
statuses from the verified detached record. A rename, regenerated copy,
summary, substitution, omission, mismatch, pre-hash state other than `REVISED
COMPLETE`, or missing detached `FROZEN` status for an included file stops
detailed read-back.

| Exact local filename | Required or optional | Artifact ID/version | Completion timestamp/timezone | Pre-hash state | SHA-256 | Detached freeze status |
| --- | --- | --- | --- | --- | --- | --- |
| `DATA-A-REVISED-WORKBOOK-v1.md` | required | | | `REVISED COMPLETE` | | `FROZEN` |
| `DATA-A-REVISED-READINESS-ASSESSMENT-v1.md` | required | | | `REVISED COMPLETE` | | `FROZEN` |
| `DATA-A-REVISED-DATA-PRODUCT-CONTRACT-v1.md` | optional | | | `REVISED COMPLETE` / `NOT USED` | | `FROZEN` / `NOT USED` |

## Decision transfer

- **Current evidence class, mapped to each material claim:** constructed
  scenario fact / constructed live-update fact / participant inference /
  proposed control / unknown / other stated class
- **Who benefits and the exact use:**
- **Current decision and bounded scope:**
- **What the assistant may search:**
- **What data or use is withheld:**
- **How we prove the exact policy used:**
- **How corrections reach the served copy:**
- **Assigned owner, or `UNASSIGNED`:**
- **Assigning or acting authority, or `UNKNOWN`:**
- **Known evidence:**
- **Unknown or disputed evidence:**
- **Largest unacceptable outcome:**
- **Immediate next action:**
- **Review date or evidence-based trigger:**
- **Separate model, action-authority, and release gates still unresolved:**
- **Separate handoff freeze timestamp/timezone, ID/version, SHA-256, and
  manifest reference:**

Freeze this file after the detailed Stage A revision. Do not revise it during
Stage B's initial read-back.
