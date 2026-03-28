from pydantic import BaseModel
from typing import List, Dict


class Action(BaseModel):
    action_type: str
    content: str


class Observation(BaseModel):
    email_text: str
    history: List[str]
    step_count: int


class Reward(BaseModel):
    score: float
    breakdown: Dict
    feedback: str