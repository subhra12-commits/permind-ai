import sys
from pathlib import Path

import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

from src.preprocessing.text_preprocessor import TextPreprocessor


class SemanticSearchEngine:
    def __init__(self):
        self.dataset_path = Path("datasets/final/preprocessed_interview_dataset.csv")
        self.index_path = Path("datasets/features/faiss_index.index")

        self.df = pd.read_csv(self.dataset_path)
        self.index = faiss.read_index(str(self.index_path))

        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")
        self.preprocessor = TextPreprocessor()

    def search(self, query: str, top_k: int = 5):
        processed_query = self.preprocessor.preprocess(query)

        query_embedding = self.model.encode(
            [processed_query],
            convert_to_numpy=True
        ).astype("float32")

        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(query_embedding, 20)

        results = []
        seen_questions = set()

        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue

            row = self.df.iloc[idx]
            question = str(row["question"]).strip()

            if question.lower() in seen_questions:
                continue

            seen_questions.add(question.lower())

            answer = row["answer"]

            if answer is None or str(answer).strip() == "" or str(answer).lower() == "nan":
                answer = "No answer available in the source dataset."

            results.append({
                "score": float(score),
                "question": question,
                "answer": answer,
                "category": row["category"],
                "difficulty": row["difficulty"],
                "dataset_name": row["dataset_name"],
                "source": row["source"]
            })

            if len(results) >= top_k:
                break

        return results