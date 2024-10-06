from flask import Blueprint ,url_for, render_template, request, redirect 
from werkzeug.security import generate_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required
from . import db
auth = Blueprint('auth',__name__)


@auth.route('/login')

def login():
    return render_template('login.html')

@auth.route('/login',methods = ['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if not user or user.password != password:
        return redirect('auth.login')
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

"""
after login  login_post  function will redirect to the profile page
in login.html page we are submitting(posting) details. once that happen then redirection will happen
"""



@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    #print(email, name, password)
    user = User.query.filter_by(email=email).first()
    if user:
        return "User existed already"
    #new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    new_user = User(email=email, name=name, password=password)
    db.session.add(new_user)
    db.session.commit()    



    return redirect (url_for('auth.login'))
"""
    above is getting the info submit form code in the sign up.html file 
after sign up process we are redirecting the login page which has login.html
"""

@auth.route('/logout')

@login_required
def logout():
    logout_user()

    return redirect('main.index')