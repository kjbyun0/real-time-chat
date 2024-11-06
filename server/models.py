from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rule = (
        '-messages.owner',
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String)

    messages = db.relationship('Message', back_populates='owner', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.id} {self.username}>'

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    serialize_rules = (
        '-owner.messages',
    )

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    owner = db.relationship('User', back_populates='messages')

    def __repr__(self):
        return f'<Message {self.id} {self.timestamp}>'
