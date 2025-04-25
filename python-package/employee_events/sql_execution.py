# sql_execution.py

from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
db_path = Path(__file__).parent / 'employee_events.db'


# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:
    
    # Define a method named `pandas_query`
    # that receives an SQL query as a string
    # and returns the query's result as a pandas dataframe
    def pandas_query(self, sql_query):
        # Connect to the SQLite database
        connection = connect(db_path)
        
        # Use pandas to execute the query and return as a DataFrame
        df = pd.read_sql_query(sql_query, connection)
        
        # Close the connection
        connection.close()
        
        return df

    # Define a method named `query`
    # that receives an SQL query as a string
    # and returns the query's result as a list of tuples.
    # (You will need to use an sqlite3 cursor)
    def query(self, sql_query):
        # Connect to the SQLite database
        connection = connect(db_path)
        
        # Create a cursor object to execute the query
        cursor = connection.cursor()
        
        # Execute the query and fetch the results
        result = cursor.execute(sql_query).fetchall()
        
        # Close the connection
        connection.close()
        
        return result


# Leave this code unchanged
def sql_runner(func):
    """
    Decorator that runs a standard SQL execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    
    return run_query
