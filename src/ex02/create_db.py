import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv


def create_db():

    load_dotenv()
    USET_DB = os.getenv("USET_DB")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST_DB")
    PORT = os.getenv("PORT")
    NEW_DATABASE = os.getenv("DATABASE")

    connection = psycopg2.connect(
        user=USET_DB, password=PASSWORD, host=HOST, port=PORT)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()
    sql_create_database = cursor.execute(f'create database {NEW_DATABASE}')
    cursor.close()
    connection.close()


if __name__ == '__main__':
    try:
        create_db()
    except Exception as e:
        print(f"Error: {e}")
