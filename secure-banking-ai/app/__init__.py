from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Single instance

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    app.secret_key = app.config['SECRET_KEY']

    # Initialize db with app
    db.init_app(app)

    # Import models here to avoid circular imports
    from .models import models

    # Register blueprint
    from .routes import main
    app.register_blueprint(main)

    # Create tables
    with app.app_context():
        db.create_all()

    return app
