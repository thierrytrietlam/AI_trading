import pandas as pd
import yfinance as yf
import time
from datetime import datetime, timedelta

# Define cryptocurrency symbol and file path
crypto = 'NVDA'
file_path = 'NVDA_true.csv'

# Initialize an empty DataFrame
dfs = pd.DataFrame()

# Loop to update every 2 minutes
while True:
    print(f"Downloading data for {crypto} at {datetime.now()}")

    # Get the latest data for the past 2 minutes
    end_time = datetime.now()
    start_time = end_time - timedelta(days=5)

    # Download the data with 1-minute intervals
    df = yf.download(crypto,start="2024-06-01", end="2024-06-30", interval="1d",auto_adjust=True)
    # df = yf.download(crypto, start=start_time, end=end_time, interval='1m')

    # If data is empty, continue the loop
    if df.empty:
        print("No new data available, waiting for the next interval.")
    else:
        # Add cryptocurrency symbol column
        df['symbol'] = crypto

        # Concatenate the new data to existing DataFrame
        dfs = pd.concat([dfs, df])

        # Drop duplicate rows based on timestamp
        dfs = dfs[~dfs.index.duplicated(keep='last')]

        # Save the combined DataFrame to CSV (overwriting each time)
        dfs.to_csv(file_path, index=True)
        print(f"Data saved to {file_path} at {datetime.now()}.")

    # Wait for 2 minutes before the next update
    time.sleep(1 * 60)
