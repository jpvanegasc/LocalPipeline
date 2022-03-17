from sqlalchemy import create_engine
from environs import Env

env = Env()
env.read_env()

engine = create_engine(env.str("DATABASE_URL"))

TABLE = "bike_rides"

table_sql = f"""
CREATE TABLE IF NOT EXISTS {TABLE}(
    ride_id varchar,
    rideable_type varchar,
    started_at timestamp,
    ended_at timestamp,
    start_station_name varchar,
    start_station_id varchar,
    end_station_name varchar,
    end_station_id varchar,
    start_lat varchar,
    start_lng varchar,
    end_lat varchar,
    end_lng varchar,
    member_casual varchar
);
"""


def create_table(drop=False):
    if drop:
        engine.execute(f"DROP TABLE IF EXISTS {TABLE};")
    engine.execute(table_sql)


if __name__ == "__main__":
    create_table(drop=True)
