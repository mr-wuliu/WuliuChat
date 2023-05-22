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
    news = ['1','2','3','4']
    rank_list = ['榜一大哥','榜二大哥','榜三大哥']
    hot_posts = ['热议','震惊','速速点击']
    check_in_status = False
    home_card = True
    chat_room = ['聊天室1','聊天室2','聊天室3','聊天室4']
    label = ['1','2','3','4']
    QA = ['如何学号前端','生活是什么','标签随机摆放']

    note = ['生活小贴士','js的100个技巧','工具网站']
    return render_template('chat/main.html',
                           news=news,
                           ranklist=rank_list,
                           hotposts=hot_posts,
                           home_card=home_card,
                           checkstatus=check_in_status)