### this is where we record data about the user and their unique identifier
from models import db
class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loginKey = db.Column(db.String(4), nullable=False, unique=True)
    
    def __repr__(self):
        return "<loginKey %s>" % self.loginKey