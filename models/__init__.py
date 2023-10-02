# Import models defined in other files
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .review import Review
from .positive_food import PositiveFood
from .negative_food import NegativeFood
from .positive_sanitary import PositiveSanitary
from .negative_sanitary import NegativeSanitary
