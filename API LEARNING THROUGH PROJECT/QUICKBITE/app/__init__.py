from flask import Flask
from .extensions import db, cors, migrate  # Correct import
from .errors import register_error_handlers
import os

def create_app():
    print("DEBUG: Creating Flask app")

    app = Flask(__name__)

    # ---------------- CONFIG ----------------
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///db.sqlite3"
    )

    # ---------------- EXTENSIONS ----------------
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)  # This should work now

    # ---------------- ERROR HANDLERS ----------------
    register_error_handlers(app)
    print("ERRORS: Registering error handlers")

    # ---------------- BLUEPRINTS ----------------
    from .routes.health import health_bp
    from .routes.orders import orders_bp
    from .routes.auth import auth_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(auth_bp)

    print("DEBUG: Blueprints registered")

    return app