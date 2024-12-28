from typing import Optional
from pydantic import BaseModel, PositiveInt


class SurveyBase(BaseModel):
    title: str
    deactivated: bool = False
    question_blocks: Optional[list] = None


class SurveyCreate(SurveyBase):
    access_token: str


class Survey(SurveyBase):
    creator_id: str


class QuestionModel(BaseModel):
    question: str


class MCQ(QuestionModel):
    dropdown: bool
    options: list[str]
    answers: str


class Checkboxes(QuestionModel):
    options: list[str]
    answers: list[str]


class YesNoQuestion(QuestionModel):
    answers: bool


class LongQuestion(QuestionModel):
    answers: str


class RatingQuestion(QuestionModel):
    start_range: PositiveInt
    end_range: PositiveInt
    answers: PositiveInt
