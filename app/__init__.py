from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)

import os
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)

from app.users.views import users_blueprint
from app.home.views import home_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)

from models import User

login_manager.login_view = 'users.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id ==int(user_id)).first()
