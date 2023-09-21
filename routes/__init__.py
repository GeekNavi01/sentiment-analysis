from flask import Blueprint

# Create blueprints for routes
auth_bp = Blueprint('auth', __name__)
reviews_bp = Blueprint('reviews', __name__)
admin_bp = Blueprint('admin', __name__)

# Import routes defined in other files to register them with the blueprints
from . import auth, reviews, admin
