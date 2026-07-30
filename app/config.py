from dotenv import load_dotenv
import os 

load_dotenv()

class settings:
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')

    DB_URI = os.getenv("DB_URI")

    CHAT_MODEL = 'llama-3.3-70b-versatile'

    EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

    TOP_K_MEMORIES = 5

    EMBEDDIN_DIMENSION = 384

settings = settings()
