from fastapi import APIRouter

from src.accounts.schemas import UserRegister, UserLogin, UserFind, User, UserInDB, Token
from src.drivers.db import insert_acc, get_acc
from src.drivers.hasher import verify_password
from src.drivers.jwtd import create_access_token, decode_access_token

app = APIRouter()


@app.post("/register")
def register(user: UserRegister):
    resv = insert_acc(user)
    assert resv == True
    return {"success": True}


@app.post("/login")
def login(user: UserLogin):
    u = UserInDB(**get_acc(UserFind(email=user.email).model_dump()))
    v = verify_password(user.password, u.hashed_password)
    if v is True:
        return {"success": True, "access_token": create_access_token(user.email)}
    return {"success": False}


@app.post("/user")
def get_user(token: Token):
    email = decode_access_token(token.access_token)
    u = User(**get_acc(UserFind(email=email).model_dump()))
    return {"success": True, "result": u}
