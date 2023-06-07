from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask_login import login_required
from flaskr.extensions import socketio, db

bp = Blueprint('chat', __name__)

@socketio.on('send', namespace='/chat')
def chat(data):
    print(data)
    socketio.emit('get',data,namespace='/chat')

@socketio.on('test',namespace='/chat')
def test():
    socketio.send('message')
@socketio.on('get')
def get():
    socketio.emit('get')

# @bp.route('/')
# def home():
#     return render_template('chat/main.html')

@bp.route('/chat')
def chat():
    return render_template('chat/chat.html')
@bp.route('/channel', defaults={'page': 1})
@bp.route('/channel/<page>', methods=['GET'])
def channel(page):
    cards = []
    class card:
        img = ""
        href = ""
        title = ""
    title_list = ['游戏','公共','新闻','编程讨论','社区维护']
    if page == 1:
        for i in range(1,5):
            card_ = card()
            card_.img = 'img/channel/channel'+str(i) + '.jpg'
            card_.title = title_list[i-1]
            cards.append(card_)

    return render_template('chat/channel.html',
                           cards=cards)
@bp.route('/favorites')
@login_required
def favorites():
    return render_template('chat/favorites.html')

@bp.route('/message')
@login_required
def message():
    return render_template('chat/message.html')
@bp.route('/user')
@login_required
def user():
    return render_template('chat/user.html')

@bp.route('/settings')
@login_required
def settings():
    return render_template('chat/settings.html')
