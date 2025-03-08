#### this is where we record details about the accident footage
from models import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from datetime import datetime, timezone
import json
    #create the db model
class Pointers(db.Model):
    primary_keys = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(500), nullable = False)
    description = db.Column(db.Text, nullable = True)
    verification_report = db.Column(db.Text, nullable=True)
    energy = db.Column(db.Float, nullable = True)
    impact_force = db.Column(db.Float, nullable = True)
    street_name = db.Column(db.String(255), nullable = True)
    coordinates = db.Column(db.String, nullable = True)
    migration_id = db.Column(JSON, nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f'<VideoUploaded {self.primary_keys}>'

    def serialize_coordinates(self, coords):
        self.coordinates = json.dump(coords)

    def deserialize_coordinates(coords):
        return json.loads(self.coordinates) if self.coordinates else []  
