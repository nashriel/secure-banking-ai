import os

class Config:
    # Use DATABASE_URL from env (production), fallback to local dev DB
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://myuser:mypassword@localhost:5432/banking_system"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecurekey123")  # replace in prod
