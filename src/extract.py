import logging
from io import BytesIO
from zipfile import ZipFile

import requests

logging.basicConfig(level=logging.INFO)

BUCKET = "https://s3.amazonaws.com/tripdata"


def extract(year, month):
    filename = f"{year}{month}-citibike-tripdata.csv"
    logging.info(f"Requesting file '{filename}'")
    r = requests.get(f"{BUCKET}/{filename}.zip")

    if r.ok:
        logging.info("Unzipping file")
        with ZipFile(BytesIO(r.content)) as zf:
            with open(f"../data/{filename}", mode="w+") as f:
                f.write(zf.read(filename).decode("utf-8") )
        logging.info("File saved in disk")
    else:
        logging.error("Unable to get file from url")


if __name__ == "__main__":
    import sys

    year = sys.argv[1]
    month = sys.argv[2]

    extract(year, month)
