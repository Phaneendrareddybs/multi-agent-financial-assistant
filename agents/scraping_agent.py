# agents/scraping_agent.py

def get_earnings_surprise(symbol):
    mock_data = {
        "TSM": {"actual": 1.45, "estimate": 1.39},
        "005930.KQ": {"actual": 0.82, "estimate": 0.84},  # Samsung
    }

    if symbol not in mock_data:
        return f"No earnings data available for {symbol}"

    actual = mock_data[symbol]["actual"]
    estimate = mock_data[symbol]["estimate"]
    surprise_pct = ((actual - estimate) / estimate) * 100

    summary = (
        f"{symbol} {'beat' if surprise_pct > 0 else 'missed'} estimates "
        f"by {abs(round(surprise_pct, 2))}% (Actual: {actual}, Estimate: {estimate})"
    )
    return summary
