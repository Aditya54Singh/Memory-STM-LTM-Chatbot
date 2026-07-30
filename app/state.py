from pydantic import Field

from langgraph.graph import MessagesState

from app.models.memory import (
    Memory,
    RetrievedMemory,
)


class ChatState(MessagesState):
    """
    Shared graph state.
    """

    retrieved_memories: list[RetrievedMemory] = Field(
        default_factory=list
    )

    candidate_memories: list[Memory] = Field(
        default_factory=list
    )