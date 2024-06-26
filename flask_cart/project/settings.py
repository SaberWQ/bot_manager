import flask, flask_sqlalchemy, flask_migrate

project_cart = flask.Flask(
    import_name = "project",
    static_url_path = "/static/",
    static_folder = "static",
    template_folder = "templates"
)

project_cart.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(
    app = project_cart
)
migrate = flask_migrate.Migrate(app = project_cart, db = DATABASE)