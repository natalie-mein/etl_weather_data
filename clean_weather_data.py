import pandas as pd

def clean_weather_data(df: pd.DataFrame) -> pd.DataFrame:
    # drop duplicates
    df = df.drop_duplicates()

    # fix data types
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["temperature_min"] = pd.to_numeric(df["temperature_min"], errors="coerce")
    df["temperature_max"] = pd.to_numeric(df["temperature_max"], errors="coerce")
    df["precipitation"] = pd.to_numeric(df["precipitation"], errors="coerce")

    # remove rows with missing data
    df = df.dropna(subset=["date", "temperature_min", "temperature_max"])

    # ensure temp_min isn't ever higher than temp_max
    df = df[df["temperature_min"] <= df["temperature_max"]]

    # precipitation cannot be negative
    df = df[df["precipitation"] >= 0]

    # reset index
    df = df.reset_index(drop=True)

    return df
