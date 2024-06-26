import flask
from .models import Product
from flask_login import current_user

def render_shop():
    if current_user.is_authenticated:
        is_admin = current_user.is_admin
        user_name = current_user.login
        return flask.render_template(template_name_or_list= "shop.html", products = Product.query.all(), is_admin = is_admin, user_name = user_name)
    return flask.render_template(template_name_or_list= "shop.html", products = Product.query.all())