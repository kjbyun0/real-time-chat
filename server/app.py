from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, User, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACT_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

CORS(app)

@app.route('/')
def index():
    return '<h1>Root Path</h1>'

class Messages(Resource):
    def get(self):
        messages = [message.to_dict() for message in Message.query.all()]
        return make_response(jsonify(messages), 200)
    
    def post(self):
        req = request.get_json()
        try:
            new_msg = Message(
                body = req.get('body'),
                user_id = req.get('user_id')
            )
            db.session.add(new_msg)
            db.session.commit()
        except Exception as exc:
            return make_response({
                'message': f'{exc}'
            }, 400)

        return make_response(jsonify(new_msg.to_dict()), 201)
    

api.add_resource(Messages, '/messages')


if __name__ == "__main__":
    app.run(port=5555, debug=True)