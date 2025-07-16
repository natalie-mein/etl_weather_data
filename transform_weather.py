import pandas as pd
import json

# remember to check that the csv goes in a folder
with open("data/helsinki_weather_raw.json", "r") as f:
    raw = json.load(f)

# Extract fields
dates = raw["daily"]["time"]
temp_min = raw["daily"]["temperature_2m_min"]
temp_max = raw["daily"]["temperature_2m_max"]
precip = raw["daily"]["precipitation_sum"]

# DataFrame
df = pd.DataFrame({
    "date": dates,
    "temperature_min": temp_min,
    "temperature_max": temp_max,
    "precipitation": precip
})

# datetime type
df["date"] = pd.to_datetime(df["date"])

# Sort by date just in case
df = df.sort_values("date")

# Save transformed data
df.to_csv("data/helsinki_weather_transformed.csv", index=False)
print("Transformed data saved.")