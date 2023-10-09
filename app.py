# import libraries
from flask import Flask
from flask_login import LoginManager
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.reviews import reviews_bp
from config import Config
from models import db

# Initialize Flask instance
app = Flask(__name__)

# Configure Flask instance with configuration settings
app.config.from_object(Config)

# Initialize SQLAlchemy with the Flask app
db.init_app(app)


# Initialize login manager
login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'
login_manager.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(reviews_bp)

# create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)