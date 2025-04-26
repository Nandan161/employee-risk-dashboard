import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parent / "employee_events.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Drop tables if they exist (for clean re-run)
cursor.executescript("""
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS employee_events;
DROP TABLE IF EXISTS notes;
""")

# Create tables
cursor.executescript("""
CREATE TABLE team (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT,
    shift TEXT
);

CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES team(team_id)
);

CREATE TABLE employee_events (
    id INTEGER PRIMARY KEY,
    event_date TEXT,
    employee_id INTEGER,
    team_id INTEGER,
    positive_events INTEGER,
    negative_events INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
    FOREIGN KEY (team_id) REFERENCES team(team_id)
);

CREATE TABLE notes (
    id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    note TEXT,
    note_date TEXT,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);
""")

# Insert sample data
cursor.executescript("""
INSERT INTO team (team_id, team_name, shift) VALUES
(1, 'Alpha', 'Morning'),
(2, 'Beta', 'Evening');

INSERT INTO employee (employee_id, first_name, last_name, team_id) VALUES
(1, 'Alex', 'Martinez', 1),
(2, 'Brittany', 'Williams', 2);

INSERT INTO employee_events (id, event_date, employee_id, team_id, positive_events, negative_events) VALUES
(1, '2024-01-01', 1, 1, 5, 2),
(2, '2024-01-02', 1, 1, 3, 1),
(3, '2024-01-01', 2, 2, 4, 0);

INSERT INTO notes (id, employee_id, note, note_date) VALUES
(1, 1, 'Good performance', '2024-01-02'),
(2, 2, 'Needs improvement', '2024-01-03');
""")

conn.commit()
conn.close()

print(f"✅ Database initialized at {db_path}")
