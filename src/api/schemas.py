from pydantic import BaseModel
from typing import List, Optional


class AskRequest(BaseModel):
    question: str


class RetrievedSource(BaseModel):
    score: float
    question: str
    answer: str
    category: str
    difficulty: str
    dataset_name: str
    source: str


class AskResponse(BaseModel):
    question: str
    answer: str
    retrieved_sources: List[RetrievedSource]