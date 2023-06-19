from flask import Blueprint, redirect, render_template, request, flash, send_from_directory, jsonify
from flask_login import login_user, logout_user

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')
from App.models import Customer
from App.controllers import (
    login_customer,
    login_staff,
    create_customer,
    create_staff,
)


@auth_views.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@auth_views.route('/login', methods=['POST'])
def login_action():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    user = None
    if role == 'customer':
        user = login_customer(username, password)
    elif role == 'staff':
        user = login_staff(username, password)
    
    if user:
        return redirect('/')
    flash('Invalid username/password')
    return redirect('/login')


@auth_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@auth_views.route('/signup', methods=['POST'])
def signup_action():
    username = request.form.get('username')
    password = request.form.get('password')
    new_user = create_customer(username, password)
    if new_user:
        login_user(new_user)
        return redirect('/')
    flash('User already exists')
    return redirect('/signup')

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    logout_user()
    return redirect('/')