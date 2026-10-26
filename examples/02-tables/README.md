# 02 — Tables

Extract a ruled table into a DataFrame: build a synthetic table PDF
with PyMuPDF (ruled lines + cell text), then read it back with
pdfplumber's line-based table detection and convert it to a pandas
DataFrame. All values are synthetic.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare
`python` (the hermes venv). The script writes `table.pdf` in this
directory, then re-opens it with pdfplumber.

## Expected output

```text
Tables: 1, Rows: 3, Value sum: 67
```

- Exactly 1 table detected (line strategy on both axes).
- Header row `Station | Value | Flag`, then rows S1/12/ok,
  S2/25/ok, S3/30/check.
- The DataFrame has shape (3, 3); the Value column sums to 67
  (12 + 25 + 30).

## Failure behavior

- `ModuleNotFoundError: pdfplumber` or `pymupdf` — you are not in
  the wave11 venv; use the full venv Python path above.
- 0 tables detected — the ruling lines were not drawn (check the
  `draw_line` calls) or the strategy was changed; line-based
  detection needs real ruling lines, not whitespace alignment.
- Cell text has stray whitespace — strip cell values after
  extraction (this script compares stripped values); do not adjust
  the table geometry to chase whitespace.

## Versions and evidence

- Tools: pdfplumber 0.11.10 + PyMuPDF 2.0 (fixture generator) in
  Node-1's wave11-venv (wave-11A, Wally spot-checked). pandas
  arrives in the same venv as a Streamlit dependency.
- Evidence level: design-only (gate 1 target). The table shape and
  value sum were derived during drafting; running them against the
  fleet venv is **to confirm at validation**.
