from uuid import uuid4
CONFIDENCE_THRESHOLD = 0.80
from langgraph.store.base import SearchItem

from app.database.connection import store
from app.services.deduplication import memory_exists
from app.services.updater import update_memory
from app.models.memory import Memory
from app.models.memory import RetrievedMemory
from app.services.retrieval import retrieve_memories


class MemoryService:
    """
    Handles all Long-Term Memory operations.

    Nodes should ONLY call this class.
    They should never directly call PostgresStore.
    """

    def __init__(self):
        self.store = store

    ####################################################################
    # Namespace
    ####################################################################

    @staticmethod
    def get_namespace(
        user_id: str,
        category: str = "memories",
    ) -> tuple:

        return (
            "user",
            user_id,
            category,
        )

    ####################################################################
    # Retrieve
    ####################################################################

    def retrieve(
    self,
    user_id: str,
    query: str,
    category: str = "memories",
) -> list[RetrievedMemory]:

        search_results = retrieve_memories(
            user_id=user_id,
            query=query,
            namespace=category,
        )

        retrieved_memories = []

        for result in search_results:

            retrieved_memories.append(
                RetrievedMemory(
                    key=result.key,
                    category=result.value['category'],
                    memory=result.value["memory"],
                    score=result.score,
                )
            )

        return retrieved_memories

    ####################################################################
    # Save
    ####################################################################

    def save(
    self,
    user_id: str,
    memory: Memory,
    ) -> bool:
        
        """
        Save a memory if:
        1. Confidence is high enough.
        2. It doesn't already exist.
        """

        # Ignore low confidence memories
        if memory.confidence < CONFIDENCE_THRESHOLD:
            return False

        namespace = self.get_namespace(
            user_id=user_id,
            category="memories",
        )

    # Duplicate check
        if memory_exists(
            user_id=user_id,
            memory=memory.memory,
            namespace="memories",
        ):
            return False

        self.store.put(
            namespace=namespace,
            key=str(uuid4()),
            value={
                "memory": memory.memory,
                "category": memory.category,
                "confidence": memory.confidence,
            },
        )

        return True

    ####################################################################
    # Update
    ####################################################################

    def update(
        self,
        user_id: str,
        category: str,
        key: str,
        memory: str,
    ):

        namespace = self.get_namespace(
            user_id=user_id,
            category="memories",
        )

        update_memory(
            namespace=namespace,
            key=key,
            value={
                "memory": memory,
            },
        )

    ####################################################################
    # Delete
    ####################################################################

    def delete(
        self,
        user_id: str,
        category: str,
        key: str,
    ):

        namespace = self.get_namespace(
        user_id=user_id,
        category="memories",
    )

        self.store.delete(
            namespace,
            key,
        )


memory_service = MemoryService()