from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from .models.models import db, Login, Transaction, Deposit, Withdrawal

# If you want to use blueprints (recommended with app factory):
main = Blueprint('main', __name__)

# Example route
@main.route('/')
def index():
    return render_template('welcome.html')

@main.route("/login")
def login():
    return render_template("Login.html")


@main.route("/register")
def register():
    # Temporary shortcut until registration is built
    return redirect(url_for("dashboard"))

@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

