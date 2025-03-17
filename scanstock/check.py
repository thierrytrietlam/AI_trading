import yfinance as yf

aapl= yf.Ticker("bak")
print(aapl)
aapl_historical = aapl.history(start="2025-03-11", end="2025-03-15", interval="15m")
# print(aapl)
print(aapl_historical)