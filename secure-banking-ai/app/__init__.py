from flask import Flask
from flask_wtf.csrf import CSRFProtect
from .models.models import db

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
    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

