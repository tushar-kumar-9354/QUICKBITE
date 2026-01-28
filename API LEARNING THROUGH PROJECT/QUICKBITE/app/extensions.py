from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()  # Use capital M for class, lowercase for variable

print("EXTENSIONS: DB, CORS & Migrate initialized")