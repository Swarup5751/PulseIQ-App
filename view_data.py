import sqlite3
import pandas as pd

conn = sqlite3.connect('data/inventory.db')

tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables:\n", tables)

table_name = tables.iloc[0, 0]

df = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 10;", conn)
print("\nData:\n", df)

conn.close()