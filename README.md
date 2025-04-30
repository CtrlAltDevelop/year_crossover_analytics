# Year Crossover Analytics

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Python-blue)

## Overview

**Year Crossover Analytics** is a desktop tool designed to analyze trade data from two MetaTrader 5 report files and identify trades that span across calendar years. It helps traders ensure that positions opened in one year and closed in another meet compliance or performance review criteria.

---

## Features

- 📊 Detect trades with mismatched open/close years
- 📅 Flag trades where close date occurs *before* January 1st of the new year
- 📁 Load two CSV-based MT5 reports and merge/analyze
- 🧠 Generate statistics (e.g. flagged trade count, total profit)
- ✅ Export problematic trades to CSV

---

## Quick Start

### 1. Setup Environment

```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
    python.exe -m pip install --upgrade pip
    pip install -r requirements
```

### 2. Launch the App
```bash
  python run.py
```

## Build to Executable (Windows)
To create a single `.exe` file:

1. Make sure `run.py`, `icon.ico`, and `VERSION` exist in your project root.

2. Build:
```bash
    python setup.py
```
| Output: `build/YearCrossoverAnalytics_v0.1.0.exe`


## Version

Current Version: **1.0.0**  
Build: **0**

Version information is embedded directly into the Windows executable using the `VERSION` file.

## License

This project is licensed under the [MIT License](LICENSE).

© 2025 Zarif Alpha Group. Permission is granted to use, copy, modify, and distribute this software under the terms of the MIT License.

## Maintainer

Developed and maintained by **Zarif - Alpha Group**  
📧 Contact: mohammadzarif@pm.me
🌐 Website: [CtrlAltDevelop](https://github.com/CtrlAltDevelop)
