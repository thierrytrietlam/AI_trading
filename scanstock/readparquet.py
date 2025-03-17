import pandas as pd
df = pd.read_parquet("stocks.parquet", engine="pyarrow")
print(df)
