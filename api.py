import os
from flask import Flask 
from flask_restful import Api, reqparse, Resource 
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS, cross_origin

db_path = os.path.join(os.path.dirname(__file__), 'app.db')
db_uri = 'sqlite:///{}'.format(db_path)

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super secret'

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

#import routes and resources for user
from routes.user_routes import *
from resources.user_resources.user import *

#import routes and resources for tasks
from routes.task_routes import *
from resources.task_resources.task import *


if __name__ == '__main__':
	from config.db import db 
	db.init_app(app)
	app.run(host='localhost', port=5000)