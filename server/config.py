from dotenv import load_dotenv
import os
from urllib.parse import quote
import redis


load_dotenv()

class ApplicationConfig:
    password = "@Betini2024"
    encoded_password = quote(password)
    SECRET_KEY = os.environ["SECRET_KEY"]

    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f"mysql://root:{encoded_password}@localhost/SBHP_db"

    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")