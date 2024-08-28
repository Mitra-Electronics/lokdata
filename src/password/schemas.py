from typing import Union
from pydantic import BaseModel, EmailStr
from datetime import date


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    date: date
    disabled: bool


class UserInDB(User):
    hashed_password: str
