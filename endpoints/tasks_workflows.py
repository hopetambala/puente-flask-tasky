from models.tasks_workflows import TasksWorkflowsModel
from flask_restful import Resource, reqparse


class TasksWorkflow(Resource):

    def get(self, task_workflow_id):
        task_workflows = TasksWorkflowsModel.find_by_id(task_workflow_id)
        print(task_workflows)
        if task_workflows:
            return {
                'task_workflow': [task_workflow.json() for task_workflow in task_workflows]
            }, 200
        else:
            return {'message': 'Task Workflow not found!'}, 404

class TasksWorkflows(Resource):

    def get(self):
        tasks = TasksWorkflowsModel.find_all_task_workflows()
        if tasks:
            return {'taskworkflows': [task.json() for task in tasks]}, 200
        else:
            return {'message': 'No tasks found!'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help='This field is mandatory!')                  
        parser.add_argument('description',
                            type=str,
                            required=True,
                            help='This field is mandatory!')

        data_payload = parser.parse_args()

        task_workflow = TasksWorkflowsModel.find_by_name(data_payload['name'])
        
        if task_workflow:
            return {'message': 'Task Workflow already in database!'}
        else:
            TasksWorkflowsModel.add_task_workflow(data_payload['name'],
                                data_payload['description'])
            return {'message': 'Task Workflow "{name}" successfully added to database!'
                        .format(name=data_payload['name'])}, 201

class TasksByWorkflow(Resource):

    def get(self, task_workflow_id):
        task_workflows = TasksWorkflowsModel.find_all_tasks_by_task_workflows_id(task_workflow_id)
        print(task_workflows)
        if task_workflows:
            return {
                'task_workflow': [task_workflow.json() for task_workflow in task_workflows]
            }, 200
        else:
            return {'message': 'Task Workflow not found!'}, 404