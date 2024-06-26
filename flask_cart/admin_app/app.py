import flask

admin = flask.Blueprint(
    name = "admin",
    import_name= 'admin_app',
    template_folder= 'templates',
    static_folder= 'static',
    static_url_path= '/admin/'

)