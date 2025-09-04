from app import db
from datetime import datetime

class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
