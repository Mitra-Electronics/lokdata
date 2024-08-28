from fastapi import APIRouter

app = APIRouter()


@app.get("/login")
def login():
    pass
