from dataclasses import dataclass
from datetime import time
import uuid

from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT

app = Flask(__name__)
api = Api(app)
jwt = JWT(app)

questions = []

@dataclass()
class Question(Resource):
    id: int
    uuid: uuid.uuid1()
    question: str
    created_at: time
    created_by: str
    update_at: time
    update_by: str
    is_active: bool


# 1. As a user I can get list of question with pagination
def get(self, id):
    pass


# 2. As a user I can create new question
def post(self, id):
    pass

# 3. As a user I can update existing question
def put(self, id):
    pass

# 4. As a user I can delete question
def delete(self, id):
    pass

# 5. As a user I can get detail question with uuid
def get(self, id, uuid):
    pass