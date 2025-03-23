import jwt
import os
import random
from .. models.User import User
from ..models.Database import Database

JWT_SECRET = os.getenv('JWT_SECRET', random.randbytes(32).hex())
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
session = Database.get_session()

def create_user(username, email, password):
    try:    
        new_user = User(username=username, email=email, password=password)
        session.add(new_user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False

def check_user(username, password):
    user = session.query(User).filter(User.username == username).first()
    if user != None and user.check_password(password):
        return True
    return False
    
def user_exist(username, email):
    return session.query(User).filter(User.username == username, User.email == email).all()

