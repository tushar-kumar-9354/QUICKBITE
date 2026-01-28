# reset_db.py
from app import create_app
from app.extensions import db
import os

app = create_app()

with app.app_context():
    # Delete old database
    if os.path.exists("instance/db.sqlite3"):
        os.remove("instance/db.sqlite3")
        print("Deleted old database")
    
    # Create all tables
    db.create_all()
    print("Database tables created!")