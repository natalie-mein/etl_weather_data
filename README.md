# Weather data ETL

## Purpose

The purpose of this project is to create a simple ETL pipeline featuring weather data in Helsinki from 2010-2024. With the final product, you could analyse changes in average temperature, precipitation and humidity in Helsinki from 2010 to 2024 using historical weather data.

## Current pipeline setup

Extract → raw data saved as CSV
Transform → rename, sort, format
Clean → fix data types, drop bad rows
Save → final output as parquet
Load to BigQuery (final)


Extraction (extract_weather_data.py)

Pulls historical weather data from Open-Meteo API.

Saves raw CSV locally.

Cleaning + Transformation (transform_weather_data.py + clean_weather_data.py)

Renames columns, fixes datatypes, drops invalid/missing rows.

Saves transformed data to Parquet.

Loading (load_to_bigquery.py)

Loads transformed Parquet into BigQuery.

Uses google-cloud-bigquery client with autodetect=True.
