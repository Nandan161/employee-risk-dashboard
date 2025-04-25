# team.py

# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies for SQL execution
from .sql_execution import sql_runner  # Use sql_runner now

# Create a subclass of QueryBase called `Team`
class Team(QueryBase):

    # Set the class attribute `name` to the string "team"
    name = "team"

    # Define a `names` method that receives no arguments
    # This method should return a list of tuples from an SQL execution
    @sql_runner
    def names(self):
        # Query 5: Get team name and team_id for all teams
        return f"""
            SELECT team_name, team_id
            FROM {self.name}
        """

    # Define a `username` method that receives an ID argument
    # This method should return a list of tuples from an SQL execution
    @sql_runner
    def username(self, id):
        # Query 6: Get team name for the team related to the given ID
        return f"""
            SELECT team_name
            FROM {self.name}
            WHERE team_id = {id}
        """

    # Below is a method with an SQL query
    # This SQL query generates the data needed for the machine learning model.
    # Alter this method to return a pandas dataframe
    def model_data(self, id):
        # Query: Get positive and negative events for the specified team
        query = f"""
            SELECT positive_events, negative_events 
            FROM (
                SELECT team_id
                     , SUM(positive_events) positive_events
                     , SUM(negative_events) negative_events
                FROM {self.name}
                JOIN employee_events
                    USING(team_id)
                WHERE {self.name}.{self.name}_id = {id}
                GROUP BY team_id
            )
        """
        return self.pandas_query(query)
