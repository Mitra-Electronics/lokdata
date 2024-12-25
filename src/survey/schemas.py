from pydantic import BaseModel

class SurveyCreate(BaseModel):
    creator_id: str
    title: str
    question_blocks: list