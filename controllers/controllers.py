from models.models import *
from flask import Flask, request, render_template, redirect , flash
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy

app.secret_key = "afatyxuny" 

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form.get('username')
        psswrd = request.form.get('password')
        user = User.query.filter_by(username = uname , password = psswrd).first()
        if user:
            flash("Logged in successfully!", "success") 
            if user.id == 1:
                return redirect('/admin_dashboard')
            else:
                return redirect('/user_dashboard')
        else:
            flash("Invalid username or password!", "danger")
        return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        qualification = request.form.get('qualification')
        dob = request.form.get('dob')
        dob = datetime.strptime(dob, '%Y-%m-%d').date()
        new_user = User(username = username , password = password , full_name = full_name, qualification = qualification, dob = dob)
        db.session.add(new_user)
        db.session.commit()
    flash("Registration successful! Please log in.", "success")
    return redirect('/register')

@app.route('/admin_dashboard' , methods = ['GET' , 'POST'])
def admin_dashboard():
    return redirect('/admin_dashboard')

@app.route('/user_dashboard' , methods = ['GET' , 'POST'])
def user_dashboard():
    return redirect('/user_dashboard') 




