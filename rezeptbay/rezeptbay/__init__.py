from flask import Flask

from .extentions import mongo
from .main import main
from .extentions import login_manager

def create_app(config_object="rezeptbay.settings"):
	app = Flask(__name__)
	app.config.from_object(config_object)
	mongo.init_app(app)
	login_manager.init_app(app)

	app.register_blueprint(main)
	app.secret_key = "ece904dfb1a4431733e53f96f4c36aa8ea76529b1143a3bc"

	return app