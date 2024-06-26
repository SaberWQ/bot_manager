import flask
from shop_app.models import Product
from flask_login import current_user

def render_cart():
    if flask.request.cookies:
        list_id_products = flask.request.cookies.get('products').split(' ')

        list_products = []
        list_same_id = []
    
        for id_product in list_id_products:
            count_products = list_id_products.count(id_product)
            if id_product not in list_same_id:
                list_products.append(Product.query.get(id_product))
                list_same_id.append(id_product)
                if list_products[-1].count >= count_products:
                    list_products[-1].count = count_products 

    if current_user.is_authenticated:
        is_admin = current_user.is_admin
        user_name = current_user.login
        return flask.render_template(template_name_or_list = "cart.html", products = list_products, is_admin = is_admin, user_name = user_name)
    return flask.render_template(template_name_or_list = "cart.html")