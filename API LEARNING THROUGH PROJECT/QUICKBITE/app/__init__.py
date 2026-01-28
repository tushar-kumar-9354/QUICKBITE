from flask import Flask
from .extensions import db, cors
from .errors import register_error_handlers
import os

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///db.sqlite3"
    )

    db.init_app(app)
    cors.init_app(app)

    print("EXTENSIONS: DB & CORS initialized")

    register_error_handlers(app)  # <-- PASS INSTANCE
    print("ERRORS: Registering error handlers")

    from .routes.orders import orders_bp
    from .routes.auth import auth_bp

    app.register_blueprint(orders_bp)
    app.register_blueprint(auth_bp)

    return app
