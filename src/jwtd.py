from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status
import jwt
from jwt.exceptions import InvalidTokenError


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
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        u = decoded_jwt.get("sub")
        if u is None:
            raise credentials_exception
        return u
    except InvalidTokenError:
        raise credentials_exception
