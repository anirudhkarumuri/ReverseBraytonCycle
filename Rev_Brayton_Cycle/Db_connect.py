import sqlite3
import pandas as pd
from sqlite3 import Connection

class DatabaseConnection:
    _instance = None
    """
    Implementing singleton pattern
    """
    def __new__(cls, db_file):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db_file = db_file
        return cls._instance

    def __enter__(self) -> Connection:
        # Create a new connection when the context starts
        self._connection = sqlite3.connect(self.db_file)
        return self._connection


    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the connection when the context ends
        if self._connection:
            self._connection.close()
            self._connection = None  # Clear the connection instance


