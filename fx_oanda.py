import requests
from datetime import datetime, timedelta

url = "https://fxds-public-exchange-rates-api.oanda.com/cc-api/currencies"

today = datetime.now().strftime("%Y-%m-%d")
yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

currencies = {
    "AED": "UAE Dirham", "ARS": "Argentine Peso", "AUD": "Australian Dollar",
    "BDT": "Bangladeshi Taka", "BGN": "Bulgarian Lev", "BHD": "Bahraini Dinar",
    "BRL": "Brazilian Real", "CAD": "Canadian Dollar", "CHF": "Swiss Franc",
    "CLP": "Chilean Peso", "CNY": "Chinese Yuan", "COP": "Colombian Peso",
    "CZK": "Czech Koruna", "DKK": "Danish Krone", "DZD": "Algerian Dinar",
    "EGP": "Egyptian Pound", "EUR": "Euro", "GBP": "British Pound",
    "GEL": "Georgian Lari", "GHS": "Ghanaian Cedi", "HKD": "Hong Kong Dollar",
    "HRK": "Croatian Kuna", "HUF": "Hungarian Forint", "IDR": "Indonesian Rupiah",
    "ILS": "Israeli Shekel", "INR": "Indian Rupee", "ISK": "Icelandic Krona",
    "JOD": "Jordanian Dinar", "JPY": "Japanese Yen", "KES": "Kenyan Shilling",
    "KRW": "South Korean Won", "KWD": "Kuwaiti Dinar", "KZT": "Kazakhstani Tenge",
    "LKR": "Sri Lankan Rupee", "MAD": "Moroccan Dirham", "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit", "NGN": "Nigerian Naira", "NOK": "Norwegian Krone",
    "NZD": "New Zealand Dollar", "OMR": "Omani Rial", "PEN": "Peruvian Sol",
    "PHP": "Philippine Peso", "PKR": "Pakistani Rupee", "PLN": "Polish Zloty",
    "QAR": "Qatari Riyal", "RON": "Romanian Leu", "RUB": "Russian Ruble",
    "SAR": "Saudi Riyal", "SEK": "Swedish Krona", "SGD": "Singapore Dollar",
    "THB": "Thai Baht", "TRY": "Turkish Lira", "TWD": "Taiwan Dollar",
    "TZS": "Tanzanian Shilling", "UAH": "Ukrainian Hryvnia", "VND": "Vietnamese Dong",
    "ZAR": "South African Rand",
}

print("Testing EUR (same as your currency.py)...")
params = {
    "base": "USD",
    "quote": "EUR",
    "data_type": "general_currency_pair",
    "start_date": yesterday,
    "end_date": today,
}
res = requests.get(url, params=params)
print(f"Status: {res.status_code}")
print(res.json())
print()

if res.status_code != 200:
    print("EUR test failed! Aborting.")
    exit()

print("Fetching all currencies...")
print()

results = {}
codes = sorted(currencies.keys())

for i, code in enumerate(codes, 1):
    params = {
        "base": "USD",
        "quote": code,
        "data_type": "general_currency_pair",
        "start_date": yesterday,
        "end_date": today,
    }
    res = requests.get(url, params=params)
    try:
        data = res.json()
        if data.get("response") and len(data["response"]) > 0:
            entry = data["response"][-1]
            bid = float(entry["average_bid"])
            ask = float(entry["average_ask"])
            mid = (bid + ask) / 2
            results[code] = {"bid": bid, "ask": ask, "mid": mid, "date": entry.get("close_time", "")[:10]}
            print(f"  [{i:>2}/{len(codes)}] {code}  OK  bid={bid:.6f}  ask={ask:.6f}  mid={mid:.6f}")
        else:
            print(f"  [{i:>2}/{len(codes)}] {code}  EMPTY  {data}")
    except Exception as e:
        print(f"  [{i:>2}/{len(codes)}] {code}  ERROR  {e}  status={res.status_code}  body={res.text[:100]}")

print()
print("=" * 96)
print("  RESULTS")
print("=" * 96)
print(f"  {'#':>3}  {'Code':<5} {'Currency':<25} {'Avg Bid':>12} {'Avg Ask':>12} {'Mid Rate':>12} {'1 Unit=?USD':>14}")
print("  " + "-" * 88)

date_used = ""
for i, code in enumerate(codes, 1):
    name = currencies[code]
    if code in results:
        r = results[code]
        inv = 1.0 / r["mid"] if r["mid"] else 0
        if r.get("date") and not date_used:
            date_used = r["date"]
        print(f"  {i:>3}  {code:<5} {name:<25} {r['bid']:>12.6f} {r['ask']:>12.6f} {r['mid']:>12.6f} {inv:>14.6f}")
    else:
        print(f"  {i:>3}  {code:<5} {name:<25}  --- FAILED ---")

print("  " + "-" * 88)
print(f"  Source    : OANDA (fxds-public-exchange-rates-api.oanda.com)")
print(f"  Found     : {len(results)}/{len(codes)}")
print(f"  Failed    : {len(codes) - len(results)}/{len(codes)}")
if date_used:
    print(f"  Rate Date : {date_used}")
print()
