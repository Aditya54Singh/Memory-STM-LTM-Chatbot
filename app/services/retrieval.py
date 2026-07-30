from langgraph.store.base import SearchItem

from app.database.connection import store
from app.config import settings

def retrieve_memories(user_id :str, query:str, namespace : str ="memories")-> list[SearchItem]:
    """
    Perform semantic search over the user's memories.

    Args:
        user_id: Unique user id.
        query: User query.
        namespace: Memory namespace.

    Returns:
        Top-K relevant memories.
    """

    return store.search(
        ("user", user_id, namespace),
        query=query,
        limit=settings.TOP_K_MEMORIES,
    )

