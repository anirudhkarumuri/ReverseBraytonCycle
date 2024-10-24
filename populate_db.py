import os

import pandas as pd
import tabulate
import sqlite3
from tabulate import tabulate

# Using sqlite3 as no external sql servers are required, sqlite3 is embedded and comes with python package.

# Step 1: Read the CSV file into a DataFrame
csv_file_path = 'Air_properties.csv'
df = pd.read_csv(csv_file_path, delimiter=',', encoding='utf-8')

# Step 2: Connect to SQLite database (it will create the database if it doesn't exist)
db_file_path = os.path.join(os.getcwd(),"Rev_Brayton_Cycle",'thermodynamic_properties.db')
conn = sqlite3.connect(db_file_path)

table_name = 'properties'
df.to_sql(table_name, conn, if_exists='replace', index=False)
query = "SELECT * FROM " + table_name
df = pd.read_sql(query, conn)
print(tabulate(df, tablefmt="psql", headers="keys", showindex=False))
conn.close()
