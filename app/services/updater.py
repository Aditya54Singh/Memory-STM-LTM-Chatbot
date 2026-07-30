from app.database.connection import store

PROFILE_FIELDS = (
    'name',
    'location',
    'age',
    'profession'
)

def update_memory(
        namespace : tuple,
        key : str,
        value : dict
):
    """
    Replace an existing memory.
    """

    store.put(
        namespace,
        key,
        value,
    )