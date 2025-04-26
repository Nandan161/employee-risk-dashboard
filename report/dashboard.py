import sys
import os
from fastapi import FastAPI  # <-- Add this import

# Add the python-package folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'python-package')))
# Add the 'report' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'report')))

from employee_events.query_base import QueryBase
from employee_events.employee import Employee
from employee_events.team import Team

# Import the load_model function from utils.py
from .utils import load_model

# Your existing component classes
from report.base_components import (
    Dropdown,
    BaseComponent,
    Radio,
    MatplotlibViz,
    DataTable
)
from report.combined_components import FormGroup, CombinedComponent

# Your existing class definitions for components like ReportDropdown, Header, LineChart, BarChart, etc.

# Initialize FastAPI app instance
app = FastAPI()

# Define the report generation function
def report(id, entity):
    try:
        print(f"Generating report for ID: {id}, Entity: {entity}")
        
        username = entity.username(id)
        model_df = entity.model_data(id)
        notes_df = entity.notes(id)
        events_df = entity.event_counts(id)

        print("Fetched data successfully")

        return {
            "username": username,
            "model_data": model_df.to_dict(),
            "notes": notes_df.to_dict(orient="records"),
            "events": events_df.to_dict(orient="records")
        }

    except Exception as e:
        print(f"Error in report(): {e}")
        return {"error": f"Something went wrong with the report generation: {e}"}

# Root route (For example, accessing http://127.0.0.1:8000/)
@app.get('/')
def root():
    return report(1, Employee())

# Route for employee by ID
@app.get('/employee/{id}')
def employee(id: str):
    return report(id, Employee())

# Route for team by ID
@app.get('/team/{id}')
def team(id: str):
    return report(id, Team())

# Update dropdown route
@app.get('/update_dropdown{r}')
def update_dropdown(r):
    dropdown = DashboardFilters.children[1]
    print('PARAM', r.query_params['profile_type'])
    if r.query_params['profile_type'] == 'Team':
        return dropdown(None, Team())
    elif r.query_params['profile_type'] == 'Employee':
        return dropdown(None, Employee())

# Update data route (POST request)
@app.post('/update_data')
async def update_data(r):
    from fasthtml.common import RedirectResponse
    data = await r.form()
    profile_type = data._dict['profile_type']
    id = data._dict['user-selection']
    if profile_type == 'Employee':
        return RedirectResponse(f"/employee/{id}", status_code=303)
    elif profile_type == 'Team':
        return RedirectResponse(f"/team/{id}", status_code=303)

# If you want to serve this app using Uvicorn, you can run it from the command line as shown:
# uvicorn dashboard:app --host 127.0.0.1 --port 8000 --reload
