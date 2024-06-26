import flask

registration = flask.Blueprint(
    name = "registration",
    import_name = "registration_app",
    template_folder = "templates"
)