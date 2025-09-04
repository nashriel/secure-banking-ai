from flask import Flask
from flask_wtf.csrf import CSRFProtect
from app.models.models import db
from config import Config  # load centralized config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Secret key for session & CSRF
    app.secret_key = app.config.get("SECRET_KEY", "supersecurekey123")

    csrf = CSRFProtect(app)

    # Import and register blueprint
    from app.routes import main
    app.register_blueprint(main, url_prefix="")  # ✅ no prefix, clean endpoints

    with app.app_context():
        db.create_all()

    return app
