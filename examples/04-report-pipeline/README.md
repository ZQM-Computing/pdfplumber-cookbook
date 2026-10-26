# 04 — Report pipeline

A reporting pipeline: extract tables from every page of a synthetic
two-page PDF, concatenate them into one DataFrame, and compute
count, sum, and mean. All values are synthetic station readings.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare
`python` (the hermes venv). The script writes `report.pdf` in this
directory, then re-opens it with pdfplumber.

## Expected output

```text
Pages: 2, Rows: 8, Value sum: 360, Mean: 45.0
```

- Page 1 table: values 10, 20, 30, 40. Page 2 table: values 50, 60,
  70, 80.
- Concatenated DataFrame: 8 rows, 3 columns (Station, Value, Flag).
- Sum 360, mean 45.0 — hand-computed, asserted by the script.

## Failure behavior

- `ModuleNotFoundError: pdfplumber` or `pymupdf` — you are not in
  the wave11 venv; use the full venv Python path above.
- Fewer than 2 tables — one page's ruling lines are missing; check
  that both pages draw the full rule grid (see the `draw_table`
  helper in `run.py`).
- Mean differs — a page's values were edited; restore the
  `PAGES` table in `run.py`, do not adjust the assertions.
- A `None` cell breaks the DataFrame — an empty cell extracts as
  `None`; this fixture has no empty cells. Strip and guard on
  `None` before converting if your own tables have gaps.

## Versions and evidence

- Tools: pdfplumber 0.11.10 + PyMuPDF 2.0 (fixture generator) in
  Node-1's wave11-venv (wave-11A, Wally spot-checked). pandas
  arrives in the same venv as a Streamlit dependency.
- Evidence level: design-only (gate 1 target). The row count, sum,
  and mean were derived during drafting; running them against the
  fleet venv is **to confirm at validation**.
