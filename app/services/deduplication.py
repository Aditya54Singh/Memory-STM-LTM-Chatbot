from app.database.connection import store

SIMILARITY_THRESHOLD =  0.90

def memory_exists(user_id : str, memory : str, namespace : str = 'memories') -> bool :
    """
    Check whether a similar memory already exists.
    """

    results = store.search(
        ('user',user_id,namespace),
        query = memory,
        limit = 1,
    )

    if not results:
        return False
    
    top_result = results[0]

    return top_result.score >= SIMILARITY_THRESHOLD