from fastapi import APIRouter

from src.accounts.schemas import UserRegister, UserLogin, UserFind, User
from src.db import insert_acc, get_acc
from src.hasher import verify_password
from src.jwtd import create_access_token

app = APIRouter()


@app.post("/register")
def register(user: UserRegister):
    resv = insert_acc(user)
    assert resv == True
    return {"success": True}


@app.post("/login")
def login(user: UserLogin):
    u = User(**get_acc(UserFind(email=user.email)))
    v = verify_password(user.password, u.hashed_password)
    if v is True:
        return {"success": True, "access_token": create_access_token(user.email)}
    return {"success": False}


@app.post("/user")
def get_user(token: str):
    return
