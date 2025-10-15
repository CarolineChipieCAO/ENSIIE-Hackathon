import yfinance as yf

# Société Générale (GLE.PA), Tesla (TSLA), Bitcoin (BTC-USD)
tickers = ["GLE.PA", "TSLA", "BTC-USD"]

for t in tickers:
    prices = yf.download(t, period="7d", interval="1d")
    print(prices)