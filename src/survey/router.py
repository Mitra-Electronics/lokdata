from fastapi import APIRouter
from src.drivers.jwtd import decode_access_token
from src.survey.schemas import SurveyCreate, Survey
from src.drivers.db import get_acc, insert_survey
from src.schemas import Token

app = APIRouter()


@app.post("/get")
def get_survey(params: Token):
    email = decode_access_token(params.access_token)
    surveys = get_survey(email)
    if surveys is None:
        return {"success": False}
    return {"success": True, "result": surveys}


@app.post("/create")
def create_survey(params: SurveyCreate):
    temp = params.model_dump()
    email = decode_access_token(params.access_token)
    temp["creator_id"] = get_acc({"email": email})["_id"]
    data = Survey(**temp).model_dump()
    res = insert_survey(data)
    return {"success": res}
