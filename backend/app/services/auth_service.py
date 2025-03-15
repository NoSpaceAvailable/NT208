import jwt
import os
import random
from .. models.User import User

JWT_SECRET = os.getenv('JWT_SECRET', random.randbytes(32).hex())
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')

def verify(token: str) -> bool:
    try:
        jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return True
    except jwt.ExpiredSignatureError as e:
        raise e
    except jwt.InvalidTokenError as e:
        raise e

def sign(User) -> str:
    return jwt.encode({
        'id': User.id,
        'username': User.username,
        'email': User.email,
        'reputation': User.reputation,
    }, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decode(token: str) -> User:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return User(
            id=payload['id'],
            username=payload['username'],
            email=payload['email'],
            reputation=payload['reputation'],
        )
    except jwt.ExpiredSignatureError as e:
        raise e
    except jwt.InvalidTokenError as e:
        raise e
    
