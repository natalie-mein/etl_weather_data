import pandas as pd
from clean_weather_data import clean_weather_data

# load raw extracted data
df = pd.read_csv("data/helsinki_weather_2010_2024.csv")

# convert date column to datetime
df["time"] = pd.to_datetime(df["time"])

df = df.rename(columns={
    "time": "date",
    "temperature_2m_min": "temperature_min",
    "temperature_2m_max": "temperature_max",
    "precipitation_sum": "precipitation"
})

# datetime type
df["date"] = pd.to_datetime(df["date"])

# Sort by date just in case
df = df.sort_values("date")

# clean the data
df_clean = clean_weather_data(df)

# Save transformed data to parquet
df_clean.to_parquet("data/helsinki_weather_transformed.parquet", index=False)

print("Transformed and cleaned data saved.")
