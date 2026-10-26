# 01-text-extract (pdfplumber) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Synthetic document ONLY. Fixture built with PyMuPDF (pdfplumber
# reads PDFs; it does not create them); extraction with pdfplumber.
import pymupdf
import pdfplumber

doc = pymupdf.open()
page = doc.new_page(width=612, height=792)
page.insert_text((72, 72), "SYNTHETIC WORD REPORT", fontsize=14, fontname="helv")
page.insert_text((72, 110), "Alpha bravo charlie", fontsize=11, fontname="helv")
page.insert_text((72, 130), "Delta echo foxtrot", fontsize=11, fontname="helv")
doc.save("fixture.pdf")

with pdfplumber.open("fixture.pdf") as pdf:
    p = pdf.pages[0]
    text = p.extract_text()
    words = p.extract_words()
    chars = p.chars

lines = [line for line in text.splitlines() if line.strip()]
assert len(lines) == 3, lines
assert len(words) == 9, [w["text"] for w in words]
assert {w["text"] for w in words} == {
    "SYNTHETIC", "WORD", "REPORT",
    "Alpha", "bravo", "charlie",
    "Delta", "echo", "foxtrot",
}
# Characters: letters only (spaces are not chars in pdfplumber's list).
# Title 19 + line 1 17 + line 2 16 = 52.
letters = [c for c in chars if c["text"].strip()]
assert len(letters) == 52, len(letters)
print(f"Lines: {len(lines)}, Words: {len(words)}, Chars: {len(letters)}")
