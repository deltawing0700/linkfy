from flask import Flask
from extensions import db
import os

#blueprints imports
from blueprints.main import main
from blueprints.api import api
from blueprints.auth import auth
#just to enable migrations

def create_app():
    app = Flask(__name__)

    #App configuration
    app.config.from_pyfile("config.cfg")
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://rklcrmjh:Llw7JwFCU58fZS9B9wX6zCfcRzieUPrC@rogue.db.elephantsql.com:5432/rklcrmjh"
    app.config["SECRET_KEY"] = "testestsadxxcv"

    #extension initialization
    db.init_app(app)
    # login_manager.init_app(app)


    #blueprint registration
    app.register_blueprint(main)
    app.register_blueprint(api)
    app.register_blueprint(auth)
    return app