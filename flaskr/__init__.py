import os

from flask import Flask, render_template
from flaskr.extensions import db, login_manager, socketio, bootstrap
from flaskr.blueprint import auth, chat, home

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    """
    註冊服務
    """
    register_extensions(app)
    register_blueprint(app)
    with app.app_context():
        db.create_all()

    return app


def register_extensions(app: Flask):
    """
    加载扩展
    :param app:
    :return:
    """
    db.init_app(app)  # mysql数据库
    login_manager.init_app(app)  # 登录验证
    socketio.init_app(app)  # 连接会话
    bootstrap.init_app(app)


def register_blueprint(app: Flask):
    """
    加载蓝图
    :param app:
    :return:
    """
    app.register_blueprint(auth.bp)
    app.register_blueprint(chat.bp)
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='home')


def register_error_handlers(app: Flask):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('common/error.html')