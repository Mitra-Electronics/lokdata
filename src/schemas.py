from pydantic import BaseModel
from typing import Union


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    username: Union[str, None] = None
