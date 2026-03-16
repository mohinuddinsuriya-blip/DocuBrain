from jose import jwt
from datetime import datetime, timedelta

SECRET = "supersecret"

def create_token(user):

    payload = {
        "sub": user,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }

    return jwt.encode(payload, SECRET)