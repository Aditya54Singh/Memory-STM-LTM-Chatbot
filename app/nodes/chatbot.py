from app.llm.groq import chat_llm

from app.prompts.chatboy import CHATBOT_SYSTEM_PROMPT

from langchain_core.messages import SystemMessage


def chatbot_node(state):
    """
    Generate the assistant response using

    1. System Prompt
    2. Retrieved Long-Term Memories
    3. Conversation History (STM)
    """

    if state['retrieved_memories']:
        memory_context = "\n".join(
            f" - {memory.memory}"
            for memory in state['retrieved_memories']
        )
    
    else:
        memory_context = "No relevant memories."

    system_prompt = f"""
    {CHATBOT_SYSTEM_PROMPT}

    Relevant User Memories:

    {memory_context}
    """

    messages = [
        SystemMessage(content=system_prompt),
        *state['messages']
    ]

    response = chat_llm.invoke(
        messages
    )

    return {

        "messages": [
            response
        ]

    }