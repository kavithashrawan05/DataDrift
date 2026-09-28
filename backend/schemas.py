from pydantic import BaseModel
from typing import Optional


class ConversationRequest(BaseModel):
    customer: str
    message: str


class RecallRequest(BaseModel):
    customer: str
    query: str


class MeetingBriefRequest(BaseModel):
    customer: str
    topic: Optional[str] = None


class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None