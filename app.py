from flask import Flask
from extensions import db, login_manager
import os

#blueprints imports
from blueprints.main import main
from blueprints.api import api
from blueprints.auth import auth
#just to enable migrations
import models



app = Flask(__name__)

#App configuration
app.config.from_pyfile("config.cfg")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SECRET_KEY"] = os.environ.get("APP_SECRET")

#extension initialization
db.init_app(app)
login_manager.init_app(app)

#db.create_all(app=app)


#blueprint registration
app.register_blueprint(main)
app.register_blueprint(api)
app.register_blueprint(auth)