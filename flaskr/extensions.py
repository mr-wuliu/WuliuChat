from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap5

db = SQLAlchemy()
socketio = SocketIO()
login_manager = LoginManager()
bootstrap = Bootstrap5()

@login_manager.user_loader
def load_user(id):
    from flaskr.models import User
    return User.query.get(int(id))

login_manager.login_view = 'auth.login'
