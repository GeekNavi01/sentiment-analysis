# import libraries and modules
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# PositiveFood model
class PositiveFood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False)