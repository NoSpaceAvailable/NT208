import os

SECRET_KEY = os.getenv('SECRET_KEY', 'haha')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@db:5432/shop')
SQLALCHEMY_TRACK_MODIFICATIONS = False