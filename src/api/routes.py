from fastapi import APIRouter, HTTPException

from src.api.schemas import AskRequest, AskResponse
from src.rag.rag_engine import RAGEngine

router = APIRouter()

rag_engine = RAGEngine()


@router.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    try:
        result = rag_engine.answer_question(request.question)

        return {
            "question": result["question"],
            "answer": result["answer"],
            "retrieved_sources": result["retrieved_results"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))