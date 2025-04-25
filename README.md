
# Software Engineering for Data Scientists 

This repository contains starter code for the **Software Engineering for Data Scientists** final project. Please reference your course materials for documentation on this repository's structure and important files. Happy coding!

# Employee Retention Dashboard

A data-driven dashboard built with FastHTML to help managers monitor employee performance, identify at-risk talent, and take proactive steps to retain key employees. It integrates SQL-backed data pipelines, predictive modeling, and a modular Python backend.

## 🔍 Project Overview

This project solves a business need where top-performing employees are being recruited by competitors. Managers can now view:
- Performance trends
- Positive/negative events
- Machine learning predictions for employee attrition

## 📦 Features

- 📊 Dashboard showing employee/team performance and recruitment risk
- ⚙️ Python package with reusable SQL execution logic and query classes
- 🔁 Decorator/Mixin for clean and reusable database interaction
- 🧠 Integrated ML model (via pickle) for attrition prediction
- 🧪 Unit tests for SQLite schema validation
- ✅ GitHub Actions to ensure CI for all code updates

### Repository Structure
```
├── README.md
├── assets
│   ├── model.pkl
│   └── report.css
├── env
├── python-package
│   ├── employee_events
│   │   ├── __init__.py
│   │   ├── employee.py
│   │   ├── employee_events.db
│   │   ├── query_base.py
│   │   ├── sql_execution.py
│   │   └── team.py
│   ├── requirements.txt
│   ├── setup.py
├── report
│   ├── base_components
│   │   ├── __init__.py
│   │   ├── base_component.py
│   │   ├── data_table.py
│   │   ├── dropdown.py
│   │   ├── matplotlib_viz.py
│   │   └── radio.py
│   ├── combined_components
│   │   ├── __init__.py
│   │   ├── combined_component.py
│   │   └── form_group.py
│   ├── dashboard.py
│   └── utils.py
├── requirements.txt
├── start
├── tests
    └── test_employee_events.py
```

### employee_events.db

```mermaid
erDiagram

  employee {
    INTEGER employee_id PK
    TEXT first_name
    TEXT last_name
    INTEGER team_id
    
  }

  employee_events {
    TEXT event_date
    INTEGER employee_id FK
    INTEGER team_id FK
    INTEGER positive_events
    INTEGER negative_events
  }

  notes {
    INTEGER employee_id PK
    INTEGER team_id PK
    TEXT note
    TEXT note_date PK
  }

  team {
    INTEGER team_id PK
    TEXT team_name
    TEXT shift
    TEXT manager_name
  }

  team ||--o{ employee_events : "team_id"
  employee ||--o{ employee_events : "employee_id"
  notes }o--o{ employee_events : ""
```
