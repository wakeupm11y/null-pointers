from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

















































































app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maxi.db'


    #initialise the database
db = SQLAlchemy(app)

    #create the db model
class Pointers(db.Model):
    primary_keys = db.Column(db.Integer, primary_key = True)
    link = db.Column(db.String(500), nullable = False)
    description = db.Column(db.Text, nullable = True)
    verification_report = db.column(db.Text, nullable=True)
    energy = db.column()
    impact_force = db.column()
    street_name = db.column()
    coordinates = db.column()
    migration_id = db.column()

    def __repr__(self):
        return f'<Videoupload {self.primry_keys}>'


if __name__ == "__main__":
    with app.app_context():
        db.create_all()