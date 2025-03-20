from datetime import datetime
from flask import request, render_template, redirect , flash
from flask import current_app as app
from models.models import *
from werkzeug.security import generate_password_hash, check_password_hash
from models.database import db

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        uname = request.form.get('username')
        psswrd = request.form.get('password')
        user = User.query.filter_by(username=uname).first()

        if user and check_password_hash(user.password, psswrd):
            flash("Logged in successfully!", "success") 

            if user.id == 1:
                return redirect('/admin_dashboard')
            
            else:
                return redirect('/user_dashboard')
        else:
            flash("Invalid username or password!", "danger")
            return render_template('login.html')

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
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(username = username , password = hashed_password , full_name = full_name, qualification = qualification, dob = dob)
        db.session.add(new_user)
        db.session.commit()
    flash("Registration successful! Please log in.", "success")
    return redirect('/login')

@app.route('/admin_dashboard' , methods = ['GET' , 'POST'])
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route('/user_dashboard' , methods = ['GET' , 'POST'])
def user_dashboard():
    return render_template("user_dashboard.html")


