# 03-crop-filter (pdfplumber) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Synthetic page ONLY. Fixture built with PyMuPDF; crop/filter with
# pdfplumber. Crop boxes are (x0, top, x1, bottom), top-based.
import pymupdf
import pdfplumber

doc = pymupdf.open()
page = doc.new_page(width=612, height=792)
page.insert_text((72, 60), "HEADER BAND TEXT", fontsize=16, fontname="helv")
page.insert_text((72, 150), "BODY LINE ONE", fontsize=11, fontname="helv")
page.insert_text((72, 180), "BODY LINE TWO", fontsize=11, fontname="helv")
page.draw_line((72, 100), (540, 100))
page.draw_rect(pymupdf.Rect(72, 200, 200, 240))
doc.save("crop.pdf")

with pdfplumber.open("crop.pdf") as pdf:
    p = pdf.pages[0]
    cropped = p.crop((0, 120, 612, 792))
    ctext = cropped.extract_text() or ""
    header_gone = "HEADER BAND TEXT" not in ctext
    body_ok = "BODY LINE ONE" in ctext and "BODY LINE TWO" in ctext
    lines = p.filter(lambda o: o["object_type"] == "line")
    big = p.filter(lambda o: o["object_type"] == "char" and o["size"] > 14)
    big_text = big.extract_text() or ""
    big_letters = [c for c in big.chars if c["text"].strip()]
    assert header_gone and body_ok, ctext
    assert len(lines.objects["line"]) == 1, lines.objects["line"]
    assert "HEADER" in big_text and "BODY" not in big_text, big_text
    assert len(big_letters) == 14, len(big_letters)
    print(f"Crop header gone: {header_gone}, Body intact: {body_ok}, "
          f"Lines: {len(lines.objects['line'])}, Big chars: {len(big_letters)}")
