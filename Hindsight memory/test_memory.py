from memory_service import (
    retain_customer_memory,
    recall_customer_memory
)


def main():

    customer = "ABC Technologies"

    conversation = """
    During the sales meeting, ABC Technologies said
    their budget is ₹10 lakh.

    Their biggest concern is security.

    They are also considering Microsoft as a competitor.
    """

    print("Saving customer conversation...")
    
    retain_customer_memory(
        customer_name=customer,
        conversation=conversation
    )

    print("Memory stored successfully.")

    print("\nRecalling customer information...")

    question = "What is ABC Technologies' budget?"

    memories = recall_customer_memory(
        customer_name=customer,
        question=question
    )

    print("\nRelevant memories:")

    for memory in memories:
        print(f"- {memory['text']}")
        print(f"  Type: {memory['type']}")


if __name__ == "__main__":
    main()