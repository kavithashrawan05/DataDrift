from hindsight_config import client, BANK_ID


def retain_customer_memory(customer_name: str, conversation: str):
    """
    Store a customer conversation in Hindsight.
    """

    content = f"""
Customer: {customer_name}

Conversation:
{conversation}
"""

    result = client.retain(
        bank_id=BANK_ID,
        content=content
    )

    return result


def recall_customer_memory(customer_name: str, question: str):
    """
    Retrieve relevant customer memories from Hindsight.
    """

    query = f"""
Customer: {customer_name}

Question:
{question}
"""

    result = client.recall(
        bank_id=BANK_ID,
        query=query
    )

    memories = []

    for memory in result.results:
        memories.append({
            "text": memory.text,
            "type": memory.type
        })

    return memories