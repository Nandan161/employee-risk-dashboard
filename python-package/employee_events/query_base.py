import sqlite3
import pandas as pd
from pathlib import Path

class QueryBase:
    # Set the class attribute `name` to an empty string
    name = ""

    # Define the path to the database
    db_path = Path(__file__).parent.parent / "employee_events.db"

    # Define a `names` method that receives no passed arguments
    def names(self):
        # Return an empty list by default
        return []

    # Define an `event_counts` method that receives an `id` argument
    def event_counts(self, id):
        # Query to group by event_date and sum positive and negative events
        query = f"""
            SELECT event_date,
                   SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events
                USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
            GROUP BY event_date
            ORDER BY event_date;
        """
        # Execute the query and return the result as a pandas dataframe
        return self.execute_query(query)

    # Define a `notes` method that receives an `id` argument
    def notes(self, id):
        # Query to return note_date and note from the notes table
        query = f"""
            SELECT note_date, note
            FROM notes
            JOIN {self.name}
                USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
        """
        # Execute the query and return the result as a pandas dataframe
        return self.execute_query(query)

    # Helper function to execute the query and return a pandas dataframe
    def execute_query(self, query):
        # Connect to the SQLite database
        conn = sqlite3.connect(self.db_path)
        
        # Use pandas to execute the query and return the results as a dataframe
        df = pd.read_sql_query(query, conn)
        
        # Close the connection to the database
        conn.close()
        
        return df
