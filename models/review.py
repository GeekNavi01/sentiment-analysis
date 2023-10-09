# import libraries and modules
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    is_positive = db.Column(db.Boolean, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    
    # relationships with food and sanitary tables
    positive_food = db.relationship('PositiveFood', backref='review', lazy=True)
    negative_food = db.relationship('NegativeFood', backref='review', lazy=True)
    positive_sanitary = db.relationship('PositiveSanitary', backref='review', lazy=True)
    negative_sanitary = db.relationship('NegativeSanitary', backref='review', lazy=True)