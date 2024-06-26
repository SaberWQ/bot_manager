import flask_login
from .settings import project_cart
from registration_app.models import User

project_cart.secret_key = 'key'

login_manager = flask_login.LoginManager(app= project_cart)

# login_manager.init_app(app= project_cart)

@login_manager.user_loader
def load_user(id):
    return User.query.get(ident= id)