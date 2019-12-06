from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import pymongo
from pymongo import MongoClient
import os
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = "c9197d0d4da6973d2ef559402929e501"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# add mongo url to flask config, so that flask_pymongo can use it to make connection

mongo = MongoClient("mongodb+srv://dodorus:dom195kun@cluster0-3vwwc.mongodb.net/rezeptbay?retryWrites=true&w=majority")
dbmongo = mongo["rezeptbay"]
collection = dbmongo["rezepte"]

from main import routes