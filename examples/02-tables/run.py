# 02-tables (pdfplumber) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Synthetic table ONLY. Fixture built with PyMuPDF (ruled lines +
# cell text); detection + DataFrame conversion with pdfplumber/pandas.
import pymupdf
import pdfplumber
import pandas as pd

COLS_X = [72, 228, 384, 540]
ROWS_Y = [100, 130, 160, 190, 220]
ROWS = [
    ["Station", "Value", "Flag"],
    ["S1", "12", "ok"],
    ["S2", "25", "ok"],
    ["S3", "30", "check"],
]

doc = pymupdf.open()
page = doc.new_page(width=612, height=792)
for x in COLS_X:
    page.draw_line((x, 100), (x, 220))
for y in ROWS_Y:
    page.draw_line((72, y), (540, y))
for r, row in enumerate(ROWS):
    for c, val in enumerate(row):
        page.insert_text((COLS_X[c] + 6, ROWS_Y[r] + 20), val, fontsize=11, fontname="helv")
doc.save("table.pdf")

with pdfplumber.open("table.pdf") as pdf:
    tables = pdf.pages[0].extract_tables(
        table_settings={"vertical_strategy": "lines", "horizontal_strategy": "lines"}
    )
assert len(tables) == 1, len(tables)
t = [[(cell or "").strip() for cell in row] for row in tables[0]]
assert t[0] == ["Station", "Value", "Flag"], t[0]
assert t[1][0] == "S1" and t[2][1] == "25" and t[3][2] == "check", t
df = pd.DataFrame(t[1:], columns=t[0])
assert df.shape == (3, 3), df.shape
assert df["Value"].astype(int).sum() == 67
print(f"Tables: {len(tables)}, Rows: {len(df)}, Value sum: {df['Value'].astype(int).sum()}")
