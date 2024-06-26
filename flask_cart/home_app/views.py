import flask
from shop_app.models import Product
from project.settings import DATABASE
from flask_login import current_user

def render_home():
    
    if current_user.is_authenticated:
        is_admin = current_user.is_admin 
        user_name = current_user.login
        return flask.render_template("home.html", is_admin = is_admin, user_name = user_name, is_authenticated = current_user.is_authenticated)
    return flask.render_template("home.html")
    
