from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,current_app
)
from flask_login import login_required, current_user
from flaskr.extensions import socketio, db
from flaskr.forms import RegForm
from flaskr.models import Post, Config, User
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
    sql_cmd = """ 
    select * 
    from post
    """
    posts = Post.query.order_by(Post.timestamp.asc()).paginate(page=1, per_page=20, error_out=False)
    ret = db.session.query(Post.title, User.profile).filter(Post.author== User.id).paginate(page=1, per_page=20, error_out=False)
    post_list = posts.items
    activate_user = User.query.order_by(User.like).paginate(page=1,per_page=10,error_out=False)

    hot_posts = ['热议','震惊','速速点击']
    check_in_status = False
    home_card = True
    chat_room = ['聊天室1','聊天室2','聊天室3','聊天室4']
    label = ['1','2','3','4']
    QA = ['如何学号前端','生活是什么','标签随机摆放']

    note = ['生活小贴士','js的100个技巧','工具网站']
    return render_template('chat/main.html',
                           news=ret.items,
                           ranklist=activate_user,
                           hotposts=hot_posts,
                           home_card=home_card,
                           checkstatus=check_in_status)