import requests
from datetime import datetime, timedelta

API_KEY = "MZRHT2PHI7BPM3Z1"

def fetch_stock_data(symbol):
    """Fetch daily time series data from Alpha Vantage."""
    url = (
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"
        f"&symbol={symbol}&apikey={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    
    if "Time Series (Daily)" not in data:
        return {"error": f"Data fetch failed for {symbol}", "details": data}

    time_series = data["Time Series (Daily)"]

    # Get the last 2 trading days
    dates = sorted(time_series.keys(), reverse=True)
    latest_date = dates[0]
    previous_date = dates[1]

    latest_close = float(time_series[latest_date]["4. close"])
    previous_close = float(time_series[previous_date]["4. close"])
    change_pct = ((latest_close - previous_close) / previous_close) * 100

    return {
        "symbol": symbol,
        "latest_close": latest_close,
        "previous_close": previous_close,
        "change_pct": round(change_pct, 2),
        "date": latest_date
    }

def get_market_snapshot():
    stocks = {
        "TSMC": "TSM",
        "Samsung": "005930.KQ"  # KQ = KOSDAQ (alternative: try .KS for KOSPI)
    }

    result = {}
    for name, symbol in stocks.items():
        stock_data = fetch_stock_data(symbol)
        result[name] = stock_data
    return result
