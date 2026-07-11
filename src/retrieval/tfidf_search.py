import joblib
import pandas as pd
from pathlib import Path
from sklearn.metrics.pairwise import linear_kernel

from src.preprocessing.text_preprocessor import TextPreprocessor


class TfidfSearchEngine:
    def __init__(self):
        self.dataset_path = Path(
            "datasets/final/preprocessed_interview_dataset.csv"
        )

        self.vectorizer_path = Path(
            "datasets/features/tfidf_vectorizer.pkl"
        )

        self.features_path = Path(
            "datasets/features/tfidf_features.pkl"
        )

        self.df = pd.read_csv(self.dataset_path)

        self.vectorizer = joblib.load(self.vectorizer_path)
        self.tfidf_matrix = joblib.load(self.features_path)

        self.preprocessor = TextPreprocessor()

        if len(self.df) != self.tfidf_matrix.shape[0]:
            raise ValueError(
                "Dataset row count does not match TF-IDF feature rows."
            )

    @staticmethod
    def _format_answer(answer):
        if pd.isna(answer) or str(answer).strip() == "":
            return "No answer available in the source dataset."

        return str(answer).strip()

    def search(self, query: str, top_k: int = 5):
        if not isinstance(query, str) or not query.strip():
            return []

        processed_query = self.preprocessor.preprocess(query)

        query_vector = self.vectorizer.transform([processed_query])

        similarities = linear_kernel(
            query_vector,
            self.tfidf_matrix
        ).flatten()

        # Retrieve extra candidates so duplicate questions can be skipped
        candidate_count = min(max(top_k * 5, 20), len(self.df))

        candidate_indices = similarities.argsort()[-candidate_count:][::-1]

        results = []
        seen_questions = set()

        for idx in candidate_indices:
            row = self.df.iloc[idx]

            question = str(row["question"]).strip()
            normalized_question = question.lower()

            if normalized_question in seen_questions:
                continue

            seen_questions.add(normalized_question)

            results.append({
                "score": float(similarities[idx]),
                "question": question,
                "answer": self._format_answer(row["answer"]),
                "category": str(row["category"]),
                "difficulty": str(row["difficulty"]),
                "dataset_name": str(row["dataset_name"]),
                "source": str(row["source"])
            })

            if len(results) >= top_k:
                break

        return results