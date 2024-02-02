import os
import redis


class ApplicationConfig:
    """Configuration settings"""
    db_password = os.environ.get("DB_PASSWORD")

    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{db_password}@localhost:5432/SBHP_db"
    
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url(os.environ.get("REDIS_URL"))

    SECRET_KEY = os.environ.get("SECRET_KEY")
  

   