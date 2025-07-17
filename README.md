# Weather data ETL

## Purpose

The purpose of this project is to analyse changes in average temperature, precipitation and humidity in Helsinki from 2010 to 2024 using historical weather data.

## Current piple setup

Extract → raw data saved as CSV
Transform → rename, sort, format
Clean → fix data types, drop bad rows
Save → final output as parquet
Load to BigQuery (final)
