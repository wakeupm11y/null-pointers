import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db
from routes.auth import auth
from routes.upload import upload

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24).hex() #key for flash


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maxi.db'

    #initialise the database

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(upload)


    #create the db model
class Pointers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.id
    
@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)