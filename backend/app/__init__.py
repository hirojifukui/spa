from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS

app = Flask(__name__)

db = MongoEngine()
db.init_app(app)

CORS(app)

from app import routes, models

