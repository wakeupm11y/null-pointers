import os
from models import db
from routes.auth import auth
from routes.upload import upload
from flask import Flask, render_template, request



app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24).hex() #key for flash


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maxi.db'

#initialise the database
db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(upload)

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)