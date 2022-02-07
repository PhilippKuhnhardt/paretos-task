from asyncio.windows_events import NULL
import importlib
from flask import Flask, request, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from model_interface import ModelInterface
from user import User
from model_pointer import ModelPointer

app = Flask(__name__)
auth = HTTPBasicAuth()

# In a real application the user would be dynamically generated and stored in a db
users = [User("Philipp", generate_password_hash("password"), ["multiplicationModel", "sumModel"]), User("Éric", generate_password_hash("strong_password"), ["divisionModel"])]
model_pointers = [ModelPointer("multiplicationModel", "models.multiplication_model", "MultiplicationModel"), ModelPointer("sumModel", "models.sum_model", "SumModel"), ModelPointer("divisionModel", "models.division_model", "DivisionModel")]

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
    model_pointer = next((model_pointer for model_pointer in model_pointers if model_pointer.id == model_id and model_id in user.model_access), None)

    if(model_pointer is None):
        return abort(404)

    model_module = importlib.import_module(model_pointer.path)
    model: ModelInterface = getattr(model_module, model_pointer.name)()

    json = request.get_json() 
    if(model.set_parameters(json)):
        return str(model.calc())  
    else:
        return abort(400)

        