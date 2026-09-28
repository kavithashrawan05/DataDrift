from fastapi import APIRouter
from schemas import (
    ConversationRequest,
    RecallRequest,
    MeetingBriefRequest
)

from services import (
    save_conversation,
    recall_customer,
    create_meeting_brief
)


router = APIRouter(prefix="/api")


@router.post("/conversation")
def add_conversation(request: ConversationRequest):

    result = save_conversation(
        request.customer,
        request.message
    )

    return {
        "success": True,
        "message": "Conversation stored successfully",
        "data": result
    }


@router.post("/recall")
def recall(request: RecallRequest):

    result = recall_customer(
        request.customer,
        request.query
    )

    return {
        "success": True,
        "message": "Customer information retrieved",
        "data": result
    }


@router.post("/meeting-brief")
def meeting_brief(request: MeetingBriefRequest):

    result = create_meeting_brief(
        request.customer,
        request.topic
    )

    return {
        "success": True,
        "message": "Meeting brief generated",
        "data": result
    }