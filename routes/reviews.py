# import libraries and modules
from flask import Blueprint, request, flash, redirect, render_template, url_for
from flask_login import login_required, current_user
from app import db
from models.review import Review

# Blueprint of reviews routes
reviews_bp = Blueprint('auth', __name__)

# review route
@reviews_bp.route('/submit_review', methods=['GET', 'POST'])
@login_required
def submit_review():
    if request.method == 'POST':
        try:
            text = request.form['text']
            is_positive = bool(request.form['is_positive'])
            category = request.form['category']
            review = Review(user_id=current_user.id, text=text, is_positive=is_positive, category=category)
            db.session.add(review)
            db.session.commit()
            flash('Review submitted successfully', 'success')
            return redirect(url_for('submit_review'))
        except:
            flash('Something went wrong')
            db.session.rollback()
        finally:
            db.session.close()
    return render_template('submit_review.html')