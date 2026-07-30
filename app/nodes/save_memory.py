from app.services.memory_service import memory_service

def save_memory(state,config):
    """
    Persist extracted memories into Long-Term Memory.

    MemoryService handles:
    - confidence filtering
    - duplicate detection
    - storage
    """

    user_id = config['configurable']['user_id']
    
    for memory in state['candidate_memories']:
        memory_service.save(
            user_id=user_id,
            memory=memory,
        )
    
    return {}