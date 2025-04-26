import pytest
from pathlib import Path
import sqlite3

# DO NOT redefine 'project_root' as a variable elsewhere

# Fixture to get project root
@pytest.fixture
def project_root_path():
    return Path(__file__).resolve().parent.parent

# Fixture to get path to the database file
from pathlib import Path
import pytest

@pytest.fixture
def db_path():
    project_root = Path(__file__).resolve().parent.parent  # go up to project root
    return project_root / 'python-package' / 'employee_events' / 'employee_events.db'

# Test if the database file exists
def test_db_exists(db_path):
    assert db_path.is_file(), f"{db_path} does not exist"

# Fixture to connect to the SQLite database
@pytest.fixture
def db_conn(db_path):
    return sqlite3.connect(db_path)

# Fixture to get all table names from the database
@pytest.fixture
def table_names(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [row[0] for row in cursor.fetchall()]

# Test for employee table
def test_employee_table_exists(table_names):
    assert 'employee' in table_names, "'employee' table does not exist"

# Test for team table
def test_team_table_exists(table_names):
    assert 'team' in table_names, "'team' table does not exist"

# Test for employee_events table
def test_employee_events_table_exists(table_names):
    assert 'employee_events' in table_names, "'employee_events' table does not exist"
