from fastapi import APIRouter
from src.drivers.jwtd import decode_access_token
from src.survey.schemas import SurveyCreate, Survey
from src.drivers.db import get_acc, insert_survey
from src.schemas import Token

app = APIRouter()


@app.post("/get")
def get_survey():

    return {"success": "dummy"}


@app.post("/create")
def create_survey(input: SurveyCreate):
    temp = input.model_dump()
    email = decode_access_token(input.access_token)
    temp["creator_id"] = get_acc({"email": email})["_id"]
    data = Survey(**temp).model_dump()
    res = insert_survey(data)
    return {"success": res}
