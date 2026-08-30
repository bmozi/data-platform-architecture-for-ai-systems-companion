# Stage A One-Screen Handoff

**Packet:** DATA-RV-PILOT-001 version 1.2.8
**Status:** Blank Stage A transfer; open only after the revised-detail detached
verification record verifies

Build a decision handoff, not another workbook. Use short, plain answers that a
person outside the data team can scan without verbal repair. Point to the exact
revised-record filenames instead of copying their detail. Write `UNASSIGNED` when no
owner has been assigned and `UNKNOWN` when the supplied evidence cannot
answer. Never invent a person, authority, fact, or date.

## Completed-output contract

Complete this template as exact `DATA-A-ONE-SCREEN-HANDOFF-v1.md` only after
`DATA-A-REVISED-FREEZE-VERIFICATION-v1.md` verifies. In the completed output:

- delete this guidance and every blank prompt;
- retain the title, the immutable provenance block, and Sections 1-5 only;
- use no Markdown table or copied artifact detail;
- keep every declared detail filename in the provenance block as a non-clickable
  exact-filename pointer; do not use a Markdown link, because Stage B Section 1
  receives the handoff before revised detail is released in Section 2;
- use at most four bullets in a section and one sentence per bullet; and
- target no more than `335` reader-facing words across Sections 1-5, including
  headings and labels. The hard layout contract remains no more than `450`
  reader-facing words.

Section budgets are ceilings, not targets:

- Section 1 — Decision and beneficiary: `55` words;
- Section 2 — Allowed and withheld: `55` words;
- Section 3 — Evidence and uncertainty: `85` words;
- Section 4 — Ownership, risk, and action: `85` words; and
- Section 5 — Proof, gates, and limits: `55` words.

The completed file targets one US Letter portrait page with every margin at
least 0.5 inch, body text at least 9 points, no clipping, overlap, hidden
overflow, or unreadable shrinking, and no more than 450 reader-facing words
excluding only immutable provenance metadata. The provenance block is excluded
from the reader-word count but not from page layout, so keep it to the eight
compact lines below. Put depth in the pointed-to artifacts, not an attachment,
copied inventory, or verbal note.

## Immutable provenance block

Keep the two marker comments byte-for-byte. Replace every prompt inside them
with observed, already-frozen metadata. Use one physical line per item and no
prose explanation.

<!-- IMMUTABLE PROVENANCE START -->
- Run/artifact: packet, attempt, actor, handoff artifact ID/version, completion timestamp/timezone, and `HANDOFF COMPLETE`.
- Initial lineage: exact non-clickable initial workbook and readiness filename pointers plus artifact IDs/versions/hashes.
- Revised workbook: exact non-clickable filename pointer, artifact ID/version, completion timestamp/timezone, `REVISED COMPLETE`, SHA-256, `FROZEN`.
- Revised readiness assessment: exact non-clickable filename pointer, artifact ID/version, completion timestamp/timezone, `REVISED COMPLETE`, SHA-256, `FROZEN`.
- Optional revised data-product contract: same metadata when used, or exact `NOT USED`.
- Revised governing manifest: exact non-clickable filename pointer to `DATA-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt` and its SHA-256.
- Revised detached record: exact non-clickable filename pointer to `DATA-A-REVISED-FREEZE-VERIFICATION-v1.md` and its SHA-256.
- Later handoff verification: filename-only pointer to `DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md`; no future hash or time.
<!-- IMMUTABLE PROVENANCE END -->

## 1. Decision and beneficiary — 55 words maximum

- **Current decision and bounded scope:**
- **Who benefits and the exact use:**

## 2. Allowed and withheld — 55 words maximum

- **What the assistant may search:**
- **What data or use is withheld:**

## 3. Evidence and uncertainty — 85 words maximum

- **Current evidence class, mapped to each material claim:**
- **Known evidence:**
- **Unknown or disputed evidence:**

## 4. Ownership, risk, and action — 85 words maximum

- **Assigned owner, or `UNASSIGNED`; assigning or acting authority, or `UNKNOWN`:**
- **Largest unacceptable outcome:**
- **Immediate next action:**
- **Review date or evidence-based trigger:**

## 5. Proof, gates, and limits — 55 words maximum

- **How we prove the exact policy used:**
- **How corrections reach the served copy:**
- **Separate model, action-authority, and release gates still unresolved, plus what this exercise cannot establish:**

## Freeze and layout sequence

Once the provenance block, Sections 1-5, and completion metadata are final, do
not edit the handoff. Create `DATA-A-HANDOFF-SHA256SUMS-v1.txt` over this
handoff only; the manifest never hashes itself or the later record. Verify the
manifest, capture the observed timestamp/timezone, and only then create
`DATA-A-HANDOFF-FREEZE-VERIFICATION-v1.md`. The handoff must not contain its
own hash, the detached record's hash, or a future verification time. Stage B's
sealed Phase 1 input manifest hashes the handoff, its governing manifest, and
the detached record. Do not revise the handoff during Stage B read-back.

After freeze, preserve the Markdown and render
`DATA-A-ONE-SCREEN-HANDOFF-v1.pdf`. Record page count, exact rendering command,
tool versions, PDF SHA-256, margins, text size, reader-facing word count, and
visual defects in `DATA-A-HANDOFF-LAYOUT-PROOF-v1.md`. A two-page, over-budget,
or compressed proof is `HOLD — LAYOUT FAILED`. Even `LAYOUT PASSED` is local
layout evidence, not proof that a person can scan, understand, or use the
handoff.
