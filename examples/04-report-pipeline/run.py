# 04-report-pipeline (pdfplumber) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Synthetic readings ONLY. Fixture built with PyMuPDF (ruled tables);
# extraction + analysis with pdfplumber/pandas.
import pymupdf
import pdfplumber
import pandas as pd

COLS_X = [72, 228, 384, 540]
PAGES = [
    [["Station", "Value", "Flag"],
     ["S1", "10", "ok"], ["S2", "20", "ok"],
     ["S3", "30", "ok"], ["S4", "40", "check"]],
    [["Station", "Value", "Flag"],
     ["S5", "50", "ok"], ["S6", "60", "ok"],
     ["S7", "70", "ok"], ["S8", "80", "check"]],
]


def draw_table(page, rows):
    rows_y = [100 + 30 * i for i in range(len(rows) + 1)]
    for x in COLS_X:
        page.draw_line((x, 100), (x, rows_y[-1]))
    for y in rows_y:
        page.draw_line((72, y), (540, y))
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            page.insert_text((COLS_X[c] + 6, rows_y[r] + 20), val, fontsize=11, fontname="helv")


doc = pymupdf.open()
for rows in PAGES:
    draw_table(doc.new_page(width=612, height=792), rows)
doc.save("report.pdf")

frames = []
with pdfplumber.open("report.pdf") as pdf:
    assert len(pdf.pages) == 2
    for p in pdf.pages:
        tables = p.extract_tables(
            table_settings={"vertical_strategy": "lines", "horizontal_strategy": "lines"}
        )
        assert len(tables) == 1, len(tables)
        t = [[(cell or "").strip() for cell in row] for row in tables[0]]
        frames.append(pd.DataFrame(t[1:], columns=t[0]))

df = pd.concat(frames, ignore_index=True)
total = df["Value"].astype(int).sum()
mean = df["Value"].astype(int).mean()
assert df.shape == (8, 3), df.shape
assert total == 360 and mean == 45.0, (total, mean)
print(f"Pages: 2, Rows: {len(df)}, Value sum: {total}, Mean: {mean}")
