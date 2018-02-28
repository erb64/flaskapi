from config.db import db
from api import api
from routes.task_routes import task_routes

from models.task_models.task import TaskModel 

parser = reqparse.RequestParser()
parser.add_argument(
    'title',
    type=str,
    required=True)
parser.add_argument(
    'author',
    type=str,
    requried=True)
parser.add_argument(
    'body',
    type=str,
    required=True)
parser.add_argument(
    'active',
    type=bool,
    required=True)

class CreateTask(Resource):
    def post(self):
        args = parser.parse_args()
        new_task = TaskModel(args)
        new_task.save_to_db()

        return {'message': 'Task added'}

class TaskResource(Resource):
    def get(self, id):
        task = TaskModel.find_by_id(id)

        if task:
            return {'task': task.json()}, 200
        return {'error': 'Task not found'}, 400

    def put(self, id):
        task = TaskModel.find_by_id(id)

        if task:
            args = parser.parse_args()
            task.title = args['title']
            task.body = args['body']
            task.active = args['active']
            task.save_to_db()

            return {'message' : 'Task updated'}, 200
        return {'error':'Task not found'}, 400

    def delete(self, id):
        task = TaskModel.find_by_id(id)

        if task:
            task.delete_from_db()
            return {'message' : 'Task deleted'}, 200
        return {'error':'Task not found'}, 400


class GetTasks(Resource):
    def get(self):
        tasks = TaskModel.find_by_author(author)

        if tasks:
            pass

api.add_resource(CreateTask, task_routes['create new task']['url'])
api.add_resource(TaskResource, task_routes['update task']['url'])
api.add_resource(GetTasks, task_routes['read all tasks']['url'])