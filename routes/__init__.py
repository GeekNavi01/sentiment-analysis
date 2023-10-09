from flask import Blueprint

# Create blueprints for routes
auth_bp = Blueprint('auth_bp', __name__)
reviews_bp = Blueprint('reviews_bp', __name__)
admin_bp = Blueprint('admin_bp', __name__)

# Import routes defined in other files to register them with the blueprints
from . import auth_bp, reviews_bp, admin_bp
