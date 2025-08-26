from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('login.id'))
    amount = db.Column(db.Numeric(10, 2))
    transaction_type = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Deposit(db.Model):
    __tablename__ = 'deposit'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('login.id'))
    amount = db.Column(db.Numeric(10, 2))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Withdrawal(db.Model):
    __tablename__ = 'withdrawal'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('login.id'))
    amount = db.Column(db.Numeric(10, 2))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Majid2468#$@localhost:5432/Banking System'