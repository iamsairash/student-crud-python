import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "host": "localhost",
    "database": "student_db",
    "user": "postgres",
    "password": "Hellopsql",
    "port": 5432
}

def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def get_cursor(conn):
    return conn.cursor(cursor_factory = RealDictCursor)