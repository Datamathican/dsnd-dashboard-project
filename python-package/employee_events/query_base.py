import pandas as pd
from .sql_execution import QueryMixin

# Inherit from QueryMixin to access self.pandas_query
class QueryBase(QueryMixin):

    name = ""

    def names(self):
        return []

    def event_counts(self, id):
        # Corrected SQL columns: positive_events, negative_events, employee_events table
        query = f"""
            SELECT 
                event_date, 
                SUM(positive_events) AS positive_events, 
                SUM(negative_events) AS negative_events
            FROM {self.name}
            JOIN employee_events USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
            GROUP BY event_date
            ORDER BY event_date;
        """
        return self.pandas_query(query)

    def notes(self, id):
        # Corrected SQL columns for the notes table
        query = f"""
            SELECT 
                note_date, 
                note
            FROM notes
            WHERE {self.name}_id = {id}
            ORDER BY note_date;
        """
        return self.pandas_query(query)