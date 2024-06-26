import flask

cart = flask.Blueprint(
    name = "cart",
    import_name = "cart_app",
    template_folder = "templates"
)