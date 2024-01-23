"""User authentication"""
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

def get_userid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(32), unique=True, primary_key=True, nullable=False, default=get_userid)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.Text, unique=True, nullable=False)