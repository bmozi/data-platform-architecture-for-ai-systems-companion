# Handoff Layout-Proof Record Template

**Packet:** DATA-RV-PILOT-001 version 1.2.5
**Status:** Blank facilitator-only local layout record; no layout result exists

Complete an immutable run instance as exactly
`DATA-A-HANDOFF-LAYOUT-PROOF-v1.md`. This record tests a literal local rendering
contract; it does not test whether a person can scan, understand, or use the
handoff.

## Bound inputs and rendering evidence

- Attempt ID:
- Frozen handoff Markdown exact filename: `DATA-A-ONE-SCREEN-HANDOFF-v1.md`
- Frozen handoff Markdown SHA-256:
- Handoff governing manifest filename/hash:
- Handoff detached record filename/hash:
- Generated PDF exact filename: `DATA-A-ONE-SCREEN-HANDOFF-v1.pdf`
- Generated PDF SHA-256:
- Exact rendering command:
- Renderer and supporting tool names/versions:
- Rendering timestamp/timezone:
- PDF page count:
- PDF page size/orientation: US Letter / portrait
- Minimum observed margin on every edge, inches:
- Minimum body text size, points:
- Minimum table text size, points:
- Reader-facing word count:
- Excluded immutable provenance metadata and excluded word count:
- Clipping observed: yes / no
- Overlap observed: yes / no
- Hidden overflow observed: yes / no
- Unreadable shrinking observed: yes / no
- Proof-record completion timestamp/timezone:

## Exact local gate

Record `LAYOUT PASSED` only when the retained PDF is exactly one US Letter
portrait page, every margin is at least 0.5 inch, body and table text are at
least 9 points, reader-facing content is no more than 450 words excluding only
immutable provenance metadata, and inspection finds no clipping, overlap,
hidden overflow, or unreadable shrinking. Otherwise retain the proof and
record `HOLD — LAYOUT FAILED` with every failed condition.

- Literal layout result: `LAYOUT PASSED` / `HOLD — LAYOUT FAILED`
- Failed or unverifiable condition(s):
- PDF and proof retained in run evidence: yes / no
- Human scanability/comprehension state: `UNRUN`

A favorable one-page or one-screen claim without this completed proof, its PDF,
page count, rendering command, tool versions, and PDF hash is unsupported.
