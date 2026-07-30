from langchain_core.messages import HumanMessage,SystemMessage
from app.llm.groq import chat_llm
from app.models.memory import MemoryCollection
from app.prompts.memory import MEMORY_EXTRACTION_PROMPT

memory_extractor = chat_llm.with_structured_output(
    MemoryCollection
)

def extract_memories(user_message : str) -> MemoryCollection:
        return memory_extractor.invoke(

        [

            SystemMessage(
                content=MEMORY_EXTRACTION_PROMPT
            ),

            HumanMessage(
                content=user_message
            )

        ]

    )