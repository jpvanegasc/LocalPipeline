from environs import Env
from sqlalchemy import create_engine

env = Env()
env.read_env()

engine = create_engine(env.str("DATABASE_URL"))

TABLE = "bike_rides"

table_sql = f"""
CREATE TABLE IF NOT EXISTS {TABLE}(
    ride_id             varchar,
    rideable_type       varchar,
    started_at          timestamp,
    ended_at            timestamp,
    start_station_name  varchar,
    start_station_id    varchar,
    end_station_name    varchar,
    end_station_id      varchar,
    start_lat           float,
    start_lng           float,
    end_lat             float,
    end_lng             float,
    member_casual       varchar,
    weekday_started_at  smallint

);
"""


DATA_TYPES = {
    "ride_id": str,
    "rideable_type": str,
    "started_at": str,
    "ended_at": str,
    "start_station_name": str,
    "start_station_id": str,
    "end_station_name": str,
    "end_station_id": str,
    "start_lat": float,
    "start_lng": float,
    "end_lat": float,
    "end_lng": float,
    "member_casual": str,
}


def create_table(drop=False):
    if drop:
        engine.execute(f"DROP TABLE IF EXISTS {TABLE};")
    engine.execute(table_sql)


if __name__ == "__main__":
    create_table(drop=True)
