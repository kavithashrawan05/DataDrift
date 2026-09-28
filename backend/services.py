from typing import Dict, List


# Temporary in-memory storage.
# Later this will be connected to Hindsight memory.
conversation_store: Dict[str, List[str]] = {}


def save_conversation(customer: str, message: str):
    if customer not in conversation_store:
        conversation_store[customer] = []

    conversation_store[customer].append(message)

    return {
        "customer": customer,
        "message": message,
        "stored": True
    }


def recall_customer(customer: str, query: str):
    conversations = conversation_store.get(customer, [])

    return {
        "customer": customer,
        "query": query,
        "memories": conversations
    }


def create_meeting_brief(customer: str, topic: str | None = None):
    conversations = conversation_store.get(customer, [])

    return {
        "customer": customer,
        "topic": topic,
        "previous_conversations": conversations,
        "message": "Meeting brief generated from available customer information."
    }