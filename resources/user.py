from flask_jwt import JWT, jwt_required
from datetime import datetime

# import from main
from api import app
from config.db import db
from api import api
from routes.routes import user_routes

from models.user_models.user import UserModel

class GetUser(Resource):
    def get(self, username):
        user = UserModel.find_by_username(username)

        if user:
            return {'user': user.json()}, 200
        return {'error': 'User not found'}, 401

# append api endpoint for the 
api.add_resource(GetUser, user_routes['read one user']['url'])

