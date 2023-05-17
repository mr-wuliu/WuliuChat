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
    # return render_template('common/B_base.html', form=form, username=username)
    news = ['1','2','3','4']
    rank_list = ['榜一大哥','榜二大哥','榜三大哥']
    hot_posts = ['热议','震惊','速速点击']
    check_in_status = False
    return render_template('common/base.html',
                           news=news,
                           ranklist=rank_list,
                           hotposts=hot_posts,
                           checkstatus=check_in_status)