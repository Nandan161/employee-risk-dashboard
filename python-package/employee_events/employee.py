from .query_base import QueryBase
from .sql_execution import QueryMixin  # Ensure QueryMixin is imported correctly

class Employee(QueryBase, QueryMixin):
    # Set the class attribute `name` to the string "employee"
    name = "employee"

    # Define a method called `names` that receives no arguments
    def names(self):
        sql_query = f"""
            SELECT first_name || ' ' || last_name AS full_name,
                   employee_id
            FROM {self.name}
        """
        return self.query(sql_query)

    # Define a method called `username` that receives an `id` argument
    def username(self, id):
        sql_query = f"""
            SELECT first_name || ' ' || last_name AS full_name
            FROM {self.name}
            WHERE employee_id = {id}
        """
        return self.query(sql_query)

    # Alter this method to return a pandas dataframe for the model training query
    def model_data(self, id):
        sql_query = f"""
            SELECT SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM employee_events
            WHERE employee_id = {id}
        """
        return self.pandas_query(sql_query)


if __name__ == "__main__":
    e = Employee()
    print("Employee names:")
    print(e.names())
    print("\nUsername for ID 1:")
    print(e.username(1))
    print("\nModel data for ID 1:")
    print(e.model_data(1))