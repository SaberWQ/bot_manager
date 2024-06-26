import cart_app, home_app, shop_app, admin_app, login_app, registration_app 

from .settings import project_cart

home_app.home.add_url_rule(rule = '/', view_func = home_app.render_home, methods = ['GET', 'POST'])
project_cart.register_blueprint(blueprint = home_app.home)

shop_app.shop.add_url_rule(rule = '/shop/', view_func = shop_app.render_shop, methods = ['GET', 'POST'])
project_cart.register_blueprint(blueprint = shop_app.shop)

cart_app.cart.add_url_rule(rule = '/cart/', view_func = cart_app.render_cart, methods = ['GET', 'POST'])
project_cart.register_blueprint(blueprint = cart_app.cart)

admin_app.admin.add_url_rule(rule = '/admin/', view_func = admin_app.render_admin, methods = ['GET', 'POST'])
project_cart.register_blueprint(blueprint = admin_app.admin)

login_app.login.add_url_rule(rule = '/login/', view_func=login_app.render_login, methods = ['GET', 'POST'])
project_cart.register_blueprint(blueprint = login_app.login)

registration_app.registration.add_url_rule(rule = '/registration/', view_func = registration_app.render_registration, methods = ['GET', 'POST'])
project_cart.register_blueprint(blueprint = registration_app.registration)