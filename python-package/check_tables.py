import sqlite3

# Path to your SQLite database
db_path = 'C:\\Users\\Nandan\\Github\\Data Science-Nanodegree\\employee-risk-dashboard\\python-package\\employee_events.db'

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

# Check if the tables you need exist
required_tables = ['employee', 'employee_events', 'team']
for table in required_tables:
    if table in [t[0] for t in tables]:
        print(f"Table {table} exists.")
    else:
        print(f"Table {table} does not exist.")

# Close the connection
conn.close()
