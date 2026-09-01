# Promoted handoff artifact revision 1.2.9

**Packet:** `DATA-RV-PILOT-001`
**Promotion revision:** `1.2.9`
**Source attempt:** `DATA-SYN-20260830-007`
**Evidence state:** Synthetic layout rehearsal; not a human result
**Promotion state:** Immutable review package

This directory promotes the revised one-screen handoff from the retained
synthetic attempt into the official reader-value packet tree. The prior v1
packet and synthetic-run files remain unchanged. The promoted handoff is an
artifact candidate for the next packet revision; it does not change the
packet's `Prepared and human-unrun` status.

## Contents

- `DATA-A-ONE-SCREEN-HANDOFF-v2.md` — completed synthetic handoff
- `DATA-A-ONE-SCREEN-HANDOFF-v2.html` — rendered source used for PDF creation
- `DATA-A-ONE-SCREEN-HANDOFF-v2.pdf` — one-page US Letter layout artifact
- `DATA-A-HANDOFF-LAYOUT-PROOF-v2.md` — retained renderer and inspection record
- `SHA256SUMS` — immutable member checksums for this promotion package
- `PROMOTION-RECORD.md` — source, identity, and approval boundary

The PDF layout proof establishes only local page geometry and scanability. It
does not establish comprehension, usability, data readiness, privacy, safety,
production correctness, or business value.
*** Add File: /Users/briggs/Code/architecting-data-platforms-in-the-age-of-ai-companion/testing/ai-ready-data-reader-value-v1/promoted/1.2.9/PROMOTION-RECORD.md
# Promotion record: `DATA-RV-PILOT-001` revision 1.2.9

**Recorded:** 2026-08-30
**Source attempt:** `DATA-SYN-20260830-007`
**Source packet:** `DATA-RV-PILOT-001` version `1.2.8`
**Promotion decision:** Promote the v2 handoff and its local layout proof as
an immutable review artifact set; do not promote synthetic evidence to reader
validation.

## Source and preservation

The source files are retained under
`testing/reader-pilot-results/DATA-SYN-20260830-007/`. This package contains
byte-copied files from that attempt. `DATA-A-ONE-SCREEN-HANDOFF-v1.md` and
its v1 evidence remain historical and are not replaced. A later approved
packet revision must bind these promoted files through a new governing packet
manifest and update the protocol's literal filenames together.

## Local result

The retained layout proof reports one US Letter portrait page, minimum 0.5-inch
margins, minimum 9-point body text, and no observed clipping, overlap, hidden
overflow, or unreadable shrinking. The PDF hash is recorded in `SHA256SUMS`.

## Approval boundary

This promotion does not grant licensing or distribution approval, approve the
corresponding book edition, close security or privacy review, establish
accessibility beyond the local visual inspection, or authorize publication.
The packet remains `PREPARED / HUMAN-UNRUN`. An author or release owner must
approve the next packet version, rights and terms, corresponding book edition,
security/privacy disclosure, accessibility review, and publication metadata.
*** Add File: /Users/briggs/Code/architecting-data-platforms-in-the-age-of-ai-companion/testing/ai-ready-data-reader-value-v1/promoted/1.2.9/SHA256SUMS
932a8fa2486fe916a3a9ed85b241cc2037a172f18a778cd26d12d7bab49c0036  DATA-A-HANDOFF-LAYOUT-PROOF-v2.md
00cd0364aae7811183d84dd94b42ac8aa98ecff0ec12bb6a5fd9e008101ca42f  DATA-A-ONE-SCREEN-HANDOFF-v2.html
79ec2c3a0fbf30c6cc5e8b9c9c7b605ce3781361dd16dd6352a2216654ada3a5  DATA-A-ONE-SCREEN-HANDOFF-v2.md
12addbbaaa11701ccd3159882fae0390bfeaf6511c51cdfec5219c1903d653a2  DATA-A-ONE-SCREEN-HANDOFF-v2.pdf
