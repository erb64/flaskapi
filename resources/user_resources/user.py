from flask_jwt import JWT, jwt_required 
from flask_restful import Resource, reqparse
from datetime import datetime

# import from main
from api import app
from config.db import db
from api import api
from routes.user_routes import user_routes

from models.user_models.user import UserModel

parser = reqparse.RequestParser()
parser.add_argument(
    'name',
    type=str,
    required = True)
parser.add_argument(
    'email',
    type=str,
    required = True)
parser.add_argument(
    'username',
    type=str,
    required = True)
parser.add_argument(
    'password',
    type=str,
    required = True)

class CreateUser(Resource):
    def post(self):
        args = parser.parse_args()
        new_user = UserModel(args)
        new_user.save_to_db()

        return {'message': 'User added'}

class UserResource(Resource):
    def get(self, username):
        user = UserModel.find_by_username(username)

        if user:
            return {'user': user.json()}, 200
        return {'error': 'User not found'}, 400

    def put(self, username):
        user = UserModel.find_by_username(username)

        if user:
            args = parser.parse_args()

            user.name = args['name']
            user.email = args['email']
            user.username = args['username']
            user.password = args['password']

            user.save_to_db()

            return {'message': 'User updated'}, 200
        return {'error': 'User not found'}, 400

    def delete(self, username):
        user = UserModel.find_by_username(username)

        if user:
            user.delete_from_db()
            return {'message':'User deleted from database'}, 200
        return {'error': 'User not found'}, 400


# append api endpoint for the 
api.add_resource(CreateUser, user_routes['create new user']['url'])
api.add_resource(UserResource, user_routes['update user info']['url'])


