from flask_pymongo import PyMongo
from flask_login import LoginManager

mongo = PyMongo()
login_manager = LoginManager()

#other extentions flask login placed here, initialiced in _init_
