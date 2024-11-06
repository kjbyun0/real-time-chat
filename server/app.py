from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACT_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


@app.route('/')
def index():
    return '<h1>Root Path</h1>'

class Messages(Resource):
    def get(self):
        messages = [message.to_dict() for message in Message.query.filter.all()]
        print(messages)
        return make_response(messages, 200)
    

api.add_resource(Messages, '/messages')


if __name__ == "__main__":
    app.run(port=5555, debug=True)