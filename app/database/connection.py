from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.store.postgres import PostgresStore

from app.config import settings
from app.database.embeddings import embedding_model

# Context managers
_checkpointer_cm = PostgresSaver.from_conn_string(settings.DB_URI)
_store_cm = PostgresStore.from_conn_string(
    settings.DB_URI,
    index={
        "embed": embedding_model,
        "dims": settings.EMBEDDIN_DIMENSION,
    },
)

# Actual objects
checkpointer = _checkpointer_cm.__enter__()
store = _store_cm.__enter__()

# Initialize database tables/indexes
checkpointer.setup()
store.setup()