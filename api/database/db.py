from psycopg2 import pool

import os
from dotenv import load_dotenv

load_dotenv()

db_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=100,
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)


def get_conn():
    return db_pool.getconn()


def put_conn(conn):
    db_pool.putconn(conn)
