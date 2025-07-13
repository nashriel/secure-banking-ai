from flask import Flask
from flask_wtf.csrf import CSRFProtect

# Initialize Flask app
app = Flask(__name__)

# Secret key for session & CSRF (generate a strong one in production)
app.secret_key = "supersecurekey123"  # Replace with `secrets.token_hex(16)` in prod

# CSRF Protection enabled
csrf = CSRFProtect(app)

# Import routes after app is created
from app import routes

