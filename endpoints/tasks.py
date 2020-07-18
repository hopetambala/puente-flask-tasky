from models.tasks import TasksModel
from flask_restful import Resource, reqparse


class Task(Resource):

    def get(self, task_id):
        tasks = TasksModel.find_by_id(task_id)
        print(tasks)
        if tasks:
            return {
                'task': [task.json() for task in tasks]
            }, 200
        else:
            return {'message': 'Task not found!'}, 404   

class Tasks(Resource):

    def get(self):
        tasks = TasksModel.find_all_tasks()
        if tasks:
            return {'tasks': [task.json() for task in tasks]}, 200
        else:
            return {'message': 'No tasks found!'}, 404
    
    def post(self):
        # task = TasksModel.find_by_name(task_name)
        # if task:
        #     return {'message': 'Task already in database!'}
        # else:
        parser = reqparse.RequestParser()
        
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help='This field is mandatory!')                  
        
        parser.add_argument('task_workflows_id',
                            type=int,
                            required=True,
                            help='This field is mandatory!')

        data_payload = parser.parse_args()

        task = TasksModel.find_by_name(data_payload['name'])
        
        if task:
            return {'message': 'Task already in database!'}
            
        else:
            TasksModel.add_task(data_payload['name'],
                                data_payload['task_workflows_id'])
            return {'message': 'Task "{name}" successfully added to database!'
                        .format(name=data_payload['name'])}, 201
    
    
