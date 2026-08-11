from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME


def load_llm():

    if not GROQ_API_KEY:
        raise EnvironmentError(
            "GROQ_API_KEY is not set. Add it to your .env file or set the GROQ_API_KEY environment variable."
        )

    return ChatGroq(
        model=MODEL_NAME,
        api_key=GROQ_API_KEY,
        temperature=0
    )
