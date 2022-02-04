from pickle import FALSE
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from user import User

app = Flask(__name__)
auth = HTTPBasicAuth()

# In a real application the user would be dynamically generated and stored in a db
users = [User("Philipp", generate_password_hash("password"), [1, 2]), User("Éric", generate_password_hash("strong_password"), [3])]

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