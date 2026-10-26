# 01 — Text extract

Extract text with word and line awareness: build a synthetic PDF
with PyMuPDF (pdfplumber reads PDFs; it does not create them), then
read it back with pdfplumber as full text, as words with bounding
boxes, and as characters. All text is synthetic, not a real document.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare
`python` (the hermes venv). The script writes `fixture.pdf` in this
directory, then re-opens it with pdfplumber.

## Expected output

```text
Lines: 3, Words: 9, Chars: 52
```

- 3 non-empty text lines: title, two body lines.
- 9 words: title 3, body lines 3 + 3.
- 52 letters: title 19 ("SYNTHETIC" 9 + "WORD" 4 + "REPORT" 6),
  line 1 17 ("Alpha" 5 + "bravo" 5 + "charlie" 7), line 2 16
  ("Delta" 5 + "echo" 4 + "foxtrot" 7). Spaces are not characters
  in pdfplumber's `chars` list, so the script counts letters only.

## Failure behavior

- `ModuleNotFoundError: pdfplumber` or `pymupdf` — you are not in
  the wave11 venv; use the full venv Python path above. The fixture
  generator needs PyMuPDF; the extraction needs pdfplumber. Both
  live in the same venv.
- Word count differs — the fixture was edited; restore the three
  `insert_text` calls from `run.py`, do not adjust the assertions.
- Text lines merged into one — the fixture lines were placed too
  close together for pdfplumber's line grouping; keep the 20 pt line
  spacing from `run.py`.

## Versions and evidence

- Tools: pdfplumber 0.11.10 + PyMuPDF 2.0 (fixture generator) in
  Node-1's wave11-venv (wave-11A, Wally spot-checked).
- Evidence level: design-only (gate 1 target). Line/word/character
  counts were derived during drafting; running them against the
  fleet venv is **to confirm at validation**.
