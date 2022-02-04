from asyncio.windows_events import NULL
from operator import truediv
from pickle import FALSE
from flask import Flask, request, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from user import User
from model import Model

app = Flask(__name__)
auth = HTTPBasicAuth()

# Model-Functions
def calc1(input):
    return input * 2

def calc2(input):
    return input * input

def calc3(input):
    return input ** 2

# In a real application the user would be dynamically generated and stored in a db
users = [User("Philipp", generate_password_hash("password"), ["model1", "model2"]), User("Éric", generate_password_hash("strong_password"), ["model3"])]
models = [Model("model1", calc1), Model("model2", calc2), Model("model3", calc3)]

@auth.verify_password
def verify_password(username, password):
    return next((user for user in users if user.name == username and check_password_hash(user.password_hash, password)), False)

@auth.get_user_roles
def get_user_roles(user: User):
    return user.model_access

@app.route('/')
@auth.login_required
def index():
    user: User = auth.current_user()
    return "Hello, {}. Models you have access to: {}!".format(user.name, ", ".join(str(x) for x in user.model_access))

@app.route('/models/<model_id>', methods = ['POST'])
@auth.login_required
def calc_model(model_id):
    user: User = auth.current_user()
    model = next((model for model in models if model.id == model_id and model_id in user.model_access), None)
    if(model is None):
        return abort(404)

    json = request.get_json() 
    result = model.calc(int(json['number']))
    return str(result)

    

        