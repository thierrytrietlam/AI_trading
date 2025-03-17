import pandas as pd
import yfinance as yf
import time
from datetime import datetime, timezone, timedelta

# Define stock symbols and file path
symbols = ['AAPL', '9988.HK']
parquet_file = 'stocks.parquet'

# Initialize an empty DataFrame
dfs = pd.DataFrame()

# Loop to update every 2 minutes
while True:
    print(f"\n📥 Downloading data for {symbols} at {datetime.now()}")

    # Get the latest data for the past day
    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(days=1)

    # Fetch intraday stock data (1-hour interval)
    df = yf.download(symbols, start=start_time, end=end_time, interval="1h")

    # Skip if no new data is available
    if df.empty:
        print("⚠️ No new data available, waiting for the next interval.")
    else:
        # Flatten multi-index columns (if multiple symbols)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = ['_'.join(col).strip() for col in df.columns]

        # Convert wide format to long format
        df = df.stack(level=0).reset_index()

        # Rename columns for clarity
        df.columns = ['Datetime', 'symbol', 'Open', 'High', 'Low', 'Close', 'Volume']

        # Sort by Datetime and Symbol
        df = df.sort_values(['Datetime', 'symbol'])

        # Merge with existing data and remove duplicates
        dfs = pd.concat([dfs, df])
        dfs = dfs.drop_duplicates(subset=['Datetime', 'symbol'], keep='last')

        # Save the DataFrame to Parquet
        dfs.to_parquet(parquet_file, engine="pyarrow", index=False)
        print(f"✅ Data saved to {parquet_file} at {datetime.now()}.")

    # Wait for 2 minutes before the next update
    time.sleep(2 * 60)
