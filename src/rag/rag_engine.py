from google import genai

from src.retrieval.semantic_search import SemanticSearchEngine
from src.rag.config import GEMINI_API_KEY, GEMINI_MODEL, TOP_K_RESULTS
from src.rag.prompt_builder import build_interview_prompt


class RAGEngine:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found. Please add it to your .env file.")

        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.search_engine = SemanticSearchEngine()

    def has_strong_dataset_answer(self, result):
        answer = str(result["answer"]).strip()

        if answer == "" or answer.lower() == "nan":
            return False

        if answer == "No answer available in the source dataset.":
            return False

        if result["score"] < 0.82:
            return False

        if len(answer.split()) < 12:
            return False

        return True

    def answer_question(self, user_question: str):
        retrieved_results = self.search_engine.search(
            query=user_question,
            top_k=TOP_K_RESULTS
        )

        for result in retrieved_results:
            if self.has_strong_dataset_answer(result):
                return {
                    "question": user_question,
                    "answer": result["answer"],
                    "retrieved_results": retrieved_results,
                    "response_type": "retrieval_only"
                }

        prompt = build_interview_prompt(
            user_question=user_question,
            retrieved_results=retrieved_results
        )

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return {
            "question": user_question,
            "answer": response.text,
            "retrieved_results": retrieved_results,
            "response_type": "gemini_generated"
        }