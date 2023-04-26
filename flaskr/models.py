from flaskr.extensions import db
from flask_login import UserMixin, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
# from flask_login import UserMixin
# class EntityBase(object):
#     def to_json(self):
#         fields = self.__dict__
#         if "_sa_instance_state" in fields:
#             del fields["_sa_instance_state"]
#         return fields

# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.INTEGER,primary_key=True)
#     username = db.Column(db.String(80),unique=True)
#     password = db.Column(db.String(80),nullable=False)


class User(db.Model,UserMixin): #, EntityBase):
    #数据表明、字段
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(20))
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20), nullable=False)
    messages = db.relationship('Message',back_populates='author', cascade='all')
    # head = db.Column(db.String(100))
    # nickName = db.Column(db.String(100))
    # status = db.Column(db.Date)
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