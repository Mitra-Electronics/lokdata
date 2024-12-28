from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime


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


class UserInDB(User):
    hashed_password: str
