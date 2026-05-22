# FX Rate Terminal

> Live & historical exchange rates for 58 currencies — all in one sleek, self-contained HTML file.

![FX Rate Terminal](https://img.shields.io/badge/currencies-58-f0a000?style=flat-square)
![Zero dependencies](https://img.shields.io/badge/dependencies-zero-00d4c8?style=flat-square)
![Single file](https://img.shields.io/badge/delivery-single%20HTML%20file-00c97a?style=flat-square)
![OANDA API](https://img.shields.io/badge/data-OANDA%20Public%20API-f04060?style=flat-square)

---

## Features

- **Live ticker** — scrolling real-time rates for 16 major pairs across the top of the page
- **58 currencies** — from G10 majors to frontier-market currencies
- **Custom base currency** — USD, EUR, GBP, JPY, CHF, CAD, AUD, CNY, INR, SGD
- **Rate types** — Average Bid, Average Ask, or Mid Rate
- **Historical lookups** — pick any past date; data goes back years via OANDA
- **Currency selector** — searchable multi-select dropdown with presets (G10, BRICS+, Asia Pacific, Middle East, Africa, and more)
- **Favourites** — star currencies; they persist across sessions via localStorage
- **Sortable table** — click any column header to sort ascending/descending
- **Bid-ask spread** display in percentage terms
- **Excel Paste Mode** — paste a column directly from a spreadsheet; duplicate rows are preserved and each gets its own rate row. A "Unique currencies only" toggle collapses duplicates when needed.
- **Copy & export** — copy the rates column, copy the full table (tab-separated for Excel), or download as CSV
- **Zero dependencies** — no npm, no build step, no server. Open the file and go.

---

## Quick Start

```bash
# Clone
git clone https://github.com/your-username/fx-rate-terminal.git

# Open — that's it
open fx-rate-terminal.html
```

No server needed. Double-click the HTML file in Finder / Explorer and it works.

---

## Usage

### Standard lookup
1. Set **Date**, **Rate Type**, and **Base Currency** at the top
2. Choose currencies via presets (G10, BRICS+…) or the search dropdown
3. Click **⚡ Fetch Rates**

### Excel Paste Mode
1. Copy a column from Excel (including rows with repeated currencies)
2. Paste into the text area
3. Toggle **Unique currencies only** ON if you only want one row per currency; leave it OFF (default) to get a rate row for every pasted row
4. Click **⚡ Fetch Pasted Rates**
5. Use **📊 Rates Col** to copy just the rates column back into Excel

---

## Data Source

Rates come from the [OANDA public exchange-rates API](https://www.oanda.com).  
They are **indicative** and intended for reference only — not for trading or financial decisions.

> **CORS note:** If you host this on GitHub Pages (or any static host), the OANDA API may be blocked by CORS.  
> Running the file locally (double-clicking it) works without any issues.

---

## File Structure

~~~
fx-rate-terminal.html   ← entire app: HTML + CSS + JS in one file
README.md
~~~

---

## Browser Support

Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

---

## License

MIT — do whatever you like with it.
