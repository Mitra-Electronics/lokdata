from fastapi import APIRouter
from src.survey.schemas import SurveyCreate

app = APIRouter()

@app.post("/get")
def get_survey():
    return {"success":"dummy"}

@app.post("/create")
def create_survey(input: SurveyCreate):
    return {"success":"dummy"}
