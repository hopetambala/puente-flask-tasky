import sqlite3, sys


class TasksWorkflowsModel:
    def __init__(self, task_workflows_id, name, description):
        self.task_workflows_id = task_workflows_id
        self.name = name
        self.description = description

    @classmethod
    def find_by_name(cls, name):
        task_workflows = list()
        connection = sqlite3.connect("./db/tasky.db")
        cursor = connection.cursor()
        query = "SELECT * FROM task_workflows WHERE name=?;"
        result = cursor.execute(query, (name,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                task_workflows.append(TasksWorkflowsModel(row[0], row[1], row[2]))
            return task_workflows
        connection.close()

    @classmethod
    def find_by_id(cls, task_workflows_id):
        task_workflows = list()
        connection = sqlite3.connect("./db/tasky.db")
        cursor = connection.cursor()
        query = "SELECT * FROM task_workflows WHERE task_workflows_id=?;"
        result = cursor.execute(query, (task_workflows_id,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                task_workflows.append(TasksWorkflowsModel(row[0], row[1], row[2]))
            return task_workflows
        connection.close()

    @classmethod
    def find_all_task_workflows(cls):
        task_workflows = list()
        connection = sqlite3.connect("./db/tasky.db")
        cursor = connection.cursor()
        query = "SELECT * FROM task_workflows;"
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                task_workflows.append(TasksWorkflowsModel(row[0], row[1], row[2]))
            return task_workflows
        connection.close()

    @classmethod
    def find_all_tasks_by_task_workflows_id(cls, task_workflows_id):
        tasks_by_task_workflows_id = list()
        connection = sqlite3.connect("./db/tasky.db")
        cursor = connection.cursor()
        query = 'SELECT task_id, tasks.name as "Task Name", task_workflows.name as "Task Workflow Name", task_workflows.description as "Description" FROM tasks INNER JOIN task_workflows ON task_workflows.task_workflows_id = tasks.task_workflows_id WHERE task_workflows.task_workflows_id=?;'
        result = cursor.execute(query, (task_workflows_id,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                tasks_by_task_workflows_id.append(
                    TasksWorkflowsModel(row[0], row[1], row[2])
                )
            return tasks_by_task_workflows_id
        connection.close()

    @classmethod
    def add_task_workflow(self, name, description):
        connection = sqlite3.connect("./db/tasky.db")
        cursor = connection.cursor()
        query = "INSERT INTO task_workflows VALUES(NULL, ?, ?);"
        cursor.execute(query, (name, description))
        connection.commit()
        connection.close()

    def json(self):
        return {
            "task_workflows_id": self.task_workflows_id,
            "name": self.name,
            "description": self.description,
        }
