import flask
import flask_login
from registration_app.models import User

def render_login():
    if flask.request.method == 'POST':
        users = User.query.all()
        for user in users:
            if user.login == flask.request.form['login'] and user.password == flask.request.form['password']:
                flask_login.login_user(user)
                
    is_admin = False

    if not flask_login.current_user.is_authenticated:
        return flask.render_template('login.html')
    else:
        is_admin = flask_login.current_user.is_admin
        return flask.redirect('/')