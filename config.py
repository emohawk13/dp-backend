import os

class Config:
    # Fetch the DATABASE_URI set by create_db.py
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://username:password@localhost/default_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'SuperSecretKeyDevPipeline1')
