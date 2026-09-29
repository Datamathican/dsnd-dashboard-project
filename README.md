# Employee Events Performance Dashboard

This repository contains the completed final project for the **Software Engineering for Data Scientists** course. It provides an interactive web dashboard built with FastHTML, SQLite, and Matplotlib to track and visualize employee and team performance events, including machine learning predictions for recruitment risk.

## Dashboard Preview
<img width="1689" height="958" alt="Screenshot 2026-09-29 at 19 42 08" src="https://github.com/user-attachments/assets/f0c97084-8ae3-45f1-b82e-b20daa16b623" />



## Getting Started

To run this dashboard locally, clone the repository and set up your environment:

1. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt

   ```
2.**Install the custom data access package:**
  ```bash
   cd python-package
pip install -e .

```
**Usage**

Start the web server:
```bash
python3 report/dashboard.py

```

The app will run locally and provide a localhost URL in the terminal

**Run the unit tests:**
```bash
pytest

```

**Repository Structure**
```bash
├── README.md
├── assets
│   ├── model.pkl
│   └── report.css
├── env
├── python-package
│   ├── employee_events
│   │   ├── __init__.py
│   │   ├── employee.py
│   │   ├── employee_events.db
│   │   ├── query_base.py
│   │   ├── sql_execution.py
│   │   └── team.py
│   ├── requirements.txt
│   ├── setup.py
├── report
│   ├── base_components
│   │   ├── __init__.py
│   │   ├── base_component.py
│   │   ├── data_table.py
│   │   ├── dropdown.py
│   │   ├── matplotlib_viz.py
│   │   └── radio.py
│   ├── combined_components
│   │   ├── __init__.py
│   │   ├── combined_component.py
│   │   └── form_group.py
│   ├── dashboard.py
│   └── utils.py
├── requirements.txt
├── start
├── tests
    └── test_employee_events.py
```
  **Database Schema (employee_events.db)**
```bash
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
