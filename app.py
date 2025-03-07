from flask import Flask, render_template, requests
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///maxi.db'

#initialise the database
db = SQLAlchemy(app)

#create the db model
class Pointers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, defualt = datetime.utcnow)

def __repr__(self):
    return '<Name %r>' % self.id
