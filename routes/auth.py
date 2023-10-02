# import libraries
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Blueprint of authentication routes
auth_bp = Blueprint('auth_bp', __name__)

# Initialize Flask-Login
login_manager = LoginManager()

# Register route
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            
            # Check if the username and email are unique
            existing_user = User.query.filter_by(username=username).first()
            existing_email = User.query.filter_by(email=email).first()
            
            if existing_user:
                flash('Username already exists. Please choose a different username.', 'error')
            elif existing_email:
                flash('Email address already registered. Please use a different email.', 'error')
            else:
                # Create a new user
                hashed_password = generate_password_hash(password, method='sha256')
                new_user = User(username=username, email=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash('Account created successfully. You can now log in.', 'success')
                return redirect(url_for('login'))
        except:
            flash('Something went wrong')
            db.session.rollback()
        finally:
            db.session.close()
    
    return render_template('signup.html')

# Define the user_loader callback function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            
            # Check if the user exists
            user = User.query.filter_by(username=username).first()
            
            if user and check_password_hash(user.password, password):
                login_user(user, remember=True)  # Login the user
                flash('Logged in successfully.', 'success')
                return redirect(url_for('index'))
            else:
                flash('Login failed. Please check your username and password.', 'error')
        except:
            flash('Something went wrong. Please try again')
            db.session.rollback()
        finally:
            db.session.close()
    
    return render_template('login.html')

# logout route
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()  # Logout the user
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))