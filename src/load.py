import logging

import pandas as pd

from base import DATA_TYPES, engine, TABLE

logging.basicConfig(level=logging.INFO)


def file_loaded(year, month):
    with engine.connect() as conn:
        res = conn.execute(
            f"""
            SELECT * FROM {TABLE} 
            WHERE 
                EXTRACT(MONTH FROM started_at) = {month} 
                AND EXTRACT(YEAR FROM started_at) = {year};
            """
        )

        return bool(len(res.all()))


def load(year, month):
    if file_loaded(year, month):
        logging.info("File already loaded, skipping")
        return

    filename = f"{year}{month}-citibike-tripdata.csv"
    dates = ["started_at", "ended_at"]
    try:
        df = pd.read_csv(
            f"data/{filename}", index_col=0, parse_dates=dates, dtype=DATA_TYPES
        )
        logging.info(f"Loaded '{filename}' into DF")
    except:
        logging.error(f"Failed to load '{filename}' into DF", exc_info=True)
        return

    # Add weekday
    df["weekday_started_at"] = df["started_at"].map(lambda x: x.weekday())

    connection = engine.connect()

    try:
        df = df.to_sql(TABLE, connection, if_exists="append")
    except Exception:
        logging.error("DF failed to load into postgres", exc_info=True)
    else:
        logging.info(f"File '{filename}' loaded in Postgres")
    finally:
        connection.close()


if __name__ == "__main__":
    import sys

    from base import create_table

    year = sys.argv[1]
    month = sys.argv[2]

    create_table()
    load(year, month)
