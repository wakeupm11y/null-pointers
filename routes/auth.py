from flask import Flask,Blueprint, render_template, url_for, request, redirect, flash
import random
from models.user import Login 
from models import db
import string

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'login' in request.form:
            anon_id = request.form['anon_id']
            user = Login.query.filter_by(loginKey=anon_id).first()
            if user:
                flash('Login successful!', 'success')
                return redirect(url_for('home'))  # Redirect to home page after login
            else:
                flash('Invalid ID. Please try again.', 'danger')
        elif 'generateID' in request.form:
            characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
            new_id = ''.join(random.choices(characters, k=4))
            while Login.query.filter_by(loginKey=new_id).first():
                new_id = ''.join(random.choices(characters, k=4))
            new_user = Login(loginKey=new_id)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Your new ID is: {new_id}', 'success')
    return render_template("login.html")
