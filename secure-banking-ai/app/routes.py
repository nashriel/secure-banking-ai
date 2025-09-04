from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from .models.models import db, Login, Transaction, Deposit, Withdrawal

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('welcome.html')




@main.route("/register")
def register():
    # Temporary shortcut until registration is built
    return redirect(url_for("main.dashboard"))  # ✅ fixed here

@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@main.route("/signup")
def signup():
    return render_template("Signup.html")

@main.route("/login")
def login():
    return render_template("Login.html")

