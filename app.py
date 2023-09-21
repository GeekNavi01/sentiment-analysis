# import libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from routes import *
from config import Config

# Initialize Flask instance
app = Flask(__name__)

# Configure Flask instance with configuration settings
app.config.from_object(Config)

# Initialize database instance
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(reviews_bp)
app.register_blueprint(admin_bp)

# create database tables
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)