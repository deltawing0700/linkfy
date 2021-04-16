import os

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient


db = SQLAlchemy()
login_manager = LoginManager()
oauth_client = WebApplicationClient( os.environ['GOOGLE_CLIENT_ID'])