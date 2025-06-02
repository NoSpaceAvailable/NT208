from sqlalchemy import or_
import os
import random
from app.models.User import User
from app.models.Database import Database

JWT_SECRET = os.getenv('JWT_SECRET', random.randbytes(32).hex())
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')

def create_user(username, email, password, is_oauth2 = False):
    session = Database.get_session()
    try:
        new_user = User(username=username, email=email, password=password, is_oauth2=is_oauth2)
        session.add(new_user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False
    finally:
        session.close()

def check_user(username, password):
    session = Database.get_session()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user != None and user.check_password(password):
            return True
        return False
    finally:
        session.close()
    
def user_exist(username, email):
    session = Database.get_session()
    try:
        return session.query(User).filter(
            or_(
                User.username == username, 
                User.email == email
            )
        ).first() is not None
    finally:
        session.close()

def email_exist(email):
    session = Database.get_session()
    try:
        return session.query(User).filter(User.email == email).first() is not None
    finally:
        session.close()

def username_exist(username):
    session = Database.get_session()
    try:
        return session.query(User).filter(User.username == username).first() is not None
    finally:
        session.close()

def get_username_by_email(email):
    session = Database.get_session()
    try:
        return session.query(User).filter(User.email == email).first().username
    finally:
        session.close()