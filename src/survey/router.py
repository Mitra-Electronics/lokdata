from fastapi import APIRouter

app = APIRouter()

@app.post("/create")
def create_survey():
    return {"success":True}