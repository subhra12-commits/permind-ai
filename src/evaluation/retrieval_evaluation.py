import sys
import time
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1] / "retrieval"))

from semantic_search import SemanticSearchEngine
from config import TEST_QUERIES_FILE, RETRIEVAL_REPORT_FILE


def main():
    print("=" * 70)
    print("RETRIEVAL EVALUATION")
    print("=" * 70)

    engine = SemanticSearchEngine()
    test_df = pd.read_csv(TEST_QUERIES_FILE)

    results = []

    for _, row in test_df.iterrows():
        query = row["query"]
        expected_keyword = str(row["expected_keyword"]).lower()

        start_time = time.time()
        retrieved = engine.search(query, top_k=5)
        latency = time.time() - start_time

        retrieved_text = " ".join(
            [
                str(item["question"]) + " " + str(item["answer"])
                for item in retrieved
            ]
        ).lower()

        keyword_found = expected_keyword in retrieved_text

        results.append({
            "query": query,
            "expected_keyword": expected_keyword,
            "keyword_found": keyword_found,
            "top_score": retrieved[0]["score"] if retrieved else 0,
            "latency_seconds": round(latency, 4),
            "top_question": retrieved[0]["question"] if retrieved else ""
        })

    report_df = pd.DataFrame(results)

    report_df.to_csv(RETRIEVAL_REPORT_FILE, index=False)

    accuracy = report_df["keyword_found"].mean() * 100
    avg_latency = report_df["latency_seconds"].mean()

    print("\nEvaluation Summary")
    print(f"Total Queries       : {len(report_df)}")
    print(f"Keyword Match Score : {accuracy:.2f}%")
    print(f"Average Latency     : {avg_latency:.4f} seconds")

    print("\nSaved report:")
    print(RETRIEVAL_REPORT_FILE)


if __name__ == "__main__":
    main()