from dotenv import load_dotenv
from pathlib import Path
import os

root = Path(__file__).resolve().parent
for dotenv_path in [root / ".env", root / ".venv" / ".env"]:
    if dotenv_path.exists():
        load_dotenv(dotenv_path=dotenv_path)
        break

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "llama-3.3-70b-versatile"
LLM_MODEL = MODEL_NAME

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

DB_DIRECTORY = "chroma_db"