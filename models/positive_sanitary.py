# import libraries and modules
from app import db

# PositiveSanitary model
class PositiveSanitary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False)