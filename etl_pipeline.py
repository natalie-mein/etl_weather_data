from extract_weather import main as extract
from transform_weather import main as transform
from load_to_bigquery import main as load

if __name__ == "__main__":
    extract()
    transform()
    load()

import logging

logging.basicConfig(level=logging.INFO)

def run_pipeline():
    logging.info("Starting extraction...")
    extract()
    logging.info("Extraction complete.")

    logging.info("Starting transformation...")
    transform()
    logging.info("Transformation complete.")

    logging.info("Starting load...")
    load()
    logging.info("Load complete.")

if __name__ == "__main__":
    run_pipeline()
