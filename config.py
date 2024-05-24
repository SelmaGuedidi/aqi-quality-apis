import os

from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

DB_HOST = os.environ.get('RDS_HOST')
DB_USER = os.environ.get('RDS_USER')
DB_PASSWORD = os.environ.get('RDS_PASSWORD')
DB_NAME = os.environ.get('RDS_DB_NAME')


DB_PATH = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

#  IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = DB_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
CORS(app)
moment = Moment(app)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)



