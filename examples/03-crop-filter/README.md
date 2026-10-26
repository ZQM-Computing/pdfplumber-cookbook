# 03 — Crop and filter

Crop a page to a zone and filter its objects: build a synthetic page
with a header band, two body lines, a rule, and a box — then crop
away the header and prove the body survives, filter to lines only,
and filter to large (heading-size) characters only.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare
`python` (the hermes venv). The script writes `crop.pdf` in this
directory, then re-opens it with pdfplumber.

## Expected output

```text
Crop header gone: True, Body intact: True, Lines: 1, Big chars: 14
```

- The cropped zone (top 120 to bottom) contains both body lines
  and none of the header text.
- Exactly 1 line object (the rule at y=100).
- Exactly 14 large characters: the letters of "HEADER BAND TEXT"
  (6 + 4 + 4), set at 16 pt while body text is 11 pt. Spaces are not
  characters in pdfplumber's `chars` list.

## Coordinate note

pdfplumber crop boxes are (x0, top, x1, bottom) in top-based
coordinates — the same top origin PyMuPDF uses for `insert_text`
here, so the header at y=60 falls above the crop top of 120 and the
body at y=150/180 falls inside. If your fixture uses a different
origin, convert before cropping; a flipped crop silently returns
the wrong zone.

## Failure behavior

- `ModuleNotFoundError: pdfplumber` or `pymupdf` — you are not in
  the wave11 venv; use the full venv Python path above.
- Header still present after cropping — the crop top is above the
  header baseline; raise it past the header (120 here) and re-check.
- Line count differs — the box drawn with `draw_rect` is a rect
  object, not a line; only the explicit `draw_line` rule counts as
  a line. Do not count rects as lines.

## Versions and evidence

- Tools: pdfplumber 0.11.10 + PyMuPDF 2.0 (fixture generator) in
  Node-1's wave11-venv (wave-11A, Wally spot-checked).
- Evidence level: design-only (gate 1 target). The crop/filter
  results were derived during drafting; running them against the
  fleet venv is **to confirm at validation**.
