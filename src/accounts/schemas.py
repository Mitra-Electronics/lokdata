from typing import Optional, Union
from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: PhoneNumber


class UserFind(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[PhoneNumber] = None


class UserRegister(UserBase):
    password: str


class User(UserBase):
    datetime: datetime
    disabled: bool
    hashed_password: str


class UserInDB(User):
    hashed_password: str
