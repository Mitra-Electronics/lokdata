from fastapi import APIRouter

from src.accounts.schemas import UserRegister, UserLogin, UserFind, User, UserInDB
from src.drivers.db import insert_acc, get_acc
from src.drivers.hasher import verify_password
from src.drivers.jwtd import create_access_token, decode_access_token
from src.schemas import Token

app = APIRouter()


@app.post("/register")
def register(params: UserRegister):
    resv = insert_acc(params)
    assert resv == True
    return {"success": True}


@app.post("/login")
def login(params: UserLogin):
    u = UserInDB(**get_acc(UserFind(email=params.email).model_dump()))
    v = verify_password(params.password, u.hashed_password)
    if v is True:
        return {"success": True, "access_token": create_access_token(params.email)}
    return {"success": False}


@app.post("/user")
def get_user(params: Token):
    email = decode_access_token(params.access_token)
    u = User(**get_acc(UserFind(email=email).model_dump()))
    return {"success": True, "result": u}
