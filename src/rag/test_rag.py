from src.rag.rag_engine import RAGEngine

engine = RAGEngine()

question = input("Enter your interview question: ")

result = engine.answer_question(question)

print("\nAI Interview Bot Answer")
print("=" * 70)
print(result["answer"])

print("\nRetrieved Sources")
print("=" * 70)

for i, source in enumerate(result["retrieved_results"], start=1):
    print(f"\nSource {i}")
    print(f"Score      : {source['score']:.4f}")
    print(f"Category   : {source['category']}")
    print(f"Difficulty : {source['difficulty']}")
    print(f"Question   : {source['question']}")