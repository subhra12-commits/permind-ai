import time
import pandas as pd

from src.rag.rag_engine import RAGEngine
from src.evaluation.config import (
    TEST_QUERIES_FILE,
    REPORTS_DIR
)

OUTPUT_FILE = REPORTS_DIR / "rag_evaluation_report.csv"


def main():
    print("=" * 70)
    print("RAG EVALUATION")
    print("=" * 70)

    engine = RAGEngine()

    test_df = pd.read_csv(TEST_QUERIES_FILE)

    results = []

    for _, row in test_df.iterrows():

        query = row["query"]

        print(f"\nEvaluating: {query}")

        start = time.time()

        response = engine.answer_question(query)

        latency = time.time() - start

        answer = response["answer"]

        results.append({
            "query": query,
            "latency_seconds": round(latency, 3),
            "answer_length_words": len(answer.split()),
            "retrieved_sources": len(response["retrieved_results"]),
            "generated_answer": answer
        })



    time.sleep(20)

    report = pd.DataFrame(results)

    report.to_csv(OUTPUT_FILE, index=False)

    print("\n" + "=" * 70)
    print("RAG EVALUATION SUMMARY")
    print("=" * 70)

    print(f"Queries Tested      : {len(report)}")
    print(f"Average Latency     : {report['latency_seconds'].mean():.3f} sec")
    print(f"Average Answer Size : {report['answer_length_words'].mean():.1f} words")
    print(f"Average Sources     : {report['retrieved_sources'].mean():.1f}")

    print("\nSaved:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()