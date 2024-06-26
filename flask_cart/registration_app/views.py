import flask, flask_login
from registration_app.models import User
from project.settings import DATABASE

def render_registration():
    is_registration = False
    if flask.request.method == 'POST':
        try:
            user = User(
                login = flask.request.form['login'],
                password = flask.request.form['password'],
                is_admin = False
            )
            DATABASE.session.add(user)
            DATABASE.session.commit()
            is_registration = True
        except Exception as e:
            print(e)  
            is_registration = False
    return flask.render_template(template_name_or_list= "registration.html", is_registration = is_registration)