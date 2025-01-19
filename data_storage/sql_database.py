import os
import sqlite3
from .base_database import DatabaseInterface

class SQLDatabase(DatabaseInterface):
    def __init__(self):
        self.connection = None

    def connect(self):
        db_path = os.getenv("SQL_DATABASE_URL", "sqlite.db")
        self.connection = sqlite3.connect(db_path)
        print(f"Connected to SQL database: {db_path}")

    def insert(self, data):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO my_table (col1, col2) VALUES (?, ?)", (data["col1"], data["col2"]))
        self.connection.commit()
        print("Data inserted into SQL database.")

    def query(self, query_params):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM my_table WHERE col1 = ?", (query_params["col1"],))
        results = cursor.fetchall()
        return results
