
# 💱 FX Rate Finder — OANDA Direct

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Fetches **exact mid-market FX exchange rates** from OANDA's public API for **58 currencies** against USD.

## ✨ Features

- **Exact OANDA rates** — same values as [oanda.com/currency-converter](https://www.oanda.com/currency-converter/)
- **58 currencies** supported
- **Mid-market rate**: `mid = (average_bid + average_ask) / 2`
- **No API key required** — uses OANDA's public endpoint
- **3 tools included**:
  - `fx_oanda.py` — CLI, prints all rates in terminal
  - `fx_server.py` — Flask web app with dark theme UI
  - `index.html` — Standalone HTML (needs Flask backend running)

## 🚀 Quick Start

### Install
```bash
pip install -r requirements.txt
