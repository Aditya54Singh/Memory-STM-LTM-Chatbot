from app.services.memory_service import memory_service


def retrieve_memory_node(state, config):
    """
    Retrieve relevant memories from Long-Term Memory.
    """

    user_id = config["configurable"]["user_id"]

    query = state["messages"][-1].content

    return {
        "retrieved_memories": memory_service.retrieve(
            user_id=user_id,
            query=query,
        )
    }