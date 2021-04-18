from app import create_app
from extensions import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import models, os

app = create_app()


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://rklcrmjh:Llw7JwFCU58fZS9B9wX6zCfcRzieUPrC@rogue.db.elephantsql.com:5432/rklcrmjh"
print(app.config["SQLALCHEMY_DATABASE_URI"])
db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()