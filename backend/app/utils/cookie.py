import jwt
from ..global_config import jwt_config

SECRET = jwt_config["JWT_SECRET"]
ALG = jwt_config["JWT_ALG"]

def sign_token(payload: dict):
    return jwt.encode(payload=payload, key=SECRET, algorithm=ALG)

def verify(token: str):
    try:
        jwt.decode(token, key=SECRET, algorithms=ALG)
        return True
    except:
        return False
