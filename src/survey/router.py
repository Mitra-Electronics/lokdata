from fastapi import APIRouter

app = APIRouter()

@app.post("/get")
def get_survey():
    return {"success":"dummy"}

@app.post("/create")
def create_survey():
    return {"success":"dummy"}
