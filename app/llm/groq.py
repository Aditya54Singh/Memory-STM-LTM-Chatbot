from langchain_groq import ChatGroq
from app.config import settings

chat_llm = ChatGroq(
    model=settings.CHAT_MODEL,
    temperature=0.2,
    api_key=settings.GROQ_API_KEY,
)