import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def fetch_bitcoin_data():
    crypto = "GC=F"
    file_path = "/opt/airflow/dags/crypto_data.csv"  # Adjust path for Airflow

    print(f"Downloading data for {crypto} at {datetime.now()}")

    # Fetch data (adjust interval if needed)
    df = yf.download(crypto, period="1d", interval="1m")  # Use '5m' instead of '1m' for reliability

    # Save data to CSV
    if not df.empty:
        df.to_csv(file_path, index=True)
        print(f"✅ Data saved to {file_path} at {datetime.now()}")
    else:
        print("⚠️ No new data available.")

