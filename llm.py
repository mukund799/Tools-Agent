from langchain_cohere import ChatCohere
import os
from dotenv import load_dotenv
load_dotenv()
def load_llm():
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    llm = ChatCohere(model="command-r", cohere_api_key="")
    return llm