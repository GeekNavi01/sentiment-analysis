# import libraries and modules
from app import db

# NegativeSanitary model
class NegativeSanitary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False)