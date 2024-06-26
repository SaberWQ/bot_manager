import flask 
from shop_app.models import Product
from project.settings import DATABASE
import os
import flask_login

def render_admin():
    if flask.request.method == 'POST':
        try:
            if flask.request.form.get('del') == None:
                product = Product(
                    name = flask.request.form['name'],
                    description = flask.request.form['description'],
                    price = flask.request.form['price'],
                    count = flask.request.form['count'],
                    discount = flask.request.form['discount'],
                )   
                DATABASE.session.add(product)
                DATABASE.session.commit()

                image = flask.request.files['image']
                image.save(os.path.abspath(__file__ + f"/../../shop_app/static/images/{product.name}.png"))
            else:
                product_id = int(flask.request.form['del'])
                product_del = Product.query.get(product_id)
                os.remove(os.path.abspath(__file__ + f"/../../shop_app/static/images/{product_del.name}.png"))
                if Product.query.get(product_id) != None:
                    DATABASE.session.delete(product_del)
                    DATABASE.session.commit()
                    
        except Exception as e:
            print(e)
    if flask_login.current_user.is_authenticated:
        is_admin = flask_login.current_user.is_admin 
        user_name = flask_login.current_user.login
        return flask.render_template(template_name_or_list= 'admin.html', products = Product.query.all(), is_admin = is_admin, user_name = user_name)
    else:
        return flask.render_template(template_name_or_list= 'admin.html', products = Product.query.all())