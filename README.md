# pdfplumber Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **pdfplumber cookbook** — table and text extraction from PDFs. Installed in wave-11 (Node-1 wave11-venv, Wally spot-checked 2026-10-25). First pattern pass written below (design-only, gate 1 target). It is intended for Developers who pull tables and text out of PDFs into DataFrames. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public. First pattern pass written (design-only, gate 1 target — none runtime-validated on the fleet yet).

**What this repository is:** pdfplumber patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Developers who pull tables and text out of PDFs into DataFrames.

## Prerequisites

- pdfplumber 0.11.10 in Node-1's wave11-venv (`C:\geo-tools\wave11-venv`, Python 3.12.10) — invoke the venv Python by full path, never bare `python` (hermes venv)
- Fixtures are generated at runtime with PyMuPDF 2.0 (same venv); pdfplumber reads PDFs, it does not create them
- pandas arrives in the same venv as a Streamlit dependency (table-to-DataFrame conversions)

## Patterns

| # | Example | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 01 | [examples/01-text-extract](examples/01-text-extract) | Extracting text with word and line awareness | Written (design-only) |
| 02 | [examples/02-tables](examples/02-tables) | Extracting tables into DataFrames | Written (design-only) |
| 03 | [examples/03-crop-filter](examples/03-crop-filter) | Cropping pages and filtering objects | Written (design-only) |
| 04 | [examples/04-report-pipeline](examples/04-report-pipeline) | A reporting pipeline: PDF tables → DataFrame → analysis | Written (design-only) |

## Repository layout

```text
pdfplumber-cookbook/
├── examples/
│   ├── 01-text-extract/
│   ├── 02-tables/
│   ├── 03-crop-filter/
│   └── 04-report-pipeline/
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: all four table rows (design-only, gate 1 target)
- Validation pass: run each pattern against the fleet environment and promote to gate 3

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [pymupdf-cookbook](https://github.com/ZQM-Computing/pymupdf-cookbook) — PDF text, layout, and redaction from Python
- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
- [duckdb-spatial-cookbook](https://github.com/ZQM-Computing/duckdb-spatial-cookbook) — Analytical geospatial SQL with DuckDB Spatial
