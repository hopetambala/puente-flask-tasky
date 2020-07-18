import sqlite3
import csv
import sys

connection = sqlite3.connect("./db/tasky.db")
cursor = connection.cursor()
create_task_workflows_table = "{}{}{}".format(
    "CREATE TABLE IF NOT EXISTS",
    " task_workflows(task_workflows_id INTEGER PRIMARY KEY AUTOINCREMENT,",
    " name text NOT NULL, description text);",
)

cursor.execute(create_task_workflows_table)

create_tasks_table = "{}{}{}{}{}".format(
    "CREATE TABLE IF NOT EXISTS",
    " tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,",
    " name text NOT NULL,",
    " task_workflows_id INTEGER NOT NULL,",
    " FOREIGN KEY (task_workflows_id) REFERENCES task_workflows(task_workflows_id));",
)
cursor.execute(create_tasks_table)

with open("./db/tasks.csv", "rt") as f:
    rows = csv.reader(f)
    next(rows)  # Skip the header row.
    for row in rows:
        query = "INSERT OR REPLACE INTO tasks VALUES(?, ?, ?)"
        cursor.execute(query, row)

with open("./db/tasks_list.csv", "rt") as f:
    rows = csv.reader(f)
    next(rows)  # Skip the header row.
    for row in rows:
        query = "INSERT OR REPLACE INTO task_workflows VALUES(?, ?, ?)"
        cursor.execute(query, row)

connection.commit()
connection.close()

print("Database successfully created and populated with data!")
