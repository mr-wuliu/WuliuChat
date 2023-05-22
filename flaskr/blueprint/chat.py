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
@login_required
def home():
    return render_template('chat/home.html')

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
