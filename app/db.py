import os
import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")

class Database:
    _connection = None

    @staticmethod
    def get_connection():
        if Database._connection is None:
            try:
                Database._connection = psycopg.connect(DATABASE_URL)
            except Exception as e:
                print("Error connecting to the database:", e)
                Database._connection = psycopg.connect(":memory:")
        return Database._connection
