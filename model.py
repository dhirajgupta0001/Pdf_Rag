from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_ollama import OllamaEmbeddings
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = init_chat_model(
    "gpt-oss:20b-cloud",
    model_provider="openai",
    api_key=api_key,
    base_url="https://ollama.com/v1",
)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434",
)
