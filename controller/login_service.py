from model.user_model import User
from database.database import db
from main import login_manager
from flask_login import login_user, logout_user

@login_manager.user_loader
def get_user(id):
    return User.query.get(id=id)

