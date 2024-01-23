from dotenv import load_dotenv
import os
import secrets
from urllib.parse import quote
import redis

load_dotenv()

class ApplicationConfig:
    password = os.getenv("DB_PASSWORD")
    encoded_password = quote(password)

    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f"mysql://root:{encoded_password}@localhost/SBHP_db"

    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = True
    SESSION_KEY_PREFIX = '2ew'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")

    SECRET_KEY = os.getenv("SECRET_KEY")
  

   