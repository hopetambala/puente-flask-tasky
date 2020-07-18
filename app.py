from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api

from endpoints.tasks import Task, Tasks
from endpoints.tasks_workflows import TasksWorkflow, TasksWorkflows, TasksByWorkflow

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return: the rendered template 'home.html'
    """
    return "Puente's Task and Messages Management API"


api.add_resource(Task, "/tasks/<string:task_id>")
api.add_resource(Tasks, "/tasks")
api.add_resource(TasksWorkflow, "/taskworkflows/<string:task_id>")
api.add_resource(TasksWorkflows, "/taskworkflows")
api.add_resource(TasksByWorkflow, "/taskworkflows/tasks/<string:task_workflow_id>")

if __name__ == "__main__":
    app.run(debug=True)
