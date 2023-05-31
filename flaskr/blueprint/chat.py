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

@bp.route('/')
def home():
    return render_template('chat/home.html')

@bp.route('/chat')
def chat():
    return render_template('chat/chat.html')

@bp.route('/channel')
def channel():
    cards = []
    class card:
        img = ""
        href = ""
    card1 = card()
    card1.img = "img/channel/channel1.jpg"
    card2 = card()
    card2.img = "img/channel/channel2.jpg"
    card3 = card()
    card3.img = "img/channel/channel3.jpg"
    card4 = card()
    card4.img = "img/channel/channel4.jpg"
    cards.append(card1)
    cards.append(card2)
    cards.append(card3)
    cards.append(card4)
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
