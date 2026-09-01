# Handoff Layout Proof v2

- Attempt: `DATA-SYN-20260830-007`
- Markdown: `DATA-A-ONE-SCREEN-HANDOFF-v2.md`
- HTML: `DATA-A-ONE-SCREEN-HANDOFF-v2.html`
- PDF: `DATA-A-ONE-SCREEN-HANDOFF-v2.pdf`
- Renderer: WeasyPrint 69.0 with Poppler 26.04.0 for raster inspection
- CSS: `DATA-A-ONE-SCREEN-HANDOFF-v2.css`
- Contract: US Letter portrait, margins at least 0.5 inch, body text at least 9 points
- Exact rendering command: `pandoc DATA-A-ONE-SCREEN-HANDOFF-v2.md --standalone --metadata title='' -o DATA-A-ONE-SCREEN-HANDOFF-v2.html`; `weasyprint DATA-A-ONE-SCREEN-HANDOFF-v2.html DATA-A-ONE-SCREEN-HANDOFF-v2.pdf --stylesheet DATA-A-ONE-SCREEN-HANDOFF-v2.css`; `pdftoppm -png -r 150 DATA-A-ONE-SCREEN-HANDOFF-v2.pdf page`
- Result: `LAYOUT PASSED` locally
- Page metrics: exactly 1 page; Letter portrait (612 x 792 points); 0.5-inch page margins; body text 9 points; no clipping, overlap, hidden overflow, or unreadable shrinking observed in raster inspection.
- PDF SHA-256: `12addbbaaa11701ccd3159882fae0390bfeaf6511c51cdfec5219c1903d653a2`
- Raster inspection: one page reviewed; title is singular, all five sections are present, text is legible, and no clipping/overlap/overflow was observed.
- Human scanability/comprehension: `UNRUN`

This v2 proof is a renderer/layout trial only. It does not establish human
comprehension, practitioner usability, readiness, or safety.
