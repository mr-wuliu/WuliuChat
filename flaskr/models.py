from flaskr.extensions import db
from flask_login import UserMixin, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model,UserMixin):
    #数据表明、字段
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(20))
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20), nullable=False)
    messages = db.relationship('Message',back_populates='author', cascade='all')
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password, password)
    @property
    def is_admin(self):
        return True


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='messages')