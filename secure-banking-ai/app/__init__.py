from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "your-secret-key"
csrf = CSRFProtect(app)

from app import routes
