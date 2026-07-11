import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", "5"))

# faiss for local development
# tfidf for lightweight cloud deployment
SEARCH_BACKEND = os.getenv("SEARCH_BACKEND", "faiss").lower()