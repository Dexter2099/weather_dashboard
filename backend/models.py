from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime)
