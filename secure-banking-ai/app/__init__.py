from flask import Flask
from flask_wtf.csrf import CSRFProtect
from .models.models import db
from app import create_app

app = create_app()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Majid2468#$@localhost:5432/Banking System'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Secret key for session & CSRF (generate a strong one in production)
    app.secret_key = "supersecurekey123"  # Replace with `secrets.token_hex(16)` in prod

    # CSRF Protection enabled
    csrf = CSRFProtect(app)

    # Import routes after app is created
    from app import routes

    return app

with app.app_context():
    # Create the database tables if they don't exist
    db.create_all()

    # Start the Flask shell
    from flask import shell
    shell()

