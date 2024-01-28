import os
from urllib.parse import quote
import redis


class ApplicationConfig:
    """Configuration settings"""
    password = os.environ.get("DB_PASSWORD")
    encoded_password = quote(password)

    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # f"mysql://root:{encoded_password}@localhost/SBHP_db"

    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = True
    SESSION_KEY_PREFIX = '2ew'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url(os.environ.get("REDIS_URL"))

    SECRET_KEY = os.environ.get("SECRET_KEY")
  

   