import logging

import pandas as pd

from base import engine, TABLE

logging.basicConfig(level=logging.INFO)


def unique_id(df: pd.DataFrame):
    """Ride ID must be unique"""
    unique = df["ride_id"].is_unique

    if unique:
        logging.info("Ride ID is unique")
        return
    else:
        logging.error("Ride ID is not unique")
        exit(1)


def main():
    connection = engine.connect()
    df = pd.read_sql(TABLE, connection)
    logging.info("Connected to DB")

    unique_id(df)


if __name__ == "__main__":
    main()
