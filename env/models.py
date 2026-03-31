from pydantic import BaseModel
from typing import List, Dict


class Observation(BaseModel):
    ticket_id: str
    customer_message: str
    order_status: str
    issue_type: str
    history: List[Dict]


class Action(BaseModel):
    response: str
    action_type: str  # reply | refund | escalate


class Reward(BaseModel):
    score: float
    feedback: str