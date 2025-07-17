import requests
import pandas as pd
from datetime import date, timedelta
import os

# Helsinki coordinates
latitude = 60.1695
longitude = 24.9354
timezone = "Europe/Helsinki"

# Date range
start_year = 2010
end_year = 2024

# Open-Meteo historical API endpoint
url = "https://archive-api.open-meteo.com/v1/archive"

# Variables to request
daily_vars = "temperature_2m_max,temperature_2m_min,precipitation_sum"

# Store all years in one dataFrame
all_data = []

for year in range(start_year, end_year + 1):
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": daily_vars,
        "timezone": "Europe/Helsinki"
    }
    # print(params)
    response = requests.get(url, params=params)
    data = response.json()

    # Error check
    if "daily" not in data:
        print(f"Error for year {year}: {data}")
        continue
    
    df = pd.DataFrame(data["daily"])
    df["year"] = year
    all_data.append(df)

# Combine all years
weather_df = pd.concat(all_data, ignore_index=True)

# Save to CSV
os.makedirs("data", exist_ok=True)
weather_df.to_csv("data/helsinki_weather_2010_2024.csv", index=False)

print("Saved to helsini_weather_2010_2024.csv")
