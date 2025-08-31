import pandas as pd
from google.cloud import bigquery
import os

os.environ["XXXXX"] = os.getenv("XXXXX")

df = pd.read_parquet("data/helsinki_weather_transformed.parquet")

# BigQuery project and table details
project_id = "etl-weather-data-csv-project"
dataset_id = "weather_data"
table_id = "helsinki_weather"

# table path
table_ref = f"{project_id}.{dataset_id}.{table_id}"

# initialize BigQuery client
client = bigquery.Client(project=project_id)

#define job configuration
job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE", #write_append, write_truncate, write_empty
    autodetect=True,                    # let BQ infer schema from df
)

#load dataframe into BigQuery
load_job = client.load_table_from_dataframe(
    df,
    table_ref,
    job_config=job_config
)

# wait for job to finish
load_job.result()

# verify the table was loaded
table = client.get_table(table_ref)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns into {table_ref}")


