from fastapi import APIRouter

app = APIRouter()


@app.get("/list")
def list_passwords():
    pass
