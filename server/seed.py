
from app import app
from models import db, User, Message

if __name__ == '__main__':
    with app.app_context():
        User.query.delete()
        Message.query.delete()
        db.session.commit()

        users = []
        for i in range(10):
            users.append(User(
                username = f'user{i}',
                name = f'name{i}'
            ))
        db.session.add_all(users)
        
        messages = []
        for i in range(30):
            messages.append(Message(
                body = f'sentense - {i}',
                owner = users[i % 10]
            ))
        db.session.add_all(messages)

        db.session.commit()
        