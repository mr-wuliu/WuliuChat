from flaskr.extensions import db
from flask_login import UserMixin, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, UserMixin):
    # 数据表明、字段
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(100))
    username = db.Column(db.String(50), unique=True)
    profile = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    like = db.Column(db.Integer, default=0)
    messages = db.relationship('Message', back_populates='author', cascade='all')
    posts = db.relationship("Post", backref="post")

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
    @property
    def gravatar(self):
        return self.profile

    @property
    def is_admin(self):
        return True


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='messages')

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    context = db.Column(db.Text)
    like = db.Column(db.Integer, default=0)

class Config(db.Model):
    __tablename__ = 'config'
    id = db.Column(db.Integer, primary_key=True)
    ConfigName = db.Column(db.String(50), nullable=False)
    ConfigValue = db.Column(db.Integer,nullable=False)


if __name__ == "__main__":
    db.create_all()
