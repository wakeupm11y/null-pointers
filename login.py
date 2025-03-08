from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import random
import string

login = Flask(__name__)
login.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logins.db'
login.config['SECRET_KEY'] = 'your_secret_key'  # Needed for flash messages
db = SQLAlchemy(login)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loginKey = db.Column(db.String(4), nullable=False, unique=True)
    
    def __repr__(self):
        return "<loginKey %s>" % self.loginKey

@login.route('/', methods=['GET', 'POST'])
def login_view():
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
    return render_template('login.html')

@login.route('/home')
def home():
    return "Welcome to the home page!"  # Placeholder for the home page

@login.route('/upload')
def upload():
    return "Upload page placeholder"  # Placeholder for the upload page

if __name__ == '__main__':
    with login.app_context():  # Create an application context
        db.create_all()  # Create the database tables
    login.run(debug=True)