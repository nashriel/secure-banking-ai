from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models.models import db, Login, Transaction, Deposit, Withdrawal
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

# ---------------- Home Page ----------------
@main.route('/')
def index():
    return render_template('welcome.html')

#byashriel
# ---------------- Signup ----------------
@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        # Check if passwords match
        if password != confirm:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('main.signup'))

        # Check if username or email already exists
        existing_user = Login.query.filter(
            (Login.username == username) | (Login.email == email)
        ).first()
        if existing_user:
            flash('Username or email already taken. Choose another.', 'danger')
            return redirect(url_for('main.signup'))

        # Hash the password using pbkdf2:sha256
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        # Save to database
        new_user = Login(fullname=fullname, email=email, username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Auto-login after signup
        session['user_id'] = new_user.id
        session['username'] = new_user.username

        flash('Account created successfully! Welcome to your dashboard!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('Signup.html')


# ---------------- Login ----------------
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = Login.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            # Save user info in session
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('main.login'))

    return render_template('Login.html')


# ---------------- Dashboard ----------------
@main.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first.', 'warning')
        return redirect(url_for('main.login'))

    user_id = session['user_id']
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    deposits = Deposit.query.filter_by(user_id=user_id).all()
    withdrawals = Withdrawal.query.filter_by(user_id=user_id).all()

    return render_template(
        'dashboard.html',
        username=session['username'],
        transactions=transactions,
        deposits=deposits,
        withdrawals=withdrawals
    )


# ---------------- Logout ----------------
@main.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
