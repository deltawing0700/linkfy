from flask import Flask
from extensions import db
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

#extension initialization
db.init_app(app)

#db.create_all(app=app)


#blueprint registration
app.register_blueprint(main)
app.register_blueprint(api)
app.register_blueprint(auth)