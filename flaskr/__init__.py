import os

from flask import Flask
# from flaskr.db import get_db
# from flaskr import config
from flaskr.extensions import db, login_manager, socketio
from flaskr.blueprint import auth, chat


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)#, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    # )
    #
    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)
    #
    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass
    """
    註冊服務
    """
    # 加載SQLite數據庫
    # from flaskr.extensions import db
    # db.init_app(app)
    # from . import db
    # db.init_app(app)
    # # MySQL数据库
    # from flaskr.extensions import db
    # db.init_app(app)
    # db.create_all()
    # from extensions import db
    # 加載flask_login
    # from flaskr.extensions import login_manager
    # login_manager.init_app(app)
    register_extensions(app)
    register_blueprint(app)
    """
    加載藍圖
    """
    # 認證
    # from flaskr.blueprint import auth
    # app.register_blueprint(auth.bp)
    # # 聊天
    # from flaskr.blueprint import chat
    # app.register_blueprint(chat.bp)
    # app.add_url_rule('/', endpoint='home')


    return app


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

def register_blueprint(app):
    app.register_blueprint(auth.bp)
    app.register_blueprint(chat.bp)
    app.add_url_rule('/', endpoint='home')