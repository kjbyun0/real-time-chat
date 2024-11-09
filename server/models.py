from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rule = (
        '-messages.user',
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String)

    messages = db.relationship('Message', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.id} {self.username}>'

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    serialize_rules = (
        '-user.messages',
    )

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='messages')

    def __repr__(self):
        return f'<Message {self.id} {self.timestamp}>'
