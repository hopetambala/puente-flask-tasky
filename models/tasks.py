import sqlite3, sys

class TasksModel:

    def __init__(self, task_id, name, task_workflows_id):
        self.task_id = task_id
        self.name = name
        self.task_workflows_id = task_workflows_id

    @classmethod
    def find_by_name(cls, task):
        tasks = list()
        connection = sqlite3.connect('./db/tasky.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM tasks WHERE name=?;'
        result = cursor.execute(query, (task,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                tasks.append(TasksModel(row[0], row[1], row[2]))
            return tasks
        connection.close()

    @classmethod
    def find_by_id(cls, id):
        tasks = list()
        connection = sqlite3.connect('./db/tasky.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM tasks WHERE task_id=?;'
        result = cursor.execute(query, (id,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                tasks.append(TasksModel(row[0], row[1], row[2]))
            return tasks
        connection.close()

    @classmethod
    def find_all_tasks(cls):
        tasks = list()
        connection = sqlite3.connect('./db/tasky.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM tasks;'
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                tasks.append(TasksModel(row[0], row[1], row[2]))
            return tasks
        connection.close()

    @classmethod
    def add_task(self, name,task_workflows_id):
        connection = sqlite3.connect('./db/tasky.db')
        cursor = connection.cursor()
        query = 'INSERT INTO tasks VALUES(NULL, ?,?);'
        cursor.execute(query, (name,task_workflows_id,))
        connection.commit()
        connection.close()

    def json(self):
        return {
            'task_id': self.task_id,
            'name': self.name,
            'task_workflows_id': self.task_workflows_id,
        }