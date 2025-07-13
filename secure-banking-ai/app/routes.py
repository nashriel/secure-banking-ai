from app import app
from flask import render_template, redirect, url_for

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/login")
def login():
    # Temporary shortcut until login form is built
    return redirect(url_for("dashboard"))

@app.route("/register")
def register():
    # Temporary shortcut until registration is built
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

