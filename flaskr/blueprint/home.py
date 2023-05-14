from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask_login import login_required
from flaskr.extensions import socketio, db
from flaskr.forms import RegForm

bp = Blueprint('home',__name__)

@bp.route('/home', methods=['GET','POST'])
def home():
    username = False
    form = RegForm()
    if form.validate_on_submit():
        # 取出username欄位的輸入值
        username = form.username.data
        # 重設username欄位
        form.username.data = ''
    return render_template('common/B_base.html', form=form, username=username)
