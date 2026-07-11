from google import genai

from src.rag.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    TOP_K_RESULTS,
    SEARCH_BACKEND
)
from src.rag.prompt_builder import build_interview_prompt


class RAGEngine:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY not found. Please configure it."
            )

        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.search_engine = self._create_search_engine()

    def _create_search_engine(self):
        if SEARCH_BACKEND == "tfidf":
            from src.retrieval.tfidf_search import TfidfSearchEngine

            print("Retrieval backend: TF-IDF")
            return TfidfSearchEngine()

        if SEARCH_BACKEND == "faiss":
            # Lazy import prevents PyTorch/SentenceTransformers
            # from loading on the lightweight Render deployment.
            from src.retrieval.semantic_search import SemanticSearchEngine

            print("Retrieval backend: BGE + FAISS")
            return SemanticSearchEngine()

        raise ValueError(
            f"Unsupported SEARCH_BACKEND: {SEARCH_BACKEND}. "
            "Use 'faiss' or 'tfidf'."
        )

    @staticmethod
    def has_strong_dataset_answer(result):
        answer = str(result["answer"]).strip()

        if not answer or answer.lower() == "nan":
            return False

        if answer == "No answer available in the source dataset.":
            return False

        # TF-IDF and FAISS scores are not directly comparable,
        # so use backend-specific confidence thresholds.
        threshold = 0.82 if SEARCH_BACKEND == "faiss" else 0.35

        if result["score"] < threshold:
            return False

        if len(answer.split()) < 12:
            return False

        return True

    def answer_question(self, user_question: str):
        retrieved_results = self.search_engine.search(
            query=user_question,
            top_k=TOP_K_RESULTS
        )

        if not retrieved_results:
            raise ValueError("No relevant interview content was found.")

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