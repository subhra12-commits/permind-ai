from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import router

app = FastAPI(
    title="AI Interview Bot API",
    description="FastAPI backend for the AI Interview Bot using RAG and Gemini.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "AI Interview Bot API is running",
        "status": "healthy"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }