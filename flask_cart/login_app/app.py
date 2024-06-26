import flask

login = flask.Blueprint(
    name = 'login',
    import_name = 'login_app',
    template_folder = 'templates',
    static_folder= 'static',
    static_url_path= '/login/'
)