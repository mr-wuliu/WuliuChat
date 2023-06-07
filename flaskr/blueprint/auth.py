import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# from flaskr.extensions import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user
from flaskr.models import User
from flaskr.extensions import db
# from flaskr.db import get_db
# from flask_login import login_required, LoginManager
# 创建一个名为auth的 Blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')


# 用户注册视图, 该视图会返回用于填写的表单
"""
注册时, 对于输入的用户密码需要转换为哈希值用于存储
"""
@bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        profile = request.form['profile']

        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required'
        elif not profile:
            error = 'Profile is required'

        # db = None
        user = User.query.filter_by(username=username).first()
        if user is not None:
            flash('The account is already register')
            return render_template('auth/register.html', status='已注册')

        if error is None:
            user = User(username=username,
                        profile=profile)

            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('chat.home'))
        flash(error)
    return render_template('auth/register.html')


# 登錄視圖
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None
        user = User.query.filter_by(username=username).first()
        if user is None:
            error = 'Incorrect username'
        elif not user.verify_password(password):
            error = 'Incorrect password'
        if error is None:
            login_user(user)
            return redirect(url_for('home.home'))
        return render_template('auth/login.html',error=error)

    return render_template('auth/login.html')


# 註銷用戶
@bp.route('/logout')
# @login_required
def logout():
    # 清除會話
    logout_user()
    return redirect(url_for('auth.login'))
