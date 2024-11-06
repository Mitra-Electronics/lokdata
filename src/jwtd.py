from datetime import datetime, timedelta, timezone

import jwt


SECRET_KEY = "82f239f4b946ce2937d92bd4f46ab09c946671f23edbf359b408d8fbfb650ba3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(email: str | datetime, expires_delta: timedelta | None = None):
    to_encode = {"sub": email}
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
