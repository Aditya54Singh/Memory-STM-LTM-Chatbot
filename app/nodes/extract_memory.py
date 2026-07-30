from langchain_core.messages import HumanMessage

from app.llm.memory_extractor import extract_memories


def extract_memory_node(state):
    """
    Extract candidate long-term memories from the latest
    human message.
    """

    latest_human_message = None

    # Traverse backwards to find the most recent HumanMessage
    for message in reversed(state["messages"]):

        if isinstance(message, HumanMessage):

            latest_human_message = message.content
            break

    # No user message found
    if latest_human_message is None:

        return {
            "candidate_memories": []
        }

    ####################################################################
    # Extract Memories
    ####################################################################

    extracted = extract_memories(
        latest_human_message
    )

    return {
        "candidate_memories": extracted.memories
    }