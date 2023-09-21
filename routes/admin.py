from collections import defaultdict
from flask_login import login_required
from flask import Blueprint, render_template
from bokeh.embed import components
from utils import create_bokeh_plot
from models.negative_food import NegativeFood
from models.positive_food import PositiveFood
from models.negative_sanitary import NegativeSanitary
from models.positive_sanitary import PositiveSanitary

# Blueprint of admin routes
admin_bp = Blueprint('auth', __name__)

# admin route
@admin_bp.route('/admin_dashboard')
@login_required
def admin_dashboard():
    # Count the number of reviews in each category
    categories = ['Positive Food', 'Negative Food', 'Positive Sanitary', 'Negative Sanitary']
    review_counts = defaultdict(int)
    
    for category in categories:
        if category == 'Positive Food':
            count = PositiveFood.query.count()
        elif category == 'Negative Food':
            count = NegativeFood.query.count()
        elif category == 'Positive Sanitary':
            count = PositiveSanitary.query.count()
        elif category == 'Negative Sanitary':
            count = NegativeSanitary.query.count()
        else:
            count = 0
        
        review_counts[category] = count
    
    # Create a Bokeh plot
    p = create_bokeh_plot(review_counts)
    script, div = components(p)
    
    return render_template('admin_dashboard.html', script=script, div=div)
